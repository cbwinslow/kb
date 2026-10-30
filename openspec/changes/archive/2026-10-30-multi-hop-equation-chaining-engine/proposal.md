# Proposal: Multi-Hop Equation Chaining Engine

## Why
While `FormulaChainingEngine` performs single-step formula substitution within documents, scientific derivations frequently span multiple papers and cross disciplinary boundaries—from collision mechanics and aerodynamic flight trajectories to run expectancy and macroscopic value metrics (e.g., $v_{\text{pitch}}, v_{\text{bat}} \to v_{\text{exit}} \to \text{Trajectory}(x, y, z) \to \Delta RE \to \text{WAR}$). Researchers and quantitative modelers currently lack an automated multi-hop derivation engine that can discover full cross-paper DAGs, verify dimensional and physical invariants between connected nodes using SymPy units, and generate end-to-end closed-form equations bridging micro-observables to macroscopic metrics.

## What Changes
- **Multi-Hop Derivation Discovery**: Extends `FormulaChainingEngine` to discover directed derivation paths across disparate papers in PostgreSQL using `SymbolOntology` canonical concept matching.
- **Dimensional & Domain Invariant Verification**: Adds physical dimensional compatibility checks using `sympy.physics.units` to ensure variables chained across papers have compatible physical dimensions (e.g. velocity $[L T^{-1}]$, energy $[M L^2 T^{-2}]$, dimensionless ratios).
- **End-to-End AST Composition & Simplification**: Recursively composes upstream equations into downstream target equations, generating unified closed-form SymPy ASTs, LaTeX derivations, and substitution step traces.
- **CLI & Query API**: Introduces `kb equations chain --from <concept/id> --to <concept/id> [--max-depth <d>]` and exposes `equationChain(sourceId, targetId)` resolver in Strawberry GraphQL.

## Capabilities

### Modified Capabilities
- `equation-chaining`: Adds cross-paper multi-hop derivation graph resolution, dimensional unit compatibility verification, and end-to-end closed-form equation compilation.
- `lineage-graph`: Extends derivation edge inference to trace canonical parameter lineages and multi-step substitution trajectories across distinct scientific papers.

## Impact
- **Modules**: Extends `src/kb/math/chaining.py` and `src/kb/analysis/lineage.py`.
- **CLI**: Expands `src/kb/cli.py` with multi-hop chaining arguments.
- **GraphQL**: Adds `ChainedDerivationGraph` and `equationChain` query in `src/kb/graphql/schema.py`.
- **Dependencies**: SymPy units (`sympy.physics.units`). Zero external runtime dependencies added.
