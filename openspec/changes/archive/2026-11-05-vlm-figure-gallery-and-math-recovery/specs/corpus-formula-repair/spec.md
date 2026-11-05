# Spec Delta: corpus-formula-repair

## ADDED Requirements

### Requirement: Unicode Mathematical and Structural AST Recovery
The system SHALL normalize Unicode mathematical alphanumeric characters, combining vector marks, expectation angle brackets, unbraced summation indices, and equivalence operators during formula sanitization.

#### Scenario: Normalizing Unicode math alphanumeric symbols and vector marks
- **WHEN** raw LaTeX contains Unicode Mathematical Alphanumeric characters (U+1D400..U+1D7FF) or combining vector arrows (`\u20d7`)
- **THEN** system normalizes them to base ASCII/Greek letters, strips combining marks, and yields a parseable SymPy expression

#### Scenario: Normalizing expectation brackets and unbraced summation indices
- **WHEN** raw LaTeX contains angle expectation brackets (`\langle ... \rangle`) or unbraced summation indices (`\sum i`)
- **THEN** system converts brackets to parentheses and wraps summation indices into standard LaTeX subscript form (`\sum_{i}`)
