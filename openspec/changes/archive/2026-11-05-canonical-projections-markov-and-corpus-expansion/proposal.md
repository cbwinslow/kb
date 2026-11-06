# Proposal: Canonical Projections, Markov Models, and Quantitative Corpus Expansion

## Why
While the knowledge base holds 311 documents and 6,199 formulas, critical industry-standard baseball forecasting architectures—specifically PECOTA, ZiPS, and Marcel—and discrete Markov chain game-state models are currently referenced only in bibliography citations and comparative discussions rather than primary mathematical entities. Ingesting canonical specifications, mathematical formulations, and expanded research literature directly equips researchers and AI agents with first-class callable projection systems and game-state evaluation engines.

## What Changes
- Ingest canonical, mathematically complete technical specifications for **PECOTA** (Mahalanobis distance similarity, comparable weighting, age curves, percentile distributions).
- Ingest canonical specifications for **ZiPS** ($8/5/4/3$ recency decay, archetype aging transitions, regression to the mean sample-size weighting, comp-based variance).
- Ingest canonical specifications for **Marcel the Monkey** ($5/4/3$ weighting, $+1200\text{ PA} / +100\text{ IP}$ regression, piecewise 30-age adjustment).
- Ingest foundational **Discrete Markov Chain Game-State Models** (Bukiet et al. 1997 / Tango RE24: $24 \times 24$ state transition matrix $P$, fundamental matrix $N = (I - Q)^{-1}$, and run scoring vectors).
- Ingest expanded high-value quantitative literature across pitch aerodynamics (Nathan trajectory physics, Seam-Shifted Wake), catcher framing (GAM spatial splines), defensive metrics (Statcast OAA catch probability), and machine learning sequencing.
- Run formula extraction, AST verification, and code compilation to expose new verified equations in `packages/kb_formulas` and the Web UI Playground.

## Capabilities

### New Capabilities
- `projection-systems`: Canonical mathematical formulations and algorithmic specifications for PECOTA, ZiPS, and Marcel forecasting models.
- `markov-baseball-models`: Discrete-time Markov chain transition matrices, absorbing state formulations, fundamental matrix inversions, and run expectancy derivations.

### Modified Capabilities
- `document-ingestion`: Ingest structured markdown methodologies and quantitative literature into PostgreSQL with metadata indexing and homelab SFTP vaulting.
- `web-glossary-harvester`: Expand canonical glossary parser to ingest structured projection architectures and matrix models.

## Impact
- Expands knowledge base with core forecasting and game-state models essential for modern sabermetric research.
- Adds new Grade A callable equations to `packages/kb_formulas` and the interactive Web UI Playground.
- Preserves all database invariants, homelab storage isolation, and zero-error quality gates.
