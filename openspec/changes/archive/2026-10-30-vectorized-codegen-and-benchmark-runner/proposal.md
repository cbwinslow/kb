# Proposal: Vectorized Code Generation & Empirical Benchmark Runner

## Why
While `kb` generates standalone formula functions in `packages/kb_formulas` and stores 1,256 extracted empirical tables in `kb_benchmark_tables`, there is currently no automated system that compiles all verified Grade A formulas into high-performance vectorized Polars expressions and evaluates them against real-world Parquet datasets at scale. Researchers and downstream libraries (such as `sabermetricspy`) need guaranteed mathematical fidelity, measured by empirical error metrics (MAE, RMSE, and $R^2$), across millions of historical Retrosheet and Statcast tracking events.

## What Changes
- **Vectorized Polars AST Compilation**: Automatically compiles all verified Grade A equations into optimized, type-safe Polars expression functions (`pl.Expr`) and vectorized NumPy callables.
- **Automated Parameter-to-Column Binding**: Employs `SymbolOntology` to map symbolic equation variables (e.g., $v_{exit}, \theta, \omega$) directly to table columns in `kb_benchmark_tables` and external Parquet event tables.
- **Empirical Accuracy Runner**: Executes batch vectorized evaluations across empirical datasets, calculates statistical validation metrics ($R^2 \ge 0.99$, $\text{MAE} \le 10^{-4}$), and updates `validation_details` in PostgreSQL.
- **CLI Benchmark Suite**: Adds `kb benchmark accuracy --grade A [--dataset <path>] [--json]` to evaluate and report corpus-wide numerical fidelity.

## Capabilities

### Modified Capabilities
- `numerical-accuracy`: Extends numerical accuracy verification from scalar unit tests to large-scale vectorized evaluation against empirical Parquet tables.
- `benchmark-extraction`: Adds automated parameter-to-column schema binding between extracted benchmark tables and compiled formula ASTs.

## Impact
- **Modules**: Expands `src/kb/library/generator.py` and `src/kb/qa/accuracy.py`.
- **CLI**: Adds `kb benchmark accuracy` command in `src/kb/cli.py`.
- **Package**: Regenerates `packages/kb_formulas` with full vectorized Polars expression suites.
- **Dependencies**: Polars (`polars`), NumPy (`numpy`), PyArrow (`pyarrow`).
