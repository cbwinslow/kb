# Spec Delta: mcp-server

## ADDED Requirements

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
