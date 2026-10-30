# Tasks: Vectorized Code Generation & Empirical Benchmark Runner

## 1. Vectorized AST Compilation & Export
- [x] 1.1 Extend `src/kb/library/generator.py` to compile SymPy ASTs to vectorized `pl.Expr` expressions for all Grade A formulas.
- [x] 1.2 Update package generation script to refresh `packages/kb_formulas` with typed Polars bindings.

## 2. Parameter-to-Column Binding Engine
- [x] 2.1 Implement `bind_formula_to_table` utility mapping table column headers to formula symbols via `SymbolOntology`.
- [x] 2.2 Handle missing column fallbacks and default constant injection.

## 3. Empirical Accuracy Evaluation Suite
- [x] 3.1 Implement vectorized benchmark evaluation runner in `src/kb/qa/accuracy.py`.
- [x] 3.2 Compute statistical validation metrics (MAE, RMSE, $R^2$) and persist telemetry into `kb_formulas.validation_details`.

## 4. CLI Subcommand Implementation
- [x] 4.1 Add `kb benchmark accuracy` command to `src/kb/cli.py` with filtering options (`--grade`, `--min-score`, `--json`).
- [x] 4.2 Generate tabular CLI accuracy report with throughput and error metrics.

## 5. Verification & Testing
- [x] 5.1 Add unit tests in `tests/test_codegen.py` and `tests/test_benchmark_runner.py`.
- [x] 5.2 Validate quality gates: `uv run ruff check`, `uv run pyright`, `uv run pytest`.
