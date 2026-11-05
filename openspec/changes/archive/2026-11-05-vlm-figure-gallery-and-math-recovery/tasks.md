# Tasks: Multimodal Figure Studio & Gallery and Unicode Math AST Recovery

## 1. Unicode Math Sanitizer V4 & Corpus Elevation

- [x] 1.1 Implement Unicode math normalization heuristics in `src/kb/math/sanitizer.py` (Math Alphanumeric NFKD decomposition, combining vector arrow and overline stripping, expectation angle brackets, unbraced `\sum` subscripts, and fullwidth equation tags)
- [x] 1.2 Add unit tests for all new normalization rules in `tests/test_sanitizer_coverage.py` and verify with `uv run pytest tests/test_sanitizer_coverage.py`
- [x] 1.3 Execute `kb corpus repair-all --batch-size 100` on the PostgreSQL corpus and recompile `packages/kb_formulas` via `FormulaLibraryGenerator`

## 2. Multimodal Figure Studio & Gallery in Web UI

- [x] 2.1 Implement `GET /api/figures` endpoint in `src/kb/ui/app.py` supporting `citekey`, `diagram_type`, `q` search query, and pagination
- [x] 2.2 Implement `GET /api/figures/{id}` endpoint in `src/kb/ui/app.py` returning full figure metadata with resolved linked `Formula` entities
- [x] 2.3 Add "Figures & Multimodal" navigation tab, search/filter controls, and responsive card grid in the Starlette dashboard HTML/JS
- [x] 2.4 Add integration tests for figure API endpoints in `tests/test_ui.py` and verify with `uv run pytest tests/test_ui.py`

## 3. Quality Gates, ADR-038 & Archival

- [x] 3.1 Record formal architectural decision in `docs/DECISIONS.md` as ADR-038
- [x] 3.2 Run full quality gates: `uv run --no-sync ruff check src/ tests/ packages/`, `uv run --no-sync pyright src/ tests/ packages/`, and `uv run --no-sync pytest tests/`
- [x] 3.3 Update `README.md` and `openspec/project.md` with new figure gallery endpoints and updated formula stats
- [x] 3.4 Archive the change to `openspec/changes/archive/` and sync specs
