# Spec Delta: mathematical-quality-gate

## ADDED Requirements

### Requirement: Interactive On-Demand Formula Re-Validation
The system SHALL support on-demand single-formula re-validation and scorecard refreshing triggered via REST endpoints.

#### Scenario: On-demand re-validation upon formula repair
- **WHEN** a repair request is received via `/api/formulas/{id}/repair`
- **THEN** system executes AST repair, invokes the multi-tier quality gate, updates `kb_formulas` with the new validation score and status, and returns the updated scorecard payload
