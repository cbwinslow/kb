# Spec Delta: corpus-formula-repair

## ADDED Requirements

### Requirement: Batch Formula Repair with Quality Gate Integration
The system SHALL support batch-level repair and automated quality gate score elevation across all formulas in `kb_formulas`.

#### Scenario: Progressive repair and scorecard elevation
- **WHEN** user executes `kb corpus repair-all` or `kb formulas repair --evaluate-grades`
- **THEN** system processes invalid or unvalidated formulas, sanitizes LaTeX representations, parses SymPy ASTs, assigns Tier 1–4 diagnostic scores, and writes letter grades in progressive transaction batches.

#### Scenario: Updating diagnostic validation details in-place
- **WHEN** an unvalidated formula is processed by the batch repair pipeline
- **THEN** formula record is updated with `validation_status` ('verified', 'provisional', 'degraded', or 'failed'), `validation_score` (0.0 to 100.0), and a structured `validation_details` JSON payload.
