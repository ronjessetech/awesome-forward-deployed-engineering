# 48-Hour FDE Rapid Prototyping Grading Rubric

During FDE technical assessments or fellowship sprints, evaluators grade on **production pragmatism, integration speed, and clarity**—not clever one-liners. Aim for **85+ / 100** across these 5 dimensions:

| Category | Weight | What Top 5% Candidates Do | Common Red Flags |
| :--- | :---: | :--- | :--- |
| **1. Integration & Data Correctness** | 25% | Strict input validation (`Pydantic`/`Zod`), handles null/dirty client fields gracefully, deterministic idempotent writes. | Unhandled `KeyError` / `TypeError` on dirty rows; silent data drops. |
| **2. API & Failure Resiliency** | 25% | Timeouts on every outbound HTTP call, clear HTTP status codes (`400`, `422`, `502`), retry/backoff on transient upstream errors. | No request timeouts; swallowing exceptions with bare `except: pass`. |
| **3. Security & Tenant Hygiene** | 20% | Parameterized SQL queries, env-based secrets (never hardcoded), tenant scoping enforced server-side, CORS restricted. | Raw SQL string interpolation; committing `.env` files or API keys. |
| **4. Reproducibility & Packaging** | 15% | One-command startup (`docker compose up`), multi-stage Dockerfile, clear `.env.example`, `/health` endpoint. | "Works on my machine" with undocumented local setup steps. |
| **5. Executive Clarity & Docs** | 15% | Crisp `README.md` with architecture diagram, known limitations, trade-offs made for speed, and how to test in 60 seconds. | Wall of unformatted text or zero instructions on how to demo. |
