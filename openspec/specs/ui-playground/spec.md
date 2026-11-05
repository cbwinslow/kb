# ui-playground Specification

## Purpose
Expands the web dashboard (`kb ui serve`) with an interactive calculation playground and visual simulation environment, while strictly guaranteeing backward compatibility and zero regressions for existing UI tabs and API routes.

## Requirements

### Requirement: Interactive Playground Interface
The system SHALL provide a dedicated "Playground" tab accessible in the main navigation. It MUST support both preset canonical formulas and custom LaTeX input, generating reactive parameter controls dynamically.

#### Scenario: Navigating to formula playground
- **WHEN** user opens the playground view
- **THEN** system presents preset formulas and reactive parameter inputs

### Requirement: Real-time Evaluation Integration
Parameter adjustments MUST trigger dynamic evaluations against the `/api/eval` backend endpoint. Evaluation errors or invalid input combinations MUST display user-friendly error banners without crashing the web page or server.

#### Scenario: Adjusting formula parameter sliders
- **WHEN** user adjusts input sliders
- **THEN** system evaluates formula and renders computed output

### Requirement: Sensitivity Curve Visualization
The system SHALL provide interactive chart rendering displaying sensitivity curves.

#### Scenario: Plotting sensitivity curves
- **WHEN** parameter is swept across ranges
- **THEN** system plots sensitivity curves dynamically

### Requirement: Preservation of Existing Functionality
Existing tabs and their API routes MUST NOT experience any regressions or disruptions.

#### Scenario: Backward compatibility check
- **WHEN** existing endpoints are accessed
- **THEN** lineage, formulas, tables, and search views function as expected

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

### Requirement: Compiled Formula Registry Integration
The Web UI playground SHALL integrate with the standalone compiled formula library (`packages/kb_formulas`), providing a searchable dropdown of compiled scientific functions, automatically populating typed input fields for each function parameter, and executing calculations via `/api/formulas/compiled/{func_name}/eval`.

#### Scenario: Selecting compiled formula from registry
- **WHEN** user selects a compiled function from the playground dropdown
- **THEN** system fetches the function signature and docstring from `/api/formulas/compiled/{func_name}`, generating typed parameter inputs and displaying default values

#### Scenario: Executing live calculation in browser
- **WHEN** user inputs valid numeric arguments and clicks "Calculate"
- **THEN** system executes the compiled formula function and displays the numerical result along with a 2D parameter sensitivity plot

### Requirement: Multi-Format Code Export
The playground SHALL provide 1-click code export buttons allowing users to copy the active formula in Python scalar syntax, vectorized Polars expression syntax, SymPy symbolic syntax, or curl API format.

#### Scenario: Copying Polars expression code
- **WHEN** user clicks "Copy Polars Code" on an evaluated formula
- **THEN** system copies the corresponding `expr_*` expression snippet to the user's clipboard
