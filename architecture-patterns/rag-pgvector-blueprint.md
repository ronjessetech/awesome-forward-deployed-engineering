# Hybrid RAG + `pgvector` Enterprise Blueprint

Enterprise clients rarely want a generic chatbot—they want **verifiable, tenant-isolated answers** over messy internal documents (PDFs, SOPs, compliance policies, ticket logs) with citations and sub-2-second time-to-first-token (TTFT).

---

## 1. PostgreSQL + `pgvector` Schema (Multi-Tenant Ready)

Always enforce `tenant_id` filtering **inside the SQL query**, never in application memory after retrieval.

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE document_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id TEXT NOT NULL,
    document_name TEXT NOT NULL,
    section_title TEXT DEFAULT '',
    content TEXT NOT NULL,
    content_tsv tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED,
    embedding vector(1536) NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Fast approximate nearest neighbor search
CREATE INDEX idx_chunks_embedding_hnsw
    ON document_chunks USING hnsw (embedding vector_cosine_ops);

-- Fast lexical keyword search (critical for SKUs, error codes, legal clause IDs)
CREATE INDEX idx_chunks_tsv_gin
    ON document_chunks USING gin (content_tsv);

-- Tenant partitioning filter
CREATE INDEX idx_chunks_tenant
    ON document_chunks (tenant_id);
```

---

## 2. Why Hybrid Search (Vector + BM25) Beats Pure Vector Search

Pure semantic embeddings struggle on exact enterprise strings like:
- Part numbers (`SKU-9942-B`)
- Invoice / Contract IDs (`PO-2026-884`)
- Specific compliance regulations (`ISO 26262 ASIL-D`)

Combining **HNSW cosine similarity** with **PostgreSQL full-text search** via **Reciprocal Rank Fusion (RRF)** solves both semantic meaning and exact-token matching inside a single database:

```sql
WITH semantic_search AS (
    SELECT id,
           ROW_NUMBER() OVER (ORDER BY embedding <=> $2) AS rank
    FROM document_chunks
    WHERE tenant_id = $1
    ORDER BY embedding <=> $2
    LIMIT 25
),
keyword_search AS (
    SELECT id,
           ROW_NUMBER() OVER (ORDER BY ts_rank_cd(content_tsv, plainto_tsquery('english', $3)) DESC) AS rank
    FROM document_chunks
    WHERE tenant_id = $1
      AND content_tsv @@ plainto_tsquery('english', $3)
    LIMIT 25
)
SELECT
    c.id,
    c.document_name,
    c.section_title,
    c.content,
    COALESCE(1.0 / (60 + s.rank), 0.0) + COALESCE(1.0 / (60 + k.rank), 0.0) AS rrf_score
FROM document_chunks c
LEFT JOIN semantic_search s ON c.id = s.id
LEFT JOIN keyword_search k ON c.id = k.id
WHERE s.id IS NOT NULL OR k.id IS NOT NULL
ORDER BY rrf_score DESC
LIMIT 6;
```

---

## 3. FDE Production Checklist Before Client Demo
- **Chunking:** Preserve structural boundaries (headers, markdown tables) using 400–600 token chunks with 15% overlap.
- **Citations:** Return `[Source: document_name, section_title]` metadata alongside every generated claim.
- **Abstention Guard:** Prompt the model to explicitly reply *"Not found in verified client records"* when retrieved context falls below threshold.
- **Streaming:** Stream tokens over **Server-Sent Events (SSE)** so client stakeholders see immediate responsiveness.
- **Evaluation:** Curate 25 gold-standard Q&A pairs from the client's domain expert and track *Retrieval Recall@5* and *Faithfulness* before going live.
