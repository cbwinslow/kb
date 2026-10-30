# Tasks: V2 Corpus Intelligence & Multimodal Platform

## 1. Scholarly UI Explorer & 1-Click Ingestion

- [ ] 1.1 Add `/api/search/external` and `/api/harvest/ingest-url` endpoints in `src/kb/ui/app.py` and verify via testclient
- [ ] 1.2 Implement background async ingestion worker with job status tracking in `src/kb/ui/app.py`
- [ ] 1.3 Add "Scholarly Explorer" view with live arXiv/OpenAlex search cards and 1-click ingest buttons in `src/kb/ui/static/index.html`
- [ ] 1.4 Write unit tests in `tests/test_ui_search.py` verifying external search endpoint and job status polling

## 2. Advanced Formula Sanitizer V3 & AST Recovery

- [ ] 2.1 Implement compound acronym registry (`BABIP`, `wOBA`, `wRAA`, `ERA`, `FIP`) in `src/kb/math/sanitizer.py`
- [ ] 2.2 Add bracket stack rebalancer for unclosed `\left` / `\right` delimiters in `src/kb/math/sanitizer.py`
- [ ] 2.3 Implement piecewise cases parser converting `\begin{cases}` environments to SymPy `Piecewise` in `src/kb/math/sanitizer.py`
- [ ] 2.4 Update `src/kb/math/repair.py` to leverage Sanitizer V3 and verify recovery of synthetic Grade F formulas in `tests/test_sanitizer_v3.py`

## 3. Empirical Accuracy Auto-Binding Engine & Fixtures

- [ ] 3.1 Implement `HeuristicColumnMatcher` resolving formula AST symbols to dataset columns in `src/kb/qa/accuracy.py`
- [ ] 3.2 Add automated fixture discovery scanning `data/fixtures/*.parquet` in `src/kb/qa/accuracy.py`
- [ ] 3.3 Add `kb benchmark accuracy --all` support in `src/kb/cli.py`
- [ ] 3.4 Write unit tests in `tests/test_accuracy_autobind.py` verifying heuristic column resolution and error metric calculations

## 4. Multimodal Figure VLM Grounding & MCP Tooling

- [ ] 4.1 Update `Figure` database model in `src/kb/storage/models.py` with `vlm_summary`, `detected_curves`, and `formula_ids`
- [ ] 4.2 Implement `FigureVLMProcessor` for curve and axis extraction in `src/kb/enrich/vlm.py`
- [ ] 4.3 Add `kb_get_figure` and `kb_search_figures` tools to FastMCP server in `src/kb/mcp/server.py`
- [ ] 4.4 Write unit tests in `tests/test_figure_vlm.py` verifying figure metadata extraction and MCP tool responses

## 5. End-to-End Verification & Delivery

- [ ] 5.1 Run full test suite with `uv run pytest tests/` verifying 100% test pass rate
- [ ] 5.2 Run static typing check with `uv run pyright src/ tests/ packages/` verifying 0 errors
- [ ] 5.3 Run linter with `uv run ruff check src/ tests/ packages/` verifying 0 warnings
- [ ] 5.4 Document architectural decisions in `docs/DECISIONS.md`
- [ ] 5.5 Commit changes with conventional commits and push to `origin/master`

## Workflow follow-up

- Archive the change after implementation and test verification (`openspec archive`).
- Verify main specs are updated in `openspec/specs/`.
