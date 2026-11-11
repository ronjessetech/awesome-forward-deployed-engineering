# Enterprise FDE System Design Scenarios

FDE interviews test **pragmatic architecture under messy constraints**, not abstract whiteboard theory. Practice sketching end-to-end data flow, failure modes, security, and 48-hour MVP vs. Week-4 production trade-offs for these 8 prompts.

---

### Scenario 1: Healthcare SOP & Claims RAG Bridge
**Prompt:** A regional healthcare network has 15,000 scanned PDF policy manuals and claims billing codes stored in SharePoint. Nurses spend 20 minutes per call searching rules.
- **Evaluate:** OCR/layout-aware chunking, preserving billing code exact tokens (Hybrid BM25 + `pgvector`), strict citation links, abstention when confidence is low, and HIPAA PII redaction.

### Scenario 2: Flaky Legacy ERP Order Sync
**Prompt:** A manufacturing client runs an on-prem ERP from 2008 that exports nightly CSVs via SFTP and has a SOAP/REST endpoint that throws 502 errors under >5 req/sec.
- **Evaluate:** Decoupled ingestion worker, rate-limited token bucket client, idempotency hashes to avoid duplicate rows on retry, Redis dead-letter queue for malformed CSV lines, and reconciliation alerting.

### Scenario 3: Air-Gapped Defense / Finance VPC Deployment
**Prompt:** A financial institution forbids outbound internet calls from production subnets. They need your analytics + AI app running completely inside their private VPC.
- **Evaluate:** Multi-stage offline Docker images pushed to private registry (ECR/ACR), self-hosted open-weights inference or private VPC endpoints, Helm/Terraform parameterization, and local log aggregation.

### Scenario 4: Multi-Tenant Customer Support Triage Copilot
**Prompt:** Build an internal triage dashboard for a SaaS company serving 400 enterprise tenants. Support agents need instant ticket summaries and suggested SQL diagnostic queries without ever leaking data across tenants.
- **Evaluate:** Server-side `tenant_id` extraction from verified OIDC JWTs, database row-level isolation or mandatory tenant predicates, parameterized read-only SQL templates (never executing raw LLM-generated arbitrary SQL against prod!).

### Scenario 5: Real-Time Factory Telemetry Anomaly Dashboard
**Prompt:** 500 IoT sensors push MQTT temperature/vibration frames every second. Plant supervisors need a React live dashboard flagging anomalies within 3 seconds.
- **Evaluate:** Lightweight ingestion buffer (Redis Streams / Kafka), time-window aggregation (TimescaleDB/PostgreSQL partitioning), WebSocket / SSE push to frontend, and backpressure handling on dashboard reconnects.

### Scenario 6: Legal Contract Redline & Diff Pipeline
**Prompt:** Legal ops receives 200 vendor contracts/week in `.docx` format and wants automated clause-by-clause risk scoring against their playbook.
- **Evaluate:** Async job queue (`202 Accepted` upload -> worker -> status polling/SSE), structured JSON schema enforcement for risk categories, human-in-the-loop approval state machine, and immutable audit logs.

### Scenario 7: Zero-Downtime Legacy DB Migration Bridge
**Prompt:** Client needs to migrate customer billing data from a legacy Oracle/SQL Server monolith to PostgreSQL while keeping both systems live for 60 days.
- **Evaluate:** Dual-write or CDC (Change Data Capture) synchronization, shadow-read verification diffing scripts, rollback toggles, and checksum reconciliation.

### Scenario 8: 48-Hour Executive Pilot Under Ambiguity
**Prompt:** An enterprise VP says *"We want AI to automate our procurement approvals"* with no spec and messy Excel spreadsheets. What do you build for Friday?
- **Evaluate:** Scoping down to 1 high-value workflow (e.g., PO line-item validation against vendor price sheet), ingesting 50 sample rows via Pydantic, building a clean 2-screen React UI showing flagged discrepancies + confidence, and leaving clean extension hooks.
