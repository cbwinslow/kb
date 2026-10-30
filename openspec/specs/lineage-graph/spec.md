# lineage-graph Specification

## Purpose
Infers and represents mathematical formula derivation networks (DAGs) across scientific literature based on mathematical symbol overlap and relation classification.

## Requirements

### Requirement: Formula Lineage Inference
The system SHALL infer directed derivation edges between extracted formulas by analyzing mathematical symbol overlaps and structural similarities, and construct multi-hop derivation trajectories across papers.

#### Scenario: Detecting derivation relation via Jaccard symbol similarity
- **WHEN** two formulas share significant mathematical variables ($\text{Jaccard index} \ge 0.35$ and shared symbols $\ge 2$)
- **THEN** system infers a derivation relationship edge connecting the earlier paper formula to the later formula

#### Scenario: Multi-hop lineage DAG construction
- **WHEN** multiple equations form a chain connecting low-level experimental observables to high-level summary metrics
- **THEN** system constructs a directed acyclic graph (DAG) representing the complete multi-hop lineage path with edge metadata specifying substituted variables and dimensional mappings

### Requirement: Relation Type Classification
The system SHALL classify derivation edges into distinct relation categories: equality, approximation, specialization, or generalization.

#### Scenario: Classifying equality vs. approximation relation
- **WHEN** an edge connects two formulas with explicit algebraic equality
- **THEN** system tags the relation as equality (`EQUALS`); when Taylor expansions or empirical limits are detected, system tags the relation as approximation (`APPROXIMATES`)

### Requirement: Interactive Lineage Visualization Export
The system SHALL export the derivation graph into interactive visual representations (HTML, SVG, JSON).

#### Scenario: Visualizing formula lineage DAG
- **WHEN** user opens the lineage dashboard (`lineage_dashboard.html` or `/api/lineage`)
- **THEN** system renders interactive nodes with formula LaTeX, citekeys, and color-coded relation edges
