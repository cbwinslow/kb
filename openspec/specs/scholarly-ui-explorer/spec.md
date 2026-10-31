# Scholarly UI Explorer Specification

## Purpose
Enables interactive web discovery of scientific literature and background 1-click preprint ingestion within the visual research explorer dashboard.

## Requirements

### Requirement 1: Interactive Scholarly Search Interface
The UI dashboard SHALL provide a dedicated search view that accepts queries and displays live results from arXiv and OpenAlex with title, authors, publication year, citation count, abstract snippet, and direct paper links.

#### Scenario: User queries literature from UI
- **WHEN** user inputs a search query and submits the external search form in the browser
- **THEN** the dashboard displays normalized result cards with author names, citation metrics, and direct links without page reload

### Requirement 2: Asynchronous 1-Click Preprint Ingestion
The UI server SHALL expose an endpoint that accepts a paper URL or identifier and launches asynchronous background ingestion on the workstation GPU without blocking the user interface.

#### Scenario: User initiates 1-click ingestion
- **WHEN** user clicks "Ingest Preprint" on a search result card
- **THEN** the system dispatches background ingestion, returns a job token, and displays live layout parsing and formula extraction progress in the UI

### Requirement 3: Ingestion Notification and Vault Status
The UI dashboard SHALL notify the user when background ingestion completes and display links to the newly indexed document, extracted formulas, and SFTP vault status.

#### Scenario: Ingestion completion notification
- **WHEN** background document parsing and database indexing finish
- **THEN** the UI displays a success banner with the generated citekey and updates corpus counters in real time
