# mcp-server Specification

## Purpose
Exposes Model Context Protocol (MCP) tools for coding assistants and agents to query scientific papers, formulas, and benchmarks.

## Requirements

### Requirement: Literature Search MCP Tool
The system SHALL provide an MCP tool (`kb_search_literature`) returning ranked scientific paper sections with citations and relevance scores.

#### Scenario: Searching literature from coding agent
- **WHEN** an AI assistant invokes `kb_search_literature` with query keywords or concepts
- **THEN** system returns matching paper chunks, titles, authors, years, and BibTeX citation keys

### Requirement: Formula Retrieval MCP Tool
The system SHALL provide an MCP tool (`kb_get_formula`) returning verified LaTeX equations and corresponding Python expressions.

#### Scenario: Fetching verified formula for implementation
- **WHEN** an AI assistant invokes `kb_get_formula` with a paper ID or formula identifier
- **THEN** system returns the exact LaTeX representation, variable definitions, and validated Python AST

### Requirement: Benchmark Fixture MCP Tool
The system SHALL provide an MCP tool (`kb_get_benchmark_table`) returning empirical benchmark tables in JSON or Parquet formats.

#### Scenario: Fetching test fixture data for unit tests
- **WHEN** an AI assistant invokes `kb_get_benchmark_table` with a table or paper identifier
- **THEN** system returns the tabular dataset ready for ingestion into unit test suites

### Requirement: Citation Network MCP Tool
The system SHALL provide an MCP tool (`kb_get_citations`) returning papers citing or referenced by a target paper.

#### Scenario: Exploring paper lineage from agent
- **WHEN** an AI assistant invokes `kb_get_citations` with a citekey or DOI
- **THEN** system returns lists of citing papers and referenced works with titles, years, citation counts, and OpenAlex IDs

### Requirement: Related Papers MCP Tool
The system SHALL provide an MCP tool (`kb_get_related_papers`) returning conceptually and methodologically related research papers.

#### Scenario: Finding related literature
- **WHEN** an AI assistant invokes `kb_get_related_papers` with a citekey or topic query
- **THEN** system returns ranked related papers from OpenAlex with abstracts, citation counts, and open-access links
