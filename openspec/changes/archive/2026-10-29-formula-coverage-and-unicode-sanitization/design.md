# Design: Formula Coverage Metrics, Universal Unicode Sanitization & Corpus Repair

## Architectural Overview
This change enhances the mathematical processing subsystem across normalization, diagnostic evaluation, and data integrity:

```
[ Raw LaTeX / OCR Output ]
            │
            ▼
┌──────────────────────────────────────────────┐
│ Universal EquationSanitizer                  │
│ - NFKD normalization of U+1D400-U+1D7FF      │
│ - 60+ Unicode Greek letters & variants       │
│ - 40+ Unicode Math Operators                 │
│ - Font macro unwrapping (\boldsymbol, etc.)  │
│ - Delimiter balancing & symbol protection    │
└──────────────────────────────────────────────┘
            │
            ▼
┌──────────────────────────────────────────────┐
│ FormulaExtractor (SymPy parse_latex)         │
│ - Generates validated Symbolic AST           │
│ - Extracts LHS, RHS, free symbols            │
└──────────────────────────────────────────────┘
            │
            ▼
┌──────────────────────────────────────────────┐
│ FormulaCoverageAnalyzer                      │
│ - AST Parse Yield & Equality Ratio           │
│ - Symbol Taxonomy & Ontology Mapping         │
│ - Definition Graph Completeness              │
│ - Orphan / Unresolved Variable Discovery     │
│ - Error Diagnostics & Char Accounting        │
└──────────────────────────────────────────────┘
            │
    ┌───────┴───────────────┬──────────────────────┐
    ▼                       ▼                      ▼
[ CLI: kb formulas ]   [ /graphql API ]   [ UI Dashboard Tab ]
```

## Detailed Component Design

### 1. Universal EquationSanitizer Enhancements
- **Mathematical Alphanumerics ($U+1D400 - U+1D7FF$)**:
  - Automatically identifies characters in the range and applies `unicodedata.normalize('NFKD', c)` to collapse italic, bold, sans-serif, and blackboard-bold glyphs into standard ASCII equivalents (`a-z`, `A-Z`, `0-9`).
- **Comprehensive Greek Alphabet Mapping**:
  - Mappings for all lowercase ($\alpha$ through $\omega$), uppercase ($\Gamma, \Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma, \Upsilon, \Phi, \Psi, \Omega$), and typographic variants ($\vartheta, \varphi, \varpi, \varrho, \varsigma, \epsilon, \phi$).
- **Mathematical Operators**:
  - $\sum \to \text{\\sum }$, $\prod \to \text{\\prod }$, $\int \to \text{\\int }$, $\partial \to \text{\\partial }$, $\sqrt{} \to \text{\\sqrt }$, $\in \to \text{\\in }$, $\notin \to \text{\\notin }$, $\le \to \text{\\le }$, $\ge \to \text{\\ge }$, $\ne \to \text{\\ne }$, $\approx \to \text{\\approx }$, $\sim \to \text{\\sim }$, $\equiv \to \text{\\equiv }$, $\infty \to \text{\\infty }$, $\pm \to \text{\\pm }$, $\mp \to \text{\\mp }$, $\times \to \text{\\times }$, $\cdot \to \text{\\cdot }$, $\parallel \to |$, $\perp \to \text{\\perp }$, $\propto \to \text{\\propto }$.
  - Replacement character `\uFFFD` replaced with whitespace.
- **Font & Macro Stripping**:
  - Regex replacement for `\boldsymbol{X}`, `\bm{X}`, `\mathbf{X}`, `\mathbb{X}`, `\mathcal{X}`, `\mathrm{X}` $\to$ `X`.
  - Replace `\operatorname{Var}` $\to$ `Var`, `\operatorname{E}` $\to$ `E`, `\operatorname{Cov}` $\to$ `Cov`, `\operatorname{Pr}` $\to$ `P`.
- **Delimiter Repair**:
  - Auto-balances missing closing/opening curly braces.
  - Strips trailing punctuation (commas, periods, semicolons).

### 2. FormulaCoverageAnalyzer
- **Metrics Collected**:
  - `total_formulas`: Total formula count in database or subset.
  - `valid_formulas`: Count of formulas successfully parsed by SymPy.
  - `equality_formulas`: Count of formulas with explicit equality ($LHS = RHS$).
  - `parse_yield_pct`: `(valid / total) * 100`.
  - `unique_symbols`: Total distinct symbols extracted across all formulas.
  - `defined_symbols`: Symbols appearing on equation LHS.
  - `consumed_symbols`: Symbols appearing in RHS expressions.
  - `ontology_mapped_symbols`: Symbols resolving to `SymbolOntology` canonical concepts.
  - `orphan_symbols`: Consumed symbols that are never defined on any LHS or ontology.
  - `error_taxonomy`: Frequency distribution of parser failure reasons.
  - `character_accounting`: Frequency distribution of non-ASCII characters encountered.

### 3. In-Place Repair Engine (`kb formulas repair`)
- Iterates over stored formulas with batch size (default 250).
- Applies `EquationSanitizer.sanitize(raw_latex)`.
- Re-parses via `FormulaExtractor.parse_latex_string`.
- Updates `sanitized_latex`, `sympy_repr`, `symbols`, `is_valid`, `is_equality`, `lhs`, and `rhs`.
- Commits transactions progressively and reports repaired formula count.
