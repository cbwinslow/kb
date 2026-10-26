# performance-benchmarking Specification

## Purpose
Profiles and verifies the speed, throughput, latency, and mathematical quality of core components, including formula execution, dense embedding generation, hybrid search, and corpus compilation yield.

## Requirements

### Requirement: Formula Execution Throughput Benchmarking
The system SHALL benchmark formula execution speed comparing pure Python scalar calculations against vectorized Polars column expressions over large synthetic datasets ($N \ge 10,000$ rows).

#### Scenario: Benchmarking scalar vs Polars speedup
- **WHEN** user executes `kb benchmark --formulas --rows 100000`
- **THEN** system evaluates sample formulas on $100,000$ rows, reports elapsed times in milliseconds, throughput in rows/sec, and speedup multipliers ($\ge 10\times$)

### Requirement: Embedding Throughput Profiling
The system SHALL profile dense vector embedding generation throughput, measuring latency per text chunk and chunks generated per second.

#### Scenario: Benchmarking embedding generation
- **WHEN** user executes `kb benchmark --embeddings`
- **THEN** system generates embeddings for sample text chunks and outputs total time, latency per chunk in milliseconds, and hardware device utilized

### Requirement: Hybrid Search Latency Profiling
The system SHALL measure response times for Hybrid Search queries across both dense vector distance and lexical `tsvector` matching combined with Reciprocal Rank Fusion.

#### Scenario: Benchmarking search response times
- **WHEN** user executes `kb benchmark --search`
- **THEN** system executes sample search queries and reports P50, P95, and maximum latency in milliseconds

### Requirement: Corpus Mathematical Quality Scorecard
The system SHALL audit extracted formulas in the database and report AST parse success rate, equality ratio, and compilation yield.

#### Scenario: Running corpus quality audit
- **WHEN** user executes `kb benchmark --quality`
- **THEN** system queries all stored formulas, reports total count, verified valid count, compilable functions, and percentage yields
