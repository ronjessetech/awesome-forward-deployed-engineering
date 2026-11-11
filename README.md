# Awesome Forward Deployed Engineering (FDE) Roadmap 🚀

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Official Pre-Fellowship Hub](https://img.shields.io/badge/Official_Pre--Fellowship_Hub-Flugelsoft_Academy-4F46E5?style=for-the-badge)](https://flugelsoft-academy.flugelsoft.com/roadmap?utm_source=github&utm_medium=awesome_fde&utm_campaign=badge)
[![Test Your Readiness](https://img.shields.io/badge/Test_Your_Readiness-Interactive_Checklist_%26_Quiz-10B981?style=for-the-badge)](https://flugelsoft-academy.flugelsoft.com/roadmap?utm_source=github&utm_medium=awesome_fde&utm_campaign=quiz)

> A curated 2026 playbook, system architecture reference, interview prep guide, and starter stack for **Forward Deployed Engineers (FDE)** — the high-impact hybrid engineering role pioneered by Palantir, OpenAI, Scale AI, and Databricks ($145k–$210k+ compensation).

---

## Contents

- [What is a Forward Deployed Engineer?](#what-is-a-forward-deployed-engineer)
- [Traditional SWE vs. Forward Deployed Engineer](#traditional-swe-vs-forward-deployed-engineer)
- [The 4 Technical Pillars of FDE](#the-4-technical-pillars-of-fde)
- [12-Week FDE Skill Roadmap](#12-week-fde-skill-roadmap)
- [Enterprise Architecture Patterns](#-enterprise-architecture-patterns)
- [FDE Interview & Discovery Prep](#-fde-interview--discovery-prep)
- [48-Hour Client MVP Starter Stack](#-48-hour-client-mvp-starter-stack)
- [Curated Free Learning Resources](#-curated-free-learning-resources)
- [Non-Tech & Domain-Switcher On-Ramp](#-non-tech--domain-switcher-on-ramp)
- [Fellowship & Verified Portfolios](#-fellowship--verified-portfolios)
- [Contributing](#contributing)

---

## What is a Forward Deployed Engineer?

Most software engineers build generalized product features from an internal sprint backlog for hypothetical future users.

A **Forward Deployed Engineer (FDE)** operates at the intersection of deep full-stack/AI engineering and live enterprise problem-solving. Embedded directly with strategic customers, FDEs:
- Lead technical discovery with customer engineering leaders and domain operators.
- Integrate messy real-world data (legacy SQL servers, unstructured PDFs, rate-limited ERPs).
- Ship functional production prototypes and domain-adapted AI pipelines in **48–72 hours**, then harden them for zero-trust VPC or on-premise deployment.

---

## Traditional SWE vs. Forward Deployed Engineer

| Dimension | Traditional SWE | Forward Deployed Engineer (FDE) |
| :--- | :--- | :--- |
| **Primary Workflow** | Internal Jira tickets & platform roadmaps | Direct client discovery & custom integration bridges |
| **Feedback Loop** | Quarterly release cycles | 48–72 hour prototypes & live stakeholder demos |
| **Tech Stack** | Deep specialization in one layer | Pragmatic polyglot (`Python`, `TypeScript`, `SQL`, `Docker`, `RAG`) |
| **Data Reality** | Clean internal schemas | Messy enterprise CSVs, legacy DBs & flaky external APIs |
| **Interview Filter** | Abstract algorithmic puzzles | API integration speed, architecture judgment & communication |
| **Domain Advantage** | Mostly pure CS fundamentals | Finance, healthcare, ops & logistics backgrounds are superpowers |

> 🎯 **Track your readiness interactively:** Use the free **[5-Phase Readiness Checklist & Career Matcher Quiz](https://flugelsoft-academy.flugelsoft.com/roadmap?utm_source=github&utm_medium=awesome_fde&utm_campaign=table_cta)** on Flugelsoft Academy.

---

## The 4 Technical Pillars of FDE

1. **Enterprise APIs & Systems Integration** — OpenAPI contracts, REST & gRPC, OAuth2/OIDC/SAML SSO, webhooks, idempotency, retries, and circuit breakers.
2. **Applied AI & Rapid Prototyping** — FastAPI async backends, React streaming UIs, `pgvector` hybrid RAG pipelines, structured JSON tool calling, and evaluation harnesses.
3. **Resilient Data Ingestion Pipelines** — Schema normalization, Pydantic/Zod validation, PostgreSQL indexing, and Redis dead-letter queues.
4. **Client VPC Deployment & Zero-Trust** — Multi-stage Dockerfiles, Docker Compose / Kubernetes manifests, secrets hygiene, and least-privilege network isolation.

---

## 12-Week FDE Skill Roadmap

### Weeks 1–3: Polyglot Core & Containerization
- [ ] Async Python microservices with **FastAPI** and strict **Pydantic** schemas
- [ ] Modern **TypeScript** & **React** component prototyping for fast client dashboards
- [ ] Linux shell streams (`stdin`/`stdout`, permissions), clean Git rebasing, and multi-stage **Docker** builds

### Weeks 4–6: Enterprise Data Bridges & Resiliency
- [ ] Relational modeling, B-Tree indexing, and SQL `JOIN` / aggregation tuning in **PostgreSQL**
- [ ] Building fault-tolerant external API connectors with exponential backoff, jitter, and circuit breakers
- [ ] Implementing **OAuth2 / OIDC** auth flows, token refresh, and tenant-scoped RBAC

### Weeks 7–9: Applied AI & Domain RAG Systems
- [ ] Hybrid semantic + keyword retrieval with **pgvector** and custom document chunking
- [ ] Server-Sent Events (SSE) streaming responses and structured tool execution
- [ ] Evaluation benchmarks to measure retrieval precision and prevent hallucinations

### Weeks 10–12: Client Packaging & Stakeholder Discovery
- [ ] Packaging full stacks via `docker-compose` and Kubernetes manifests for private client VPCs
- [ ] Leading 30-minute technical discovery sessions and scannable whiteboard architecture reviews
- [ ] Delivering crisp, 10-minute live executive stakeholder demos

---

## 🏗️ Enterprise Architecture Patterns

Production-oriented technical blueprints included directly in this repository:

- [**Hybrid RAG + `pgvector` Blueprint**](./architecture-patterns/rag-pgvector-blueprint.md) — Schema design, Reciprocal Rank Fusion (RRF), SSE streaming, and RAG evaluation loops.
- [**Enterprise OAuth2, SAML SSO & Multi-Tenant RBAC**](./architecture-patterns/enterprise-oauth2-sso.md) — Designing secure tenant isolation, JWKS verification, and audit logging.
- [**Resilient API Connectors & Data Bridges**](./architecture-patterns/resilient-api-connectors.md) — Idempotency keys, circuit breakers, exponential backoff with jitter, and dead-letter queues.

---

## 💼 FDE Interview & Discovery Prep

- [**30-Minute Client Technical Discovery Script**](./interview-prep/technical-discovery-script.md) — Discovery questions, scoping 48-hour pilots, and avoiding scope creep.
- [**Enterprise FDE System Design Scenarios**](./interview-prep/system-design-scenarios.md) — 8 real-world enterprise integration & AI architecture prompts with design checklists.
- [**48-Hour Rapid Prototyping Grading Rubric**](./interview-prep/live-coding-rubric.md) — How engineering panels score FDE live-coding & take-home exercises.

---

## ⚡ 48-Hour Client MVP Starter Stack

Jump straight into building an FDE prototype using the included boilerplate:
- [**FastAPI + PostgreSQL (`pgvector`) + Redis + Docker Starter**](./starter-templates/fastapi-react-docker-starter/README.md) — Includes health endpoints, Pydantic contracts, SSE streaming pattern, and a reusable circuit-breaker client.

---

## 📚 Curated Free Learning Resources

### Polyglot Core & Architecture
- [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/) — Async Python APIs & automatic OpenAPI schemas
- [The TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) — Strict type narrowing, generics & utility types
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) — Relational design, ACID transactions & query plans
- [Docker Get Started](https://docs.docker.com/get-started/) — Multi-stage builds, networking & Compose

### Enterprise Integration & Distributed Systems
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/) — Asynchronous messaging, routers & idempotent receivers
- [System Design Primer](https://github.com/donnemartin/system-design-primer) — Load balancing, caching, queues & trade-offs
- [Redis University](https://university.redis.io/) — Rate limiting, Pub/Sub & in-memory caching patterns
- [Full Stack Open](https://fullstackopen.com/en/) — End-to-end modern web client-server communication

---

## 🌱 Non-Tech & Domain-Switcher On-Ramp

Coming from **finance, healthcare, operations, mechanical engineering, or another non-CS domain**? Domain fluency is a massive advantage in Forward Deployed Engineering because enterprise clients hire FDEs who actually understand their business workflows.

- Start with **no terminal or local setup** via the **[Phase 0 Browser Sandbox Guide & Plain-English Jargon Demystifier](https://flugelsoft-academy.flugelsoft.com/roadmap?utm_source=github&utm_medium=awesome_fde&utm_campaign=nontech)**.
- Take the **[2-Minute Career Matcher Quiz](https://flugelsoft-academy.flugelsoft.com/roadmap?utm_source=github&utm_medium=awesome_fde&utm_campaign=quiz_bottom)** to see how your background maps to FDE, Data, SDET, or Full-Stack roles.

---

## 🎓 Fellowship & Verified Portfolios

If you want structured 1-on-1 mentorship from Staff Engineers, line-by-line PR rubric audits, live client discovery simulations, and a **Public Verified Portfolio (0–100 Job Readiness Index)**:

- **[Explore the 12-Week FDE Fellowship Track](https://flugelsoft-academy.flugelsoft.com/?utm_source=github&utm_medium=awesome_fde)**
- **[View the Interactive FDE Role Roadmap](https://flugelsoft-academy.flugelsoft.com/roadmap?utm_source=github&utm_medium=awesome_fde)**
- **[Apply for Cohort Admissions / 100% Merit Grant](https://flugelsoft-academy.flugelsoft.com/register?role=Student&utm_source=github&utm_medium=awesome_fde)**

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before opening a pull request with new architecture patterns, interview scenarios, or verified open-source tools.

## License

Released under the [MIT License](./LICENSE).
