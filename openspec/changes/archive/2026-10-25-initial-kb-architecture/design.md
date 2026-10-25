# Design: Initial Architecture for Scientific Knowledge Base (kb)

## Context
See `proposal.md` for overall motivation. The design operates across two distinct hardware machines:
1. `cbwwin` (workstation with NVIDIA RTX 3060 12GB VRAM): runs local compute-heavy document layout models (Docling), SymPy formula AST extraction, and embedding model inference.
2. `cbwdellr720` (homelab server with bare-metal PostgreSQL 16): acts as the persistent vault, hosting relational metadata, vector embeddings (`pgvector`), original PDFs, extracted fixtures, and running the FastMCP daemon.

## Goals / Non-Goals

**Goals:**
- Provide a clean, modular Python codebase managed by `uv` with strict type checking (`pyright`) and linting (`ruff`).
- Deliver end-to-end document parsing that preserves inline/display LaTeX math (`$$...$$`) and table matrices using IBM Docling.
- Enable symbolic algebraic verification of formulas via SymPy, translating them into executable Python ASTs.
- Provide a database layer (SQLAlchemy 2.0 async + `asyncpg` + `pgvector`) supporting hybrid Reciprocal Rank Fusion (dense embeddings + sparse keyword search).
- Provide a FastMCP server implementing `kb_search_literature`, `kb_get_formula`, `kb_get_benchmark_table`, and `kb_get_bibtex`.
- Provide read-only integration with local Zotero SQLite databases and Better BibTeX citekeys.

**Non-Goals:**
- Building a custom end-user Web GUI (the system is agent-first, accessed via FastMCP and CLI; Zotero serves as the visual desktop reader).
- Direct fine-tuning or training of foundation models (we use off-the-shelf pre-trained weights for Docling and `bge-m3`).
- In-memory ephemeral vector stores (everything is persistently backed by PostgreSQL on `cbwdellr720`).

## Decisions

### 1. Document Parsing: IBM Docling over PyPDF/Marker
- **Rationale**: Docling features superior layout awareness (DocLayNet + TableFormer), correctly parsing multi-column scientific layouts, preserving KaTeX/LaTeX math delimiters, and extracting structured markdown/HTML tables.
- **Alternatives considered**:
  - *Marker*: Fast, but Docling provides cleaner programmatic JSON/Markdown models and tighter PyTorch integration.
  - *Standard PDF scrapers (pypdf/pdfminer)*: Excluded because they garble math formulas into unparseable text.

### 2. Storage & Vector Search: PostgreSQL 16 + `pgvector` + `tsvector` on `cbwdellr720`
- **Rationale**: Eliminates the overhead and fragility of running a separate vector database (e.g. Pinecone, Chroma, Qdrant). PostgreSQL bare-metal on the homelab reliably handles relational bibliographic metadata, vector embeddings with HNSW/IVFFlat indexes, and full-text inverted indexes (`tsvector`).
- **Hybrid Retrieval Algorithm**: Reciprocal Rank Fusion (RRF):
  $$\text{RRF\_Score}(d) = \frac{1}{60 + \text{rank}_{\text{dense}}(d)} + \frac{1}{60 + \text{rank}_{\text{sparse}}(d)}$$
- **Alternatives considered**:
  - *Chroma / DuckDB*: Poor multi-machine client/server concurrency; not persistent across agent sessions.

### 3. Embeddings: `BAAI/bge-m3`
- **Rationale**: Leading multilingual, multimodal open embedding model supporting dense vectors (1024-dim), sparse lexical representations, and multi-vector retrieval. Runs comfortably on the 12GB RTX 3060.
- **Alternatives considered**:
  - *text-embedding-3-small*: Requires external cloud API calls and ongoing costs; `bge-m3` is fully local and self-hosted.

### 4. Agent Interface: FastMCP (Python)
- **Rationale**: Official, standardized Model Context Protocol library with async support. Allows seamless integration into Antigravity, Claude Code, and other AI pair programmers over stdio or SSE/streamable HTTP.
- **Alternatives considered**:
  - *Custom REST API*: Requires writing custom agent client tools; FastMCP is natively recognized by agentic harnesses.

### 5. Document Chunking & Mathematical Invariant Testing Strategy
- **Scientific Chunking Failure Modes**:
  1. *Delimiter & Formula Slicing*: Fixed character/token windows cut across `$$...$$` and `\begin{align}` blocks, producing broken LaTeX that SymPy and KaTeX cannot parse.
  2. *Orphan Variable Definitions*: Formulas and parameter definitions (e.g. "$R$ is runs scored") are severed into separate chunks, destroying semantic reasoning.
  3. *Tabular Matrix Obliteration*: Slicing tables strips row keys, column headers, units, and sample sizes.
  4. *Hierarchical Amnesia*: Without section breadcrumbs (`H1 > H2 > H3`), chunks like "the second exponent is 1.83" lose all contextual meaning.
  5. *Representation Dilution*: Chunk sizes that are too large dilute dense vector embeddings (`bge-m3`), while chunks that are too small lose derivation proofs.
- **Structural Solutions Implemented in `kb`**:
  - **Docling AST `HybridChunker`**: Operates on structured `DoclingDocument` nodes rather than raw strings. Respects section hierarchies and preserves tables and math as unbreakable atomic blocks.
  - **Entity Isolation**: Formulas and Tables are extracted as first-class database entities (`Formula` with SymPy AST, `BenchmarkTable` with PyArrow/Parquet), with relational links to parent chunks and documents.
  - **Breadcrumb Context Enrichment**: Every chunk prepends `[Document: <title> | Citekey: <citekey> | Section: <H1 > H2 > H3>]` to text sent to `bge-m3` and PostgreSQL full-text search.
- **Test-and-Validate Enforcement Loop**:
  - Every ingestion pipeline stage is guarded by invariant tests in `tests/test_ingest.py`:
    - Math balance invariant (no unmatched `$` or unclosed environments).
    - Table structure invariant (no headless or sliced rows).
    - Metadata invariant (every chunk must carry heading breadcrumbs and parent citekey).
    - Complete CI verification loop: `uv run ruff check .`, `uv run pyright`, and `uv run pytest` enforced before any task is marked complete.

## Risks / Trade-offs

- **[Risk] Heavy dependency footprint for Docling / PyTorch**:
  - *Mitigation*: Separate package extras in `pyproject.toml` (e.g. `kb[ingest]` with PyTorch/Docling, and `kb[server]` or `kb[client]` for lightweight MCP querying).
- **[Risk] Scanned bitmap papers with poor OCR quality**:
  - *Mitigation*: Configure Docling's EasyOCR/Tesseract fallback pipeline when native digital font glyphs are absent.
- **[Risk] Network latency to homelab `cbwdellr720`**:
  - *Mitigation*: Connection pooling with `asyncpg`, local metadata caching on `cbwwin`, and direct high-speed cable / LAN routing.

## Open Questions

- *PostgreSQL pgvector extension setup*: Verify that `pgvector` package is installed on the bare-metal Debian/Ubuntu/RHEL OS of `cbwdellr720` (will test and document standard setup command).
