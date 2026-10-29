# formula-verification Specification

## Purpose
Validates extracted LaTeX formulas using computer algebra, checks mathematical syntax, and generates executable Python representations.

## Requirements

### Requirement: LaTeX Equation Parsing and Verification
The system SHALL parse isolated LaTeX equations, verify mathematical syntactic validity using symbolic computer algebra, and assess multi-tier validation health scorecards.

#### Scenario: Valid algebraic equation parsing
- **WHEN** a syntactically correct LaTeX equation is submitted for verification
- **THEN** system successfully builds a SymPy symbolic expression tree, executes multi-tier mathematical quality gates, and reports verification status alongside numerical health score

#### Scenario: Malformed or OCR-degraded equation handling
- **WHEN** an equation with missing closing delimiters, invalid subscripts, or unparseable OCR artifacts is parsed
- **THEN** system flags the equation as unverified, logs the specific syntax error, sets validation score to zero, and retains raw text without raising fatal exceptions

### Requirement: Python AST Generation from Symbolic Formulas
The system SHALL generate executable Python function definitions or expressions corresponding to verified formulas.

#### Scenario: Generate Python expression for univariate formula
- **WHEN** user or agent requests Python code for a verified equation (e.g., Pythagorean expectation)
- **THEN** system outputs an executable Python expression with mapped variable parameters

### Requirement: Mathematical Symbol Extraction and Inter-Equation Cross-Referencing
The system SHALL extract mathematical variable symbols and detect inter-equation label cross-references across scientific texts.

#### Scenario: Extracting free symbols and variable glossary
- **WHEN** LaTeX equations are parsed from a document
- **THEN** system identifies distinct free mathematical symbols and extracts explanatory variable glossaries where present

#### Scenario: Identifying inter-equation label cross-references
- **WHEN** text or equation comments reference other equations in the document (e.g. "by Equation (1)" or "substituting (2) into (3)")
- **THEN** system extracts the referenced equation labels and records relational cross-references

### Requirement: Standalone Library Export and Polars Expression Generation
The system SHALL batch-compile all verified mathematical formulas into a standalone, importable Python package (`kb-formulas`) containing typed Python function implementations, KaTeX docstrings, and Polars DataFrame column expressions.

#### Scenario: Compiling formula library into standalone package
- **WHEN** `kb code export` is executed
- **THEN** system traverses all verified formulas, generates clean Python ASTs and Polars expressions with docstrings, and writes a zero-dependency module ready for wheel packaging
