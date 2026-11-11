# 48-Hour FDE Prototype Starter Stack

A clean, production-minded boilerplate for shipping client pilots fast:
- **FastAPI (Python 3.12)** with strict Pydantic schemas, SSE streaming endpoint, and built-in circuit breaker helper
- **PostgreSQL 16 + `pgvector`** ready for multi-tenant relational + hybrid vector retrieval
- **Redis 7** ready for rate-limiting, caching, and dead-letter ingestion queues

## Quickstart (60 Seconds)

```bash
docker compose up --build
```

Then verify the API:
- Health check: `http://localhost:8000/health`
- Interactive OpenAPI Docs: `http://localhost:8000/docs`
- Test SSE stream:
  ```bash
  curl -N -X POST http://localhost:8000/api/v1/pilot/query \
    -H "Content-Type: application/json" \
    -d '{"tenant_id": "acme-corp", "query": "Summarize Q3 SLA exceptions"}'
  ```
