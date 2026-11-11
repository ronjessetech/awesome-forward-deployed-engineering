import asyncio
import json
import time
from typing import AsyncGenerator

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="FDE Client Integration Bridge",
    version="0.1.0",
    description="48-hour enterprise pilot starter with Pydantic validation & SSE streaming",
)


class CircuitBreaker:
    """Minimal in-memory circuit breaker for protecting flaky enterprise upstream APIs."""

    def __init__(self, failure_threshold: int = 5, reset_timeout: float = 60.0) -> None:
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

    def record_success(self) -> None:
        self.failures = 0
        self.opened_at = None

    def record_failure(self) -> None:
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.opened_at = time.monotonic()


upstream_breaker = CircuitBreaker()


class PilotQueryRequest(BaseModel):
    tenant_id: str = Field(..., min_length=2, description="Verified organization identifier")
    query: str = Field(..., min_length=3, max_length=2000)


class ConnectorSyncRecord(BaseModel):
    source_id: str
    payload: dict
    idempotency_key: str = Field(..., min_length=8)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "circuit_open": not upstream_breaker.allow_request()}


@app.post("/api/v1/connectors/ingest", status_code=202)
async def ingest_record(record: ConnectorSyncRecord) -> dict:
    if not upstream_breaker.allow_request():
        raise HTTPException(status_code=503, detail="Upstream integration circuit open")
    # Enqueue validated record with idempotency_key for async worker processing
    return {
        "accepted": True,
        "source_id": record.source_id,
        "idempotency_key": record.idempotency_key,
    }


async def stream_pilot_answer(req: PilotQueryRequest) -> AsyncGenerator[str, None]:
    tokens = [
        f"[Tenant: {req.tenant_id}] ",
        "Searching hybrid pgvector + BM25 index... ",
        "Found 3 verified policy matches. ",
        "Drafting cited response for stakeholder review.",
    ]
    for token in tokens:
        yield f"data: {json.dumps({'token': token})}\n\n"
        await asyncio.sleep(0.15)
    yield "data: [DONE]\n\n"


@app.post("/api/v1/pilot/query")
async def query_pilot(req: PilotQueryRequest) -> StreamingResponse:
    return StreamingResponse(stream_pilot_answer(req), media_type="text/event-stream")
