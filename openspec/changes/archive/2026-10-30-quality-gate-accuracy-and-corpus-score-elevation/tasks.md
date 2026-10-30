# Tasks: Quality Gate Accuracy & Corpus Score Elevation

## 1. Domain Ontology Expansion (Scientific & Physical Principles)

- [x] 1.1 Add canonical physical and statistical concept types (`VELOCITY`, `ACCELERATION`, `TIME`, `MASS`, `FORCE`, `GRAVITY`, `AIR_DENSITY`, `DRAG_COEFFICIENT`, `LIFT_COEFFICIENT`, `ANGULAR_VELOCITY`, `RADIUS_DISTANCE`, `PROBABILITY`, `MEAN`, `VARIANCE_STDDEV`, `SAMPLE_SIZE`, `CORRELATION`, `ENERGY`, `MOMENTUM`) to `ConceptType` in `src/kb/math/ontology.py`.
- [x] 1.2 Register canonical concepts and extensive scientific LaTeX/Greek/subscript aliases in `SymbolOntology._register_default_concepts`.
- [x] 1.3 Add unit test in `tests/test_ontology.py` verifying scientific symbol resolution ($v, a, t, m, F, \rho, C_d, \omega, r, P, N, \sigma$).

## 2. Refined Acyclic & Functional Definition Checking

- [x] 2.1 Refactor `check_tier2_symbol_encoding` in `src/kb/math/validation.py` to identify function signatures (e.g. $f(x)$, $D(q)$, $V_i(s)$) and prevent function arguments from triggering false cyclic recursion.
- [x] 2.2 Add unit tests in `tests/test_validation.py` verifying that functional definitions ($f(x) = x^2 + 1$) receive full 7.0 acyclic definition points while genuine cyclic recursion ($x = x + 1$) is correctly flagged.

## 3. Dual-Strategy Parameter Space Numerical Evaluation

- [x] 3.1 Refactor `check_tier3_boundary_invariants` in `src/kb/math/validation.py` to use SymPy `evalf(subs=...)` with undefined function handling and fallback, eliminating `NameError` and `'float' object is not callable` exceptions.
- [x] 3.2 Add unit tests in `tests/test_validation.py` verifying expressions with Greek letters, undefined functions ($g(i)$), and mathematical functions evaluate without namespace exceptions.

## 4. LaTeX Round-Trip Normalization & Benchmark Table Linkage

- [x] 4.1 Normalize symbol names in `check_tier1_ast_roundtrip` (`src/kb/math/validation.py`) to eliminate false mismatches from curly brace wrappers and subscript casing.
- [x] 4.2 In `src/kb/cli.py` (`async_formulas_validate`), join or pre-fetch `kb_benchmark_tables` by document citekey and pass tables into `gate.validate_formula(f, benchmark_table=...)`.
- [x] 4.3 Add unit test in `tests/test_validation.py` verifying benchmark table linkage awards 25.0 points in Tier 4.

## 5. Corpus Validation Execution & OpenSpec Archival

- [x] 5.1 Run all unit tests (`uv run pytest tests/`).
- [x] 5.2 Execute corpus validation (`uv run kb formulas validate --all`) and measure the elevated mean quality score and grade distribution.
- [x] 5.3 Verify static analysis: `uv run ruff check` and `uv run pyright`.
- [x] 5.4 Record ADR-028 in `docs/DECISIONS.md`, sync delta specs to `openspec/specs/`, and archive the change.
