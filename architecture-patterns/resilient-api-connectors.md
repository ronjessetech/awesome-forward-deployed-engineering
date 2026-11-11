# Resilient API Connectors & Enterprise Data Bridges

Enterprise client integrations rarely look like textbook REST APIs. Expect strict rate limits, flaky VPN tunnels, 502 timeouts, duplicate webhook deliveries, and unexpected schema drift.

---

## 1. Five Golden Rules of Enterprise Connectors

1. **Idempotency Keys on Every Write:** Generate deterministic keys (e.g., `sha256(tenant_id + source_record_id + updated_at)`) so retries never create duplicate invoices, orders, or tickets.
2. **Exponential Backoff with Full Jitter:** Never retry on tight loops (which triggers thundering-herd bans). Wait `random(0, min(cap, base * 2^attempt))`.
3. **Circuit Breaker Pattern:** If a downstream client ERP fails 5 consecutive requests, open the circuit for 60 seconds and queue payloads instead of exhausting worker threads.
4. **Dead-Letter Queues (DLQ):** Poison messages (malformed JSON, unexpected null required fields) must go to a DLQ with the raw payload and validation error—never silently drop them or crash the pipeline.
5. **Strict Schema Validation at Ingestion:** Validate incoming records with **Pydantic** (Python) or **Zod** (TypeScript) immediately upon ingestion.

---

## 2. Python Async Retry + Circuit Breaker Skeleton

```python
import asyncio
import random
import time
import httpx

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, reset_timeout: float = 60.0):
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.failures = 0
        self.opened_at: float | None = None

    def allow_request(self) -> bool:
        if self.opened_at is None:
            return True
        if time.monotonic() - self.opened_at >= self.reset_timeout:
            self.opened_at = None
            self.failures = 0
            return True
        return False

    def record_success(self):
        self.failures = 0
        self.opened_at = None

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.opened_at = time.monotonic()


async def fetch_with_backoff(
    client: httpx.AsyncClient,
    url: str,
    breaker: CircuitBreaker,
    max_attempts: int = 4,
):
    if not breaker.allow_request():
        raise RuntimeError("Circuit breaker OPEN — upstream integration paused")

    for attempt in range(max_attempts):
        try:
            resp = await client.get(url, timeout=10.0)
            if resp.status_code in (429, 500, 502, 503, 504):
                raise httpx.HTTPStatusError("Retryable status", request=resp.request, response=resp)
            resp.raise_for_status()
            breaker.record_success()
            return resp.json()
        except (httpx.RequestError, httpx.HTTPStatusError):
            if attempt == max_attempts - 1:
                breaker.record_failure()
                raise
            delay = random.uniform(0, min(30.0, 0.5 * (2 ** attempt)))
            await asyncio.sleep(delay)
```

---

## 3. Webhook Ingestion Security
When receiving webhooks from client systems:
- Verify the **HMAC-SHA256 signature** header using constant-time comparison (`hmac.compare_digest`).
- Enforce a **5-minute timestamp tolerance** to block replay attacks.
- Return `202 Accepted` immediately after pushing the raw event into a **Redis queue**; process heavy ETL transforms asynchronously in a worker.
