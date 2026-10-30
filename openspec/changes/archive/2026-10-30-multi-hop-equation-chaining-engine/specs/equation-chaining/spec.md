# Spec Delta: equation-chaining

## ADDED Requirements

### Requirement: Cross-Paper Multi-Hop Chaining
The system SHALL discover constituent equations matching free RHS symbols against database formulas across different scientific papers using canonical concepts, and verify physical dimensional compatibility between connected nodes.

#### Scenario: Cross-paper parameter lineage substitution
- **WHEN** chaining a target formula with free parameters whose canonical concepts match the LHS definition of a formula from a different paper
- **THEN** system performs recursive symbolic substitution, logs the cross-paper substitution step, and constructs a unified derivation AST

#### Scenario: Dimensional invariant check between chained formulas
- **WHEN** an upstream formula output is substituted into a downstream input parameter
- **THEN** system checks dimensional equivalence via SymPy units and rejects substitution or emits a dimensional warning if dimensions are incompatible

### Requirement: Multi-Hop Query Interface
The system SHALL provide CLI and GraphQL query interfaces to execute multi-hop derivation searches between arbitrary source and target formulas or canonical concepts.

#### Scenario: Querying multi-hop derivation path
- **WHEN** user executes `kb equations chain --from BAT_SPEED --to WAR` or sends a GraphQL query `equationChain(fromConcept: "BAT_SPEED", toConcept: "WAR")`
- **THEN** system returns the directed derivation path, intermediate formulas, closed-form unified equation, and substitution trace
