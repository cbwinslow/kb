# Design: Multimodal Figure Studio & Gallery and Unicode Math AST Recovery

## 1. Architecture Overview

This change delivers two complementary capabilities:
1. An interactive web-based visual inspection studio for the 490 grounded scientific figures and diagrams in the knowledge base.
2. An advanced LaTeX normalization pass (Sanitizer V4) targeting the specific character families responsible for persistent Grade-F parsing failures.

```
┌────────────────────────────────────────────────────────┐
│                   Web Browser / UI                     │
│  "Figures & Multimodal" Gallery & Diagram Inspector    │
└───────────────────────────┬────────────────────────────┘
                            │ GET /api/figures[?diagram_type=...&q=...]
                            │ GET /api/figures/{id}
┌───────────────────────────▼────────────────────────────┐
│              Starlette REST API (app.py)               │
│  Resolves Figure entities + linked Formula ASTs        │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│              PostgreSQL 16 (cbwdellr720)               │
│  figures (490)  <─── proximity/caption ───>  formulas  │
└───────────────────────────▲────────────────────────────┘
                            │ in-place repair
┌───────────────────────────┴────────────────────────────┐
│     EquationSanitizer V4 & CorpusFormulaRepairer        │
│  - Unicode Math Alphanumeric (U+1D400-U+1D7FF)         │
│  - Combining vector arrows (\u20d7) & overlines        │
│  - Expectation angle brackets (\langle...\rangle)      │
│  - Unbraced summation subscripts (\sum i -> \sum_{i})  │
└────────────────────────────────────────────────────────┘
```

## 2. Technical Details

### 2.1 Unicode Math Sanitizer V4 (`src/kb/math/sanitizer.py`)
- **Unicode Math Alphanumeric Translation**:
  PDF layout engines and Docling OCR output Unicode mathematical characters in ranges `0x1D400`–`0x1D7FF` (bold, italic, script, fraktur, double-struck). SymPy's ANTLR grammar crashes on these codepoints. Decomposing these characters via `unicodedata.normalize("NFKD", c)` converts them directly into ASCII equivalents (`𝑢` $\to$ `u`, `𝑥` $\to$ `x`, `𝜕` $\to$ `\partial`).
- **Combining Diacritic Stripping**:
  Remove combining vector right arrow (`\u20d7`) and overlines (`\u0305`, `\u0304`) that prefix or suffix OCR tokens.
- **Expectation / Angle Bracket Normalization**:
  Convert `\langle X \rangle`, `\u3008X\u3009`, and `\u2329X\u232a` into `(X)` so ANTLR parses the internal expression algebraically instead of rejecting the bracket token.
- **Unbraced Summation Index Normalization**:
  Transform `\sum <var>` (e.g. `\sum i`, `\sum j,k`, `\sum t\in\Omega`) into proper subscripted LaTeX `\sum_{<var>}`.
- **Equivalence Operator Normalization**:
  Convert `\equiv` and `\u2261` into `=`.
- **Fullwidth Equation Number Stripping**:
  Strip `（...）` matching `[\s,;.]*[（\(][A-Za-z0-9\.\-_]+[）\)]\s*$`.

### 2.2 Multimodal Figure Studio (`src/kb/ui/app.py`)
- **API Endpoints**:
  - `GET /api/figures`: Supports optional query parameters `citekey`, `diagram_type`, `q` (search caption/summary), and `limit` (default 50, max 200). Returns array of figure JSON objects with `vlm_summary`, `detected_curves`, `axes`, `units`, `formula_ids`, and `caption`.
  - `GET /api/figures/{id}`: Returns single figure detail, including resolved `Formula` records for all associated `formula_ids` (raw LaTeX, sanitized LaTeX, validation grade, and sympy representation).
- **UI Tab Implementation**:
  - Add tab button: `[🖼️ Figures & Multimodal]`.
  - Filter bar: Search input + Diagram type dropdown (`All`, `trajectory_plot`, `contour_map`, `scatter_trend`, `schematic`, `bar_chart`, `unknown`).
  - Card view:
    - Diagram badge with distinct color coding.
    - Document citekey + Figure index header.
    - High-density VLM summary snippet.
    - Extracted axes and units badges ($x$: time [s], $y$: velocity [m/s]).
    - Interactive formula chip pills that link or expand to show KaTeX math.

## 3. Testing & Validation Strategy
1. **Sanitizer Tests**: Unit tests in `tests/test_sanitizer_coverage.py` and `tests/test_formula_repair.py` testing each new normalization rule.
2. **UI API Tests**: Integration tests in `tests/test_ui.py` testing `/api/figures` and `/api/figures/{id}` endpoints.
3. **Quality Gates**: Pass `ruff check`, `pyright`, and `pytest`.
