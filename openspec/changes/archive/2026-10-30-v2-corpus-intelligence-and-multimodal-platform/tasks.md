# Tasks: V2 Corpus Intelligence & Multimodal Platform

## 1. Scholarly UI Explorer & 1-Click Ingestion

- [x] 1.1 Add `/api/search/external` endpoint in `src/kb/ui/app.py` accepting query, source, and limit
- [x] 1.2 Implement `IngestJob` state tracking and `POST /api/harvest/ingest-url` background worker in `src/kb/ui/app.py`
- [x] 1.3 Add `GET /api/harvest/jobs/{job_id}` polling endpoint in `src/kb/ui/app.py`
- [x] 1.4 Add "Scholarly Explorer" view with live arXiv/OpenAlex search cards and 1-click ingest in `src/kb/ui/static/index.html`
- [x] 1.5 Write unit tests in `tests/test_ui_search.py` verifying external search and async job lifecycle

## 2. Advanced Formula Sanitizer V3 & AST Recovery

- [x] 2.1 Implement compound acronym registry (`BABIP`, `wOBA`, `wRAA`, `ERA`, `FIP`, `WAR`) in `src/kb/math/sanitizer.py`
- [x] 2.2 Add bracket stack rebalancer for unclosed `\left` / `\right` delimiters in `src/kb/math/sanitizer.py`
- [x] 2.3 Implement piecewise cases parser converting `\begin{cases}` environments to SymPy `Piecewise` in `src/kb/math/sanitizer.py`
- [x] 2.4 Update `CorpusFormulaRepairer` in `src/kb/math/repair.py` to use Sanitizer V3 with atomic batch rollbacks
- [x] 2.5 Write unit tests in `tests/test_sanitizer_v3.py` verifying recovery of acronyms, delimiters, and cases

## 3. Empirical Accuracy Auto-Binding Engine & Fixtures

- [x] 3.1 Implement `HeuristicColumnMatcher` resolving formula AST symbols to dataset columns in `src/kb/qa/accuracy.py`
- [x] 3.2 Add automated fixture discovery scanning `data/fixtures/*.parquet` in `src/kb/qa/accuracy.py`
- [x] 3.3 Add `kb benchmark accuracy --all` support in `src/kb/cli.py` with tabular summary output
- [x] 3.4 Write unit tests in `tests/test_accuracy_autobind.py` verifying heuristic column resolution and error metrics

## 4. Multimodal Figure VLM Grounding & MCP Tooling

- [x] 4.1 Update `Figure` database model in `src/kb/storage/models.py` with `vlm_summary`, `detected_curves`, and `formula_ids`
- [x] 4.2 Implement `FigureVLMProcessor` for curve and axis extraction in `src/kb/enrich/vlm.py`
- [x] 4.3 Add `kb_get_figure` and `kb_search_figures` tools to FastMCP server in `src/kb/mcp/server.py`
- [x] 4.4 Write unit tests in `tests/test_figure_vlm.py` verifying figure metadata extraction and MCP tool responses

## 5. End-to-End Verification & Delivery

- [x] 5.1 Run full test suite with `uv run pytest tests/` verifying 100% test pass rate
- [x] 5.2 Run static typing check with `uv run pyright src/ tests/ packages/` verifying 0 errors
- [x] 5.3 Run linter with `uv run ruff check src/ tests/ packages/` verifying 0 warnings
- [x] 5.4 Document architectural decisions in `docs/DECISIONS.md` (ADR-036)
- [x] 5.5 Commit changes with conventional commits and push to `origin/master`

## Workflow follow-up

- Archive the change after implementation and test verification (`openspec archive`).
- Verify main specs are updated in `openspec/specs/`.
