# ui-server Specification

## Purpose
Provides a local HTTP server command allowing users and AI agents to explore the scientific knowledge graph, inspect formulas, view derivation DAGs, and execute live calculations in a browser.

## Requirements

### Requirement: Interactive Dashboard Server
The system SHALL provide a CLI command `kb ui serve` that starts a local web server hosting the scientific explorer dashboard.

#### Scenario: Launching local web dashboard
- **WHEN** user executes `kb ui serve --port 8000`
- **THEN** server starts, binds to the specified port, and serves the dashboard HTML/JS assets

### Requirement: Live Formula Execution API
The UI server SHALL expose an endpoint `/api/eval` allowing dynamic execution of formulas given a formula ID and parameter values.

#### Scenario: Querying live calculation from dashboard
- **WHEN** user or frontend requests POST `/api/eval` with formula ID and input parameters
- **THEN** server computes the result via SymPy/lambdify and returns JSON containing the computed numerical value
