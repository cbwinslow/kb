# Spec Delta: benchmark-extraction

## ADDED Requirements

### Requirement: Automated Formula-to-Table Column Binding
The system SHALL bind symbolic formula parameters to column names in extracted benchmark tables using the semantic symbol ontology.

#### Scenario: Mapping formula parameters to table headers via ontology
- **WHEN** an empirical table is linked to a formula for benchmark evaluation
- **THEN** system maps table header aliases to canonical concepts and constructs the evaluation column mapping without manual schema definition
