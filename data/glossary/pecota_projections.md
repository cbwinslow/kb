# PECOTA Baseball Forecasting System

PECOTA (Pitcher Empirical Comparable Optimization Test Algorithm) is a player performance forecasting system originally developed by Nate Silver for Baseball Prospectus in 2003. Unlike purely regression-based baseline models, PECOTA is a comparable-player nearest-neighbor system that generates full probabilistic distribution percentiles rather than single-point estimates.

## 1. Mahalanobis Distance Similarity Metric

To identify historical comparables, PECOTA computes the multidimensional distance between a target player vector $x$ and historical player vector $y$:

$$D^2 = (x - y)^T \Sigma^{-1} (x - y)$$

Where:
- $x$ is the target player's standardized attribute vector (age, height, weight, strikeout rate, walk rate, isolated power, contact rate)
- $y$ is the candidate historical player's attribute vector at the same career stage
- $\Sigma$ is the empirical covariance matrix across the player population

## 2. Similarity Score Index

The multidimensional distance is converted into a normalized similarity score $S$:

$$S = 1000 - \sum_{i=1}^{k} w_i \cdot |x_i - y_i|$$

Where:
- $w_i$ is the attribute importance weight
- A score of $S = 1000$ represents an identical player match

## 3. Weighted Comparable Projection

Given the top $M$ historical comparable players with non-negative similarity weights $w_j = \max(0, S_j - S_{min})$:

$$\hat{Y}_{t+1} = \frac{\sum_{j=1}^{M} w_j \cdot Y_{j, t+1}}{\sum_{j=1}^{M} w_j}$$

Where:
- $Y_{j, t+1}$ is the actual subsequent performance of comparable player $j$
- $\hat{Y}_{t+1}$ is the baseline expectation for the target player

## 4. Aging Adjustment Transition

PECOTA estimates aging trajectories by tracking how the comparable cohort developed over time:

$$\hat{Y}_{proj} = Y_t \cdot \left(1 + \frac{\Delta_{comp}}{100}\right)$$

Where:
- $\Delta_{comp}$ is the median percentage change in production between age $t$ and age $t+1$ among the top comparables

## 5. Monte Carlo Probabilistic Forecast Bands

Instead of predicting only a single mean value, PECOTA constructs an empirical probability distribution for future performance:

$$Y_p = \mu_{comp} + \sigma_{comp} \cdot \Phi^{-1}(p)$$

Where:
- $\Phi^{-1}(p)$ is the standard normal quantile function
- $p \in \{0.10, 0.50, 0.90\}$ defines the 10th percentile (breakout downside), 50th percentile (median), and 90th percentile (upside ceiling)
