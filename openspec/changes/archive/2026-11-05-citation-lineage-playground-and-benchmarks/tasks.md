# Tasks: Citation Lineage, Live Formula Playground, Multi-Domain Harvesting, and Empirical Benchmarking

## 1. Citation Graph Query Optimization & OpenAlex Reference Enrichment

- [x] 1.1 Optimize `CitationGraphBuilder` in `src/kb/sync/citations.py` to use explicit column projections (`id`, `openalex_id`, `referenced_works`, `year`), bypassing SQLAlchemy `lazy="selectin"` chunk loads, and verify with `pytest tests/test_citations.py`
- [x] 1.2 Enhance `async_enrich_openalex` in `src/kb/cli.py` to query lightweight document columns, batch database transactions, and verify progress callbacks without memory bloat
- [x] 1.3 Execute `kb enrich openalex --all` across DOI-bearing documents and run `kb sync citations` to backfill paper-to-paper edges in `kb_citations`, verifying with `kb corpus audit`

## 2. Live Compiled Formula Playground in Web UI

- [x] 2.1 Implement `GET /api/formulas/compiled` and `POST /api/formulas/compiled/{func_name}/eval` endpoints in `src/kb/ui/app.py` introspecting the 1,743 compiled formulas from `packages/kb_formulas`
- [x] 2.2 Add unit tests in `tests/test_ui.py` covering `/api/formulas/compiled` metadata retrieval, successful execution, missing arguments, and mathematical domain errors
- [x] 2.3 Update Web UI Playground frontend in `src/kb/ui/app.py` with compiled formula search, reactive parameter controls, real-time result evaluation, sensitivity curve visualization, and multi-format code export buttons (Python, Polars, SymPy, curl)

## 3. Multi-Domain Research Harvester Execution & Corpus Ingestion

- [x] 3.1 Execute multi-domain harvesting sweeps across `biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, and `kinematics-tracking` presets via `kb sync harvest`, verifying SFTP vaulting and disk preservation
- [x] 3.2 Ground newly extracted figures via `kb figures index-all` and run formula repair via `kb corpus repair-all` to elevate mathematical quality scorecards

## 4. Empirical Accuracy Benchmarking & Leaderboard Reporting

- [x] 4.1 Enhance `EmpiricalAccuracyRunner` in `src/kb/benchmark/accuracy.py` to support `--output` and generate Markdown and JSON leaderboard reports ranking formulas by $R^2$, MAE, and RMSE
- [x] 4.2 Add unit tests for empirical accuracy leaderboard generation in `tests/test_benchmark_accuracy.py`
- [x] 4.3 Execute `kb benchmark accuracy --all --output data/benchmarks/accuracy_leaderboard.md` and surface empirical accuracy metrics in Web UI formula views

## 5. Quality Gates & Architecture Decisions

- [x] 5.1 Run all code quality gates: `uv run --no-sync ruff check src/ tests/ packages/` and `uv run --no-sync pyright src/ tests/ packages/`
- [x] 5.2 Run complete automated test suite: `uv run --no-sync pytest tests/`
- [x] 5.3 Record architectural decisions as **ADR-039** in `docs/DECISIONS.md` and validate OpenSpec change strictly

