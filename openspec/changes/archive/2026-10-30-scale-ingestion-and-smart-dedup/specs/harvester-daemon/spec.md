# Spec Delta: harvester-daemon

## MODIFIED Requirements

### Requirement: Continuous Harvest Scheduling
The system SHALL provide an asynchronous continuous harvester service (`kb sync daemon`) executing search, download, layout parsing, embedding, and archival cycles on a configurable interval with multi-source polling and duplicate suppression.

#### Scenario: Running scheduled continuous harvesting
- **WHEN** user executes `kb sync daemon --interval 3600 --queries "baseball aerodynamics"`
- **THEN** daemon polls research repositories, processes unharvested papers, uploads PDFs to homelab storage, and sleeps until the next interval

#### Scenario: Harvest loop with citation ranking and pagination
- **WHEN** daemon is scheduled with citation popularity sorting enabled
- **THEN** daemon traverses multi-page query results sorted by publication impact (`cited_by_count:desc`) while honoring rate limits.

## ADDED Requirements

### Requirement: Domain-Specific Sabermetric Preset Harvesting
The system SHALL provide curated query presets and CLI controls targeting foundational sabermetrics, statistical modeling, Retrosheet analytics, and Statcast trajectory physics.

#### Scenario: Harvesting targeted domain presets
- **WHEN** user executes `kb sync harvest --preset mlb-modeling` or `kb sync harvest --preset popular`
- **THEN** harvester expands preset into domain-specific queries across OpenAlex and arXiv, filtering out existing database works before downloading.

#### Scenario: High-volume cursor pagination
- **WHEN** a harvest query requests more papers than the single-page limit (up to 200+ papers)
- **THEN** OpenAlex source discoverer traverses cursor-based pagination tokens until reaching target quota or exhausted results.
