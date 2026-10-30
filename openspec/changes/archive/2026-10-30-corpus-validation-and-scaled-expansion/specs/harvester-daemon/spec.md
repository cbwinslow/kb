# Spec Delta: harvester-daemon

## ADDED Requirements

### Requirement: Multi-Preset Scaled Harvesting Sweeps
The system SHALL support automated sequential harvesting sweeps across multiple curated sabermetric presets.

#### Scenario: Sequential multi-domain preset sweep
- **WHEN** user executes `kb sync harvest --sweep` or invokes all presets sequentially
- **THEN** harvester executes discovery, pre-download deduplication, layout parsing, embedding, and storage cycles across `popular`, `mlb-modeling`, `statcast`, `retrosheet`, and `baseball-python` presets.

#### Scenario: Vault synchronization and disk cleanup enforcement
- **WHEN** papers are ingested during a multi-preset harvest sweep
- **THEN** system pushes downloaded PDFs and cropped figures to the homelab vault via SFTP and unlinks local staging files, preserving $\ge 1.5$ GB workstation free disk space.
