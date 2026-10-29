# Proposal: Mathematical Quality Gate & Multi-Tier Validation Engine

## Why
While the corpus yield has reached 73.5% (4,326 valid formulas), syntactic parsing alone does not guarantee that mathematical formulas are semantically correct, properly encoded in SymPy, dimensionally sound, or physically plausible. The user needs a rigorous mathematical quality gate and validation system that answers: *"How do we know what we have is mathematically correct? How do we validate our results and ensure SymPy symbols/ASTs are properly encoded?"*

Currently, there is no automated mechanism to catch accidental symbol multiplications (e.g. multi-letter acronyms parsed as products of separate variables), check dimensional compatibility between rate stats and count stats, test boundary conditions and partial derivative monotonicity, or verify outputs against empirical benchmark tables.

## What Changes
- **Multi-Tier Validation Engine (`kb.math.validation`)**:
  - **Tier 1 (AST Round-Trip Invertibility)**: Converts parsed SymPy ASTs back to LaTeX via `sympy.latex()`, re-parses them, and verifies that the symbolic free symbols, expression tree depth, and relational structure are preserved identically without loss of mathematical semantics.
  - **Tier 2 (Symbol Tokenization & Dimensional Consistency)**: Audits free symbols against known sabermetric entities and the semantic ontology (`SymbolOntology`). Detects accidental multi-letter product splittings (e.g., $w \cdot O \cdot B \cdot A$ instead of $wOBA$). Checks dimensional sanity (e.g., rate statistics $[0, 1]$ added to count statistics without normalization or weight coefficients, recursive LHS appearance in RHS).
  - **Tier 3 (Boundary Invariants & Monotonicity)**: Computes analytical partial derivatives with SymPy ($\frac{\partial f}{\partial x_i}$) to verify directional monotonicity (e.g., more runs scored increases win expectation; more runs allowed decreases it). Evaluates boundary limits and checks parameter space sampling for NaNs, division-by-zero, or imaginary numbers.
  - **Tier 4 (Empirical Benchmark Table Evaluation)**: Automatically maps formula parameters to extracted benchmark tables (`kb_benchmark_tables`) using `SymbolOntology`, executes the compiled formula, and measures mean absolute error (MAE) and relative error against ground truth.
- **Formula Quality Scorecard**: Computes a transparent 0-100 score and quality grade (A, B, C, D, F) across all 4 tiers with actionable diagnostic messages.
- **Database Model Enrichment**: Adds `validation_score`, `validation_status`, and `validation_details` JSON to `kb_formulas` to persist verification state.
- **CLI Validation Suite**: Introduces `kb formulas validate [--id <id>] [--citekey <key>] [--all] [--min-score <score>] [--json]` to run quality checks across single formulas or the entire corpus.
- **GraphQL & UI Integration**: Adds `ValidationScorecard` to GraphQL queries and embeds validation badges and expandable diagnostic breakdowns into the Web UI.

## Capabilities

### New Capabilities
- `mathematical-quality-gate`: Multi-tier mathematical quality gate providing AST round-trip verification, symbol tokenization audit, dimensional/rate consistency, boundary and monotonicity testing, empirical table comparison, and composite quality scoring.

### Modified Capabilities
- `formula-verification`: Extends formula verification requirements with automated quality gate scoring, symbol tokenization validation, and diagnostic scorecard generation.

## Impact
- **Database Schema**: Adds `validation_score` (Float), `validation_status` (String), and `validation_details` (JSONB) to `kb_formulas`.
- **New Modules**: `src/kb/math/validation.py`, `tests/test_validation.py`.
- **CLI**: Adds `kb formulas validate` subcommand in `src/kb/cli.py`.
- **GraphQL & UI**: Expands `src/kb/graphql/schema.py` and `src/kb/ui/app.py` with validation endpoints and scorecard visualization.
- **Dependencies**: Uses existing `sympy`, `polars`, `pydantic`, `sqlalchemy`. No new third-party dependencies required.
