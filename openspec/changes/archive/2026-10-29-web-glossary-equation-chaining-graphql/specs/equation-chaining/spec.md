# Specification: Symbolic Equation Chaining & System Solver

## Scope & Purpose
Expands symbolic mathematics capabilities to automatically discover, chain, and recursively substitute formulas across disparate papers and documents. Enables decomposing composite sabermetric metrics (such as Wins Above Replacement $WAR$, Runs Created, Base Runs) down to fundamental box-score primitives, as well as solving simultaneous systems of sabermetric equations via SymPy.

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
