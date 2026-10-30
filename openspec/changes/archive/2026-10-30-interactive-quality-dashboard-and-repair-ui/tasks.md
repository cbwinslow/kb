# Tasks: Interactive Quality Dashboard & 1-Click Formula Repair UI

## 1. Backend REST Endpoints & Repair Logic
- [x] 1.1 Implement `POST /api/formulas/{id}/repair` endpoint in `src/kb/ui/app.py`.
- [x] 1.2 Connect repair endpoint to `CorpusFormulaRepairer` and `FormulaQualityGate`.
- [x] 1.3 Add query parameter filtering (`grade`, `validation_status`) to `GET /api/formulas`.

## 2. Web UI Dashboard & Diagnostic Views
- [x] 2.1 Add "Quality Gate" navigation tab to `src/kb/ui/templates/index.html`.
- [x] 2.2 Implement grade distribution charts and filterable scorecard table.
- [x] 2.3 Implement expandable diagnostic drawer displaying Tier 1–4 breakdowns.
- [x] 2.4 Add 1-click "Repair Formula" button with asynchronous fetch and instant DOM updates.

## 3. Verification & Testing
- [x] 3.1 Write unit tests for `/api/formulas/{id}/repair` endpoint in `tests/test_ui.py`.
- [x] 3.2 Verify grade filtering and scorecard response payloads.
- [x] 3.3 Validate quality gates: `uv run ruff check`, `uv run pyright`, `uv run pytest`.
