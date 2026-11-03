# Figure VLM Grounding Specification

## Purpose
Enables multimodal semantic grounding, curve extraction, and formula relational linking for scientific diagrams, trajectory plots, and charts in vault storage.

## Requirements

### Requirement 1: Multimodal Figure Semantic Analysis
The system SHALL analyze extracted scientific figures to identify diagram types, axis labels, units, plotted curves, and visual trends, persisting structured visual metadata in the database.

#### Scenario: Visual analysis of trajectory plot
- **WHEN** a document containing aerodynamic or statistical trajectory figures is processed
- **THEN** the system generates visual summaries and extracts identified curve attributes into the figure record

### Requirement 2: Figure to Formula Relational Grounding
The knowledge graph SHALL link extracted scientific figures directly to mathematical formulas and derivation chains referenced in surrounding text chunks or captions.

#### Scenario: Relational linking of figures and equations
- **WHEN** a figure caption or explanatory paragraph references an equation number or mathematical symbol
- **THEN** the system registers bidirectional foreign keys between the figure entity and the corresponding formula entities

### Requirement 3: FastMCP Multimodal Figure Query Tools
The FastMCP server SHALL expose tools allowing AI agents to retrieve figure images, bounding boxes, visual captions, and grounded formula associations by document or concept query.

#### Scenario: Agent requests figure metadata via FastMCP
- **WHEN** an AI agent calls `kb_get_figure` with a valid document citekey and figure index
- **THEN** the tool returns image URLs, captions, extracted curve metadata, and linked formula IDs

### Requirement: Batch Figure VLM Grounding Pipeline and CLI Indexer
The system SHALL provide a batch figure grounding pipeline and CLI command to process ungrounded figure records across the corpus, extracting visual summaries, curves, and formula entity links.

#### Scenario: Running batch figure indexing via CLI
- **WHEN** user executes `kb figures index-all` with optional `--batch-size` and `--limit`
- **THEN** the system identifies ungrounded figures, invokes the VLM processor to extract visual summaries and curve descriptors, links nearby formula IDs, and persists the updates in PostgreSQL

#### Scenario: Dry-run and force re-indexing options
- **WHEN** user specifies `--dry-run` or `--force` during batch figure indexing
- **THEN** the system previews grounding actions without database mutations in dry-run mode, or re-processes previously grounded figures when force is enabled
