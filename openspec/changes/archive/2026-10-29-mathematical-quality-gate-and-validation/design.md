# Design: Mathematical Quality Gate & Multi-Tier Validation Engine

## Context
See `proposal.md` for motivation. KB's formula extraction and repair pipeline has recovered 73.5% of equations (4,326 valid formulas out of 5,889). However, syntactic validity in SymPy does not guarantee that formulas are mathematically or semantically correct. Current risks include:
1. Unnoticed symbol splitting (e.g. `w \cdot O \cdot B \cdot A` instead of `\text{wOBA}`).
2. Rate vs. count dimensional mismatches.
3. Hidden mathematical singularities or non-physical outputs (NaNs, negative probabilities).
4. Lack of empirical verification against ground-truth tables.

## Goals / Non-Goals

**Goals:**
- Provide a standardized 4-tier validation pipeline evaluating AST invertibility, semantic symbol encoding, boundary invariants, and empirical benchmark agreement.
- Produce an actionable `FormulaQualityScorecard` with numerical score (0-100), letter grade (A through F), and granular diagnostics for every formula.
- Persist validation status and scorecards directly into PostgreSQL (`kb_formulas`).
- Provide high-performance CLI commands (`kb formulas validate`) supporting single-formula, paper-level, and corpus-wide batch execution.
- Surface validation grades, badges, and diagnostic recommendations in the GraphQL API and Web UI.

**Non-Goals:**
- Automatically rewriting original author papers or changing published research text.
- Overriding user-curated custom symbol ontologies.
- Modifying `baseballpy` (Claude's separate project).

## Decisions

### 1. Orthogonal 4-Tier Scoring Architecture
- **Decision**: Structure validation into four equal-weighted 25-point tiers:
  - **Tier 1 (25 pts) - AST Invertibility & Round-Trip Fidelity**: `sympy.latex(expr)` -> re-parsed with `FormulaExtractor`. Verifies free symbol preservation, relational equality structure, and tree depth stability.
  - **Tier 2 (25 pts) - Semantic Symbol Encoding & Dimensional Consistency**: Verifies tokenization against `SymbolOntology`, flags accidental multi-letter product splits ($w \cdot O \cdot B \cdot A$), checks for cyclic LHS definitions, and validates rate vs. count dimensionality.
  - **Tier 3 (25 pts) - Boundary Invariants & Monotonicity Analysis**: Computes analytical partial derivatives ($\frac{\partial f}{\partial x_i}$) with SymPy to verify sign direction, and grid-samples parameter space to ensure no `NaN`, `inf`, or complex values arise within domain limits.
  - **Tier 4 (25 pts) - Empirical Benchmark Evaluation**: Binds formula parameters to extracted tables in `kb_benchmark_tables` via `SymbolOntology` and tests predictions against ground-truth values. When no empirical table exists for a paper, a normalized 15-point baseline is awarded for finite numerical executability.
- **Alternatives Considered**: Binary pass/fail validation. Rejected because real-world academic formulas have varying degrees of verification (some are theoretical without empirical tables, but mathematically sound).

### 2. Analytical Monotonicity Testing via Symbolic Differentiation
- **Decision**: Use SymPy's `diff(expr, var)` to compute closed-form symbolic gradients. Test whether partial derivatives preserve physical intuition (e.g. runs scored increases win expectation $\frac{\partial W}{\partial R_S} > 0$, while runs allowed decreases win expectation $\frac{\partial W}{\partial R_A} < 0$).
- **Alternatives Considered**: Pure finite-difference numerical perturbation. Symbolic differentiation is exact and avoids floating-point roundoff errors or step-size tuning.

### 3. Database Schema Extension
- **Decision**: Add three columns to `kb_formulas`:
  - `validation_score: Mapped[float | None]`: Overall score (0.0 to 100.0).
  - `validation_status: Mapped[str | None]`: Status string (`verified`, `provisional`, `degraded`, `failed`).
  - `validation_details: Mapped[dict[str, Any] | None]`: JSONB payload storing tier scores, check outcomes, and recommendations.
- **Alternatives Considered**: Separate `kb_formula_validations` table. Rejected for formula-centric workflows where querying formulas sorted or filtered by validation score is the primary access pattern.

## Risks / Trade-offs

- **[Risk] Heavy computational cost during corpus-wide symbolic differentiation and grid sampling.**
  → *Mitigation*: Vectorize grid sampling using `FormulaCodeGenerator` (compiled via `lambdify`), set timeout limits on symbolic differentiation, and support batch parallel CLI validation.
- **[Risk] Papers without benchmark tables might be unfairly penalized in Tier 4.**
  → *Mitigation*: Tier 4 checks whether a benchmark table exists for the document. If absent, it verifies numeric executability on synthesized plausible domain inputs and scales the score proportionally.

## Migration Plan
- Apply non-destructive schema update to `kb_formulas` adding `validation_score`, `validation_status`, and `validation_details`.
- Run validation suite against standard test formulas (Pythagorean expectation, Bill James log5, FIP, wOBA).
- Run corpus-wide validation via `kb formulas validate --all` to score all valid formulas in PostgreSQL.
