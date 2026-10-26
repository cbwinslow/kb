# Proposal: Observability, Numerical Accuracy Benchmark Suite, Interactive Web UI, and Continuous Harvesting Daemon

## 1. Problem Statement
While `kb` has scaled to 260 papers, 32,000+ chunks, and 457 compiled formula functions, four critical capabilities are needed to make it a self-sustaining, observable, and trustworthy research platform:
1. **Lack of Centralized Observability & Logging**: Logs currently depend on stdout/stderr and raw console printouts. There is no unified structured logging with rotation, CLI verbosity control, or persistent run metrics.
2. **Missing Ground-Truth Numerical Verification**: Although generated formula functions are syntactically and symbolically valid, there is no automated test suite validating formula calculation accuracy against established ground-truth references (e.g. FanGraphs, Retrosheet, Bill James benchmarks).
3. **No Live Interactive Browser Interface**: The lineage DAG dashboard exists as a static artifact; users lack a built-in CLI command to launch a lightweight local server to browse papers, explore formulas, and test calculations interactively.
4. **Manual Ingestion vs. Continuous Harvesting**: Scaling the corpus currently requires manual CLI calls. A background continuous harvesting daemon with respectful rate limiting and automatic homelab sync is needed to autonomously monitor scientific literature.

## 2. Proposed Capabilities
1. **Option A — Unified Structured Logging & Ingestion Audit (`src/kb/logging.py`)**:
   - Centralized logging initialization with console handlers, rotating file logs (`logs/kb.log`), and optional JSON structured output.
   - CLI flags: `--verbose` (`-v`), `--debug`, `--log-file`, `--quiet`.
   - Pipeline stage timing and structured error reporting.
2. **Option B — Numerical Accuracy & Benchmark Verification Suite (`tests/test_accuracy.py`)**:
   - Reference datasets and ground-truth unit tests verifying mathematical precision ($\le 10^{-4}$) for core formulas (Pythagorean expectation, FIP, wOBA, strikeout rates, run expectancy).
3. **Option C — Live Interactive Formula & Lineage Explorer UI (`kb ui serve`)**:
   - Built-in HTTP dashboard server serving interactive lineage exploration, formula code inspector, and live calculation runner at `http://127.0.0.1:8000`.
4. **Option D — Continuous Harvesting Daemon (`src/kb/sync/daemon.py` & `kb sync daemon`)**:
   - Asynchronous continuous crawler querying OpenAlex and arXiv at configurable intervals with exponential backoff, automatic Docling parsing, BGE-M3 embedding, and SFTP sync to homelab vault.

## 3. Impact & Portability
- Retains zero hardcoded credentials, full `.env` configuration, and workstation disk space protection.
- Fully compatible with Windows, Linux, and macOS.
