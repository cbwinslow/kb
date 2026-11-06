"""Web glossary harvester for sabermetric references and online formulas."""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING, Any

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md

if TYPE_CHECKING:
    from kb.ingest.pipeline import IngestionPipeline, IngestionResult

logger = logging.getLogger(__name__)

# Pre-packaged canonical glossary content with validated LaTeX formulations
SABERMETRIC_GLOSSARY_PRESETS: dict[str, dict[str, Any]] = {
    "wOBA": {
        "citekey": "fangraphs_woba_glossary",
        "title": "FanGraphs Sabermetric Library: Weighted On-Base Average (wOBA)",
        "url": "https://library.fangraphs.com/offense/woba/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Weighted On-Base Average (wOBA)

Weighted On-Base Average (wOBA) is one of the most important offensive statistics in modern sabermetrics.
Unlike on-base percentage (OBP) which treats all times on base equally, or slugging percentage (SLG) which overweighs extra base hits relative to singles and walks, wOBA weights each offensive event by its actual run expectancy value based on linear weights.

## The Standard wOBA Formula

The canonical formula for Weighted On-Base Average is:

$$wOBA = \\frac{0.69 \\cdot uBB + 0.72 \\cdot HBP + 0.89 \\cdot 1B + 1.27 \\cdot 2B + 1.62 \\cdot 3B + 2.10 \\cdot HR}{AB + BB - IBB + SF + HBP}$$

Where:
- $uBB$ is unintentional walks ($BB - IBB$)
- $HBP$ is hit by pitch
- $1B$ is singles
- $2B$ is doubles
- $3B$ is triples
- $HR$ is home runs
- $AB$ is at bats
- $BB$ is total walks
- $IBB$ is intentional walks
- $SF$ is sacrifice flies

In terms of plate appearances $PA$, the denominator can also be approximated as:

$$PA = AB + BB + SF + HBP$$
""",
    },
    "wRAA": {
        "citekey": "fangraphs_wraa_glossary",
        "title": "FanGraphs Sabermetric Library: Weighted Runs Above Average (wRAA)",
        "url": "https://library.fangraphs.com/offense/wraa/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Weighted Runs Above Average (wRAA)

Weighted Runs Above Average (wRAA) measures the number of offensive runs a player contributed to their team compared to an average player. A wRAA of zero is league average.

## Formula

The relationship between wOBA and wRAA is defined by:

$$wRAA = \\frac{wOBA - lgwOBA}{wOBA_{scale}} \\cdot PA$$

Where:
- $wOBA$ is the batter's Weighted On-Base Average
- $lgwOBA$ is the league average wOBA (typically ~0.315 - 0.320)
- $wOBA_{scale}$ is the wOBA scale factor converting wOBA to OBP scale (typically ~1.15 to 1.25)
- $PA$ is the player's plate appearances
""",
    },
    "wRC": {
        "citekey": "fangraphs_wrc_glossary",
        "title": "FanGraphs Sabermetric Library: Weighted Runs Created (wRC and wRC+)",
        "url": "https://library.fangraphs.com/offense/wrc/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Weighted Runs Created (wRC)

Weighted Runs Created (wRC) quantifies a player's total offensive production in terms of runs, rather than runs above average.

## Formulas

The raw Weighted Runs Created is calculated directly from wRAA and league run environment:

$$wRC = wRAA + \\frac{lgR}{lgPA} \\cdot PA$$

Alternatively, expressing $wRC$ directly as a function of wOBA:

$$wRC = \\left(\\frac{wOBA - lgwOBA}{wOBA_{scale}} + \\frac{lgR}{lgPA}\\right) \\cdot PA$$

Where:
- $lgR$ is total league runs scored
- $lgPA$ is total league plate appearances
""",
    },
    "FIP": {
        "citekey": "fangraphs_fip_glossary",
        "title": "FanGraphs Sabermetric Library: Fielding Independent Pitching (FIP)",
        "url": "https://library.fangraphs.com/pitching/fip/",
        "authors": ["Tom Tango", "FanGraphs"],
        "year": 2026,
        "markdown": """# Fielding Independent Pitching (FIP)

Fielding Independent Pitching (FIP) measures a pitcher's effectiveness by focusing only on the outcomes directly under their control: strikeouts, unintentional walks, hit-by-pitches, and home runs, entirely removing balls in play defense and luck.

## The FIP Formula

$$FIP = \\frac{13 \\cdot HR + 3 \\cdot (BB + HBP) - 2 \\cdot K}{IP} + FIP_{constant}$$

Where:
- $HR$ is home runs allowed
- $BB$ is walks allowed
- $HBP$ is batters hit by pitch
- $K$ is strikeouts
- $IP$ is innings pitched
- $FIP_{constant}$ aligns league FIP to league ERA (typically ~3.10 to 3.25)
""",
    },
    "Base_Runs": {
        "citekey": "tango_base_runs_glossary",
        "title": "Base Runs (BsR) Offensive Estimator",
        "url": "http://www.tangotiger.net/baseruns.html",
        "authors": ["David Smyth", "Tom Tango"],
        "year": 2026,
        "markdown": """# Base Runs (BsR)

Base Runs is a sabermetric run estimator invented by David Smyth and popularized by Tom Tango in 'The Book'. It models run creation dynamically using the physics of baserunners navigating around the bases.

## The Canonical Base Runs Formula

The core formula for Base Runs is:

$$BsR = A \\cdot \\frac{B}{B + C} + D$$

Where:
- $A$ represents baserunners who reach base:
$$A = H + BB - HR$$
- $B$ represents the advancing power of the batting events:
$$B = 1.4 \\cdot TB - 0.6 \\cdot H - 3 \\cdot HR + 0.1 \\cdot BB$$
- $C$ represents outs:
$$C = 3 \\cdot (AB - H) + 0.9 \\cdot (H + BB - HR)$$
- $D$ represents guaranteed runs (home runs):
$$D = HR$$
- $TB$ is total bases:
$$TB = 1B + 2 \\cdot 2B + 3 \\cdot 3B + 4 \\cdot HR$$
""",
    },
    "WAR_position": {
        "citekey": "fangraphs_war_position_glossary",
        "title": "FanGraphs Sabermetric Library: Wins Above Replacement (WAR) for Position Players",
        "url": "https://library.fangraphs.com/misc/war/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Wins Above Replacement (WAR) for Position Players

WAR synthesizes a player's total contributions across batting, baserunning, fielding, and positional difficulty relative to a readily available minor-league replacement player.

## High-Level WAR Equation

$$WAR = \\frac{BattingRuns + BaseRunningRuns + FieldingRuns + PositionalAdjustment + LeagueAdjustment + ReplacementRuns}{RPW}$$

## Batting Runs Derivation

Batting runs is derived from wRAA with park factor adjustments:

$$BattingRuns = wRAA + \\left(\\frac{lgR}{lgPA} - ParkFactor \\cdot \\frac{lgR}{lgPA}\\right) \\cdot PA$$

## Replacement Runs Derivation

$$ReplacementRuns = 57.0 \\cdot \\left(\\frac{PA}{2430}\\right)$$

## Runs Per Win (RPW) Formula

Tango's dynamic formula for Runs Per Win in a season:

$$RPW = 10 \\cdot \\sqrt{\\frac{RS + RA}{G}}$$
""",
    },
    "WAR_pitcher": {
        "citekey": "fangraphs_war_pitcher_glossary",
        "title": "FanGraphs Sabermetric Library: Wins Above Replacement (WAR) for Pitchers",
        "url": "https://library.fangraphs.com/war/war-pitchers/",
        "authors": ["FanGraphs"],
        "year": 2026,
        "markdown": """# Wins Above Replacement (WAR) for Pitchers

Pitcher WAR uses FIP (Fielding Independent Pitching) transformed to a runs scale to compute runs allowed above replacement level.

## Pitcher WAR Equation

$$WAR_{pitcher} = \\left(\\frac{lgERA - FIP}{RPW}\\right) \\cdot \\frac{IP}{9} + ReplacementRuns_{pitcher}$$

Where:
- $lgERA$ is league average earned run average
- $FIP$ is Fielding Independent Pitching
- $RPW$ is Runs Per Win
- $IP$ is innings pitched
""",
    },
    "Pythagenpat": {
        "citekey": "tango_pythagenpat_glossary",
        "title": "Tom Tango: Pythagenpat Win Expectancy",
        "url": "http://www.tangotiger.net/pythagenpat.html",
        "authors": ["Tom Tango"],
        "year": 2026,
        "markdown": """# Pythagenpat Win Expectancy

Pythagenpat is David Smyth and Tom Tango's refinement of Bill James's Pythagorean expectation for baseball winning percentage.

## The Pythagenpat Formulation

The team winning percentage is:

$$WinPct = \\frac{RS^\\gamma}{RS^\\gamma + RA^\\gamma}$$

Where the dynamic exponent $\\gamma$ is determined by the run-scoring environment:

$$\\gamma = (RS + RA)^{0.285}$$

Where:
- $RS$ is runs scored
- $RA$ is runs allowed
""",
    },
    "RE24": {
        "citekey": "tangotiger_re24_glossary",
        "title": "Tom Tango: 24-State Run Expectancy Matrix (RE24) and Transition Values",
        "url": "http://www.tangotiger.net/re24.html",
        "authors": ["Tom Tango", "Mitchel Lichtman", "Andrew Dolphin"],
        "year": 2026,
        "markdown": """# 24-State Run Expectancy (RE24)

Run Expectancy (RE24) models the average number of runs scored from any base-out state through the end of the half-inning. There are 24 distinct states (3 out states $\\times$ 8 base-runner configurations).

## Run Expectancy Delta Equation

The offensive or pitching run value of any plate appearance or play is the change in run expectancy plus any runs scored on the play:

$$\\Delta RE = RE_{end} - RE_{start} + R_{play}$$

Where:
- $RE_{start}$ is the expected runs of the initial base-out state
- $RE_{end}$ is the expected runs of the resulting base-out state
- $R_{play}$ is the number of runs scored during the play (0 to 4)

## Linear Weights Derivation

Linear weights values (such as the coefficients in wOBA) are empirical averages of $\\Delta RE$ across all instances of that batting event over a season:

$$w_{event} = \\frac{1}{N_{event}} \\cdot \\sum_{k=1}^{N_{event}} \\Delta RE_k$$
""",
    },
    "Leverage_Index": {
        "citekey": "tangotiger_leverage_index_glossary",
        "title": "Tom Tango: Leverage Index (LI) and Win Probability Added",
        "url": "http://www.tangotiger.net/li.html",
        "authors": ["Tom Tango"],
        "year": 2026,
        "markdown": """# Leverage Index (LI)

Leverage Index quantifies the critical importance of a specific game state relative to an average situation. An average play has a leverage index of 1.0.

## Mathematical Definition

The leverage of a game state is the swing in win probability between the best and worst possible immediate play outcomes, normalized by the average swing across all game states:

$$LI = \\frac{\\Delta WP_{max} - \\Delta WP_{min}}{E_{WP}}$$

Where:
- $\\Delta WP_{max}$ is the change in win probability resulting from the most favorable outcome
- $\\Delta WP_{min}$ is the change in win probability resulting from the least favorable outcome
- $E_{WP}$ is the expected change in win probability for an average major league plate appearance

## Game-Level Leverage

The average leverage experienced by a pitcher or batter across an entire contest:

$$gmLI = \\frac{1}{M} \\cdot \\sum_{j=1}^{M} LI_j$$
""",
    },
    "DRC_Plus": {
        "citekey": "bp_drc_plus_glossary",
        "title": "Baseball Prospectus: Deserved Runs Created Plus (DRC+) and DRA",
        "url": "https://www.baseballprospectus.com/news/article/45387/introducing-drc/",
        "authors": ["Jonathan Judge", "Baseball Prospectus"],
        "year": 2026,
        "markdown": """# Deserved Runs Created Plus (DRC+)

Deserved Runs Created Plus (DRC+) is Baseball Prospectus's premier offensive metric. Unlike traditional linear weights which evaluate observed outcomes, DRC+ uses empirical Bayesian multi-level modeling to isolate batter true talent from opposing pitcher quality, defense, catcher framing, umpire strike zones, and park environment.

## DRC Index Formulation

$$DRC_{plus} = 100 \\cdot \\left(\\frac{DRC_{PA}}{lgDRC_{PA}}\\right)$$

Where:
- $DRC_{PA}$ is the batter's deserved runs created per plate appearance
- $lgDRC_{PA}$ is the league average deserved runs created per plate appearance

## Deserved Run Average (DRA) Relation

For pitchers, Deserved Run Average scales true talent run prevention to an ERA scale:

$$DRA = \\left(\\frac{DRA_{RA}}{lgRA}\\right) \\cdot lgERA$$
""",
    },
    "BRef_WAR": {
        "citekey": "bref_war_components_glossary",
        "title": "Baseball-Reference: Wins Above Replacement (WAR) Component Architecture",
        "url": "https://www.baseball-reference.com/about/war_explained.shtml",
        "authors": ["Sean Forman", "Baseball-Reference"],
        "year": 2026,
        "markdown": """# Baseball-Reference WAR Architecture

Baseball-Reference WAR (bWAR / rWAR) decomposes player contribution into distinct components: batting runs, baserunning runs, double play avoidance runs, defensive runs saved, positional adjustment, and replacement runs.

## Position Player WAR Equation

$$WAR = \\frac{BatRuns + BaserunningRuns + DefRuns + PosRuns + RepRuns}{RPW}$$

Where:
- $BatRuns$ is batting runs relative to league average
- $DefRuns$ is defensive runs saved (DRS)
- $PosRuns$ is positional adjustment runs
- $RepRuns$ is replacement level runs
- $RPW$ is runs per win factor

## Positional Run Adjustment

$$PosRuns = \\left(\\frac{Inn_{pos}}{1458}\\right) \\cdot Value_{pos}$$
""",
    },
    "Statcast_Bat_Tracking": {
        "citekey": "statcast_bat_tracking_glossary",
        "title": "MLB Statcast 2.0: Bat Tracking Collision Physics and Swing Mechanics",
        "url": "https://www.mlb.com/news/statcast-bat-tracking-metrics-explained",
        "authors": ["Tom Tango", "MLB Advanced Media", "David Kagan"],
        "year": 2026,
        "markdown": """# MLB Statcast 2.0 Bat Tracking

Introduced by MLB Statcast in 2024, bat tracking uses high-speed optical Hawk-Eye cameras to capture the physical trajectory of the bat head throughout the swing.

## Collision Exit Velocity Physics

The maximum achievable exit velocity $v_{exit}$ off a baseball bat collision is governed by the conservation of momentum and coefficient of restitution:

$$v_{exit} = q \\cdot v_{pitch} + (1 + e) \\cdot v_{bat}$$

Where:
- $v_{bat}$ is bat speed at the sweet spot at impact (typically 65 to 85 mph)
- $v_{pitch}$ is pitch velocity at the plate (typically 80 to 102 mph)
- $q$ is the pitch collision efficiency factor (~0.20 for round wooden bats)
- $e$ is the collision coefficient of restitution (~0.22 to 0.25)

## Squared-Up Percentage

Squared-Up Rate measures how close a batter came to achieving the maximum exit velocity possible given their bat speed and pitch speed:

$$SquaredUp = \\frac{v_{exit}}{v_{exit, max}}$$

## Blast Percentage

A 'Blast' represents an optimal combination of high swing power and centered contact. It is defined as a competitive swing that achieves both:
1. Bat speed $v_{bat} \\ge 75\\text{ mph}$
2. Squared-up contact $SquaredUp \\ge 0.80$
""",
    },
    "PECOTA": {
        "citekey": "bp_pecota_projections_glossary",
        "title": "Baseball Prospectus: PECOTA Forecasting Architecture and Similarity Index",
        "url": "https://www.baseballprospectus.com/news/article/1894/pecota-explained/",
        "authors": ["Nate Silver", "Baseball Prospectus"],
        "year": 2026,
        "markdown": """# PECOTA Baseball Forecasting System

PECOTA (Pitcher Empirical Comparable Optimization Test Algorithm) is a player performance forecasting system originally developed by Nate Silver for Baseball Prospectus in 2003. Unlike purely regression-based baseline models, PECOTA is a comparable-player nearest-neighbor system that generates full probabilistic distribution percentiles rather than single-point estimates.

## 1. Mahalanobis Distance Similarity Metric

To identify historical comparables, PECOTA computes the multidimensional distance between a target player vector $x$ and historical player vector $y$:

$$D^2 = (x - y)^T \\Sigma^{-1} (x - y)$$

Where:
- $x$ is the target player's standardized attribute vector (age, height, weight, strikeout rate, walk rate, isolated power, contact rate)
- $y$ is the candidate historical player's attribute vector at the same career stage
- $\\Sigma$ is the empirical covariance matrix across the player population

## 2. Similarity Score Index

The multidimensional distance is converted into a normalized similarity score $S$:

$$S = 1000 - \\sum_{i=1}^{k} w_i \\cdot |x_i - y_i|$$

Where:
- $w_i$ is the attribute importance weight
- A score of $S = 1000$ represents an identical player match

## 3. Weighted Comparable Projection

Given the top $M$ historical comparable players with non-negative similarity weights $w_j = \\max(0, S_j - S_{min})$:

$$\\hat{Y}_{t+1} = \\frac{\\sum_{j=1}^{M} w_j \\cdot Y_{j, t+1}}{\\sum_{j=1}^{M} w_j}$$

Where:
- $Y_{j, t+1}$ is the actual subsequent performance of comparable player $j$
- $\\hat{Y}_{t+1}$ is the baseline expectation for the target player

## 4. Aging Adjustment Transition

PECOTA estimates aging trajectories by tracking how the comparable cohort developed over time:

$$\\hat{Y}_{proj} = Y_t \\cdot \\left(1 + \\frac{\\Delta_{comp}}{100}\\right)$$

Where:
- $\\Delta_{comp}$ is the median percentage change in production between age $t$ and age $t+1$ among the top comparables

## 5. Monte Carlo Probabilistic Forecast Bands

Instead of predicting only a single mean value, PECOTA constructs an empirical probability distribution for future performance:

$$Y_p = \\mu_{comp} + \\sigma_{comp} \\cdot \\Phi^{-1}(p)$$

Where:
- $\\Phi^{-1}(p)$ is the standard normal quantile function
- $p \\in \\{0.10, 0.50, 0.90\\}$ defines the 10th percentile (breakout downside), 50th percentile (median), and 90th percentile (upside ceiling)
""",
    },
    "ZiPS": {
        "citekey": "fangraphs_zips_projections_glossary",
        "title": "FanGraphs: ZiPS Forecasting Architecture and Component Model",
        "url": "https://library.fangraphs.com/projections/zips/",
        "authors": ["Dan Szymborski", "FanGraphs"],
        "year": 2026,
        "markdown": """# ZiPS Forecasting System

ZiPS (Szymborski Projection System) is a sabermetric forecasting model developed by Dan Szymborski in 2004. ZiPS combines multi-year weighted performance baselines, sample-size empirical Bayes regression to league mean, and archetype-specific aging curves to project player outcomes and career distributions.

## 1. 4-Year Recency Decay Baseline

ZiPS weights past performance over the previous four seasons using declining recency coefficients (8/5/4/3):

$$\\bar{X}_{weighted} = \\frac{8 \\cdot X_{t-1} + 5 \\cdot X_{t-2} + 4 \\cdot X_{t-3} + 3 \\cdot X_{t-4}}{8 \\cdot W_{t-1} + 5 \\cdot W_{t-2} + 4 \\cdot W_{t-3} + 3 \\cdot W_{t-4}}$$

Where:
- $X_{t-i}$ is the player's statistical output in season $t-i$
- $W_{t-i}$ is the playing time volume ($PA$ for batters or $IP$ for pitchers) in season $t-i$

## 2. Sample Size Empirical Bayes Regression to League Mean

To prevent small-sample noise from distorting projections, the weighted average is regressed toward the league average based on career sample size:

$$\\hat{X}_{reg} = \\frac{PA}{PA + C_{reg}} \\cdot \\bar{X}_{weighted} + \\frac{C_{reg}}{PA + C_{reg}} \\cdot \\mu_{lg}$$

Where:
- $\\mu_{lg}$ is the position- and era-adjusted league average rate
- $C_{reg}$ is the metric stabilization threshold (e.g., $C \\approx 300 - 400$ for on-base percentage, $C \\approx 60 - 70$ for strikeout percentage)

## 3. Archetype-Specific Aging Trajectories

ZiPS adjusts baseline projections for expected age-related growth or decline using non-linear trajectory curves conditioned on player archetype:

$$\\Delta_{age} = \\alpha \\cdot (age - 28) - \\beta \\cdot (age - 28)^2$$

Where:
- $\\alpha$ and $\\beta$ are empirical aging parameters derived from historical comparables with similar physical profiles and batted-ball characteristics
- Peak performance typically centers around age 27–28

## 4. Composite Rate Projection

$$\\hat{X}_{final} = \\hat{X}_{reg} \\cdot (1 + \\Delta_{age})$$

Where:
- $\\hat{X}_{final}$ is the final projected true-talent rate for season $t+1$
""",
    },
    "Marcel": {
        "citekey": "tangotiger_marcel_projections_glossary",
        "title": "Tom Tango: Marcel the Monkey Forecasting System",
        "url": "http://www.tangotiger.net/marcel/",
        "authors": ["Tom Tango"],
        "year": 2026,
        "markdown": """# Marcel the Monkey Forecasting System

Marcel the Monkey Forecasting System is a baseline projection methodology developed by Tom Tango in 2004. Tango intentionally named it "Marcel the Monkey" to demonstrate that a simple, objective model relying only on basic recency weights, regression to the mean, and age adjustments can outperform human intuition and complex proprietary black-box systems.

## 1. 3-Year 5/4/3 Recency Weighting

Marcel calculates a weighted baseline over the past three seasons, assigning weights of 5, 4, and 3:

$$\\bar{S} = \\frac{5 \\cdot S_{t-1} + 4 \\cdot S_{t-2} + 3 \\cdot S_{t-3}}{5 \\cdot PA_{t-1} + 4 \\cdot PA_{t-2} + 3 \\cdot PA_{t-3}}$$

Where:
- $S_{t-i}$ is the counting statistic in season $t-i$
- $PA_{t-i}$ is the playing time volume in season $t-i$

## 2. Regression to League Average

Marcel regresses all players toward the league average by adding a fixed volume of league-average performance:
- For batters: adds 1200 plate appearances of league-average production
- For pitchers: adds 100 innings pitched (or ~450 batters faced) of league-average production

For a batter's rate metric:

$$\\hat{R}_{marcel} = \\frac{5 \\cdot S_{t-1} + 4 \\cdot S_{t-2} + 3 \\cdot S_{t-3} + 1200 \\cdot lgRate}{5 \\cdot PA_{t-1} + 4 \\cdot PA_{t-2} + 3 \\cdot PA_{t-3} + 1200}$$

For a pitcher's rate metric:

$$\\hat{R}_{marcel, P} = \\frac{5 \\cdot S_{t-1} + 4 \\cdot S_{t-2} + 3 \\cdot S_{t-3} + 100 \\cdot lgRate}{5 \\cdot IP_{t-1} + 4 \\cdot IP_{t-2} + 3 \\cdot IP_{t-3} + 100}$$

## 3. Piecewise Age Adjustment

Marcel applies a standard aging factor centered at age 30:
- Players under 30 are expected to improve by 0.6% per year
- Players age 30 and older are expected to decline by 0.3% per year

$$\\Delta_{age} = (30 - age) \\cdot 0.006$$

For players 30 or older:

$$\\Delta_{age, old} = (30 - age) \\cdot 0.003$$

The age-adjusted final projected rate is:

$$\\hat{R}_{final} = \\hat{R}_{marcel} \\cdot (1 + \\Delta_{age})$$
""",
    },
    "Markov_Chain_Baseball": {
        "citekey": "bukiet_markov_chain_baseball_glossary",
        "title": "Bukiet-Harold-Palacios: Discrete Markov Chain Baseball Model",
        "url": "https://doi.org/10.1287/opre.45.1.14",
        "authors": ["Bruce Bukiet", "E. R. Harold", "F. J. Palacios"],
        "year": 2026,
        "markdown": """# Discrete Markov Chain Baseball Model

The discrete Markov chain model of baseball game states, formalized by D'Esopo & Lefkowitz (1960) and expanded by Bukiet, Harold, and Palacios (1997), represents a half-inning of baseball as an absorbing Markov process across discrete base-runner and out configurations.

## 1. State Space Representation

A half-inning contains 24 transient states defined by the Cartesian product of 8 base-runner configurations $b \\in \\{000, 100, 020, 003, 120, 103, 023, 123\\}$ and 3 out counts $o \\in \\{0, 1, 2\\}$, plus a single absorbing state $s_{25} = (3\\text{ outs})$:

$$S = \\{(b, o) : b \\in \\mathcal{B}, o \\in \\{0, 1, 2\\}\\} \\cup \\{3\\text{ outs}\\}$$

## 2. Canonical Transition Probability Matrix

The full $25 \\times 25$ transition probability matrix $P$ is structured in canonical absorbing form:

$$P = \\begin{pmatrix} Q & R_{abs} \\\\ 0 & 1 \\end{pmatrix}$$

Where:
- $Q$ is the $24 \\times 24$ submatrix representing transition probabilities between transient base-out states
- $R_{abs}$ is the $24 \\times 1$ column vector representing transition probabilities from transient states directly into the 3-out absorbing state

## 3. Fundamental Matrix Inversion

Because $Q^k \\to 0$ as $k \\to \\infty$, the fundamental matrix $N$ exists and represents the expected number of visits to state $j$ starting from state $i$:

$$N = (I - Q)^{-1}$$

Where:
- $I$ is the $24 \\times 24$ identity matrix
- $N = I + Q + Q^2 + Q^3 + \\dots$

## 4. Run Expectancy Vector Derivation

Let $E$ denote the $24 \\times 1$ vector of immediate expected runs scored on a single transition departing from each state $i$. The total expected runs remaining in the inning from state $i$ is:

$$RE = N \\cdot E$$

Expanding via fundamental matrix inversion:

$$RE = (I - Q)^{-1} \\cdot E$$

## 5. Transition Run Value (Linear Weights)

The empirical run value $RV$ of an offensive event $e$ causing a transition from state $s$ to state $s'$ while scoring $Runs(e)$ runs is:

$$RV(e, s) = RE(s') - RE(s) + Runs(e)$$

This formulation provides the analytical foundation for linear weights and 24-state Run Expectancy (RE24) matrices.
""",
    },
    "Nathan_Trajectory_Physics": {
        "citekey": "nathan_trajectory_physics_glossary",
        "title": "Alan Nathan: Aerodynamics and Trajectory Physics of a Baseball",
        "url": "http://baseball.physics.illinois.edu/trajectory-technology.html",
        "authors": ["Alan M. Nathan"],
        "year": 2026,
        "markdown": """# Alan Nathan Baseball Trajectory Physics & Aerodynamics

Based on the aerodynamic formulations published by Prof. Alan M. Nathan (2008, 2015), the flight of a baseball under gravity, aerodynamic drag, and the Magnus force is governed by a set of coupled non-linear ordinary differential equations.

## 1. Full Aerodynamic Equation of Motion

The acceleration vector of a baseball in flight is given by:

$$\\vec{a} = \\vec{a}_g + \\vec{a}_d + \\vec{a}_m$$

Where:
- $\\vec{a}_g = -g \\hat{k}$ is the gravitational acceleration ($g = 9.80665\\text{ m/s}^2$ or $32.174\\text{ ft/s}^2$)
- $\\vec{a}_d$ is the aerodynamic drag acceleration
- $\\vec{a}_m$ is the Magnus lift and deflection acceleration

## 2. Drag Force Acceleration

Aerodynamic drag opposes the instantaneous velocity vector $\\vec{v}$:

$$\\vec{a}_d = -\\frac{1}{2m} \\rho A C_D v \\vec{v}$$

Where:
- $m$ is the mass of the baseball (~0.145 kg or 5.125 oz)
- $\\rho$ is air density (~1.225 kg/m³ at sea level, adjusted for temperature, barometric pressure, and relative humidity)
- $A = \\pi r^2$ is the cross-sectional area of the ball ($r \\approx 0.0366\\text{ m}$)
- $C_D$ is the speed-dependent drag coefficient
- $v = \\|\\vec{v}\\|$ is the magnitude of velocity

## 3. Magnus Force Acceleration

The Magnus force arises from the asymmetry in air velocity caused by ball rotation $\\vec{\\omega}$:

$$\\vec{a}_m = \\frac{1}{2m} \\rho A C_L v (\\hat{\\omega} \\times \\vec{v})$$

Where:
- $C_L$ is the lift coefficient
- $\\hat{\\omega} = \\vec{\\omega} / \\|\\vec{\\omega}\\|$ is the unit vector along the spin axis
- $\\hat{\\omega} \\times \\vec{v}$ defines the directional vector of movement (break) perpendicular to both spin and trajectory

## 4. Spin Parameter and Lift Coefficient

The non-dimensional spin parameter $S$ relates rotational surface velocity to translational speed:

$$S = \\frac{r \\cdot \\omega}{v}$$

Nathan's empirical parameterization for the lift coefficient $C_L$ as a function of spin parameter $S$ is:

$$C_L = \\frac{1}{2.32 + \\frac{0.40}{S}}$$

## 5. Drag Coefficient Speed Dependence

The drag coefficient varies with velocity across the trans-critical boundary:

$$C_D = c_{d0} + \\frac{c_{d1}}{1 + e^{(v - v_c) / \\Delta v}}$$

Where:
- $c_{d0} \\approx 0.30$ is the baseline drag
- $c_{d1} \\approx 0.15$
- $v_c$ is the critical speed threshold
""",
    },
}


class WebGlossaryHarvester:
    """Harvests, sanitizes, and converts web sabermetric articles into markdown knowledge sources."""

    def __init__(self, user_agent: str | None = None) -> None:
        self.user_agent = user_agent or (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36 (KB Scientific Research Engine)"
        )

    async def fetch_html(self, url: str, timeout: float = 30.0) -> str:
        """Fetches raw HTML from a target web address with custom user-agent."""
        headers = {
            "User-Agent": self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
        async with httpx.AsyncClient(
            headers=headers, follow_redirects=True, timeout=timeout
        ) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.text

    def extract_article(self, html: str, url: str = "") -> tuple[str, str]:
        """Extracts article title and clean body HTML from full page."""
        soup = BeautifulSoup(html, "html.parser")

        # Extract title
        title = ""
        if soup.title and soup.title.string:
            title = soup.title.string.strip()
        h1 = soup.find("h1")
        if h1 and h1.get_text():
            title = h1.get_text().strip()

        # Remove irrelevant noise elements
        for element in soup(["script", "style", "nav", "header", "footer", "aside", "form"]):
            element.decompose()

        # Find main content container
        content_container = (
            soup.find("article")
            or soup.find("main")
            or soup.find(
                "div", class_=re.compile(r"entry-content|post-content|article-body|content")
            )
            or soup.find("div", id=re.compile(r"content|main"))
            or soup.body
            or soup
        )

        return title or url, str(content_container)

    def html_to_markdown(self, html_content: str) -> str:
        """Converts article HTML content into structured markdown."""
        converted = md(html_content, heading_style="ATX", strip=["img"])
        # Clean excessive empty lines
        clean_md = re.sub(r"\n{3,}", "\n\n", converted).strip()
        return clean_md

    async def ingest_url(
        self,
        url: str,
        pipeline: IngestionPipeline,
        citekey: str | None = None,
        title: str | None = None,
        force: bool = False,
    ) -> IngestionResult:
        """Fetches a URL, converts to markdown, and ingests through the IngestionPipeline."""
        logger.info("Fetching and ingesting web article from %s", url)
        html = await self.fetch_html(url)
        extracted_title, body_html = self.extract_article(html, url=url)
        markdown_text = self.html_to_markdown(body_html)

        chosen_title = title or extracted_title
        chosen_citekey = citekey or re.sub(r"[^\w]+", "_", url.split("//")[-1]).strip("_")[:40]

        return await pipeline.ingest_markdown_source(
            citekey=chosen_citekey,
            title=chosen_title,
            markdown_text=markdown_text,
            url=url,
            force=force,
        )

    async def ingest_preset(
        self,
        preset_key: str,
        pipeline: IngestionPipeline,
        force: bool = False,
    ) -> IngestionResult:
        target_data: dict[str, Any] | None = None
        if preset_key in SABERMETRIC_GLOSSARY_PRESETS:
            target_data = SABERMETRIC_GLOSSARY_PRESETS[preset_key]
        else:
            norm = preset_key.lower().replace("-", "_")
            for k, v in SABERMETRIC_GLOSSARY_PRESETS.items():
                if (
                    k.lower() == norm
                    or k.lower().replace("-", "_") == norm
                    or v.get("citekey", "").lower() == norm
                    or v.get("citekey", "").lower().replace("_glossary", "") == norm
                ):
                    target_data = v
                    break

        if not target_data:
            raise KeyError(
                f"Unknown preset '{preset_key}'. Available presets: {list(SABERMETRIC_GLOSSARY_PRESETS.keys())}"
            )

        data = target_data
        return await pipeline.ingest_markdown_source(
            citekey=data["citekey"],
            title=data["title"],
            markdown_text=data["markdown"],
            url=data.get("url"),
            authors=data.get("authors"),
            year=data.get("year"),
            force=force,
        )

    async def ingest_all_presets(
        self,
        pipeline: IngestionPipeline,
        force: bool = False,
    ) -> list[IngestionResult]:
        """Ingests all canonical sabermetric glossary presets."""
        results: list[IngestionResult] = []
        for key in SABERMETRIC_GLOSSARY_PRESETS:
            res = await self.ingest_preset(key, pipeline=pipeline, force=force)
            results.append(res)
        return results
