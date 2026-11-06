# Tasks: Canonical Projections, Markov Models, and Quantitative Corpus Expansion

## 1. Author Canonical Mathematical Specifications

- [x] 1.1 Author `data/glossary/pecota_projections.md` containing Nate Silver's PECOTA mathematical formulation (Mahalanobis distance, similarity index, comparable nearest-neighbor weighting, aging curve transitions, Monte Carlo percentile distribution bands)
- [x] 1.2 Author `data/glossary/zips_projections.md` containing Dan Szymborski's ZiPS forecasting formulation (4-year recency decay 8/5/4/3, archetype aging decay, regression to league mean with sample-size weighting, comp-based variance)
- [x] 1.3 Author `data/glossary/marcel_projections.md` containing Tom Tango's Marcel the Monkey forecasting formulation (5/4/3 baseline weighting, +1200 PA / +100 IP regression to mean, 30-age piecewise threshold)
- [x] 1.4 Author `data/glossary/markov_chain_baseball.md` containing the 24-state discrete Markov chain formulation (Bukiet et al. 1997, transition matrix P, absorbing state, fundamental matrix N = (I - Q)^-1, run expectancy vector R)
- [x] 1.5 Author `data/glossary/nathan_trajectory_physics.md` containing Alan Nathan's pitch aerodynamics formulation (drag coefficient C_D, lift coefficient C_L, Magnus force vector, spin axis decomposition, trajectory integration)

## 2. Register Presets & Ingestion Pipeline

- [x] 2.1 Register the new presets (`pecota_projections`, `zips_projections`, `marcel_projections`, `markov_chain_baseball`, `nathan_trajectory_physics`) in `src/kb/sync/web.py`
- [x] 2.2 Add unit tests in `tests/test_glossary_presets.py` validating that each preset file exists, contains required LaTeX equations, and parses cleanly into ASTs
- [x] 2.3 Execute `kb ingest glossary --preset <name>` for each new preset, asserting document chunks, embeddings, and formulas are persisted into PostgreSQL

## 3. Formula Validation, Code Compilation & Quality Gates

- [x] 3.1 Run formula repair and quality gate evaluation across the new formulas via `kb corpus repair-all` and verify validation grades
- [x] 3.2 Recompile callable formulas in `packages/kb_formulas` and `src/kb/library/generated.py`, verifying newly compiled functions are executable
- [x] 3.3 Verify Web UI reflection and execution endpoints for the new compiled formulas

## 4. Multi-Domain Quantitative Literature Harvesting

- [x] 4.1 Execute multi-domain harvesting across pitch trajectory, framing, and baseball machine learning papers with deduplication and SFTP vaulting
- [x] 4.2 Verify workstation disk hygiene (>= 1.5 GB free) and homelab storage preservation

## 5. Quality Verification & Architecture Record

- [x] 5.1 Run all code quality gates: `uv run --no-sync ruff check src/ tests/ packages/ scripts/` and `uv run --no-sync pyright src/ tests/ packages/`
- [x] 5.2 Run automated test suite: `uv run --no-sync pytest tests/`
- [x] 5.3 Record architectural decisions as **ADR-040** in `docs/DECISIONS.md` and validate OpenSpec change strictly
