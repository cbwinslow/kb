# Design: Vectorized Code Generation & Empirical Benchmark Runner

## Overview
This change automates the compilation of all verified Grade A scientific formulas into vectorized Polars expressions (`pl.Expr`) and executes large-scale empirical accuracy benchmarking against extracted tabular fixtures (`kb_benchmark_tables`) and Parquet tracking datasets.

## Architecture & Data Flow

```
[Verified Grade A Formulas (3,803)] (PostgreSQL 16)
       │
       ▼ [FormulaCompiler / AST Code Generator]
[Vectorized Polars / NumPy Functions] (packages/kb_formulas)
       │
       ▼ [SymbolOntology Parameter Binding]
[Empirical Tables & Parquet Golden Fixtures] (1,256 tables / Retrosheet / Statcast)
       │
       ▼ [Vectorized Benchmark Execution Runner]
  ├── Polars Evaluation (`df.select(formula_expr.alias("pred"))`)
  ├── Compute MAE, RMSE, Max Relative Error, R^2
       │
       ▼ [Persist Benchmark Telemetry]
[PostgreSQL kb_formulas.validation_details] (Tier 4 Score = 25.0, Empirical Error Payload)
```

## Key Components

### 1. Vectorized AST Compilation (`src/kb/library/generator.py`)
- Traverses SymPy AST and converts standard operators, power functions, logarithms, and transcendentals into Polars column expressions (`pl.col(x)`).
- Generates typed function signatures:
  ```python
  def fip_expr(hr: str = "hr", bb: str = "bb", hbp: str = "hbp", k: str = "so", ip: str = "ip", c: float = 3.10) -> pl.Expr:
      return ((13 * pl.col(hr) + 3 * (pl.col(bb) + pl.col(hbp)) - 2 * pl.col(k)) / pl.col(ip)) + c
  ```
- Packages generated functions into standalone distribution `packages/kb_formulas`.

### 2. Parameter-to-Column Binding Engine
- Reads column headers from `BenchmarkTable` in `kb_benchmark_tables`.
- Matches each header string against `SymbolOntology.match_column_name(header)`.
- Replaces generic symbol variables with specific dataframe column references.

### 3. Empirical Accuracy Evaluation Suite (`src/kb/qa/accuracy.py`)
- Evaluates vectorized expressions across all rows in the dataset in a single Polars call.
- Computes metrics:
  - $\text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i|$
  - $\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2}$
  - $R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$
- Updates database formula `validation_details` with empirical performance metrics.

### 4. CLI Benchmark Runner
- Command: `kb benchmark accuracy [--grade A] [--table-id <id>] [--dataset <path>] [--json]`.
- Summarizes throughput (rows/sec), error distribution, and pass/fail status against tolerance thresholds.
