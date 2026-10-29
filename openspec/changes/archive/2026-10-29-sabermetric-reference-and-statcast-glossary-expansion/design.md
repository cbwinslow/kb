# Design: Sabermetric Reference & Statcast 2.0 Glossary Expansion

## Context
See `proposal.md` for motivation. While classic sabermetrics (wOBA, FIP, Base Runs) are codified, modern analytical workflows depend heavily on situational leverage (Tom Tango's 24-state Run Expectancy and Leverage Index) and optical tracking physics (MLB Statcast 2.0 bat tracking). Expanding KB's canonical presets and ontology bridges these empirical metrics with academic literature formulas and machine-readable ASTs.

## Goals / Non-Goals

**Goals:**
- Add canonical reference presets in `src/kb/sync/web.py` for:
  - Tom Tango's 24-state Run Expectancy (`tangotiger_re24`)
  - Leverage Index & Win Probability Added (`tangotiger_leverage_index`)
  - Baseball Prospectus DRC+ and DRA (`bp_drc_plus_glossary`)
  - Baseball-Reference WAR components & positional adjustments (`bref_war_components`)
  - MLB Statcast 2.0 bat tracking mechanics (`statcast_bat_tracking`)
- Register new canonical concepts and aliases in `SymbolOntology` (`src/kb/math/ontology.py`).
- Validate that all extracted equations parse into valid SymPy expressions and achieve high validation scores.

**Non-Goals:**
- Modifying `baseballpy` (Claude is developing `baseballpy` independently).
- Crawling dynamic authenticated paywalls.

## Decisions

### 1. Pre-Packaged Structured Presets with LaTeX Formulations
- **Decision**: Store structured Markdown definitions in `SABERMETRIC_GLOSSARY_PRESETS` with exact mathematical LaTeX notation, parameter explanations, and publication metadata.
- **Rationale**: Provides zero-dependency, reproducible reference documents that do not break when remote websites change HTML layouts or rate-limit automated scrapers.

### 2. Symbol Ontology Extension
- **Decision**: Extend `CanonicalConcept` enum in `src/kb/math/ontology.py` with:
  - `BAT_SPEED = "bat_speed"`
  - `SWING_LENGTH = "swing_length"`
  - `ATTACK_ANGLE = "attack_angle"`
  - `FAST_SWING_RATE = "fast_swing_rate"`
  - `BLAST_RATE = "blast_rate"`
  - `SQUARED_UP_RATE = "squared_up_rate"`
  - `EXIT_VELOCITY = "exit_velocity"`
  - `LEVERAGE_INDEX = "leverage_index"`
  - `RUN_EXPECTANCY = "run_expectancy"`
- **Rationale**: Allows downstream AST generators, DataFrame binders, and equation chaining engines to recognize Statcast column names (e.g. `bat_speed`, `swing_length`, `exit_velocity`, `launch_speed`) automatically.

## Risks / Trade-offs

- **[Risk] Complex physics collision formulas might fail standard SymPy parsing.**
  → *Mitigation*: Format equations with explicit multiplication signs (`\cdot`) and clean subscript notation (`v_{exit}`, `v_{pitch}`, `v_{bat}`).
