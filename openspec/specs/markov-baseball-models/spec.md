# markov-baseball-models Specification

## Purpose
Specifies discrete-time Markov chain game-state models, transition matrices, fundamental matrix inversion, and run expectancy vector derivations for baseball analytics.

## Requirements

### Requirement: 24-State Discrete Markov Transition Matrix
The system SHALL ingest and maintain the canonical 24-state to 24-state (plus 3-out absorbing state) discrete Markov chain transition matrix $P$ representing all base-out configurations in an inning.

#### Scenario: Resolving Markov state transition matrix
- **WHEN** user or downstream engine queries baseball Markov models
- **THEN** system provides the transition probability matrix $P$ mapping states $(b, o)$ across single-event transitions (walk, single, out, home run)

### Requirement: Fundamental Matrix Inversion and Run Expectancy
The system SHALL maintain symbolic and numerical formulations for the fundamental matrix $N = (I - Q)^{-1}$ and expected runs vector $R = N \cdot E$, deriving state-transition values from plate-appearance event probabilities.

#### Scenario: Deriving run expectancy matrix from transition probabilities
- **WHEN** event probability distributions are supplied to the Markov engine
- **THEN** system inverts $(I - Q)$ to compute expected plate appearances and total expected runs for every base-out state
