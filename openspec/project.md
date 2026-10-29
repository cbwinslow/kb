# kb — Scientific Knowledge Base & Research Engine

## 1. Project Purpose & Vision
`kb` is an **Evidence-to-Code Scientific Knowledge Base and Research Engineering Engine**. It bridges the gap between academic literature (PDFs, preprints, conference proceedings, textbooks) and production quantitative code.

While built to power domain libraries like `sabermetricspy`, `kb` is fully domain-agnostic and scales from initial collections (~1,000 papers) to 10,000+ papers across multiple research fields (sports science, economics, machine learning, computational mathematics).

### Core Workflow: Evidence-to-Code
```
Academic PDF / Preprints (arXiv, OpenAlex, Zotero)
  │
  ▼ [GPU Worker on cbwwin: RTX 3060 12GB]
Docling / Marker Multimodal Parsing
  ├── Pristine LaTeX Equations ($$ ... $$) ──► SymPy Parsing & AST Validation
  ├── Tables & Baselines ────────────────────► Clean Parquet / CSV Golden Fixtures
  └── Companion Repos & Code ────────────────► Archived Scripts & Notebooks
  │
  ▼ [Homelab Vault: cbwdellr720]
PostgreSQL 16 + pgvector + tsvector
  ├── Hybrid Semantic / Keyword Search (RRF)
  ├── Structured Bibliographic Metadata & BibTeX
  └── Document Chunks & Knowledge Graph Entities
  │
  ▼ [MCP & CLI Interfaces]
FastMCP Server (LAN / ZeroTier)
  ├── kb_search_literature
  ├── kb_get_formula (LaTeX + Python AST)
  ├── kb_get_benchmark_table
  └── kb_get_bibtex
```

---

## 2. Infrastructure & Hardware Architecture

### Workstation (`cbwwin`) — The High-Compute Ingest Worker
* **Hardware**: Dedicated NVIDIA RTX 3060 (12GB VRAM), CUDA acceleration.
* **Responsibilities**:
  * GPU-accelerated document layout analysis and OCR using IBM Docling / Marker.
  * Formula extraction and SymPy validation.
  * Dense vector embedding generation (`BAAI/bge-m3` in FP16).
  * Direct CLI operations and developer workflows.

### Homelab (`cbwdellr720`) — The 24/7 Central Vault & Database
* **Hardware**: Dell PowerEdge R720, bare-metal PostgreSQL 16.
* **Network**: Private IP, ZeroTier mesh, direct high-speed cable.
* **Responsibilities**:
  * PostgreSQL 16 with `pgvector` for vector similarity and `pg_trgm` / `tsvector` for lexical search.
  * File storage for original PDFs, parsed markdown, and golden dataset fixtures (Parquet).
  * Persistent FastMCP server daemon for always-on agent queries.

---

## 3. Core Architecture & Tech Stack

* **Document Parsing**: IBM Docling (`docling`) with PyTorch / CUDA acceleration.
* **Symbolic Math Engine**: `sympy` (`sympy.parsing.latex`) for mathematical verification and Python AST generation.
* **Embeddings & Search**: `BAAI/bge-m3` (dense vectors + sparse lexical weights) with Reciprocal Rank Fusion (RRF) in PostgreSQL.
* **Relational & Vector Store**: PostgreSQL 16 + `pgvector` via `SQLAlchemy 2.0` (async) and `asyncpg`.
* **Agent Integration**: `FastMCP` (Model Context Protocol) with dynamic AST compilation and live calculation execution.
* **Bibliographic Truth**: Zotero local SQLite / Web API integration with Better BibTeX citation keys.
* **Code Generation**: Standalone formula library (`kb-formulas`) with typed Python and Polars expressions.
* **Storage Protocol**: Direct encrypted SSH/SFTP synchronization to homelab vault with automatic workstation disk space protection.
* **Semantic Symbol Ontology**: `SymbolOntology` managing canonical concept registries, author variable aliases, and zero-copy DataFrame column binding for Polars/Pandas.
* **Equation Chaining & Solver**: `FormulaChainingEngine` providing recursive cross-paper variable substitution, closed-form equation generation, and simultaneous linear system solving via SymPy.
* **Web Glossary Harvester**: `WebGlossaryHarvester` for ingesting HTML web articles and canonical sabermetric glossaries (FanGraphs, Tom Tango) into clean Markdown with LaTeX math preservation.
* **Knowledge Graph & GraphQL**: Multi-layer relational GraphQL API schema (`strawberry-graphql`) connecting Documents, Formulas, Variables, Canonical Concepts, Benchmark Tables, and Derivation Chains.
* **Formula Coverage & Repair**: `FormulaCoverageAnalyzer` and `CorpusFormulaRepairer` auditing formula yield, symbol utilization (LHS vs RHS), non-ASCII character distributions, and progressive in-place AST recovery.
* **Interactive Web Dashboard**: Starlette web application (`kb ui serve`) with interactive Lineage DAG, Formula Playground with parameter sensitivity curves, Knowledge-to-Code generator, and Coverage Scorecard.
* **Observability & QA**: Centralized rotating structured logging, execution telemetry, and ground-truth numerical accuracy verification.
* **Benchmarking Engine**: `PerformanceBenchmarker` measuring scalar vs. Polars throughput, embedding latency, and corpus quality yields.
* **Package Management**: `uv`.
* **Quality Gates**: `ruff` (linting & formatting), `pyright` (strict typing), `pytest` (test suite).
* **Architecture Decisions**: Fully documented in [`docs/DECISIONS.md`](../docs/DECISIONS.md).
