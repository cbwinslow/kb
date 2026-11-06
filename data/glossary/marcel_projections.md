# Marcel the Monkey Forecasting System

Marcel the Monkey Forecasting System is a baseline projection methodology developed by Tom Tango in 2004. Tango intentionally named it "Marcel the Monkey" to demonstrate that a simple, objective model relying only on basic recency weights, regression to the mean, and age adjustments can outperform human intuition and complex proprietary black-box systems.

## 1. 3-Year 5/4/3 Recency Weighting

Marcel calculates a weighted baseline over the past three seasons, assigning weights of 5, 4, and 3:

$$\bar{S} = \frac{5 \cdot S_{t-1} + 4 \cdot S_{t-2} + 3 \cdot S_{t-3}}{5 \cdot PA_{t-1} + 4 \cdot PA_{t-2} + 3 \cdot PA_{t-3}}$$

Where:
- $S_{t-i}$ is the counting statistic in season $t-i$
- $PA_{t-i}$ is the playing time volume in season $t-i$

## 2. Regression to League Average

Marcel regresses all players toward the league average by adding a fixed volume of league-average performance:
- For batters: adds 1200 plate appearances of league-average production
- For pitchers: adds 100 innings pitched (or ~450 batters faced) of league-average production

For a batter's rate metric:

$$\hat{R}_{marcel} = \frac{5 \cdot S_{t-1} + 4 \cdot S_{t-2} + 3 \cdot S_{t-3} + 1200 \cdot lgRate}{5 \cdot PA_{t-1} + 4 \cdot PA_{t-2} + 3 \cdot PA_{t-3} + 1200}$$

For a pitcher's rate metric:

$$\hat{R}_{marcel, P} = \frac{5 \cdot S_{t-1} + 4 \cdot S_{t-2} + 3 \cdot S_{t-3} + 100 \cdot lgRate}{5 \cdot IP_{t-1} + 4 \cdot IP_{t-2} + 3 \cdot IP_{t-3} + 100}$$

## 3. Piecewise Age Adjustment

Marcel applies a standard aging factor centered at age 30:
- Players under 30 are expected to improve by 0.6% per year
- Players age 30 and older are expected to decline by 0.3% per year

$$\Delta_{age} = (30 - age) \cdot 0.006$$

For players 30 or older:

$$\Delta_{age, old} = (30 - age) \cdot 0.003$$

The age-adjusted final projected rate is:

$$\hat{R}_{final} = \hat{R}_{marcel} \cdot (1 + \Delta_{age})$$
