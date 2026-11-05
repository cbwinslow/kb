# Proposal: Multimodal Figure Studio & Gallery and Unicode Math AST Recovery

## Why

While `kb` holds 490 grounded figures and 6,199 formulas in PostgreSQL, two high-value capabilities remain unaddressed:
1. **Interactive Multimodal UI**: The Web dashboard (`kb ui serve`) has Lineage, Formulas, and Search, but lacks a dedicated gallery for exploring the 490 grounded figures, their VLM summaries, detected curves, bounding boxes, and linked mathematical formulas.
2. **Unicode Math AST Recovery**: 1,848 formulas remain classified as Grade F due to Unicode Mathematical Alphanumeric glyphs (U+1D400-U+1D7FF), combining vector arrows (`\u20d7`), expectation brackets (`\langle...\rangle`), equivalence symbols (`\equiv`), and unbraced summation indices that can be normalized into valid SymPy ASTs.

## What Changes

- **Multimodal Figure Studio & Gallery in Web UI (`src/kb/ui/app.py`)**:
  - Add REST API endpoints:
    - `GET /api/figures`: lists grounded figures with filtering by `citekey`, `diagram_type`, or search query.
    - `GET /api/figures/{id}`: returns full metadata and resolves linked formula ASTs.
  - Implement a modern **"Figures & Multimodal"** gallery tab in the Starlette dashboard with diagram type badges (`trajectory_plot`, `contour_map`, `scatter_trend`), VLM summaries, axes/units, and clickable formula chips.
- **Sanitizer V4 Unicode Mathematical Recovery (`src/kb/math/sanitizer.py`)**:
  - Normalize Unicode Math Alphanumeric characters (`U+1D400`..`U+1D7FF`) to standard ASCII/Greek.
  - Strip combining vector arrows (`\u20d7`) and overlines (`\u0305`, `\u0304`).
  - Normalize expectation and angle brackets (`\langle ... \rangle`, `〈...〉` -> `(...)`).
  - Wrap unbraced `\sum` subscripts (`\sum i`, `\sum j,k`, `\sum t \in \Omega` -> `\sum_{...}`).
  - Convert fullwidth equation tags `（...）` and normalize equivalence `\equiv` -> `=`.
- **Corpus Repair & Standalone Package Recompilation**:
  - Run `kb corpus repair-all` on the PostgreSQL corpus to elevate recovered formulas.
  - Recompile standalone `packages/kb_formulas` with newly verified Grade A functions.

## Capabilities

### New Capabilities
- `figure-vlm-gallery`: Interactive web visualizer and REST API endpoints for searching, filtering, and inspecting grounded figures, axes, curves, and linked formulas.

### Modified Capabilities
- `corpus-formula-repair`: Enhanced LaTeX sanitization with Unicode mathematical normalizations, vector arrow transformations, and summation index wrapping.

## Impact

- **Web UI**: Starlette application gains `/api/figures`, `/api/figures/{id}`, and an interactive Multimodal gallery tab.
- **Math Engine**: `EquationSanitizer` expands recovery rate for Grade-F formulas.
- **Database**: In-place upgrade of `kb_formulas` records on `cbwdellr720:5432/kb`.
- **Formula Library**: `packages/kb_formulas` gains newly verified callable equations.
