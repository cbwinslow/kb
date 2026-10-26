# Architecture Decision Records (ADRs) & Project Decisions

This document records the architectural, technical, and mathematical decisions made in the development of the **Scientific Knowledge Base (`kb`)** and its companion libraries.

---

## Index of Decisions

- [ADR-001: Hardware Partitioning — Workstation Compute vs. Homelab Vault](#adr-001-hardware-partitioning--workstation-compute-vs-homelab-vault)
- [ADR-002: Layout-Aware Document Parsing with IBM Docling](#adr-002-layout-aware-document-parsing-with-ibm-docling)
- [ADR-003: Symbolic AST Verification and Code Generation via SymPy](#adr-003-symbolic-ast-verification-and-code-generation-via-sympy)
- [ADR-004: Relational & Vector Storage Architecture (PostgreSQL 16 + pgvector)](#adr-004-relational--vector-storage-architecture-postgresql-16--pgvector)
- [ADR-005: Hybrid Search with Reciprocal Rank Fusion (RRF)](#adr-005-hybrid-search-with-reciprocal-rank-fusion-rrf)
- [ADR-006: Equation-Context-Aware Hierarchical Chunking](#adr-006-equation-context-aware-hierarchical-chunking)
- [ADR-007: Scholarly Graph Enrichment via OpenAlex API](#adr-007-scholarly-graph-enrichment-via-openalex-api)
- [ADR-008: Standalone Formula Package (`kb-formulas`) & Vectorized Polars Expressions](#adr-008-standalone-formula-package-kb-formulas--vectorized-polars-expressions)
- [ADR-009: Model Context Protocol (FastMCP) for Dynamic Agent Compilation & Execution](#adr-009-model-context-protocol-fastmcp-for-dynamic-agent-compilation--execution)
- [ADR-010: Remote Homelab Archival via Encrypted SSH/SFTP instead of Samba (SMB)](#adr-010-remote-homelab-archival-via-encrypted-sshsftp-instead-of-samba-smb)
- [ADR-011: Workstation Disk Protection Strategy & Local Temporary Unlinking](#adr-011-workstation-disk-protection-strategy--local-temporary-unlinking)
- [ADR-012: Zero Hardcoding and Portability via Pydantic Settings & `.env`](#adr-012-zero-hardcoding-and-portability-via-pydantic-settings--env)
- [ADR-013: GPU Acceleration, Batching, and VRAM Recovery (RTX 3060 12GB)](#adr-013-gpu-acceleration-batching-and-vram-recovery-rtx-3060-12gb)
- [ADR-014: Continuous Multi-Source Harvester Daemon & Exponential Rate-Limit Backoff](#adr-014-continuous-multi-source-harvester-daemon--exponential-rate-limit-backoff)
- [ADR-015: Ground-Truth Formula Accuracy Benchmark Verification Suite](#adr-015-ground-truth-formula-accuracy-benchmark-verification-suite)
- [ADR-016: Centralized Structured Logging & Stage Timing Telemetry](#adr-016-centralized-structured-logging--stage-timing-telemetry)
- [ADR-017: Mandatory OpenSpec Discipline and Documentation Integrity](#adr-017-mandatory-openspec-discipline-and-documentation-integrity)

---

## ADR-001: Hardware Partitioning — Workstation Compute vs. Homelab Vault
- **Status**: Accepted
- **Context**: The pipeline requires heavy GPU compute for layout analysis, OCR, and dense vector embeddings, while demanding 24/7 database accessibility, large PDF storage, and MCP agent query serving.
- **Decision**: Partition hardware responsibilities:
  - **Workstation `cbwwin` (NVIDIA RTX 3060 12GB)**: High-compute ingestion worker running Docling layout parsing, OCR, and BGE-M3 embedding generation.
  - **Homelab `cbwdellr720` (Dell PowerEdge R720)**: Central 24/7 vault running bare-metal PostgreSQL 16 + pgvector, housing permanent PDF archives and Parquet fixtures.
- **Consequences**: Maximizes GPU compute speed on the desktop without straining local workstation storage; homelab maintains 24/7 data availability for LAN/remote agent queries.

---

## ADR-002: Layout-Aware Document Parsing with IBM Docling
- **Status**: Accepted
- **Context**: Standard text extraction tools (e.g. PyPDF, pypdf, pdfminer) scramble multi-column layouts, break equations into unparseable ASCII, and discard table headers.
- **Decision**: Standardize on **IBM Docling** (`docling`) with PyTorch/CUDA acceleration for document layout analysis, reading-order reconstruction, LaTeX formula extraction, and Markdown table generation.
- **Consequences**: High-fidelity extraction of complex mathematical formulas and tables. Ingestion throughput is compute-heavy (~5-15s per paper) but yields clean structured artifacts.

---

## ADR-003: Symbolic AST Verification and Code Generation via SymPy
- **Status**: Accepted
- **Context**: Extracted LaTeX equations from academic PDFs may contain OCR errors, missing delimiters, or invalid operators. Compiling raw strings directly into Python code risks runtime errors and syntax bugs.
- **Decision**: Use `sympy` and `sympy.parsing.latex` to parse extracted LaTeX formulas into symbolic expression trees. Valid equations generate executable Python ASTs and lambdified functions; unparseable equations are flagged as unverified without crashing the ingestion batch.
- **Consequences**: Zero invalid formulas enter the compiled library. Every generated function has verified symbolic integrity and clear variable signatures.

---

## ADR-004: Relational & Vector Storage Architecture (PostgreSQL 16 + pgvector)
- **Status**: Accepted
- **Context**: Scientific papers require rich relational bibliographic metadata (authors, years, citekeys, DOIs, journals) tightly coupled with high-dimensional dense vector embeddings and full-text search indexes.
- **Decision**: Deploy **PostgreSQL 16 with `pgvector`** as the unified primary datastore via SQLAlchemy 2.0 (asyncio) and `asyncpg`. Support SQLite + aiosqlite as a lightweight local development fallback.
- **Consequences**: Eliminates dual-database drift (e.g., maintaining Pinecone/Chroma separately from Postgres). Enables unified SQL queries joining bibliographic metadata, vector distance (`cosine`), and full-text BM25 rankings.

---

## ADR-005: Hybrid Search with Reciprocal Rank Fusion (RRF)
- **Status**: Accepted
- **Context**: Pure vector similarity search often misses exact mathematical variable names, proper author names, or specific jargon; pure keyword search fails on conceptual and semantic queries.
- **Decision**: Implement **Hybrid Search using Reciprocal Rank Fusion (RRF)**:
  - Dense retrieval: 1024-dimensional `BAAI/bge-m3` embeddings compared via cosine distance.
  - Sparse/lexical retrieval: PostgreSQL `tsvector` with `websearch_to_tsquery`.
  - Fusion: $RRF(d) = \sum_{m \in M} \frac{1}{60 + r_m(d)}$.
- **Consequences**: Search yields high precision for both keyword-specific queries and exploratory semantic literature queries.

---

## ADR-006: Equation-Context-Aware Hierarchical Chunking
- **Status**: Accepted
- **Context**: Standard naive text chunkers split documents by fixed token counts, frequently cutting equations in half or separating a formula from the paragraph explaining what its symbols represent.
- **Decision**: Implement **Equation-Context Chunking** in `src/kb/ingest/chunker.py`:
  - Mathematical formulas ($$ ... $$) are treated as indivisible atomic units.
  - Each formula chunk retains its immediately preceding and succeeding context paragraphs.
  - Metadata includes section hierarchy (`section_path`) and extracted mathematical symbol glossaries.
- **Consequences**: Embeddings capture both the mathematical semantics and the physical interpretation of the variables.

---

## ADR-007: Scholarly Graph Enrichment via OpenAlex API
- **Status**: Accepted
- **Context**: Research papers do not exist in isolation; understanding a formula's derivation requires traversing citation trees, co-citation networks, and resolving open-access preprints.
- **Decision**: Integrate the **OpenAlex Scholarly API** (`src/kb/enrich/openalex.py`) to discover citation counts, referenced works, citing papers, topic concepts, and Open Access PDF download URLs.
- **Consequences**: Enables autonomous paper discovery, bibliographic enrichment, and citation lineage mapping across over 250 million scholarly works.

---

## ADR-008: Standalone Formula Package (`kb-formulas`) & Vectorized Polars Expressions
- **Status**: Accepted
- **Context**: Quantitative domain libraries (such as `sabermetricspy`) and data analysis scripts need access to extracted formulas without depending on the heavy `kb` ingestion engine (Docling, PyTorch, transformers).
- **Decision**: Build a standalone code generator (`src/kb/library/generator.py`) exporting verified formulas into a zero-dependency package (`packages/kb_formulas`) with typed Python functions and Polars DataFrame column expressions (`pl.Expr`).
- **Consequences**: Downstream packages can install `kb-formulas` as a lightweight wheel and run vectorized calculations across millions of event rows in Polars with zero ML dependencies.

---

## ADR-009: Model Context Protocol (FastMCP) for Dynamic Agent Compilation & Execution
- **Status**: Accepted
- **Context**: AI coding agents need immediate access to academic literature and formulas during development, but static retrieval is insufficient when agents need to test or verify calculations with dynamic inputs.
- **Decision**: Expose a FastMCP server (`src/kb/mcp/server.py`) with literature retrieval, citation lookup, benchmark table access, and dynamic execution tools:
  - `kb_compile_formula(formula_id)`: Generates Python AST and Polars expressions on demand.
  - `kb_execute_formula(formula_id, inputs)`: Dynamically computes numerical outputs given variable parameters.
- **Consequences**: Agents can verify equations, generate unit test fixtures, and validate algorithms against scientific literature in real time.

---

## ADR-010: Remote Homelab Archival via Encrypted SSH/SFTP instead of Samba (SMB)
- **Status**: Accepted
- **Context**: Local workstation `cbwwin` storage must be preserved, requiring paper PDFs and Parquet tables to be permanently archived on the homelab vault `cbwdellr720`. Samba (SMB) shares were fragile, prone to network dropouts, and required platform-specific credentials.
- **Decision**: Deprecate Samba shares in favor of direct, encrypted **SSH/SFTP synchronization** (`SSHSyncManager` in `src/kb/sync/ssh.py`) using `paramiko` and SSH keys.
- **Consequences**: Rock-solid, cross-platform file transfers with zero OS network mount dependencies.

---

## ADR-011: Workstation Disk Protection Strategy & Local Temporary Unlinking
- **Status**: Accepted
- **Context**: Workstation `cbwwin` primary drive `C:` had constrained disk space ($\sim 3-5$ GB free). Downloading hundreds of 5-30 MB academic PDFs risked filling the drive and causing OS instability.
- **Decision**: Implement a **Stream-Parse-Upload-Unlink** lifecycle:
  1. Download PDF to temporary local workspace cache.
  2. Parse layout and extract formulas/tables with Docling into PostgreSQL.
  3. Upload PDF to `/home/cbwinslow/workspace/kb/pdfs` on `cbwdellr720` via SSH.
  4. Immediately unlink (delete) the local temporary PDF.
  5. Enforce minimum disk free space threshold ($\ge 1.5$ GB) before launching batch runs.
- **Consequences**: Preserved `C:` drive free space (currently $\ge 5.4$ GB free), allowing arbitrarily large batches to be processed safely.

---

## ADR-012: Zero Hardcoding and Portability via Pydantic Settings & `.env`
- **Status**: Accepted
- **Context**: Hardcoding hostnames, IP addresses, database passwords, or absolute filesystem paths creates security vulnerabilities and prevents repository cloning on other developer workstations.
- **Decision**: Centralize all application configuration into Pydantic Settings (`kb.config.Settings`), resolving from environment variables and `.env` files. Provide `.env.example` with clear documentation for SQLite (local) and PostgreSQL/SSH (enterprise/homelab).
- **Consequences**: The codebase is completely portable across Windows, Linux, and macOS. Zero credentials exist in git history.

---

## ADR-013: GPU Acceleration, Batching, and VRAM Recovery (RTX 3060 12GB)
- **Status**: Accepted
- **Context**: Running Docling OCR and BGE-M3 (FP16) embedding models simultaneously on the desktop caused GPU VRAM fragmentation, resulting in CUDA OOM errors and desktop UI stutter.
- **Decision**: 
  1. Set batch sizes for BGE-M3 to 16/32 with FP16 precision.
  2. Explicitly call `torch.cuda.empty_cache()` and `gc.collect()` between batch ingestion iterations.
  3. Default embedding device to CUDA when available with automatic CPU fallback.
- **Consequences**: Stable long-running ingestion batches with zero VRAM leaks and minimal impact on interactive desktop workflows.

---

## ADR-014: Continuous Multi-Source Harvester Daemon & Exponential Rate-Limit Backoff
- **Status**: Accepted
- **Context**: Scaling the knowledge base manually via ad-hoc CLI commands was inefficient, and rapid consecutive queries to academic APIs (especially arXiv) resulted in HTTP 429 Too Many Requests.
- **Decision**: Implement `ContinuousHarvesterDaemon` (`src/kb/sync/daemon.py` & `kb sync daemon`):
  - Cycles through configurable research queries across OpenAlex and arXiv.
  - Enforces minimum 3.0s request pacing between remote queries.
  - Applies exponential backoff retry on HTTP 429 errors.
  - Automatically pushes ingested PDFs to the homelab vault and unlinks local files.
- **Consequences**: Fully autonomous, polite literature harvesting without triggering remote IP blocks.

---

## ADR-015: Ground-Truth Formula Accuracy Benchmark Verification Suite
- **Status**: Accepted
- **Context**: Mathematical formulas generated by AI/SymPy pipelines must be verified not only for syntactic validity but also for numerical precision against established empirical benchmarks.
- **Decision**: Establish an automated ground-truth benchmark suite (`tests/test_accuracy.py`) verifying compiled functions against canonical sabermetric reference values (e.g., Pythagorean expectation with $\gamma=1.83$ and $\gamma=2.0$, FIP constants, linear weights) with strict numerical tolerance ($\le 10^{-4}$).
- **Consequences**: Guarantees quantitative accuracy and prevents operator precedence errors or missing coefficients.

---

## ADR-016: Centralized Structured Logging & Stage Timing Telemetry
- **Status**: Accepted
- **Context**: Raw console `print()` statements and unstructured stderr outputs made long-running ingestion runs difficult to audit and debug.
- **Decision**: Implement centralized logging (`src/kb/logging.py`) with:
  - Console handler with formatted timestamps and log levels.
  - Rotating file handlers (`10MB` max per file, 5 backups).
  - CLI flags: `--verbose`, `--debug`, `--quiet`, `--log-file`.
  - `@timed_stage` decorator measuring execution duration in milliseconds.
- **Consequences**: Complete operational visibility into layout parsing, embedding latency, and error diagnostics across CLI and daemon workflows.

---

## ADR-017: Mandatory OpenSpec Discipline and Documentation Integrity
- **Status**: Accepted
- **Context**: Complex multi-agent engineering workflows can lead to undocumented code changes, drift between implementation and design, and lost architectural rationale.
- **Decision**: Enforce OpenSpec discipline via [`AGENTS.md`](file:///c:/Users/blain/projects/kb/AGENTS.md):
  - Every major capability MUST have an OpenSpec change folder with `proposal.md`, `design.md`, `tasks.md`, and delta specs under `specs/`.
  - Main specs in `openspec/specs/` and `docs/DECISIONS.md` must be kept in continuous synchronization with code changes.
  - Zero tolerance for undocumented code or unverified modifications.
- **Consequences**: Complete traceability, reproducibility, and architectural clarity across all development cycles.
