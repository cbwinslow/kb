# Design: Dense Embedding Pipeline & Zotero Watcher Service

## Context

The initial knowledge base implementation established neural PDF parsing, formula extraction, tabular extraction, and PostgreSQL 16 storage on `cbwdellr720`. However, `kb_chunks.embedding` is currently populated with synthetic or null vectors, and new papers must be ingested manually. 

This design establishes:
1. Local GPU-accelerated dense embedding generation on `cbwwin` (NVIDIA RTX 3060 12GB VRAM) using `BAAI/bge-m3`.
2. A lightweight Zotero library watcher daemon that detects newly attached PDFs in `zotero.sqlite` and triggers the ingestion pipeline automatically.

## Goals / Non-Goals

**Goals:**
- Provide `LocalEmbeddingGenerator` generating 1024-dimensional vectors with batching and CUDA acceleration (CPU fallback).
- Embed all document chunks during `kb ingest` and store vectors in PostgreSQL `kb_chunks.embedding`.
- Compute query embeddings in `kb_search_literature` to enable true hybrid dense cosine similarity and sparse full-text retrieval.
- Provide `ZoteroWatcher` to poll `zotero.sqlite` for new papers and attachments and dispatch ingestion.
- Provide CLI commands: `kb embed <citekey|--all>` and `kb zotero watch`.

**Non-Goals:**
- Bi-directional synchronization to Zotero (we only read from Zotero; we do not modify the user's Zotero database).
- Training or fine-tuning embedding models (we use pre-trained `BAAI/bge-m3`).

## Decisions

### 1. Embedding Model & Framework: `sentence-transformers` with `BAAI/bge-m3`
- **Choice**: `BAAI/bge-m3` via `sentence-transformers`.
- **Rationale**:
  - `BAAI/bge-m3` natively outputs 1024-dimensional dense vectors, matching our `Vector(1024)` database column.
  - Supports an 8,192-token input context window, preventing truncation on large composite markdown chunks.
  - PyTorch is already part of the environment (used by Docling), so `sentence-transformers` leverages the existing PyTorch CUDA runtime on `cbwwin` with zero ONNX bridge overhead.
- **Alternatives Considered**:
  - `fastembed`: Fast CPU ONNX runtime, but lacks direct access to native PyTorch CUDA memory pinning on Windows.
  - OpenAI / Remote APIs: Violates local privacy/cost principles and introduces external rate limits.

### 2. Zotero Watcher Strategy: Cursor-Based Timestamp & SQLite Polling
- **Choice**: Periodic state-tracked polling of `zotero.sqlite` file modification time and query for `dateModified > last_sync_time`.
- **Rationale**:
  - Watching filesystem events directly on `zotero.sqlite` can trigger duplicate events during active Zotero WAL checkpointing (`.sqlite-wal`, `.sqlite-shm`).
  - Polling every $N$ seconds (default: 10s) with read-only URI connections (`mode=ro`) ensures zero risk of SQLite locks or contention with the running Zotero application.
  - State cursor persisted in `.zotero_sync_state.json` under `data/` prevents re-ingesting existing papers across restarts.

### 3. Asynchronous Query Embedding in FastMCP Server
- **Choice**: Lazy initialization of `LocalEmbeddingGenerator` in `src/kb/storage/search.py` and `src/kb/mcp/server.py`.
- **Rationale**:
  - Avoids loading the 2.2 GB embedding model into GPU VRAM if an agent is only running formula or BibTeX queries.
  - Generates query embedding only when `kb_search_literature` is called with semantic text.

## Risks / Trade-offs

- **[Risk] Cold-start latency on first embedding model load**:
  - *Mitigation*: Lazy-load singleton instance so the model loads once and stays in VRAM for subsequent queries.
- **[Risk] VRAM contention during heavy concurrent ingestion**:
  - *Mitigation*: Sequential pipeline execution (`DoclingParser` releases temporary tensors before `LocalEmbeddingGenerator` batches chunks). Total combined VRAM footprint is < 6 GB, well within the 12 GB available on the RTX 3060.
- **[Risk] Hermetic CI test execution without downloading 2.2GB model**:
  - *Mitigation*: Define an `EmbeddingProtocol` allowing unit tests to inject a deterministic in-memory mock embedder returning unit vectors.

## Migration Plan

1. Install `sentence-transformers` in `pyproject.toml`.
2. Backfill existing chunks: run `kb embed --all` to populate embeddings for already ingested papers (`miller2005`, `jensen2009`).
3. Create HNSW vector index on PostgreSQL 16 on `cbwdellr720` for sub-millisecond approximate nearest neighbor retrieval:
   ```sql
   CREATE INDEX IF NOT EXISTS ix_kb_chunks_embedding_hnsw 
   ON kb_chunks USING hnsw (embedding vector_cosine_ops);
   ```
