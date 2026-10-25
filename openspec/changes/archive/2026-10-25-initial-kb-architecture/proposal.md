# Proposal: Initial Architecture for Scientific Knowledge Base (kb)

## Why
Scientific code development—such as in `sabermetricspy`—requires grounding implementations in verified peer-reviewed literature, exact mathematical formulas, and published benchmark tables. Existing RAG and document tools (e.g. generic chat-with-PDF systems) fail in scientific domains: they garble LaTeX mathematical equations, mangle tabular empirical matrices, lack citation provenance graphs, and cannot be programmatically queried by coding agents.

`kb` solves this by introducing an **Evidence-to-Code Scientific Knowledge Base & Research Engine**. It automates the extraction of pristine LaTeX formulas, verifies their mathematical syntax via SymPy, transforms empirical tables into Parquet golden test fixtures, and indexes papers in a hybrid PostgreSQL/pgvector store accessible directly via FastMCP.

## What Changes
- **New Project Structure**: Initialize `kb` repository under `c:\Users\blain\projects\kb` with `uv`, strict typing (`pyright`), linting (`ruff`), and testing (`pytest`).
- **GPU Ingestion Pipeline**: Implement high-fidelity document layout parsing using IBM Docling accelerated by NVIDIA CUDA (RTX 3060 12GB VRAM on `cbwwin`).
- **LaTeX Math & AST Engine**: Build formula parser that isolates KaTeX/LaTeX equations, checks syntactic validity via SymPy, and emits executable Python expressions.
- **Golden Benchmark Extractor**: Transform extracted paper tables into clean Parquet and CSV fixtures linked to BibTeX citekeys.
- **PostgreSQL 16 + pgvector Hybrid Store**: Connect to bare-metal PostgreSQL 16 on `cbwdellr720` for dense vector storage (`BAAI/bge-m3`) and full-text keyword retrieval (`tsvector` / `pg_trgm`) with Reciprocal Rank Fusion (RRF).
- **FastMCP Agent Service**: Expose standard Model Context Protocol tools (`kb_search_literature`, `kb_get_formula`, `kb_get_benchmark_table`, `kb_get_bibtex`) for pair programming in Antigravity and Claude.
- **Zotero Integration**: Enable synchronization of local Zotero collections, PDF attachments, and Better BibTeX citation keys.

## Capabilities

### New Capabilities
- `document-ingestion`: GPU-accelerated PDF parsing (IBM Docling) converting academic papers into Markdown with preserved LaTeX equations, structural headings, and tables.
- `formula-verification`: Extraction and AST validation of LaTeX formulas using SymPy, checking dimensional consistency and generating executable Python representations.
- `benchmark-extraction`: Tabular data extraction transforming empirical baseline tables into versioned Parquet/CSV datasets for unit test fixtures.
- `hybrid-search`: Storage, dense vector indexing (`pgvector` with `bge-m3`), and BM25/trigram full-text retrieval over PostgreSQL 16 with Reciprocal Rank Fusion.
- `mcp-server`: FastMCP server exposing structured tools for coding assistants over stdio and network (LAN/ZeroTier).
- `zotero-sync`: Automated ingestion and synchronization from local Zotero SQLite database and Better BibTeX library.

### Modified Capabilities
*(None; initial project bootstrap)*

## Impact
- **New Codebase**: Establishes `kb` as a dedicated, standalone repository in `c:\Users\blain\projects\kb`.
- **Downstream Consumer**: `sabermetricspy` and future quantitative projects will ingest formulas, citations, and golden datasets via `kb`'s FastMCP tools.
- **Hardware Integration**: Utilizes `cbwwin`'s RTX 3060 for batch parsing and `cbwdellr720`'s bare-metal PostgreSQL 16 for persistent storage.
