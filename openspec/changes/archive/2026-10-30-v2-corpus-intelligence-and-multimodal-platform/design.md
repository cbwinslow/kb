# Design: V2 Corpus Intelligence & Multimodal Platform

## Context
See `proposal.md` for problem statement and requirements.
The system currently hosts 311 documents, 37,006 chunks, 6,199 formulas, 490 figures, and 1,395 benchmark tables across workstation `cbwwin` (Docling GPU worker) and homelab `cbwdellr720` (PostgreSQL 16 + SFTP vault). All designs must adhere strictly to:
1. Zero hardcoded paths/secrets (`kb.config.settings`).
2. Homelab storage preservation via SFTP (never Samba).
3. Workstation disk protection ($\ge 1.5$ GB free minimum).
4. Strict typing with Pyright (0 errors) and Ruff linting (0 warnings).

---

## Goals / Non-Goals

**Goals:**
- Provide a browser-based "Scholarly Explorer" in `kb ui serve` with live arXiv/OpenAlex queries and background 1-click ingestion.
- Implement `LaTeXSanitizerV3` to recover Grade F formulas with compound acronym preservation (`BABIP`, `wOBA`), bracket rebalancing, and piecewise cases conversion.
- Provide fuzzy heuristic column binding between formula AST symbols and Parquet tracking datasets in `EmpiricalAccuracyRunner`.
- Implement `FigureVLMProcessor` to extract visual axes and curves from the 490 vaulted figures, linking them to mathematical formulas and exposing MCP figure query tools.

**Non-Goals:**
- Heavy client-side React/Vue frameworks (UI remains lightweight vanilla HTML/JS embedded within Starlette).
- Full OCR engine replacement (IBM Docling remains the primary layout and text engine).
- Real-time video processing (only static publication figures and charts are analyzed).

---

## Decisions

### 1. Scholarly UI Explorer & Background Ingestion Loop
- **Decision**: Expose REST endpoints `/api/search/external` and `/api/harvest/ingest-url` on the Starlette web application (`src/kb/ui/app.py`).
- **Rationale**: Reuses the newly implemented `ScholarlyWebSearcher`. The ingestion endpoint dispatches background `asyncio` tasks tracked by unique job IDs, polling status via `/api/harvest/jobs/{id}` so the browser remains responsive while Docling runs CUDA layout analysis.
- **Alternatives Considered**: Synchronous blocking HTTP POST (rejected: PDF layout parsing takes 5-15s per paper, which would trigger HTTP request timeouts).

### 2. Formula Sanitizer V3 Architecture
- **Decision**: Extend `LaTeXSanitizer` with token protection registries and recursive delimiter balancing in `src/kb/math/sanitizer.py`.
- **Token Protection**: Acronyms like `BABIP`, `wOBA`, `wRAA`, `ERA`, `FIP` are wrapped in SymPy `Symbol("BABIP")` wrappers prior to LaTeX AST parsing, preventing character splitting.
- **Piecewise Environments**: `\begin{cases} ... \end{cases}` blocks are regex-extracted and transformed into `sympy.Piecewise` syntax.
- **Alternatives Considered**: Regex-only substitutions without AST verification (rejected: violates ADR-003, invalid formulas must not enter the library).

### 3. Heuristic Column Auto-Binding & Fixture Discovery
- **Decision**: Implement `HeuristicColumnMatcher` in `src/kb/qa/accuracy.py` combining Levenshtein string distance with domain synonym maps (`v_0` $\leftrightarrow$ `exit_velocity`, `\theta` $\leftrightarrow$ `launch_angle`).
- **Fixture Registry**: The runner automatically checks `data/fixtures/*.parquet` for golden tracking datasets, evaluates matching formulas, and records empirical scorecards without manual CLI mapping.
- **Alternatives Considered**: Strict 1:1 symbol matching (rejected: academic papers write $v_0$ while MLB Statcast datasets label the column `launch_speed`).

### 4. Multimodal Figure Grounding & Relational Schema
- **Decision**: Update `kb_figures` table schema with `vlm_summary`, `detected_curves` (JSON), and `formula_ids` (JSON).
- **Tooling**: Register `kb_get_figure` and `kb_search_figures` in FastMCP (`src/kb/mcp/server.py`).
- **Storage**: Vaulted figure files continue to stream over SFTP from `cbwdellr720` on demand; temporary workstation previews are cleaned up immediately to protect disk floors.

---

## Risks / Trade-offs

- **[Risk]** Background 1-click ingestion consumes GPU VRAM while the user is browsing.
  - *Mitigation*: Queue ingestion jobs sequentially with concurrency limit 1; clear PyTorch CUDA cache between documents (`torch.cuda.empty_cache()`).
- **[Risk]** Fuzzy column matching binds formulas to incorrect dataset attributes.
  - *Mitigation*: Require minimum confidence threshold $\ge 0.75$; fall back to `SymbolOntology` canonical registry if ambiguity exists.
- **[Risk]** Sanitizer V3 rebalancing alters mathematical semantics.
  - *Mitigation*: Quality gate Tier 1–4 tests re-validate all repaired formulas with SymPy evaluation before updating PostgreSQL records.
