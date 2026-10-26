# Design: Observability, Numerical Accuracy, Interactive UI, and Harvester Daemon

## Architecture Overview

```
                      ┌───────────────────────────────────────────────┐
                      │                 CLI Entrypoint                │
                      │  kb [--verbose] [--log-file] [subcommand]      │
                      └───────────────────────┬───────────────────────┘
                                              │
                     ┌────────────────────────┴───────────────────────┐
                     │                                                │
         ┌───────────▼───────────┐                        ┌───────────▼───────────┐
         │ Option A: Logging &   │                        │ Option C: UI Server   │
         │ Observability         │                        │ `kb ui serve`         │
         │ - src/kb/logging.py   │                        │ - aiohttp/http.server │
         │ - rotating file logs  │                        │ - lineage dashboard   │
         │ - execution timers    │                        │ - live formula runner │
         └───────────┬───────────┘                        └───────────────────────┘
                     │
         ┌───────────▼───────────┐                        ┌───────────────────────┐
         │ Option D: Continuous  │                        │ Option B: Numerical   │
         │ Harvester Daemon      │                        │ Accuracy Verification │
         │ - src/kb/sync/        │                        │ - tests/test_accuracy │
         │   daemon.py           │                        │ - ground-truth data   │
         │ - schedule & backoff  │                        │ - tolerance <= 1e-4   │
         │ - homelab SFTP push   │                        └───────────────────────┘
         └───────────────────────┘
```

## Detailed Component Specifications

### 1. `src/kb/logging.py`
- Exposes `setup_logging(level: str = "INFO", log_file: Path | None = None, json_format: bool = False) -> None`.
- Formats standard log records with ISO timestamps, logger names, line numbers, and levels.
- Supports rotating file handler with max 10MB per file, keeping 5 backups.
- Timing decorator `@timed_stage(stage_name)` logging latency in milliseconds.

### 2. `tests/test_accuracy.py`
- Ground-truth reference values for standard quantitative baseball models:
  - **Pythagorean Expectation**:
    - Formula: $W\% = \frac{R^\gamma}{R^\gamma + RA^\gamma}$
    - Exponent $\gamma = 1.83$: 750 RS, 650 RA -> expected win pct $\approx 0.5647$.
  - **Fielding Independent Pitching (FIP)**:
    - Formula: $\text{FIP} = \frac{13 \cdot \text{HR} + 3 \cdot (\text{BB} + \text{HBP}) - 2 \cdot K}{\text{IP}} + C$
    - Test standard values: 20 HR, 50 BB, 5 HBP, 180 K, 200 IP, $C=3.10$ -> $\approx 2.925$.
  - **Weighted On-Base Average (wOBA)**:
    - Verifies linear weights dot product consistency.
- Tests verify compiled functions in `src/kb/library/generated.py` and `kb_formulas.generated`.

### 3. `src/kb/ui/server.py`
- Lightweight asynchronous HTTP server using standard Python `http.server` or `asyncio`/`aiohttp`.
- Serves the interactive lineage explorer, documentation, and live formula evaluation endpoint (`/api/eval?formula_id=...&inputs=...`).

### 4. `src/kb/sync/daemon.py`
- Asynchronous harvester daemon `ContinuousHarvesterDaemon`.
- Configurable interval (default: 3600s), queries, limit per query.
- Runs ingestion pipeline, generates BGE-M3 embeddings, uploads PDFs to homelab via `SSHStorageSync`, and purges local temp files.
