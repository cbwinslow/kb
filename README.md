# Scientific Knowledge Base (`kb`)

A high-performance, domain-agnostic scientific research engine and knowledge-to-code compiler. `kb` automatically ingests peer-reviewed preprints and publications (arXiv, OpenAlex), parses complex LaTeX equations and benchmark tables, generates dense BGE-M3 vector embeddings, constructs mathematical derivation graphs, and compiles equations into standalone, type-safe Python and Polars libraries.

---

## Key Features

1. **Portable Architecture**:
   - Zero hardcoded credentials or machine-specific paths.
   - Built with `pydantic-settings` supporting `.env` configuration.
   - Operates identically on local development environments (using SQLite / local directories) or enterprise homelabs (using PostgreSQL 16 + pgvector + remote SSH/SFTP storage vaults).

2. **Automated Harvesting & Ingestion**:
   - Automated arXiv query harvesters with deduplication and metadata enrichment.
   - High-fidelity PDF layout parsing (Docling) for sections, tables, and math equations.
   - Enhanced LaTeX sanitizers mapping Unicode Greek symbols, piecewise functions, and OCR artifacts into valid SymPy expressions.

3. **Homelab Remote Archiving via SSH/SFTP**:
   - Direct, encrypted synchronization of raw PDFs and Parquet benchmark fixtures to homelab storage (`/home/.../workspace/kb/`) via SSH keys (`~/.ssh/id_ed25519`).
   - Prevents local workstation disk exhaustion through automatic host floor monitoring.

4. **Knowledge-to-Code & Standalone Formula Library**:
   - Automatically compiles extracted equations into executable Python functions and vectorized Polars expressions (`expr_*`).
   - Generates KaTeX-compliant docstrings with complete paper titles, authors, citation keys, and parameter annotations.
   - Validated against empirical benchmark tables extracted from literature.

5. **Interactive Visual Dashboard**:
   - FastMCP server daemon for integration with AI agents.
   - Interactive HTML5 canvas visualizer showcasing documents, embedded chunks, mathematical formula lineage, and benchmark tables.

---

## Quickstart & Setup

### 1. Prerequisites
- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) (recommended) or standard `pip`

### 2. Installation
```bash
git clone https://github.com/cbwinslow/kb.git
cd kb
uv sync
```

### 3. Environment Configuration
Copy the template configuration file:
```bash
cp .env.example .env
```

Edit `.env` for your environment:

#### Option A: Local Standalone (SQLite)
```dotenv
KB_DATABASE_URL=sqlite+aiosqlite:///data/kb.db
KB_DATA_DIR=data
KB_FIXTURES_DIR=data/fixtures
KB_PDF_DOWNLOAD_DIR=data/arxiv_papers
KB_EMBEDDING_DEVICE=cpu
```

#### Option B: Enterprise / Homelab (PostgreSQL + SSH)
```dotenv
KB_DATABASE_URL=postgresql+asyncpg://user:password@homelab-host:5432/kb
KB_DATA_DIR=data
KB_FIXTURES_DIR=data/fixtures
KB_PDF_DOWNLOAD_DIR=data/arxiv_papers
KB_EMBEDDING_DEVICE=cuda

# Encrypted SSH Remote Archiving
KB_SSH_HOST=homelab-host
KB_SSH_PORT=22
KB_SSH_USER=user
KB_SSH_KEY_PATH=~/.ssh/id_ed25519
KB_SSH_REMOTE_PDF_DIR=/home/user/workspace/kb/pdfs
KB_SSH_REMOTE_FIXTURES_DIR=/home/user/workspace/kb/fixtures
```

---

## CLI Reference

`kb` provides an intuitive CLI for all research workflows:

### Database Management
```bash
# Verify connectivity
uv run kb db check

# Initialize tables, vector extension, and indexes
uv run kb db init
```

### Remote Homelab Synchronization
```bash
# Test SSH/SFTP connection and homelab storage readiness
uv run kb sync ssh-check

# Archive local Parquet fixtures and PDFs to homelab vault
uv run kb sync ssh-push
```

### Preprint Harvesting & Ingestion
```bash
# Harvest top 10 baseball analytics preprints from arXiv
uv run kb sync harvest --query "baseball OR sabermetrics OR statcast" --limit 10

# Ingest a specific paper PDF manually
uv run kb ingest path/to/paper.pdf --citekey author2026 --title "Advanced Run Expectancy"
```

### Continuous Multi-Source Harvester Daemon
```bash
# Run continuous background harvester across OpenAlex and arXiv with automatic homelab push
uv run kb sync daemon --interval 3600 --limit-per-query 5
```

### Observability & Structured Logging
```bash
# Enable verbose debug logs and persistent rotating file logging
uv run kb --verbose --log-file logs/kb.log db check
```

### Standalone Formula Library Export
```bash
# Compile verified literature equations into standalone typed Python + Polars library
uv run kb code export --output src/kb/library/generated.py
```

### Search & Question Answering
```bash
# Hybrid vector (dense BGE-M3) + BM25 keyword search
uv run kb search "Pythagorean expectation formula" --limit 5

# Evidence-grounded QA answering over corpus
uv run kb ask "How is park-adjusted win probability calculated?"
```

### Multi-Hop Equation Chaining & System Solving
```bash
# Find and solve multi-hop symbolic derivation chain connecting concepts across papers
uv run kb equations chain --from "BAT_SPEED" --to "WAR" --max-depth 5

# Chain formulas from a specific root equation with JSON output
uv run kb formulas chain --formula-id "form_woba" --max-depth 4 --json
```

### Interactive UI Dashboard & Live Evaluation API
```bash
# Launch interactive dashboard with Quality Gate, 1-click repair, and formula playground
uv run kb ui serve --host 127.0.0.1 --port 8080
# Endpoints include: /api/stats, /api/lineage, /api/formulas, /api/tables, /api/search, /api/eval, /api/formulas/{id}/repair, /api/documents/{id}/figures
```

### Performance & Quality Benchmarking Suite
```bash
# Run complete benchmark suite (Scalar vs. Polars speed, embedding latency, search, quality)
uv run kb benchmark --all

# Run empirical accuracy benchmark against Parquet datasets for Grade A formulas
uv run kb benchmark accuracy --grade A --limit 50

# Benchmark formula execution throughput on 100,000 rows
uv run kb benchmark --formulas --rows 100000

# Audit corpus formula mathematical quality and compilation yield
uv run kb benchmark --quality
```

---

## Standalone Formula Library Usage

The generated formula library (`src/kb/library/generated.py`) can be imported directly into Python applications or Polars data pipelines:

```python
import polars as pl
from kb.library.generated import (
    calc_w_a_r_q_1312_7,
    expr_w_a_r_q_1312_7,
)

# 1. Scalar calculation
war_metric = calc_w_a_r_q_1312_7(A=1.0, R=10.0, e=0.5, l=1.0, p=0.8, q=2.0, r=1.5)
print("Scalar WAR metric:", war_metric)

# 2. Vectorized Polars computation across DataFrame
df = pl.DataFrame({
    "A": [1.0, 1.2],
    "R": [10.0, 12.0],
    "e": [0.5, 0.4],
    "l": [1.0, 1.0],
    "p": [0.8, 0.9],
    "q": [2.0, 2.5],
    "r": [1.5, 1.2],
})

df_with_war = df.with_columns(WAR=expr_w_a_r_q_1312_7())
print(df_with_war)
```

---

## Testing & Quality Assurance

Run the complete 90-test automated test suite:
```bash
uv run pytest tests/
```

Linting and strict type checking:
```bash
uv run ruff check src/ tests/ scripts/ packages/
uv run pyright src/kb/config.py src/kb/logging.py src/kb/sync/ src/kb/ui/ src/kb/cli.py packages/kb_formulas/src/
```

---

## License
MIT License.
