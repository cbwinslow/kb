# Design: Multi-Hop Equation Chaining Engine

## Overview
The Multi-Hop Equation Chaining Engine extends `src/kb/math/chaining.py` and `src/kb/analysis/lineage.py` to bridge equations across documents in the scientific corpus. By combining `SymbolOntology` canonical concepts with SymPy symbolic manipulation and physical unit validation, the engine constructs directed derivation paths from micro-observables (such as pitch/bat velocity) to macroscopic statistics (such as run expectancy and WAR).

## Architecture & Data Flow

```
[Source Formula / Concept] (e.g. BAT_SPEED, PITCH_SPEED)
       │
       ▼ [SymbolOntology Canonical Concept Lookup]
[Collision Formula] (v_exit = q * v_pitch + (1 + e) * v_bat)
       │
       ▼ [SymPy Units Dimensional Check: [L/T] == [L/T]]
[Aerodynamic Trajectory Formula] (Distance = f(v_exit, launch_angle, spin))
       │
       ▼ [Linear Weights / RE24 Model]
[Delta RE Formula] (delta_RE = RE_end - RE_start + Runs)
       │
       ▼ [Win Expectancy & WAR Model]
[Target Metric: WAR] (WAR = Total Runs / Runs Per Win)
```

## Key Components

### 1. Multi-Hop Graph Search (`MultiHopChainingEngine`)
- Implemented in `src/kb/math/chaining.py`.
- Discovers directed paths in the formula corpus using Breadth-First Search (BFS) / Dijkstra search over canonical concept mappings.
- Each formula node exposes:
  - LHS defined symbol & associated `ConceptType`.
  - Free RHS symbols & associated `ConceptType` mappings.
- Edge creation condition: An edge exists from Formula $A$ to Formula $B$ if the canonical concept of $LHS(A)$ matches the canonical concept of an unresolved $RHS$ symbol in $B$.

### 2. Dimensional Invariant Checker (`DimensionalValidator`)
- Utilizes `sympy.physics.units` and `SymbolOntology` physical dimensions.
- Validates that when substituting variable $u$ with expression $E$, $[u] \equiv [E]$.
- Flags dimensionless ratios vs. dimensional quantities to prevent non-physical substitutions.

### 3. Closed-Form Recursive Substitution
- Recursively performs `expr.subs(substitutions)` while applying `sympy.simplify()`.
- Produces a single unified SymPy expression expressing the target metric exclusively in terms of primitive root observables.
- Generates LaTeX derivation steps for presentation in the UI and CLI.

### 4. CLI and GraphQL Interfaces
- CLI: `kb equations chain --from <concept_or_id> --to <concept_or_id> [--max-depth 5] [--json]`.
- GraphQL: Resolver `equationChain(fromConcept: String!, toConcept: String!): ChainedDerivationType`.
