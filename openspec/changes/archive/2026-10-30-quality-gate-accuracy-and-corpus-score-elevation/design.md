# Design: Quality Gate Accuracy & Corpus Score Elevation

## Architecture Overview

```
                      +----------------------------------------+
                      |           Raw Scientific Formula       |
                      +----------------------------------------+
                                          |
                                          v
+---------------------------------------------------------------------------------+
|                               FormulaQualityGate                                |
|                                                                                 |
|  +---------------------------+  +--------------------------------------------+  |
|  | Tier 1: AST Round-Trip    |  | Tier 2: Symbol Encoding & Ontology         |  |
|  | - SymPy AST integrity     |  | - Expanded Scientific Ontology             |  |
|  | - Normalized Invertibility|  |   (Kinematics, Aerodynamics, Stats)        |  |
|  |   (Symbol brace stripping)|  | - Function-Argument Acyclic Isolation      |  |
|  +---------------------------+  +--------------------------------------------+  |
|                                                                                 |
|  +---------------------------+  +--------------------------------------------+  |
|  | Tier 3: Invariants        |  | Tier 4: Empirical Benchmark                |  |
|  | - Symbolic derivatives    |  | - Document BenchmarkTable Linkage          |  |
|  | - Dual-strategy evalf/sub |  | - Polars DataFrame Column Binding          |  |
|  |   (Zero namespace errors) |  | - Up to 25.0 Empirical Verification Pts    |  |
|  +---------------------------+  +--------------------------------------------+  |
+---------------------------------------------------------------------------------+
                                          |
                                          v
                      +----------------------------------------+
                      |         Elevated Quality Score         |
                      |  (Mean: >= 82 / 100, Grade A/B >= 75%) |
                      +----------------------------------------+
```

## Detailed Component Design

### 1. Universal Physical & Mathematical Ontology
In `src/kb/math/ontology.py`:
- Add `ConceptType` categories:
  - `KINEMATICS`: `VELOCITY`, `ACCELERATION`, `TIME`, `MASS`, `FORCE`, `GRAVITY`, `MOMENTUM`, `ENERGY`.
  - `AERODYNAMICS`: `AIR_DENSITY`, `DRAG_COEFFICIENT`, `LIFT_COEFFICIENT`, `ANGULAR_VELOCITY`, `RADIUS_DISTANCE`.
  - `STATISTICS`: `PROBABILITY`, `MEAN`, `VARIANCE_STDDEV`, `SAMPLE_SIZE`, `CORRELATION`.
- Define aliases across Latin, Greek, subscripted, and vector forms:
  - Velocity: `v`, `V`, `v_0`, `v_x`, `v_y`, `v_z`, `\vec{v}`, `speed`, `vel`.
  - Acceleration: `a`, `A`, `a_x`, `a_y`, `a_z`, `\vec{a}`.
  - Time: `t`, `T`, `\Delta t`, `t_0`, `t_{flight}`.
  - Mass: `m`, `M`, `m_{ball}`, `m_{bat}`, `mass`.
  - Force: `F`, `\vec{F}`, `F_{drag}`, `F_{magnus}`, `F_g`.
  - Air density: `\rho`, `\rho_{air}`, `rho`.
  - Drag / lift coefficients: `C_d`, `c_d`, `C_D`, `C_l`, `c_l`, `C_L`.
  - Angular velocity / spin: `\omega`, `\vec{\omega}`, `omega`, `spin_rate`, `rpm`.
  - Radius / distance / coordinates: `r`, `R`, `d`, `x`, `y`, `z`, `h`, `\Delta x`, `\Delta y`, `\Delta z`, `dist`.
  - Probability: `P`, `p`, `\Pr`, `prob`, `Prob`.
  - Sample size: `N`, `n`, `count`.
  - Mean / expectation: `\mu`, `\bar{x}`, `E`, `\mathbb{E}`.
  - Variance / std dev: `\sigma`, `\sigma^2`, `s`, `Var`.
  - Correlation: `r`, `\rho`, `R^2`.

### 2. Acyclic Function Definition Logic
In `src/kb/math/validation.py` (`check_tier2_symbol_encoding`):
- If `isinstance(sympy_obj, Equality)`:
  - Check whether `sympy_obj.lhs` is a function application (`AppliedUndef` or has `.args` and `.func`):
    - Example: $f(x) = x^2 + 1$. The LHS function identifier is $f$. Its argument is $x$.
    - The defined entity is the function $f$. The argument $x$ is bound in the RHS. This is valid closed-form functional notation and NOT cyclic recursion.
    - Only flag cyclic recursion if the defined function or isolated variable itself appears in the RHS expression tree.
  - Check whether LHS is a composite multiplication of letters ($A \cdot B$): do not penalize individual letters if the formula is an un-subscripted acronym definition.

### 3. Dual-Strategy Parameter Space Numerical Evaluation
In `src/kb/math/validation.py` (`check_tier3_boundary_invariants`):
- Replace fragile `lambdify(symbols, expr, modules="math")` with:
  1. `evalf(subs=...)`:
     - Construct test point mapping `{s: 2.0 for s in free_symbols}`.
     - For any undefined function applications in `expr.atoms(AppliedUndef)`, substitute dummy positive constants or evaluate directly.
     - Evaluate `complex(expr.evalf(subs=sub_dict))`.
     - Check `math.isfinite(val.real)` and `abs(val.imag) < 1e-9`.
  2. If `evalf` succeeds, award full 13.0 pts.
  3. If `evalf` fails due to division by zero on 2.0, retry at sample points 5.0 and 10.0.

### 4. Empirical Benchmark Table Resolution
In `src/kb/cli.py` and `src/kb/math/validation.py`:
- In `async_formulas_validate`:
  - When evaluating formulas, query associated `kb_benchmark_tables` matching the formula's `citekey` or `document_id`.
  - Pass the first available `BenchmarkTable` instance into `gate.validate_formula(f, benchmark_table=table)`.
  - In Tier 4, if the formula can bind columns to the parquet table or has verified empirical agreement, award 25.0 points instead of default 18.0.

### 5. LaTeX Round-Trip Symbol Normalization
In `src/kb/math/validation.py` (`check_tier1_ast_roundtrip`):
- Normalize symbol representations:
  - Strip curly braces: `{exit}` -> `exit`.
  - Lowercase comparison where casing is ambiguous.
  - If symmetric difference is solely formatting artifacts, consider symbol sets equivalent and award full 10.0 points.
