# Spec Delta: document-ingestion

## ADDED Requirements

### Requirement: Equation Derivation Co-occurrence and Window Clustering
The system SHALL detect sequential and coupled mathematical equations within a derivation section and cluster them into unified semantic chunks within the target token budget.

#### Scenario: Clustering coupled equations into atomic retrieval units
- **WHEN** multiple equations appear sequentially in a mathematical derivation or model definition
- **THEN** chunker preserves the equations within the same retrieval chunk when their combined token length adheres to the chunk size limit

#### Scenario: Binding preceding premise and trailing variable definitions
- **WHEN** a display equation is preceded by an explanatory sentence or followed by a variable definition clause (e.g. "where $X$ denotes...")
- **THEN** system keeps the framing sentences and variable definitions unified with the equation rather than splitting them into separate chunks

### Requirement: Mathematical Symbol and Variable Context Enrichment
The system SHALL extract mathematical symbols and variable definitions present in a chunk and enrich the chunk context header with a structured symbol index.

#### Scenario: Emitting symbol index context header
- **WHEN** a chunk contains mathematical equations with free variables or parameter symbols
- **THEN** system prepends a structured descriptor `[Symbols: ...]` to the chunk's enriched text for dense and sparse indexing
