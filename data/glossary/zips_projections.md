# ZiPS Forecasting System

ZiPS (Szymborski Projection System) is a sabermetric forecasting model developed by Dan Szymborski in 2004. ZiPS combines multi-year weighted performance baselines, sample-size empirical Bayes regression to league mean, and archetype-specific aging curves to project player outcomes and career distributions.

## 1. 4-Year Recency Decay Baseline

ZiPS weights past performance over the previous four seasons using declining recency coefficients (8/5/4/3):

$$\bar{X}_{weighted} = \frac{8 \cdot X_{t-1} + 5 \cdot X_{t-2} + 4 \cdot X_{t-3} + 3 \cdot X_{t-4}}{8 \cdot W_{t-1} + 5 \cdot W_{t-2} + 4 \cdot W_{t-3} + 3 \cdot W_{t-4}}$$

Where:
- $X_{t-i}$ is the player's statistical output in season $t-i$
- $W_{t-i}$ is the playing time volume ($PA$ for batters or $IP$ for pitchers) in season $t-i$

## 2. Sample Size Empirical Bayes Regression to League Mean

To prevent small-sample noise from distorting projections, the weighted average is regressed toward the league average based on career sample size:

$$\hat{X}_{reg} = \frac{PA}{PA + C_{reg}} \cdot \bar{X}_{weighted} + \frac{C_{reg}}{PA + C_{reg}} \cdot \mu_{lg}$$

Where:
- $\mu_{lg}$ is the position- and era-adjusted league average rate
- $C_{reg}$ is the metric stabilization threshold (e.g., $C \approx 300 - 400$ for on-base percentage, $C \approx 60 - 70$ for strikeout percentage)

## 3. Archetype-Specific Aging Trajectories

ZiPS adjusts baseline projections for expected age-related growth or decline using non-linear trajectory curves conditioned on player archetype:

$$\Delta_{age} = \alpha \cdot (age - 28) - \beta \cdot (age - 28)^2$$

Where:
- $\alpha$ and $\beta$ are empirical aging parameters derived from historical comparables with similar physical profiles and batted-ball characteristics
- Peak performance typically centers around age 27–28

## 4. Composite Rate Projection

$$\hat{X}_{final} = \hat{X}_{reg} \cdot (1 + \Delta_{age})$$

Where:
- $\hat{X}_{final}$ is the final projected true-talent rate for season $t+1$
