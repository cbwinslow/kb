# harvester-daemon Specification

## Purpose
Automates continuous, scheduled discovery and ingestion of scientific research papers from arXiv and OpenAlex with respectful rate limiting and remote homelab archival.

## Requirements

### Requirement: Continuous Harvest Scheduling
The system SHALL provide an asynchronous continuous harvester service (`kb sync daemon`) executing search, download, layout parsing, embedding, and archival cycles on a configurable interval.

#### Scenario: Running scheduled continuous harvesting
- **WHEN** user executes `kb sync daemon --interval 3600 --queries "baseball aerodynamics"`
- **THEN** daemon polls research repositories, processes unharvested papers, uploads PDFs to homelab storage, and sleeps until the next interval

### Requirement: Respectful Rate Limiting and Backoff
The daemon SHALL enforce query spacing ($\ge 3.0$ seconds) and exponential backoff retry on HTTP 429 rate limits.

#### Scenario: Handling rate limit backoff
- **WHEN** remote repository returns HTTP 429 Too Many Requests
- **THEN** daemon backs off exponentially before retrying without crashing the service
