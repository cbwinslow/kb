# Proposal: Dense Embedding Pipeline & Zotero Watcher Service

## Why

While the initial knowledge base architecture established neural PDF layout parsing, formula AST extraction, benchmark extraction, and PostgreSQL 16 relational storage, semantic vector retrieval currently relies on keyword matching without live dense vector embeddings, and ingestion requires manual CLI commands. To achieve fully autonomous grounding for scientific software development, the knowledge base must:
1. Generate high-fidelity 1024-dimensional dense semantic embeddings using local GPU inference (`BAAI/bge-m3` on the NVIDIA RTX 3060 12GB workstation `cbwwin`) for both document chunks and search queries.
2. Provide a background watcher daemon for local Zotero libraries (`zotero.sqlite`) that detects newly cataloged papers and attachments, automatically executing the end-to-end ingestion pipeline into PostgreSQL 16 on `cbwdellr720`.

## What Changes

- Add a local GPU-accelerated embedding inference pipeline in `src/kb/storage/embeddings.py` wrapping `sentence-transformers` / `BAAI/bge-m3` with CUDA acceleration and multi-threaded CPU fallback.
- Integrate embedding computation into `kb ingest` to populate `kb_chunks.embedding` (`Vector(1024)`).
- Update `HybridSearchEngine` in `src/kb/storage/search.py` and the FastMCP tool `kb_search_literature` to embed incoming text queries and execute true cosine vector search against PostgreSQL 16.
- Implement `ZoteroWatcher` daemon in `src/kb/zotero/watcher.py` to monitor `zotero.sqlite` modifications, compute library diffs, and dispatch automatic ingestion for newly attached PDFs.
- Add CLI commands: `kb embed <citekey|--all>` and `kb zotero watch`.

## Capabilities

### Modified Capabilities

- `hybrid-search`: Adds automated 1024-d dense embedding generation for ingested chunks and query vectors using local GPU inference (`BAAI/bge-m3`).
- `zotero-sync`: Adds background library monitoring and automated ingestion triggering for newly added research papers and attachments.

## Impact

- **Dependencies**: Adds `sentence-transformers` and `torch` with CUDA acceleration in `pyproject.toml`.
- **Database**: Populates `kb_chunks.embedding` with live float vectors and builds HNSW index on `cbwdellr720`.
- **Performance**: Embeds chunks locally on `cbwwin` utilizing the RTX 3060 12GB VRAM before streaming records to `cbwdellr720`.
- **Agent Service**: `kb_search_literature` MCP tool achieves true hybrid semantic retrieval combining BGE-M3 dense similarity and PostgreSQL `tsvector` sparse BM25 ranking.
