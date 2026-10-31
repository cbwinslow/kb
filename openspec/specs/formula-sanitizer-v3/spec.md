# Formula Sanitizer V3 Specification

## Purpose
Provides advanced mathematical LaTeX normalization, multi-character acronym protection, and structural case reconstruction to recover failed formulas into verified symbolic ASTs.

## Requirements

### Requirement 1: Multi-Character Acronym Protection
The sanitizer MUST identify multi-character domain acronyms and variable names (such as BABIP, wOBA, wRAA, ERA, and FIP) and format them as atomic LaTeX operators or text tokens so they do not parse as multiplied single-letter variables.

#### Scenario: Preserving compound sabermetric metric names
- **WHEN** raw LaTeX contains terms like `\text{BABIP}` or standalone multi-letter identifiers
- **THEN** the sanitizer preserves the compound token as a single named SymPy Symbol rather than individual multiplied characters

### Requirement 2: Structural Delimiter Rebalancing
The sanitizer MUST inspect mathematical expressions for mismatched or unclosed delimiters (including `\left(`, `\right]`, `\left\{`, and unescaped pipe symbols) and balance them before AST compilation.

#### Scenario: Repairing unclosed delimiters
- **WHEN** an equation string contains an unclosed `\left(` without a matching `\right)`
- **THEN** the sanitizer inserts matching balancing tokens to ensure standard LaTeX syntax validation

### Requirement 3: Piecewise Cases Environment Reconstruction
The sanitizer MUST detect `\begin{cases}` environments and reconstruct them into valid piecewise relational expressions compatible with symbolic AST engines.

#### Scenario: Parsing piecewise formulas
- **WHEN** extracted LaTeX contains a multi-branch conditional equation defined within a cases environment
- **THEN** the sanitizer translates the branches and conditions into a valid SymPy Piecewise expression

### Requirement 4: Atomic Batch Formula Recovery
The formula repair engine MUST process failed Grade F formulas in configurable transaction batches, re-evaluating quality tier scorecards and committing only successfully recovered formulas.

#### Scenario: Batch repair of Grade F formulas
- **WHEN** the user executes batch repair across invalid corpus formulas
- **THEN** recovered formulas receive updated AST representations and letter grades while failed formulas remain logged without rolling back successful updates
