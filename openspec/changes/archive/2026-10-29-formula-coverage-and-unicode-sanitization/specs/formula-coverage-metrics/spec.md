# Specification: Formula & Variable Coverage Metrics Engine

## Scope & Purpose
Provides comprehensive audit, metrics collection, and diagnostic reporting on mathematical formula parsing yield, symbol definitions vs. usages, ontology integration rates, unconstrained/orphan variables, and non-ASCII character distributions across the scientific corpus.

## Requirements
1. **Coverage Metrics Data Models**:
   - `FormulaCoverageReport` MUST encapsulate:
     - `total_formulas`: Total formulas inspected.
     - `valid_formulas`: Formulas successfully parsed by SymPy.
     - `equality_formulas`: Formulas containing explicit equality ($LHS = RHS$).
     - `parse_yield_pct`: Ratio of valid to total formulas.
     - `unique_symbols`: Distinct symbol names extracted.
     - `defined_symbols`: Symbols appearing on the LHS of equality formulas.
     - `consumed_symbols`: Free symbols appearing on the RHS.
     - `ontology_mapped_symbols`: Symbols mapping to `SymbolOntology` canonical concepts.
     - `orphan_symbols`: Consumed symbols that lack an LHS definition and do not resolve to canonical concepts.
     - `error_taxonomy`: Distribution of parsing errors by category.
     - `character_accounting`: Frequency distribution of non-ASCII characters.
2. **Analysis Capabilities**:
   - `FormulaCoverageAnalyzer.analyze_corpus(limit)` MUST evaluate the database corpus.
   - `FormulaCoverageAnalyzer.analyze_extracted_formulas(formulas)` MUST evaluate arbitrary formula lists in memory.
   - MUST provide formatting helpers: `to_markdown()` and `to_json()`.
3. **Interfaces**:
   - CLI command `kb formulas coverage [--report <path>] [--json]` under `kb.cli`.
   - GraphQL schema type `FormulaCoverageType` and query `formulaCoverage` under `src/kb/graphql/schema.py`.
   - REST API endpoint `/api/coverage` and UI stats summary under `src/kb/ui/app.py`.
