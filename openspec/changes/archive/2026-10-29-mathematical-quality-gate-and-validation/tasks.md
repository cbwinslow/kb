# Tasks: Mathematical Quality Gate & Multi-Tier Validation Engine

## 1. Storage Schema & Model Updates

- [x] 1.1 Extend `Formula` model in `src/kb/storage/models.py` with `validation_score`, `validation_status`, and `validation_details` fields and verify model instantiation in unit tests.
- [x] 1.2 Implement database column sync / migration helper in `src/kb/storage/database.py` to ensure PostgreSQL table `kb_formulas` contains the new columns without destroying data.

## 2. Core Multi-Tier Validation Engine (`src/kb/math/validation.py`)

- [x] 2.1 Implement `Tier 1: AST Invertibility & Round-Trip Checker` (`check_ast_roundtrip`) verifying LaTeX -> SymPy -> LaTeX -> SymPy cycle, symbol identity, and structure.
- [x] 2.2 Implement `Tier 2: Semantic Symbol Tokenization & Dimensional Checker` (`check_symbol_encoding_and_dimensions`) detecting multi-letter acronym splits ($w \cdot O \cdot B \cdot A$), checking cyclic LHS, and verifying rate vs count consistency.
- [x] 2.3 Implement `Tier 3: Boundary Invariants & Monotonicity Analyzer` (`check_boundary_invariants_and_monotonicity`) evaluating analytical partial derivatives $\frac{\partial f}{\partial x_i}$ and grid sampling parameter spaces for NaNs, infinities, and singularities.
- [x] 2.4 Implement `Tier 4: Empirical Benchmark Table Verifier` (`check_empirical_benchmark`) querying `kb_benchmark_tables`, binding columns via `SymbolOntology`, and testing ground-truth relative error.
- [x] 2.5 Implement `FormulaQualityScorecard` and `FormulaQualityGate` composite scoring class compiling 0-100 scores, letter grades (A-F), and actionable diagnostic recommendations.

## 3. CLI Subcommand Implementation (`src/kb/cli.py`)

- [x] 3.1 Implement `kb formulas validate` CLI command supporting `--id`, `--citekey`, `--all`, `--min-score`, and `--json` flags.
- [x] 3.2 Implement batch corpus validation loop persisting validation scores, statuses, and diagnostic payloads to PostgreSQL.

## 4. GraphQL & Web UI Integration

- [x] 4.1 Add `ValidationScorecardType` and `validateFormula` query resolver to `src/kb/graphql/schema.py`.
- [x] 4.2 Add `/api/formulas/validate` endpoint in `src/kb/ui/app.py` and display validation score badges and diagnostic drawers in the Web UI.

## 5. Verification, Documentation & Archival

- [x] 5.1 Implement comprehensive unit tests in `tests/test_validation.py` covering all 4 validation tiers, scorecard generation, and edge cases.
- [x] 5.2 Execute live corpus validation on PostgreSQL and verify score distribution across papers.
- [x] 5.3 Run full quality checks: `uv run ruff check`, `uv run pyright`, `uv run pytest`.
- [x] 5.4 Record ADR-026 in `docs/DECISIONS.md`, sync delta specs to `openspec/specs/`, and archive the change.
