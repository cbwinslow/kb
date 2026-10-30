# Spec Delta: lineage-graph

## MODIFIED Requirements

### Requirement: Formula Lineage Inference
The system SHALL infer directed derivation edges between extracted formulas by analyzing mathematical symbol overlaps and structural similarities, and construct multi-hop derivation trajectories across papers.

#### Scenario: Detecting derivation relation via Jaccard symbol similarity
- **WHEN** two formulas share significant mathematical variables ($\text{Jaccard index} \ge 0.35$ and shared symbols $\ge 2$)
- **THEN** system infers a derivation relationship edge connecting the earlier paper formula to the later formula

#### Scenario: Multi-hop lineage DAG construction
- **WHEN** multiple equations form a chain connecting low-level experimental observables to high-level summary metrics
- **THEN** system constructs a directed acyclic graph (DAG) representing the complete multi-hop lineage path with edge metadata specifying substituted variables and dimensional mappings
