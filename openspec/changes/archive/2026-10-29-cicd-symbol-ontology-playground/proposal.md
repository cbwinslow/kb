# Proposal: CI/CD Distribution, Symbol Ontology & Interactive Web UI Playground

## 1. Problem Statement
With the `kb` engine having reached over 5,800 extracted formulas, 450+ compiled Python functions, and sub-millisecond Polars execution, three critical capabilities are required to elevate the platform for production usage and external quantitative workflows:
1. **CI/CD & PyPI Distribution (Issue #2)**:
   - There is no automated GitHub Actions workflow to validate pull requests and commits across platforms (`ubuntu-latest`, `windows-latest`).
   - The compiled standalone formula library (`packages/kb_formulas`) is generated locally but lacks an automated continuous deployment pipeline to build wheels/sdists and publish to PyPI and GitHub releases upon version tagging.
2. **Semantic Symbol Ontology & Canonical Column Mapping (Issue #3)**:
   - Extracted formulas from diverse academic and sabermetric literature employ discordant variable notations for identical physical concepts (e.g. $R_S, \text{RS}, R, r$ all denote runs scored; $H_R, \text{HR}, hr$ all denote home runs; $I_P, \text{IP}$ denote innings pitched).
   - Downstream data processing with raw tabular DataFrames (from Retrosheet, Statcast, Chadwick, Lahman, or `baseballpy`) currently requires manual column renaming before compiled formula expressions can evaluate against them.
3. **Interactive Calculation Playground & Feature Hardening (Issue #4)**:
   - The existing web UI (`kb ui serve`) supports formula browsing, LaTeX rendering, lineage graph visualization, and benchmark table inspection, but lacks an interactive sandbox where users can dynamically manipulate inputs via sliders/forms, observe real-time recalculations, and visualize parameter sensitivity curves.
   - All interactive UI capabilities must be rigorously isolated and specified to avoid breaking existing tabs or API routes.

## 2. Proposed Solution
1. **Automated CI/CD Pipeline (`.github/workflows/`)**:
   - `ci.yml`: Automated multi-OS testing matrix (Ubuntu & Windows, Python 3.12) running `ruff check`, `pyright`, and `pytest`.
   - `publish-formulas.yml`: Automated build of `packages/kb_formulas` into binary wheels and source distributions using `uv build`, with publishing upon GitHub release tag creation.
2. **Semantic Symbol Ontology (`src/kb/math/ontology.py`)**:
   - Implement `SymbolOntology` with canonical concept definitions, synonym dictionaries, and AST symbol normalization.
   - Implement `map_dataframe_columns` for Polars and Pandas DataFrames, enabling zero-configuration formula binding.
3. **Interactive Web UI Calculation Playground (`src/kb/ui/`)**:
   - Add an interactive calculation workbench tab to the web UI (`/` and `/playground`).
   - Allow dynamic parameter variation with instant reactive feedback via `/api/eval`.
   - Embed real-time Chart.js interactive curves for canonical formulas (Pythagorean win expectancy curves, FIP vs ERA, etc.).
   - Preserve all existing UI endpoints, lineage views, and API behaviors.

## 3. Impact & Portability
- 100% portable across Windows, Linux, and macOS.
- Zero hardcoded paths or secrets.
- Enforces strict backward compatibility with existing tests and APIs.
