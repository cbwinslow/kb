# Tasks: Corpus Formula Elevation, Batch Figure VLM Grounding, and Multi-Domain Preset Harvesting

## 1. Grade-F Formula AST Recovery & Corpus Quality Elevation

- [x] 1.1 Implement targeted Grade-F recovery heuristics in `EquationSanitizer` and `CorpusFormulaRepairer` (acronym preservation, array unwrapping, delimiter rebalancing), and verify with unit tests in `tests/test_formula_repair.py`
- [x] 1.2 Run `kb corpus repair-all --batch-size 100` on the PostgreSQL corpus and verify elevation in formula grades (recovering Grade-F formulas into Grade A/B/C) via `kb corpus audit`
- [x] 1.3 Recompile standalone formula library `packages/kb_formulas` via `FormulaLibraryGenerator.export_to_file()` and verify test suite passes with `uv run pytest tests/test_formula_library.py`

## 2. Batch Figure VLM Grounding Pipeline & CLI Indexer

- [x] 2.1 Implement `FigureBatchIndexer` in `src/kb/enrich/vlm.py` with bounding box extraction, visual summary generation, and proximity-based formula ID linking
- [x] 2.2 Wire `kb figures index-all` CLI command in `src/kb/cli.py` with `--batch-size`, `--limit`, `--force`, and `--dry-run` options
- [x] 2.3 Write integration tests for batch figure indexing in `tests/test_figure_vlm.py` and verify with `uv run pytest tests/test_figure_vlm.py`

## 3. Multi-Domain Harvester Presets & Expansion

- [x] 3.1 Expand `OpenAlexClient.get_preset_queries()` in `src/kb/enrich/openalex.py` with `biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, and `kinematics-tracking` presets
- [x] 3.2 Update CLI harvest command validation and help in `src/kb/cli.py` to support all new presets and verify with unit tests in `tests/test_openalex.py`
- [x] 3.3 Execute targeted test harvest with `--preset aerodynamics-pinn --max-papers 2 --dry-run-dedup` to verify query resolution and deduplication filtering

## 4. Quality Gates, ADR Documentation & Sync

- [x] 4.1 Record formal architectural decision in `docs/DECISIONS.md` as ADR-037
- [x] 4.2 Run full quality gates: `uv run ruff check src/ tests/ packages/`, `uv run pyright src/ tests/ packages/`, and `uv run pytest tests/`
- [x] 4.3 Update `README.md` and `openspec/project.md` with new capabilities, CLI commands, and telemetry

## Workflow follow-up

- Archive the change `corpus-elevation-vlm-and-domain-expansion` to `openspec/changes/archive/`.
- Verify sync to main specs under `openspec/specs/`.
