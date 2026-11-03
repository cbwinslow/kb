# Spec Delta: openalex-enrichment

## ADDED Requirements

### Requirement: Multi-Domain Research Taxonomy Presets
The system SHALL provide curated multi-domain research presets in OpenAlex discovery for automated literature harvesting beyond single-domain sports analytics.

#### Scenario: Querying multi-domain preset harvesters
- **WHEN** user executes `kb sync harvest` with `--preset` set to `biomechanics`, `aerodynamics-pinn`, `sports-econometrics`, or `kinematics-tracking`
- **THEN** the system resolves the domain query parameters, searches OpenAlex works with citation ranking and cursor pagination, and filters results against the duplicate resolver

#### Scenario: Validating supported preset names
- **WHEN** user requests available presets or provides an unknown preset name
- **THEN** the system provides the complete list of valid multi-domain presets and rejects unrecognized presets with informative usage guidance
