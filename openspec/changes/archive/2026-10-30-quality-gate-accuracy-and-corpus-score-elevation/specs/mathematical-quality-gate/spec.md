# mathematical-quality-gate Delta Specification

## MODIFIED Requirements

### Requirement: Semantic Symbol Tokenization and Dimensional Consistency
The system SHALL audit formula symbols against domain ontology to detect fragmented multi-letter acronyms, check dimensional consistency between rate metrics and count metrics, and accurately distinguish between cyclic variable recursion ($x = x + 1$) and standard functional definitions ($f(x) = \text{expression}(x)$) where input arguments appear on the RHS.

#### Scenario: Flagging accidental symbol splitting
- **WHEN** an equation contains single-letter variables that spell known multi-letter domain statistics (such as $w \cdot O \cdot B \cdot A$ instead of $wOBA$)
- **THEN** the system flags an encoding warning and suggests atomic token repair

#### Scenario: Verifying rate and count consistency
- **WHEN** an equation directly adds rate statistics without weighting coefficients or contains cyclic LHS definitions
- **THEN** the system notes a dimensional sanity warning in the validation scorecard

#### Scenario: Functional definition parameter isolation
- **WHEN** an equation defines an applied function $f(x) = x^2 + 1$ or $D(q) = \frac{q^2}{q^2 + (1-q)^2}$
- **THEN** the system isolates the function symbol from its arguments, recognizes $x$ or $q$ as independent arguments, and awards full acyclic definition score

### Requirement: Boundary Invariants and Monotonicity Analysis
The system SHALL evaluate symbolic partial derivatives and parameter space samples to verify physical monotonicity, absence of singularities, and bounded outputs, using robust dual-strategy numerical substitution to prevent Python namespace exceptions on undefined or Greek functions.

#### Scenario: Testing win probability monotonicity
- **WHEN** evaluating a win expectation formula with runs scored and runs allowed
- **THEN** the system computes partial derivatives, confirms positive derivative with respect to runs scored and negative with respect to runs allowed, and verifies bounded range $[0, 1]$

#### Scenario: Detecting division-by-zero or NaN in plausible domain
- **WHEN** a formula yields NaN, infinity, or complex numbers within standard domain input intervals
- **THEN** the system flags a boundary violation and reports the failing input vector

#### Scenario: Robust parameter space evaluation
- **WHEN** an expression contains Greek symbols or undefined functions (such as $\rho$ or $g(i)$)
- **THEN** the system evaluates finite values via SymPy substitution without raising Python `NameError` or type errors

### Requirement: Empirical Benchmark Ground-Truth Evaluation
The system SHALL evaluate compiled executable formulas against extracted tabular benchmark data fixtures and assess absolute and relative error tolerances, correlating formulas with their parent document's extracted benchmark tables during corpus validation to award full empirical ground-truth verification points.

#### Scenario: Benchmarking against empirical tables
- **WHEN** a formula has associated benchmark tables in the corpus
- **THEN** the system binds table columns via ontology, evaluates predictions against ground truth, and verifies mean absolute error against tolerance $\epsilon \le 10^{-4}$

#### Scenario: Automatic benchmark table linkage
- **WHEN** validating a formula whose document contains extracted benchmark tables
- **THEN** the system binds table columns via ontology and awards empirical verification points (up to 25.0)
