# Spec Delta: harvester-daemon

## ADDED Requirements

### Requirement: Multi-Disciplinary Quantitative Research Presets Ingestion
The harvester SHALL support execution across multi-domain research presets (`biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, `kinematics-tracking`), ingesting candidate papers into PostgreSQL, extracting mathematical formulas and figures via Docling, and synchronizing artifacts to the homelab SFTP vault.

#### Scenario: Harvesting biomechanics and PINN literature
- **WHEN** user executes `kb sync harvest --preset biomechanics --limit 10` or `kb sync harvest --preset aerodynamics-pinn --limit 10`
- **THEN** system queries OpenAlex and arXiv, filters duplicates, downloads open-access PDFs, parses layout and formulas, and vaults storage artifacts remotely
