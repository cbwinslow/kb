# Proposal: Interactive Quality Dashboard & 1-Click Formula Repair UI

## Why
While `kb formulas validate` evaluates quality scores and diagnostics via CLI, researchers and analysts exploring formulas in the web browser lack an intuitive dashboard to filter equations by quality grade (A, B, C, D, F) or validation status (`verified`, `provisional`, `degraded`, `failed`). When an equation exhibits remediable syntax or tokenization defects (such as unicode normalization remnants or split multi-letter acronyms), users must currently edit or repair via command-line scripts rather than clicking a single button in the web interface to repair and immediately re-validate the AST.

## What Changes
- **Interactive Quality Dashboard Tab**: Adds a dedicated "Quality & Scorecards" view in the web UI displaying grade distribution charts, score histograms, and filterable formula lists.
- **Detailed Diagnostic Drawer**: Clicking any formula expands a diagnostic drawer showing the Tier 1–4 breakdown (AST Invertibility, Symbol Tokenization, Boundary Monotonicity, Empirical Accuracy) with explicit check-by-check explanations.
- **1-Click Formula Repair Trigger**: A repair button invokes the `/api/formulas/repair` backend endpoint, executing `CorpusFormulaRepairer` on the selected formula and immediately re-running `FormulaQualityGate` to update the displayed grade in real time.
- **Grade & Status Filtering**: Provides multi-select pill filters for Letter Grades (A, B, C, D, F) and Validation Statuses.

## Capabilities

### Modified Capabilities
- `ui-playground`: Adds quality gate inspection views, grade filters, detailed diagnostic drawers, and interactive AST repair triggers.
- `mathematical-quality-gate`: Extends real-time re-validation workflows triggered dynamically via UI endpoints.

## Impact
- **Web UI**: Extends `src/kb/ui/templates/index.html` (or modular UI assets) and `src/kb/ui/app.py`.
- **API**: Adds `/api/formulas/{id}/repair` endpoint triggering in-place sanitization and quality gate re-evaluation.
- **Dependencies**: Frontend relies on vanilla JavaScript, Chart.js, and CSS; no new npm or backend dependencies required.
