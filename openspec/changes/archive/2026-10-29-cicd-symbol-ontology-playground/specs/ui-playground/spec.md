# Specification: Interactive Web UI Calculation Playground

## Scope & Purpose
Expands the web dashboard (`kb ui serve`) with an interactive calculation playground and visual simulation environment, while strictly guaranteeing backward compatibility and zero regressions for existing UI tabs and API routes.

## Requirements
1. **Interactive Playground Interface**:
   - MUST provide a dedicated "Playground" tab accessible in the main navigation.
   - MUST support both preset canonical formulas (e.g., Pythagorean Expectation, FIP, wOBA) and custom LaTeX / expression input.
   - MUST dynamically generate reactive parameter control sliders and numeric fields based on the input symbols required by the formula.
2. **Real-time Evaluation Integration**:
   - Parameter adjustments MUST trigger dynamic evaluations against the `/api/eval` backend endpoint.
   - Evaluation errors or invalid input combinations MUST display user-friendly error banners without crashing the web page or server.
3. **Sensitivity Curve Visualization**:
   - MUST provide interactive chart rendering (via Chart.js or HTML Canvas) displaying sensitivity curves (e.g. sweeping Runs Scored from 500 to 1000 while holding Runs Allowed constant to plot Win Expectancy).
4. **Preservation of Existing Functionality**:
   - Existing tabs (Lineage Graph, Formulas, Benchmark Tables, Hybrid Search) and their API routes MUST NOT experience any regressions or disruptions.
