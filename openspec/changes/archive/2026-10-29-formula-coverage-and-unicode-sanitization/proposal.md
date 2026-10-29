# Proposal: Formula Coverage Metrics, Universal Unicode Sanitization & Corpus Repair

## Problem Statement
Empirical audit of the 5,889 extracted formulas in the scientific corpus reveals that only ~1,042 (17.7%) are recognized as valid SymPy expressions, leaving 4,847 unparsed. 

Diagnostic character frequency analysis identified that over 50% of the parse failures are caused by:
1. **Unicode Mathematical & Greek Characters**: Unconverted Unicode Greek characters (e.g. $\theta, \alpha, \beta, \gamma, \tau, \sigma, \pi, \phi, \lambda$ occurring over 10,000 times), Unicode math operators ($\sum, \prod, \int, \parallel, \in, \partial, \sqrt{}, \approx$), and Unicode mathematical alphanumeric letters ($U+1D400 - U+1D7FF$ such as $𝑡, 𝑧, 𝑖$ emitted by Docling OCR).
2. **Unsupported LaTeX Font & Function Macros**: LaTeX wrappers like `\boldsymbol{}`, `\bm{}`, `\mathbf{}`, `\mathbb{}`, `\mathcal{}`, `\operatorname{}` which SymPy treats as unknown multiplicative identifiers rather than variables.
3. **Lack of Coverage Tracking & Symbol Accounting**: The system lacks tools to measure which extracted variables are defined on an equation LHS, which are consumed on the RHS, which resolve to canonical baseball ontology concepts, and which remain unlinked or orphaned.
4. **Stale Stored Formulas**: Formulas ingested in earlier papers have outdated `sanitized_latex` and require an automated, in-place corpus repair mechanism.

## Proposed Solutions
1. **Universal Unicode & Mathematical Sanitizer (`src/kb/math/sanitizer.py`)**:
   - Comprehensive Unicode Greek mapping covering all standard Greek, archaic, and variant symbols.
   - Comprehensive Unicode mathematical operator translations to standard LaTeX.
   - Decomposition and normalization of Mathematical Alphanumeric Symbols ($U+1D400 - U+1D7FF$) to standard alphanumeric characters via `NFKD`.
   - Stripping and normalization of LaTeX styling/font macros.
   - Robust delimiter and trailing punctuation repair.

2. **Formula Coverage & Symbol Accounting Engine (`src/kb/math/coverage.py`)**:
   - `FormulaCoverageAnalyzer` computing:
     - AST validation yield, equality ratio, and compilation rates.
     - Symbol graph completeness (ratio of consumed RHS symbols with corresponding LHS definitions).
     - Ontology resolution coverage (ratio of variables mapping to canonical concepts).
     - Orphan / unconstrained variable identification.
     - Error taxonomy classification (unrecognized tokens, syntax errors, unbalanced delimiters).
   - CLI command `kb formulas coverage [--report <file.md>] [--json]`.
   - Integration into the UI Dashboard and GraphQL schema.

3. **In-Place Corpus Formula Repair (`kb formulas repair`)**:
   - Safe transactional batch migration iterating over stored formulas, re-sanitizing raw LaTeX, re-validating with SymPy, and updating database records in-place.
