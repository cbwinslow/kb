# Design: Interactive Quality Dashboard & 1-Click Formula Repair UI

## Overview
This change adds a comprehensive Quality Gate inspection and interactive repair interface to the Starlette web dashboard (`kb ui serve`). Researchers can view corpus quality yields (Grades A through F), filter formulas, inspect exact Tier 1–4 failures, and trigger automatic sanitization and AST recovery with one click.

## Architecture & Data Flow

```
[Web Browser Client]
       │
       ├── GET /api/formulas?grade=A,B&status=verified ──► [Filterable Scorecard View]
       │                                                         │
       │                                                         ▼
       │                                              [Detailed Diagnostic Drawer]
       │                                              - Tier 1: AST Invertibility (25/25)
       │                                              - Tier 2: Tokenization & Dimensions (25/25)
       │                                              - Tier 3: Boundary Monotonicity (25/25)
       │                                              - Tier 4: Empirical Accuracy (25/25)
       │
       └── POST /api/formulas/{id}/repair 
              │
              ▼ [CorpusFormulaRepairer Pipeline]
              - Stage 1-5 Unicode Sanitizer
              - Multi-letter acronym tokenization
              │
              ▼ [FormulaQualityGate Evaluation]
              - Real-time Tier 1-4 re-scoring
              │
              ▼ [Update PostgreSQL kb_formulas]
              - validation_score, validation_status, validation_details
              │
              └──► Returns Updated Scorecard JSON to Client (Instant DOM Badge Update)
```

## Key Components

### 1. Quality & Scorecard UI View (`src/kb/ui/app.py`, HTML templates)
- Adds a "Quality Gate" navigation tab.
- Summarizes corpus statistics:
  - Total formulas, valid SymPy count, mean score, Grade distribution histogram.
- Interactive filter controls:
  - Letter grade pills: `A` (90-100), `B` (80-89), `C` (70-79), `D` (60-69), `F` (<60).
  - Status pills: `verified`, `provisional`, `degraded`, `failed`.
  - Search bar filtering by symbol or citekey.

### 2. Diagnostic Inspection Drawer
- Slide-out or expandable drawer for every formula card:
  - Tier 1 (Round-trip invertibility): Displays re-parsed LaTeX and symbol comparison.
  - Tier 2 (Symbol tokenization): Highlights multi-letter acronym splittings and undefined variables.
  - Tier 3 (Monotonicity & bounds): Displays analytical derivative signs and domain testing intervals.
  - Tier 4 (Empirical benchmark): Displays MAE, RMSE, and associated table ID.

### 3. Real-Time Repair Endpoint (`/api/formulas/{id}/repair`)
- Route: `POST /api/formulas/{id}/repair`.
- Loads target formula from database.
- Runs `CorpusFormulaRepairer.repair_formula(raw_latex)`.
- If repair succeeds, runs `FormulaQualityGate.evaluate_formula(repaired_formula)`.
- Commits updated AST, LaTeX, score, status, and details to database.
- Returns updated `FormulaQualityScorecard` as JSON.
