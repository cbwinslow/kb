# Tasks: Dense Embedding Pipeline & Zotero Watcher Service

## 1. Local Dense Embedding Pipeline

- [x] 1.1 Add `sentence-transformers` dependency to `pyproject.toml` and verify resolution with `uv sync`
- [x] 1.2 Implement `LocalEmbeddingGenerator` and `EmbeddingProtocol` in `src/kb/storage/embeddings.py` supporting `BAAI/bge-m3` with CUDA acceleration and batching
- [x] 1.3 Implement unit tests in `tests/test_embeddings.py` verifying 1024-d vector output, normalization, and mock fallback

## 2. Ingestion Pipeline Vectorization & Backfill

- [x] 2.1 Integrate batch embedding generation into `kb ingest` pipeline in `src/kb/cli.py` populating `kb_chunks.embedding`
- [x] 2.2 Implement CLI command `kb embed` (`--all` or `--citekey <key>`) in `src/kb/cli.py` to backfill missing chunk embeddings
- [x] 2.3 Verify vector backfill and database persistence asserting non-null vectors in PostgreSQL

## 3. Hybrid Search Vectorization & MCP Integration

- [x] 3.1 Update `HybridSearchEngine` in `src/kb/storage/search.py` to vectorize input queries and execute cosine similarity ranking
- [x] 3.2 Update FastMCP tool `kb_search_literature` in `src/kb/mcp/server.py` to generate query embeddings and execute true dense + sparse RRF fusion
- [x] 3.3 Verify hybrid search retrieval in `tests/test_mcp.py` asserting fused rankings on real vector embeddings

## 4. Zotero Watcher Daemon & Auto-Ingestion

- [x] 4.1 Implement `ZoteroWatcher` in `src/kb/zotero/watcher.py` tracking `zotero.sqlite` modification timestamps and managing `.zotero_sync_state.json` cursor
- [x] 4.2 Implement auto-ingestion dispatching pipeline execution for newly detected PDF attachments
- [x] 4.3 Implement CLI command `kb zotero watch` (`--interval N`) and verify watcher polling and item dispatch in `tests/test_watcher.py`

## Workflow follow-up

- Validate all OpenSpec artifacts with `openspec validate embeddings-and-zotero-sync`.
- Archive the change after implementation and test verification are complete.
