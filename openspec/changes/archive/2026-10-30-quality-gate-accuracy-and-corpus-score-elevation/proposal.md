# Proposal: Quality Gate Accuracy & Corpus Score Elevation

## 1. Problem Statement & Motivation
In the initial corpus-wide mathematical quality gate execution across 4,356 valid scientific formulas, the mean corpus score reached 71.8 / 100 with 63.8% achieving Grade A or B. While this marks significant maturity, comprehensive diagnostic telemetry of the 1,576 formulas scoring Grade C, D, or F revealed five systemic root causes artificially depressing quality scores:

1. **Domain Ontology Coverage Gap (50.5% failure rate, ~4.5 pts lost)**:
   `SymbolOntology` only defined ~35 baseball-specific terms. Academic papers in baseball aerodynamics, trajectory modeling, ball-bat collision mechanics, and biometrics extensively employ universal physical and statistical symbols ($v, t, m, a, F, \theta, \omega, r, d, \rho, C_d, C_l, g, E, p, P, N, \mu, \sigma$). These symbols fail resolution to canonical concepts, causing widespread Tier 2 point deductions.
2. **False Cyclic Recursion Penalties (20.9% failure rate, 4.0 pts lost)**:
   In standard mathematical function definitions (e.g. $f(x) = \dots$, $D(q) = \dots$, $V_i(s) = \dots$), the function arguments in the LHS signature were incorrectly treated as "cyclic variables" appearing in the RHS. Furthermore, un-subscripted multi-letter metric differences (e.g. $\Delta RE = RE_{end} - RE_{start} + R_{play}$ sharing $R$) triggered false circular definition flags.
3. **`lambdify` Compilation Failures in Parameter Space Evaluation (18.5% failure rate, 10.0-13.0 pts lost)**:
   Using `lambdify(symbols, expr, modules="math")` caused `NameError` (e.g. `name 'rho' is not defined`, `name 'g' is not defined`) when expressions contained undefined functions or symbols not part of the standard Python `math` module, or raised `'float' object is not callable` when applied functions were present.
4. **Unlinked Benchmark Tables in Tier 4 Empirical Verification (Capped at 18.0 pts)**:
   Although the corpus contains **1,256 extracted benchmark tables** in `kb_benchmark_tables`, the corpus validation loop never passed parent document benchmark tables to `validate_formula`, leaving formulas unable to achieve the full 25.0 points in Tier 4.
5. **LaTeX Round-Trip Invertibility Subscript Normalization (33.3% failure rate, 5.0 pts lost)**:
   Cosmetic differences in generated LaTeX (e.g. `v_{exit}` vs `v_exit`, or subscript bracket groupings) caused exact set inequality between original free symbols and re-parsed symbols despite semantic equivalence.

## 2. Proposed Changes
1. **Physical & Mathematical Science Ontology Expansion (`src/kb/math/ontology.py`)**:
   Add canonical scientific domains to `SymbolOntology`:
   - Kinematics & Mechanics: `VELOCITY`, `ACCELERATION`, `TIME`, `MASS`, `FORCE`, `GRAVITY`, `MOMENTUM`, `ENERGY`.
   - Aerodynamics & Ballistics: `AIR_DENSITY`, `DRAG_COEFFICIENT`, `LIFT_COEFFICIENT`, `ATTACK_ANGLE`, `ANGULAR_VELOCITY` (spin rate), `RADIUS_DISTANCE`.
   - Probability & Statistics: `PROBABILITY`, `MEAN`, `VARIANCE_STDDEV`, `SAMPLE_SIZE`, `CORRELATION`.
2. **Refined Acyclic Definition Analysis (`src/kb/math/validation.py`)**:
   - For equality relations where LHS is an applied function $f(x_1, \dots, x_k)$, distinguish between the dependent function symbol $f$ and independent argument variables $(x_1, \dots, x_k)$, ensuring function arguments appearing in RHS are recognized as valid parameterizations rather than cyclic recursion.
   - Ignore atomic symbol overlap occurring only as prefixes or within multi-token acronyms.
3. **Robust Dual-Strategy Numerical Evaluator (`src/kb/math/validation.py`)**:
   - Implement primary evaluation via SymPy's native `expr.evalf(subs=...)` across positive test vectors, handling arbitrary mathematical functions, undefined functions, and Greek parameters without Python namespace exceptions.
   - Retain `lambdify` as a secondary acceleration path with fallback.
4. **Corpus Benchmark Table Linkage (`src/kb/cli.py`, `src/kb/math/validation.py`)**:
   - During `kb formulas validate`, look up benchmark tables from `kb_benchmark_tables` for the formula's document.
   - Award up to 25.0 pts in Tier 4 when formula parameters bind to columns in document tables and produce valid finite evaluations.
5. **LaTeX Round-Trip Symbol Normalization (`src/kb/math/validation.py`)**:
   - Normalize symbol strings (stripping enclosing braces, uniform subscript casing) prior to set comparison in Tier 1.

## 3. Success Criteria
- Mean corpus quality score improves from 71.8 to $\ge 82.0$ / 100 across the 4,356+ formulas in PostgreSQL.
- Grade A and B proportion increases from 63.8% to $\ge 75\%$.
- Domain Ontology Mapping failure rate drops from 50.5% to $< 20\%$.
- Parameter space finite evaluation failure rate drops from 18.5% to $< 5\%$.
- All 144 unit and integration tests pass with zero regressions.
- Static typing (`pyright`) and linting (`ruff`) maintain 100% compliance.
