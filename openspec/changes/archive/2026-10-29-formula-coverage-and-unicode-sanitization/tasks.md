# Tasks: Formula Coverage Metrics, Universal Unicode Sanitization & Corpus Repair

## Phase 1: Universal Unicode & Mathematical Sanitizer
- [x] 1.1 Expand Greek and variant character mapping in `src/kb/math/sanitizer.py`:
  - [x] 1.1.1 Add full lowercase Greek alphabet ($\alpha, \beta, \gamma, \delta, \epsilon, \zeta, \eta, \theta, \iota, \kappa, \lambda, \mu, \nu, \xi, \pi, \rho, \sigma, \tau, \upsilon, \phi, \chi, \psi, \omega$).
  - [x] 1.1.2 Add Greek typographical variants ($\vartheta, \varphi, \varpi, \varrho, \varsigma, \epsilon, \phi, \vartheta$).
  - [x] 1.1.3 Add uppercase Greek alphabet ($\Gamma, \Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma, \Upsilon, \Phi, \Psi, \Omega$).
- [x] 1.2 Expand Mathematical Operators and Symbols in `src/kb/math/sanitizer.py`:
  - [x] 1.2.1 Add operators ($\sum, \prod, \int, \oint, \partial, \nabla, \sqrt{}, \pm, \mp$).
  - [x] 1.2.2 Add relational symbols ($\in, \notin, \subset, \subseteq, \le, \ge, \ne, \approx, \sim, \simeq, \equiv, \propto, \perp$).
  - [x] 1.2.3 Add multiplication and norm characters ($\times, \cdot, \ast, \parallel, \vert, \dots$).
  - [x] 1.2.4 Handle Unicode primes and accents (`′`, `″`, `ˆ`, `˜`, `¯`, `˙`, `¨`).
  - [x] 1.2.5 Strip Unicode replacement glitch characters (`\uFFFD`).
- [x] 1.3 Implement Mathematical Alphanumeric normalization in `src/kb/math/sanitizer.py`:
  - [x] 1.3.1 Detect glyphs in Unicode range $U+1D400 - U+1D7FF$ (Math Italic, Bold, Script, Fraktur, Double-struck).
  - [x] 1.3.2 Apply `unicodedata.normalize('NFKD', ...)` to convert to standard ASCII letters/digits.
- [x] 1.4 Implement LaTeX font and wrapper stripping in `src/kb/math/sanitizer.py`:
  - [x] 1.4.1 Unwrap `\boldsymbol{...}`, `\bm{...}`, `\mathbf{...}`, `\mathbb{...}`, `\mathcal{...}`, `\mathrm{...}`, `\text{...}`.
  - [x] 1.4.2 Convert statistical function wrappers `\operatorname{Var}`, `\operatorname{E}`, `\operatorname{Cov}`, `\operatorname{Pr}`.
  - [x] 1.4.3 Balance unclosed curly braces and remove dangling operators.
- [x] 1.5 Write unit tests in `tests/test_sanitizer_coverage.py`:
  - [x] 1.5.1 Test Unicode Greek and operator transformations.
  - [x] 1.5.2 Test Mathematical Alphanumeric normalization.
  - [x] 1.5.3 Test font macro unwrapping and brace balancing.

## Phase 2: Formula & Symbol Coverage Metrics Engine
- [x] 2.1 Implement `FormulaCoverageReport` and `CoverageMetrics` dataclasses in `src/kb/math/coverage.py`:
  - [x] 2.1.1 Total formula, valid formula, and equality counts.
  - [x] 2.1.2 Unique symbols, defined LHS variables, consumed RHS variables.
  - [x] 2.1.3 Ontology-mapped variable ratio and list of unmapped/orphan variables.
  - [x] 2.1.4 Character frequency accounting for non-ASCII/Unicode glyphs.
  - [x] 2.1.5 Error taxonomy distribution (syntax error, unknown token, unbalanced brackets).
- [x] 2.2 Implement `FormulaCoverageAnalyzer` in `src/kb/math/coverage.py`:
  - [x] 2.2.1 `analyze_corpus(limit: int | None = None)` scanning database formulas.
  - [x] 2.2.2 `analyze_extracted_formulas(formulas: list[ExtractedFormula])` for in-memory analysis.
  - [x] 2.2.3 Generate markdown and JSON report formatting (`to_markdown()`, `to_json()`).
- [x] 2.3 Integrate coverage metrics into GraphQL schema and UI Dashboard:
  - [x] 2.3.1 Add `FormulaCoverageType` to `src/kb/graphql/schema.py`.
  - [x] 2.3.2 Add `formulaCoverage` query field to Strawberry schema.
  - [x] 2.3.3 Add coverage endpoint `/api/coverage` and UI stats card in `src/kb/ui/app.py`.
- [x] 2.4 Add CLI command `kb formulas coverage [--report <path>] [--json]` in `src/kb/cli.py`.
- [x] 2.5 Write unit tests in `tests/test_coverage_analyzer.py`:
  - [x] 2.5.1 Test yield calculations and variable partitioning.
  - [x] 2.5.2 Test orphan variable detection and ontology mapping rates.
  - [x] 2.5.3 Test markdown and JSON report generation.

## Phase 3: In-Place Corpus Re-Sanitization & Repair
- [x] 3.1 Implement `CorpusFormulaRepairer` in `src/kb/math/repair.py`:
  - [x] 3.1.1 Batch scanner iterating over stored formulas in PostgreSQL.
  - [x] 3.1.2 Re-sanitize raw LaTeX with upgraded `EquationSanitizer`.
  - [x] 3.1.3 Re-parse with `FormulaExtractor` into SymPy AST.
  - [x] 3.1.4 Update database columns (`sanitized_latex`, `sympy_repr`, `symbols`, `is_valid`, `is_equality`, `lhs`, `rhs`).
  - [x] 3.1.5 Batch progress reporting and transaction checkpointing.
- [x] 3.2 Add CLI command `kb formulas repair [--batch-size 250] [--dry-run]` in `src/kb/cli.py`.
- [x] 3.3 Write unit tests in `tests/test_formula_repair.py`.

## Phase 4: Verification, Quality Gates & OpenSpec Synchronization
- [x] 4.1 Record formal ADR-024 in `docs/DECISIONS.md`.
- [x] 4.2 Run in-place repair on stored formulas to elevate corpus yield.
- [x] 4.3 Run `uv run ruff check` and `uv run ruff format`.
- [x] 4.4 Run `uv run pyright` ensuring zero type errors.
- [x] 4.5 Run `uv run pytest` ensuring all tests pass.
- [x] 4.6 Sync delta specs to `openspec/specs/` and archive the change.
- [x] 4.7 Commit and push clean working tree to GitHub repository.
