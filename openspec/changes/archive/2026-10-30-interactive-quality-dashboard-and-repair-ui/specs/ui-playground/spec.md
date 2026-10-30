# Spec Delta: ui-playground

## ADDED Requirements

### Requirement: Interactive Quality Gate Dashboard
The system SHALL provide a web dashboard tab displaying formula quality metrics, grade distributions, and filterable scorecards.

#### Scenario: Filtering formulas by quality grade
- **WHEN** user selects grade filter 'A' or status 'verified' in the UI dashboard
- **THEN** system filters the displayed formula list to show only verified Grade A equations with their respective composite scores

#### Scenario: Inspecting formula tier diagnostics
- **WHEN** user clicks on a formula scorecard card
- **THEN** system opens a diagnostic drawer displaying the point breakdown across Tiers 1–4, diagnostic messages, and actionable recommendations

### Requirement: In-Browser Formula Repair Trigger
The system SHALL provide an interactive repair button allowing users to trigger automated AST sanitization and immediate re-scoring.

#### Scenario: Executing 1-click repair in web UI
- **WHEN** user clicks the "Repair Formula" button on a degraded formula card
- **THEN** system calls `/api/formulas/{id}/repair`, runs the multi-stage repair pipeline, re-evaluates the quality gate, and updates the scorecard and grade badge without a full page reload
