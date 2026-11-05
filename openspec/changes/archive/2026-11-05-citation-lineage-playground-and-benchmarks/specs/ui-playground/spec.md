# Spec Delta: ui-playground

## ADDED Requirements

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
