# Empirical Accuracy Benchmarking Leaderboard

**Generated**: 2026-11-05 22:23:36 UTC  
**Total Formulas Evaluated**: 5  
**Top Model R²**: -0.4126

## Ranked Formula Performance

| Rank | Formula ID | Citekey | Target Column | R² Score | RMSE | MAE | Status | Rows/sec |
|:----:|:-----------|:--------|:--------------|:--------:|:----:|:---:|:------:|:--------:|
| 1 | `form_a0a508c3582ee` | `arxiv_2609_25525` | `golden_sabermetr` | **-0.4126** | 0.0880 | 0.0721 | FLAGGED | 186,863.5 |
| 2 | `form_313ccbf49cc64` | `arxiv_2610_39088` | `golden_sabermetr` | **-12.4755** | 427.9054 | 411.7214 | FLAGGED | 409,987.3 |
| 3 | `form_e94874c9cc5d8` | `arxiv_2608_02081` | `golden_sabermetr` | **-33445802.5052** | 428.1261 | 411.9508 | FLAGGED | 1,279,263.2 |
| 4 | `form_97aae668f7885` | `arxiv_2610_39088` | `golden_sabermetr` | **-149997474644785.8125** | 906656.7708 | 866835.2068 | FLAGGED | 191,614.9 |
| 5 | `form_495a79adaad9e` | `arxiv_2610_39088` | `golden_sabermetr` | **-1572338311250900.7500** | 2935444.9061 | 2883335.5590 | FLAGGED | 860,585.2 |

## Benchmark Methodology
- **Vectorized Evaluation**: Formulas compiled to Polars expressions and evaluated across full Parquet datasets without Python loops.
- **Statistical Telemetry**: Precision scored via Coefficient of Determination ($R^2$), Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE).
- **Pass Threshold**: $R^2 \ge 0.95$ and $\text{MAE} \le 1.0$.
