# Proposal: Sabermetric Reference & Statcast 2.0 Glossary Expansion

## Why
While KB contains academic preprints and 8 initial FanGraphs presets, key modern and historical sabermetric foundations remain unencoded: Tom Tango's 24-state Run Expectancy (RE24) matrices, Leverage Index (LI), Baseball Prospectus DRC+ and Deserved Run Average (DRA), Baseball-Reference WAR component architectures, and modern MLB Statcast 2.0 bat tracking physics (bat speed, fast swing rate, squared-up rate, blast percentage, and exit velocity collision mechanics). Ingesting and codifying these references provides essential canonical equations and empirical baselines that link academic papers, player evaluations, and Retrosheet/Statcast analytics together.

## What Changes
- **Expanded Sabermetric Presets in `src/kb/sync/web.py`**:
  - **Tom Tango Tangotiger RE24 Matrix & Markov Transitions**: 24 base-out state run expectancies, linear weights, and run-expectancy delta equation: $\Delta RE = RE_{end} - RE_{start} + R_{play}$.
  - **Leverage Index (LI) & Win Probability Added (WPA)**: Quantitative definitions of swing leverage: $LI = \frac{\Delta WP_{max} - \Delta WP_{min}}{E[\Delta WP]}$.
  - **Baseball Prospectus Deserved Runs Created (DRC+) & DRA**: Mixed-model empirical Bayesian estimators isolating hitter and pitcher true-talent run contributions.
  - **Baseball-Reference WAR Architecture**: Comprehensive positional adjustment run values and defensive runs saved (dWAR) framework.
  - **Statcast 2.0 Bat Tracking Physics**:
    - Exit velocity limit equation: $v_{exit} \le v_{pitch} \cdot q + v_{bat} \cdot (1+e)$.
    - Squared-Up Rate: $SquaredUp = \frac{v_{exit}}{v_{exit, max}}$.
    - Blast Percentage: High-contact rate combining bat speed $\ge 75\text{ mph}$ with squared-up impact $\ge 80\%$.
- **Symbol Ontology Enrichment (`src/kb/math/ontology.py`)**:
  - Adds canonical concepts and aliases for `BAT_SPEED`, `SWING_LENGTH`, `ATTACK_ANGLE`, `FAST_SWING_RATE`, `BLAST_RATE`, `SQUARED_UP_RATE`, `LEVERAGE_INDEX`, and `RUN_EXPECTANCY`.
- **Pipeline Ingestion & Batch Harvester**:
  - Automatically loads and verifies all new presets into PostgreSQL with symbolic LaTeX parsing, chunking, and validation scorecards.

## Capabilities

### Modified Capabilities
- `web-glossary-harvester`: Expands preset library with Tom Tango RE24/LI, Baseball Prospectus DRC+/DRA, Baseball-Reference WAR, and Statcast 2.0 bat tracking mechanics.
- `symbol-ontology`: Registers canonical concepts and aliases for Statcast bat tracking and situation-dependent sabermetric metrics.

## Impact
- **Modules Modified**: `src/kb/sync/web.py`, `src/kb/math/ontology.py`, `tests/test_ontology.py`, `tests/test_web_ingest.py`.
- **Database**: Ingests new reference documents and formulas into `kb_documents`, `kb_chunks`, and `kb_formulas`.
