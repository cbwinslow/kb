# Tasks: Initial Architecture for Scientific Knowledge Base (kb)

## 1. Project Scaffolding & Core Configuration

- [x] 1.1 Configure `pyproject.toml` with dependencies (`docling`, `fastmcp`, `pydantic`, `sqlalchemy`, `asyncpg`, `pgvector`, `sympy`, `pyarrow`, `pytest`, `ruff`, `pyright`) and verify dependency resolution with `uv sync`
- [x] 1.2 Establish package module layout (`src/kb/ingest`, `src/kb/math`, `src/kb/storage`, `src/kb/mcp`, `src/kb/zotero`) and verify imports succeed with empty `__init__.py` files
- [x] 1.3 Configure code quality tooling (`ruff.toml` or `[tool.ruff]` in `pyproject.toml`, strict `pyright` settings) and verify `uv run ruff check .` passes cleanly

## 2. Document Ingestion & Parsing Engine

- [x] 2.1 Implement `DoclingParser` wrapping IBM Docling pipeline with CUDA/GPU acceleration fallback on `cbwwin` and verify PDF-to-Markdown conversion on sample paper
- [x] 2.2 Implement structural document chunker wrapping Docling's AST `HybridChunker` with atomic math block and table preservation and heading breadcrumb enrichment (`[Document | Citekey | Section]`)
- [x] 2.3 Implement unit and invariant tests in `tests/test_ingest.py` asserting math delimiter balance, table integrity, and breadcrumb lineage, verified with `uv run pytest tests/test_ingest.py`

## 3. Formula Extraction & Symbolic Verification

- [x] 3.1 Implement `FormulaExtractor` to scan Markdown chunks for LaTeX math blocks and parse them into SymPy symbolic expressions
- [x] 3.2 Implement equation sanitizer to repair common OCR delimiter glitches and verify with parameterized unit tests in `tests/test_formula.py`
- [x] 3.3 Implement Python AST generator that emits executable Python lambdas/functions from validated SymPy expressions and verify execution on baseball formulas (e.g. Pythagorean expectation)

## 4. Benchmark & Tabular Fixture Extractor

- [x] 4.1 Implement `TableExtractor` to convert extracted Markdown and HTML tables into typed PyArrow / Polars DataFrames
- [x] 4.2 Implement Parquet and CSV export linking datasets to BibTeX citekeys in `data/fixtures/` and verify integrity via unit test in `tests/test_benchmark.py`

## 5. Storage Layer & Hybrid Search (PostgreSQL + pgvector)

- [x] 5.1 Define SQLAlchemy 2.0 async models (`Document`, `Chunk`, `Formula`, `BenchmarkTable`) supporting `pgvector` vector columns and `tsvector` full-text search
- [x] 5.2 Implement database connection manager supporting `KB_DATABASE_URL` targeting PostgreSQL 16 on `cbwdellr720` and verify connection handshake
- [x] 5.3 Implement hybrid retrieval function combining dense cosine similarity and sparse keyword ranking via Reciprocal Rank Fusion (RRF) and verify with integration test

## 6. FastMCP Agent Service

- [x] 6.1 Implement FastMCP server entrypoint in `src/kb/mcp/server.py` defining `kb_search_literature`, `kb_get_formula`, `kb_get_benchmark_table`, and `kb_get_bibtex`
- [x] 6.2 Implement CLI entrypoint (`kb mcp serve` and `kb ingest <target>`) via `click` or `argparse`
- [x] 6.3 Register `kb` server in global `mcp_config.json` and verify tool listing via MCP inspector / test harness

## 7. Zotero Synchronization

- [x] 7.1 Implement `ZoteroReader` to discover local Zotero SQLite library and extract collections, item metadata, and linked PDF file paths
- [x] 7.2 Implement Better BibTeX citekey parser linking local library items to canonical keys and verify with unit tests in `tests/test_zotero.py`

## Workflow follow-up

- Validate all OpenSpec artifacts with `openspec validate initial-kb-architecture`.
- Archive the change after implementation and test verification are complete.
