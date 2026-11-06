# Spec Delta: projection-systems

## Purpose
Codifies canonical mathematical formulations and algorithmic specifications for baseball forecasting systems, including PECOTA, ZiPS, and Marcel the Monkey models.

## ADDED Requirements

### Requirement: PECOTA Forecasting Specification
The system SHALL ingest and maintain canonical mathematical formulas for the PECOTA forecasting architecture, including Mahalanobis career distance, comparable weighting, age-curve adjustment, and percentile forecast distributions.

#### Scenario: Querying PECOTA similarity and projection formulas
- **WHEN** user or agent searches the knowledge base for PECOTA or comparable player similarity metrics
- **THEN** system returns verified mathematical equations defining the Mahalanobis distance metric, comparable player weighting, and Monte Carlo probability percentiles

### Requirement: ZiPS Projection Architecture
The system SHALL ingest and maintain canonical mathematical formulations for the ZiPS forecasting system, including multi-year recency decay weighting, archetype-specific aging transitions, and sample-size regression to the league mean.

#### Scenario: Evaluating ZiPS recency and regression formulas
- **WHEN** user evaluates ZiPS equations in the formula library or Web UI Playground
- **THEN** system executes sample-size regression to league mean and multi-year weighted baseline calculations with valid parameter ranges

### Requirement: Marcel the Monkey Baseline Model
The system SHALL ingest and maintain canonical mathematical equations for Tom Tango's Marcel the Monkey forecasting model, including 5/4/3 season weighting, constant regression to league average, and piecewise age adjustments.

#### Scenario: Executing Marcel baseline projections
- **WHEN** user sweeps age and previous-season statistics in the formula playground
- **THEN** system computes expected regression to the mean and applies the 30-age piecewise threshold adjustment
