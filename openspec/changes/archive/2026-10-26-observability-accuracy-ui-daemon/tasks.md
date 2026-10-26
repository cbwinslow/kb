# Tasks: Observability, Numerical Accuracy, Interactive UI, and Harvester Daemon

## Phase 1: Option A — Unified Structured Logging & Observability
- [x] Create `src/kb/logging.py` with console formatting, file rotation, and execution timing decorator <!-- id: 101 -->
- [x] Add global CLI flags (`--verbose`, `--debug`, `--log-file`, `--quiet`) to `src/kb/cli.py` <!-- id: 102 -->
- [x] Add unit tests for logging setup and timing decorators in `tests/test_logging.py` <!-- id: 103 -->

## Phase 2: Option B — Ground-Truth Numerical Accuracy Test Suite
- [x] Create `tests/test_accuracy.py` with ground-truth reference values for Pythagorean, FIP, wOBA, and linear weights <!-- id: 104 -->
- [x] Verify numerical tolerance ($\le 10^{-4}$) against compiled `kb-formulas` functions <!-- id: 105 -->

## Phase 3: Option C — Live Interactive Formula & Lineage Explorer UI
- [x] Implement `src/kb/ui/server.py` with static asset serving and `/api/formulas` / `/api/eval` endpoints <!-- id: 106 -->
- [x] Wire up `kb ui serve` command in `src/kb/cli.py` with `--port` and `--host` options <!-- id: 107 -->
- [x] Add unit tests in `tests/test_ui_server.py` <!-- id: 108 -->

## Phase 4: Option D — Continuous Harvesting Daemon
- [x] Implement `src/kb/sync/daemon.py` with async scheduling, rate limit backoff, and homelab SFTP archival <!-- id: 109 -->
- [x] Add `kb sync daemon` CLI command in `src/kb/cli.py` with `--interval`, `--queries`, and `--max-runs` flags <!-- id: 110 -->
- [x] Add unit tests in `tests/test_daemon.py` <!-- id: 111 -->

## Phase 5: Verification & Documentation
- [x] Run full test suite (`pytest`) <!-- id: 112 -->
- [x] Run `ruff check` and `pyright` <!-- id: 113 -->
- [x] Update `README.md` and sync OpenSpec delta specs <!-- id: 114 -->
- [x] Commit and push to GitHub <!-- id: 115 -->
