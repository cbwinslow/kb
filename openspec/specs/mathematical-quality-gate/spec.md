# mathematical-quality-gate Specification

## Purpose
Provides a multi-tier mathematical quality gate for scientific formulas, systematically evaluating AST round-trip invertibility, semantic symbol tokenization, dimensional consistency, boundary condition invariants, and empirical ground-truth accuracy.

## Requirements

### Requirement: AST Invertibility and Round-Trip Fidelity
The system SHALL verify that a parsed SymPy formula converts back to LaTeX and re-parses into an identical symbolic AST without losing variables, relational operators, or structural depth.

#### Scenario: Successful AST round-trip verification
- **WHEN** a valid parsed formula is evaluated for AST invertibility
- **THEN** the system generates LaTeX via SymPy, re-parses it, confirms free symbols and structure match, and awards full Tier 1 points

#### Scenario: Detected round-trip degradation
- **WHEN** re-parsing the serialized LaTeX produces a different symbol set or fails to parse
- **THEN** the system flags an AST round-trip failure, logs the discrepancy, and docks Tier 1 quality points

### Requirement: Semantic Symbol Tokenization and Dimensional Consistency
The system SHALL audit formula symbols against domain ontology to detect fragmented multi-letter acronyms and check dimensional consistency between rate metrics and count metrics.

#### Scenario: Flagging accidental symbol splitting
- **WHEN** an equation contains single-letter variables that spell known multi-letter domain statistics (such as $w \cdot O \cdot B \cdot A$ instead of $wOBA$)
- **THEN** the system flags an encoding warning and suggests atomic token repair

#### Scenario: Verifying rate and count consistency
- **WHEN** an equation directly adds rate statistics without weighting coefficients or contains cyclic LHS definitions
- **THEN** the system notes a dimensional sanity warning in the validation scorecard

### Requirement: Boundary Invariants and Monotonicity Analysis
The system SHALL evaluate symbolic partial derivatives and parameter space samples to verify physical monotonicity, absence of singularities, and bounded outputs.

#### Scenario: Testing win probability monotonicity
- **WHEN** evaluating a win expectation formula with runs scored and runs allowed
- **THEN** the system computes partial derivatives, confirms positive derivative with respect to runs scored and negative with respect to runs allowed, and verifies bounded range $[0, 1]$

#### Scenario: Detecting division-by-zero or NaN in plausible domain
- **WHEN** a formula yields NaN, infinity, or complex numbers within standard domain input intervals
- **THEN** the system flags a boundary violation and reports the failing input vector

### Requirement: Empirical Benchmark Ground-Truth Evaluation
The system SHALL evaluate compiled executable formulas against extracted tabular benchmark data fixtures and assess absolute and relative error tolerances.

#### Scenario: Benchmarking against empirical tables
- **WHEN** a formula has associated benchmark tables in the corpus
- **THEN** the system binds table columns via ontology, evaluates predictions against ground truth, and verifies mean absolute error against tolerance $\epsilon \le 10^{-4}$

### Requirement: Composite Formula Quality Scorecard and CLI Reporting
The system SHALL synthesize results across all tiers into a standardized quality score from 0 to 100 with a letter grade, persist it to storage, and report diagnostics via CLI.

#### Scenario: Generating quality scorecard via CLI
- **WHEN** `kb formulas validate --id <formula_id>` is executed
- **THEN** the system outputs a detailed multi-tier scorecard breakdown, composite score, letter grade, and diagnostic recommendations
