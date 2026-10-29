# Tasks: CI/CD Distribution, Symbol Ontology & Interactive Web UI Playground

## Phase 1: CI/CD & PyPI Distribution (Issue #2)
- [x] 1.1 Create `.github/workflows/ci.yml` with dual-OS matrix (Ubuntu & Windows), Python 3.12, `uv` cache, ruff check, pyright, and pytest.
- [x] 1.2 Create `.github/workflows/publish-formulas.yml` for building wheel/sdist and publishing releases of `packages/kb_formulas`.
- [x] 1.3 Ensure `packages/kb_formulas/pyproject.toml` contains clean packaging metadata, versioning, and distribution fields.

## Phase 2: Semantic Symbol Ontology & Column Mapping (Issue #3)
- [x] 2.1 Implement `src/kb/math/ontology.py` with `CanonicalConcept`, `ConceptCatalog`, `SymbolOntology`, and normalization helpers.
- [x] 2.2 Implement DataFrame binding support for Polars (`pl.DataFrame`) and Pandas (`pd.DataFrame`) in `SymbolOntology.bind_dataframe`.
- [x] 2.3 Implement CLI command `kb code ontology` in `src/kb/cli.py`.
- [x] 2.4 Write comprehensive unit tests in `tests/test_ontology.py` verifying canonical symbol resolution, LaTeX subscript normalization, and Polars/Pandas DataFrame binding.

## Phase 3: Interactive Web UI Calculation Playground (Issue #4)
- [x] 3.1 Add interactive Calculation Playground tab and route to `src/kb/ui/app.py`.
- [x] 3.2 Add parameter sliders, custom formula evaluator, and real-time response rendering via `/api/eval`.
- [x] 3.3 Embed interactive sensitivity curve charting for canonical formulas.
- [x] 3.4 Ensure strict non-regression of existing tabs (`lineage`, `formulas`, `tables`, `search`).
- [x] 3.5 Write automated UI and API tests in `tests/test_ui.py` covering playground routes and evaluation responses.

## Phase 4: Quality Gates, Architectural Records & Spec Synchronization
- [x] 4.1 Record formal ADR-019 (Symbol Ontology & Canonical Mapping) and ADR-020 (Interactive Calculation Playground & CI/CD Packaging) in `docs/DECISIONS.md`.
- [x] 4.2 Run `uv run ruff check` and `uv run ruff format` across the codebase.
- [x] 4.3 Run `uv run pyright` ensuring zero errors.
- [x] 4.4 Run `uv run pytest` ensuring all tests pass.
- [x] 4.5 Sync delta specs into `openspec/specs/` and archive the change.
- [x] 4.6 Commit and push clean working tree to GitHub repository.
