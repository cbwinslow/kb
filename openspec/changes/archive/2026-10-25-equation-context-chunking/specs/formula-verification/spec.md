# Spec Delta: formula-verification

## ADDED Requirements

### Requirement: Mathematical Symbol Extraction and Inter-Equation Cross-Referencing
The system SHALL extract mathematical variable symbols and detect inter-equation label cross-references across scientific texts.

#### Scenario: Extracting free symbols and variable glossary
- **WHEN** LaTeX equations are parsed from a document
- **THEN** system identifies distinct free mathematical symbols and extracts explanatory variable glossaries where present

#### Scenario: Identifying inter-equation label cross-references
- **WHEN** text or equation comments reference other equations in the document (e.g. "by Equation (1)" or "substituting (2) into (3)")
- **THEN** system extracts the referenced equation labels and records relational cross-references
