# Design: Canonical Projections, Markov Models, and Quantitative Corpus Expansion

## Context
See `proposal.md` for background and motivation. The knowledge base contains 311 documents, but lacks primary mathematical entities for industry-standard forecasting systems (PECOTA, ZiPS, Marcel) and discrete Markov chain transition models. Because these systems were originally published in books, research articles, or analytical blogs rather than arXiv, they must be codified as authoritative, structured quantitative methodology specifications in `data/glossary/` and ingested through the pipeline.

## Goals / Non-Goals

**Goals:**
- Author mathematically complete canonical specifications for PECOTA, ZiPS, Marcel the Monkey, and Markov chain game-state models.
- Ingest these specifications through `WebGlossaryHarvester` and `IngestionPipeline`, generating semantic chunks, BGE-M3 embeddings, and `kb_formulas` entries.
- Ensure new formulas pass the `QualityGate` with Grade A scores and compile into callable functions in `packages/kb_formulas` and `generated.py`.
- Execute automated literature discovery and ingestion across related advanced topics (Nathan pitch aerodynamics, Magnus force, Seam-Shifted Wake, catcher framing GAMs).
- Verify homelab SFTP vaulting and maintain $\ge 1.5$ GB workstation disk floor.

**Non-Goals:**
- Creating custom training pipelines or full machine learning model retraining from scratch.
- Modifying core database schema or breaking existing GraphQL/FastMCP APIs.

## Decisions

### 1. Authoritative Structured Specification Architecture
- **Decision**: Author complete, formal technical specifications in `data/glossary/`:
  - `pecota_projections.md`: Nate Silver's Mahalanobis distance metric $D^2(x, y) = (x - y)^T \Sigma^{-1} (x - y)$, similarity score $S = 1000 - \sum w_i |x_i - y_i|$, comparable weighted projections, aging adjustments, and probability percentiles.
  - `zips_projections.md`: Dan Szymborski's 4-year weighted baseline ($8/5/4/3$ recency decay), archetype aging transitions, sample-size regression to league mean $E[X] = \frac{PA}{PA + C} \cdot \text{Obs} + \frac{C}{PA + C} \cdot \mu_{\text{lg}}$, and comp-based variance.
  - `marcel_projections.md`: Tom Tango's 5/4/3 baseline weighting, constant regression to league average ($+1200\text{ PA}$ for batters, $+100\text{ IP}$ for pitchers), and 30-age piecewise adjustments.
  - `markov_chain_baseball.md`: Bukiet, Harold, and Palacios (1997) $24 \times 24$ state transition matrix $P$, non-absorbing matrix $Q$, fundamental matrix $N = (I - Q)^{-1}$, and total expected runs vector $R = N \cdot E$.
  - `nathan_trajectory_physics.md`: Alan Nathan (2008) pitch trajectory aerodynamics, Magnus force, lift coefficient $C_L$, drag coefficient $C_D$, spin axis components, and gravity vector.
- **Alternatives Considered**: Ingesting third-party commentary blog posts. *Rejected* because blog posts often have noisy HTML, broken equation formatting, and lack formal mathematical definitions.

### 2. Integration with `WebGlossaryHarvester` and Formula Compilation
- **Decision**: Register the new specifications into `SABERMETRIC_PRESETS` in `src/kb/sync/web.py` and invoke `kb ingest glossary --preset <name>`.
- **Pipeline Execution**:
  - `IngestionPipeline.ingest_markdown_source()` chunks the text, preserves LaTeX equations atomically, and generates BGE-M3 embeddings.
  - `FormulaExtractor` and `EquationSanitizer` parse equations into SymPy ASTs.
  - `QualityGate` validates equations.
  - `FormulaCompiler` regenerates `packages/kb_formulas` and `src/kb/library/generated.py`, enabling immediate execution in the Web UI Playground.

### 3. Automated Quantitative Literature Expansion Sweeps
- **Decision**: Execute targeted harvesting queries via `kb sync harvest` across OpenAlex and arXiv focusing on sports physics, trajectory modeling, and machine learning in baseball, vaulting PDFs to homelab storage via SFTP and cleaning local temporary files.

## Risks / Trade-offs

- **[Risk]** Complex matrix expressions (like $24 \times 24$ matrices) may produce long LaTeX strings.
  $\to$ **Mitigation**: Encode the fundamental equation $N = (I - Q)^{-1}$ and element-wise transition equations $P_{(b, o) \to (b', o')}$ symbolically while providing the state mapping dictionary cleanly in markdown tables.
- **[Risk]** Disk space pressure on workstation `cbwwin` during bulk harvesting.
  $\to$ **Mitigation**: Enforce immediate SFTP upload to homelab storage and unlinking of local temporary PDF assets, asserting disk free space remains $\ge 1.5$ GB.
