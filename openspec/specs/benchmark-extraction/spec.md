# benchmark-extraction Specification

## Purpose
Extracts empirical tabular benchmarks from scientific documents into structured Parquet and CSV files for unit testing.

## Requirements

### Requirement: Tabular Structure Extraction
The system SHALL identify, extract, and convert tables from parsed academic papers into structured data objects.

#### Scenario: Extract numerical table into structured dataframe
- **WHEN** a document containing an empirical summary table (such as a 24-state run expectancy matrix) is processed
- **THEN** system preserves all row indices, column headers, and floating-point cell values without cell truncation

### Requirement: Golden Test Fixture Export
The system SHALL export verified numerical tables to standard Parquet and CSV formats linked to the document's citation key.

#### Scenario: Export benchmark dataset for test fixtures
- **WHEN** an extracted table is tagged as a benchmark fixture
- **THEN** system persists the table as a versioned Parquet file in the fixture vault and associates it with the source paper citation
