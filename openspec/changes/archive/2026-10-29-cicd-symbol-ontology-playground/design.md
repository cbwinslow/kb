# Design: CI/CD Distribution, Symbol Ontology & Interactive Web UI Playground

## Architecture Overview

```
                                +-----------------------------------------+
                                |             GitHub Actions              |
                                |  .github/workflows/ci.yml               |
                                |  .github/workflows/publish-formulas.yml |
                                +--------------------+--------------------+
                                                     |
                                                     v
                                       +---------------------------+
                                       | PyPI / Artifact Packaging |
                                       | (packages/kb_formulas)    |
                                       +---------------------------+

+----------------------------------------------------------------------------------------+
|                                    Core Engine (kb)                                    |
|                                                                                        |
|  +-------------------------------+                 +--------------------------------+  |
|  |     Symbol Ontology System    |                 |   Interactive Playground UI    |  |
|  |     (src/kb/math/ontology.py) |                 |   (src/kb/ui/app.py)           |  |
|  |                               |                 |                                |  |
|  | - Canonical Concept Catalog   |                 | - Playground Tab & Form        |  |
|  | - Symbol Normalizer / Aliases |                 | - Real-time Param Evaluation   |  |
|  | - DataFrame Column Binder     |                 | - Chart.js Sensitivity Curves  |  |
|  |   (Polars & Pandas)           |                 | - Strict Zero-Regression Guard |  |
|  +---------------+---------------+                 +---------------+----------------+  |
|                  |                                                 |                   |
|                  v                                                 v                   |
|  +-------------------------------+                 +--------------------------------+  |
|  | Formula Evaluation & Codegen  |                 | Lineage, Search & Benchmark UI |  |
|  | (src/kb/math/codegen.py)      |                 | (Unmodified & Fully Protected) |  |
|  +-------------------------------+                 +--------------------------------+  |
+----------------------------------------------------------------------------------------+
```

## Detailed Component Design

### 1. CI/CD & Packaging Architecture
- **Workflows**:
  - `.github/workflows/ci.yml`:
    - Trigger: `push` and `pull_request` on `master`.
    - OS Matrix: `ubuntu-latest`, `windows-latest`.
    - Python Version: `3.12`.
    - Tooling: Astral `uv` setup action.
    - Steps:
      - Checkout repository.
      - Install `uv` and sync dependencies: `uv sync --all-extras`.
      - Ruff Lint & Format check: `uv run ruff check src/ tests/ scripts/ packages/` and `uv run ruff format --check src/ tests/ scripts/ packages/`.
      - Pyright Typecheck: `uv run pyright src/ tests/ packages/`.
      - Pytest Suite: `uv run pytest tests/ -v`.
  - `.github/workflows/publish-formulas.yml`:
    - Trigger: Push tags matching `v*.*.*` or `workflow_dispatch`.
    - Environment: `ubuntu-latest`.
    - Steps:
      - Generate latest formula package using `kb formulas generate-package`.
      - Build wheel and sdist with `uv build packages/kb_formulas`.
      - Upload artifacts to GitHub release assets.
      - Optional publish step using PyPI API token / Trusted Publisher if configured.

### 2. Semantic Symbol Ontology (`src/kb/math/ontology.py`)
- **Canonical Concept Enum / Dataclass**:
  - `CanonicalConcept`: Defines standard physical/sabermetric variable identifier (e.g. `runs_scored`, `runs_allowed`, `home_runs`, `innings_pitched`, `strikeouts`, `walks`, `hits`, `at_bats`, `plate_appearances`, `singles`, `doubles`, `triples`, `win_pct`, `gamma`).
  - `ConceptDefinition`: Encapsulates canonical name, standard LaTeX notation, aliases, domain type (`baseball`, `general_math`, `physics`), description, and default unit/type.
- **Normalization Engine**:
  - `SymbolOntology.normalize(symbol: str) -> str`: Normalizes LaTeX artifacts (e.g. stripping `\text{}`, braces `{}`, subscripts `_`, converting `R_S` or `\text{RS}` to standard forms).
  - `SymbolOntology.resolve_canonical(symbol: str) -> CanonicalConcept | None`: Maps an arbitrary author symbol to its canonical concept.
  - `SymbolOntology.resolve_for_formula(formula_symbols: list[str], available_columns: list[str]) -> dict[str, str]`: Produces an exact variable-to-column mapping dictionary `{"R_S": "runs_scored", "R_A": "runs_allowed"}`.
  - `SymbolOntology.bind_dataframe(df: pl.DataFrame | pd.DataFrame, formula_symbols: list[str]) -> pl.DataFrame | pd.DataFrame`: Automatically renames or aliases DataFrame columns so that formula code generated from AST directly executes without user intervention.

### 3. Interactive Web UI Calculation Playground (`src/kb/ui/`)
- **UI Architecture**:
  - Add a dedicated "Playground" tab alongside "Lineage Graph", "Formulas", "Benchmark Tables", and "Hybrid Search".
  - Dedicated route `/playground` as well as tab integration on the main SPA shell.
  - Interactive parameter controls:
    - Pre-configured Canonical presets (Pythagorean Expectation with adjustable runs and $\gamma$; FIP with HR, BB, HBP, K, IP; wOBA with linear weights).
    - Custom formula selection: user can pick any formula ID from the database or enter custom formula text.
    - Dynamic input form generator: auto-detects formula input variables and generates range sliders and number inputs.
    - Reactive real-time AJAX query to `/api/eval`.
    - Real-time Chart.js sensitivity curves: generates a line chart sweeping one parameter across a realistic range (e.g. varying Runs Scored from 500 to 1000 while holding Runs Allowed constant) to plot the response curve.
- **Backward Compatibility & Regression Guard**:
  - Existing template routes (`/`, `/api/formulas`, `/api/tables`, `/api/graph`, `/api/eval`) remain strictly intact.
  - All new interactive playground UI elements are self-contained in cleanly factored JavaScript and HTML blocks.
