# Discrete Markov Chain Baseball Model

The discrete Markov chain model of baseball game states, formalized by D'Esopo & Lefkowitz (1960) and expanded by Bukiet, Harold, and Palacios (1997), represents a half-inning of baseball as an absorbing Markov process across discrete base-runner and out configurations.

## 1. State Space Representation

A half-inning contains 24 transient states defined by the Cartesian product of 8 base-runner configurations $b \in \{000, 100, 020, 003, 120, 103, 023, 123\}$ and 3 out counts $o \in \{0, 1, 2\}$, plus a single absorbing state $s_{25} = (3\text{ outs})$:

$$S = \{(b, o) : b \in \mathcal{B}, o \in \{0, 1, 2\}\} \cup \{3\text{ outs}\}$$

## 2. Canonical Transition Probability Matrix

The full $25 \times 25$ transition probability matrix $P$ is structured in canonical absorbing form:

$$P = \begin{pmatrix} Q & R_{abs} \\ 0 & 1 \end{pmatrix}$$

Where:
- $Q$ is the $24 \times 24$ submatrix representing transition probabilities between transient base-out states
- $R_{abs}$ is the $24 \times 1$ column vector representing transition probabilities from transient states directly into the 3-out absorbing state

## 3. Fundamental Matrix Inversion

Because $Q^k \to 0$ as $k \to \infty$, the fundamental matrix $N$ exists and represents the expected number of visits to state $j$ starting from state $i$:

$$N = (I - Q)^{-1}$$

Where:
- $I$ is the $24 \times 24$ identity matrix
- $N = I + Q + Q^2 + Q^3 + \dots$

## 4. Run Expectancy Vector Derivation

Let $E$ denote the $24 \times 1$ vector of immediate expected runs scored on a single transition departing from each state $i$. The total expected runs remaining in the inning from state $i$ is:

$$RE = N \cdot E$$

Expanding via fundamental matrix inversion:

$$RE = (I - Q)^{-1} \cdot E$$

## 5. Transition Run Value (Linear Weights)

The empirical run value $RV$ of an offensive event $e$ causing a transition from state $s$ to state $s'$ while scoring $Runs(e)$ runs is:

$$RV(e, s) = RE(s') - RE(s) + Runs(e)$$

This formulation provides the analytical foundation for linear weights and 24-state Run Expectancy (RE24) matrices.
