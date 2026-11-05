# Design: Citation Lineage, Live Formula Playground, Multi-Domain Harvesting, and Empirical Benchmarking

## Context

See `proposal.md` for motivation. Currently:
- PostgreSQL on `cbwdellr720` houses 311 documents, 37,006 chunks, 6,199 formulas (4,120 Grade A/B), 490 grounded figures, and 1,395 benchmark tables.
- `lazy="selectin"` on `Document` relationships causes bulk queries like `select(Document)` to hydrate all 37,006 chunks into memory, causing severe latency (~30s) during citation graph builds.
- 245 documents possess DOIs but lack `openalex_id` and `referenced_works`, resulting in only 17 citation edges.
- 1,743 verified formula functions are compiled in `packages/kb_formulas` but have no interactive runtime endpoint in the Web UI.
- Harvester presets for `biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, and `kinematics-tracking` have been defined but not executed.
- Golden Parquet fixtures exist in `data/fixtures/` and homelab vault, but global accuracy scorecards remain uncompiled.

## Goals / Non-Goals

**Goals:**
- Eliminate ORM eager loading bottlenecks in `CitationGraphBuilder` using column projections, achieving $< 2.0$s execution.
- Enrich all 245 DOI-bearing documents via OpenAlex and build dense paper-to-paper citation edges in `kb_citations`.
- Provide a responsive Web UI Playground connected to all 1,743 compiled formulas with live execution, sensitivity plots, and multi-format code export.
- Execute multi-domain harvesting sweeps and ingest new quantitative literature into the homelab vault with zero workstation disk overflow.
- Run comprehensive empirical accuracy benchmarking across Grade A formulas and golden fixtures, producing a global leaderboard and UI badges.

**Non-Goals:**
- Modifying underlying Docling parsing models or SymPy ANTLR grammar.
- Building full external graph analytics (e.g. PageRank across billions of OpenAlex papers).

## Decisions

### 1. Column Projections in Citation Graph Traversals
- **Decision**: Query `select(Document.id, Document.openalex_id, Document.referenced_works, Document.year)` instead of `select(Document)`.
- **Rationale**: Completely bypasses SQLAlchemy's `lazy="selectin"` cascading loads for chunks and formulas. Reduces network data transfer from $\sim 150$ MB to $< 200$ KB and latency from 30.7s to $< 1.0$s.
- **Alternatives Considered**: Modifying `Document` relationship declarations from `lazy="selectin"` to `lazy="raise"` or `lazy="select"` — rejected because existing ingestion and CLI workflows rely on `lazy="selectin"` for single-document transactions.

### 2. Compiled Formula Introspection & Execution API
- **Decision**: Dynamically inspect the compiled module (`packages/kb_formulas/src/kb_formulas/generated.py` / `src/kb/library/generated.py`) using Python's standard `inspect` module and expose two dedicated endpoints:
  - `GET /api/formulas/compiled`: returns list of compiled functions with signatures, docstrings, parameter names, and default values.
  - `POST /api/formulas/compiled/{func_name}/eval`: validates input parameter dict, casts values to floats, calls the compiled Python function, and returns computed result or exception message.
- **Rationale**: Decouples UI formula execution from raw LaTeX string compilation at runtime. Guarantees 100% type safety and instant execution ($< 1$ms per evaluation).
- **Alternatives Considered**: In-browser Pyodide WebAssembly execution — rejected due to heavy browser bundle download and slower cold starts.

### 3. Multi-Domain Harvesting & Homelab SFTP Vaulting
- **Decision**: Execute `kb sync harvest --preset <domain> --limit 10` sequentially across `biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, and `kinematics-tracking`. Ensure downloaded PDFs are uploaded to homelab SFTP vault and locally unlinked after ingestion to enforce the $\ge 1.5$ GB disk floor.
- **Rationale**: Expands the domain diversity of the knowledge base into computational physics and biomechanics while strictly preserving workstation storage.

### 4. Empirical Accuracy Leaderboard Engine
- **Decision**: Enhance `EmpiricalAccuracyRunner` with an automated fixture scanner that loops through golden Parquet datasets in `data/fixtures/`, maps Grade A formulas, evaluates vectorized Polars expressions, computes MAE/RMSE/$R^2$, and writes `data/benchmarks/accuracy_leaderboard.md`.
- **Rationale**: Ground-truth verification across tabular tracking data proves empirical predictive power beyond purely symbolic syntax correctness.

## Risks / Trade-offs

- **[Risk]** OpenAlex API rate limiting during batch enrichment of 245 papers.
  $\to$ *Mitigation*: Enforce 100ms polite query spacing with exponential backoff on HTTP 429, and persist progress in transactions of 25 papers.
- **[Risk]** GPU VRAM contention on workstation `cbwwin` during Docling ingestion of newly harvested papers.
  $\to$ *Mitigation*: Process papers sequentially with explicit PyTorch CUDA cache clearing (`torch.cuda.empty_cache()`) between papers.
- **[Risk]** Formula evaluation inputs out of mathematical domain (e.g., division by zero, negative square roots).
  $\to$ *Mitigation*: Catch `ZeroDivisionError`, `ValueError`, and `FloatingPointError` in `/api/formulas/compiled/{func_name}/eval`, returning structured JSON error payloads instead of HTTP 500s.
