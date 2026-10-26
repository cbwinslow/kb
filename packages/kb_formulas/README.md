# `kb-formulas`

Standalone scientific formula and metric library for sports analytics, sabermetrics, and statistical modeling, compiled directly from peer-reviewed literature in the Scientific Knowledge Base (`kb`).

## Features
- **Zero Heavy Dependencies**: Requires only Python 3.10+ and `polars`. No PyTorch, no Docling, no database required.
- **Dual Execution Modes**:
  - `calc_*`: Typed Python scalar functions (`float -> float`).
  - `expr_*`: Vectorized Polars expressions (`-> pl.Expr`) for high-throughput DataFrame batch processing.
- **Full Literature Grounding**: Every function includes KaTeX-compliant docstrings citing the original paper title, authors, year, and citation key.

## Installation
```bash
pip install kb-formulas
```

Or install locally from the repository:
```bash
pip install ./packages/kb_formulas
```

## Quick Example
```python
import polars as pl
from kb_formulas import (
    calc_w_a_r_q_1312_7,
    expr_w_a_r_q_1312_7,
)

# 1. Scalar Calculation
war = calc_w_a_r_q_1312_7(A=1.0, R=10.0, e=0.5, l=1.0, p=0.8, q=2.0, r=1.5)
print("Calculated metric:", war)

# 2. High-speed Polars Vectorized DataFrame Processing
df = pl.DataFrame({
    "A": [1.0, 1.2],
    "R": [10.0, 12.0],
    "e": [0.5, 0.4],
    "l": [1.0, 1.0],
    "p": [0.8, 0.9],
    "q": [2.0, 2.5],
    "r": [1.5, 1.2],
})

df_out = df.with_columns(WAR=expr_w_a_r_q_1312_7())
print(df_out)
```
