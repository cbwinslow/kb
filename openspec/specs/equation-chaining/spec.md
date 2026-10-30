# equation-chaining Specification

## Purpose
Expands symbolic mathematics capabilities to automatically discover, chain, and recursively substitute formulas across disparate papers and documents. Enables decomposing composite sabermetric metrics down to fundamental box-score primitives, as well as solving simultaneous systems of sabermetric equations via SymPy.

## Requirements

1. **Data Structures**:
   - `SubstitutionStep`: Tracks individual substitution events, recording the variable symbol substituted, source formula ID / citekey, source expression, and substituted target expression.
   - `ChainedFormulaResult`: Contains target formula ID, closed-form unified SymPy expression, closed-form LaTeX representation, substitution trace steps, ordered set of primitive (unresolved) symbols, and compiled Python / Polars evaluation code.
2. **Formula Chaining Engine**:
   - `FormulaChainingEngine` in `kb.math.chaining`:
     - Discovers constituent equations matching free RHS symbols against database formulas where `LHS == symbol` or canonical concept matches.
     - Supports recursive substitution (`sympy.subs`) with configurable `max_depth` (default 5) and cycle detection to prevent infinite recursion.
     - Simplifies unified expressions via `sympy.simplify`.
     - Compiles unified closed-form expressions to vectorized Polars column expressions and pure Python callables via `FormulaCompiler`.
3. **Simultaneous Systems of Equations**:
   - `solve_system(formula_ids: list[str], target_symbols: list[str])` MUST parse constituent formulas into SymPy equations ($LHS - RHS = 0$) and apply `sympy.solve` to derive analytical solutions for target unknown parameters.
4. **CLI & Programmatic Access**:
   - Exposed via CLI commands `kb formulas chain --id <id> [--max-depth <d>]` and `kb formulas solve --ids <id1> <id2> --symbols <sym1> <sym2>`.

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
