# Tasks: Sabermetric Reference & Statcast 2.0 Glossary Expansion

## 1. Symbol Ontology Extension

- [x] 1.1 Add canonical concepts (`BAT_SPEED`, `SWING_LENGTH`, `ATTACK_ANGLE`, `FAST_SWING_RATE`, `BLAST_RATE`, `SQUARED_UP_RATE`, `EXIT_VELOCITY`, `LEVERAGE_INDEX`, `RUN_EXPECTANCY`) and aliases to `src/kb/math/ontology.py`.
- [x] 1.2 Verify concept resolution and column binding in `tests/test_ontology.py`.

## 2. Sabermetric & Statcast Presets Expansion

- [x] 2.1 Implement Tom Tango RE24 (`tangotiger_re24`) and Leverage Index (`tangotiger_leverage_index`) presets in `src/kb/sync/web.py`.
- [x] 2.2 Implement Baseball Prospectus DRC+/DRA (`bp_drc_plus_glossary`) and Baseball-Reference WAR (`bref_war_components`) presets in `src/kb/sync/web.py`.
- [x] 2.3 Implement Statcast 2.0 bat tracking collision mechanics (`statcast_bat_tracking`) preset in `src/kb/sync/web.py`.

## 3. Verification, Pipeline Ingestion & Archival

- [x] 3.1 Implement unit tests verifying formula extraction and SymPy validation for all new presets in `tests/test_web_ingest.py`.
- [x] 3.2 Execute batch ingestion of presets into PostgreSQL database when connected.
- [x] 3.3 Run quality checks: `uv run ruff check`, `uv run pyright`, `uv run pytest`.
- [x] 3.4 Record ADR-027 in `docs/DECISIONS.md`, sync delta specs to `openspec/specs/`, and archive the change.
