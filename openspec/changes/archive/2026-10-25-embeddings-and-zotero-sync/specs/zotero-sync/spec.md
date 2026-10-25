# Spec Delta: zotero-sync

## ADDED Requirements

### Requirement: Automated Zotero Library Monitoring and Auto-Ingestion
The system SHALL monitor the local Zotero SQLite library for changes and automatically execute the ingestion pipeline for newly detected paper attachments.

#### Scenario: Detecting library modifications via watcher
- **WHEN** the Zotero database modification timestamp updates or polling interval elapses
- **THEN** system identifies reference items added or modified since the last recorded synchronization cursor

#### Scenario: Auto-ingesting newly attached PDF
- **WHEN** an unindexed reference item with a valid PDF file attachment is discovered
- **THEN** system automatically executes document parsing, formula extraction, table extraction, and database persistence
