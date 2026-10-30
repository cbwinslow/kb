# Tasks: Multi-Hop Equation Chaining Engine

## 1. Dimensional Invariant & Concept Lineage Engine
- [x] 1.1 Implement dimensional validation utility in `src/kb/math/units.py` using `sympy.physics.units` and ontology dimensions.
- [x] 1.2 Extend `SymbolOntology` with dimensional mapping attributes (length, time, mass, dimensionless).

## 2. Multi-Hop Graph Traversal & Chaining
- [x] 2.1 Implement multi-hop pathfinder in `src/kb/math/chaining.py` traversing formulas via canonical concept matching.
- [x] 2.2 Implement cycle detection and max-depth bounds in cross-paper recursive AST substitution.
- [x] 2.3 Implement unified closed-form AST derivation and LaTeX step formatting.

## 3. CLI & GraphQL Query Endpoints
- [x] 3.1 Add `kb equations chain` command to `src/kb/cli.py` with `--from`, `--to`, and `--json` support.
- [x] 3.2 Implement `equationChain` GraphQL query and types in `src/kb/graphql/schema.py`.

## 4. Verification & Testing
- [x] 4.1 Write comprehensive unit tests in `tests/test_chaining.py` testing bat collision to WAR derivation path.
- [x] 4.2 Verify dimensional rejection on incompatible unit substitutions.
- [x] 4.3 Run full quality gates: `uv run ruff check`, `uv run pyright`, `uv run pytest`.
