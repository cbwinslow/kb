# Alan Nathan Baseball Trajectory Physics & Aerodynamics

Based on the aerodynamic formulations published by Prof. Alan M. Nathan (2008, 2015), the flight of a baseball under gravity, aerodynamic drag, and the Magnus force is governed by a set of coupled non-linear ordinary differential equations.

## 1. Full Aerodynamic Equation of Motion

The acceleration vector of a baseball in flight is given by:

$$\vec{a} = \vec{a}_g + \vec{a}_d + \vec{a}_m$$

Where:
- $\vec{a}_g = -g \hat{k}$ is the gravitational acceleration ($g = 9.80665\text{ m/s}^2$ or $32.174\text{ ft/s}^2$)
- $\vec{a}_d$ is the aerodynamic drag acceleration
- $\vec{a}_m$ is the Magnus lift and deflection acceleration

## 2. Drag Force Acceleration

Aerodynamic drag opposes the instantaneous velocity vector $\vec{v}$:

$$\vec{a}_d = -\frac{1}{2m} \rho A C_D v \vec{v}$$

Where:
- $m$ is the mass of the baseball (~0.145 kg or 5.125 oz)
- $\rho$ is air density (~1.225 kg/m³ at sea level, adjusted for temperature, barometric pressure, and relative humidity)
- $A = \pi r^2$ is the cross-sectional area of the ball ($r \approx 0.0366\text{ m}$)
- $C_D$ is the speed-dependent drag coefficient
- $v = \|\vec{v}\|$ is the magnitude of velocity

## 3. Magnus Force Acceleration

The Magnus force arises from the asymmetry in air velocity caused by ball rotation $\vec{\omega}$:

$$\vec{a}_m = \frac{1}{2m} \rho A C_L v (\hat{\omega} \times \vec{v})$$

Where:
- $C_L$ is the lift coefficient
- $\hat{\omega} = \vec{\omega} / \|\vec{\omega}\|$ is the unit vector along the spin axis
- $\hat{\omega} \times \vec{v}$ defines the directional vector of movement (break) perpendicular to both spin and trajectory

## 4. Spin Parameter and Lift Coefficient

The non-dimensional spin parameter $S$ relates rotational surface velocity to translational speed:

$$S = \frac{r \cdot \omega}{v}$$

Nathan's empirical parameterization for the lift coefficient $C_L$ as a function of spin parameter $S$ is:

$$C_L = \frac{1}{2.32 + \frac{0.40}{S}}$$

## 5. Drag Coefficient Speed Dependence

The drag coefficient varies with velocity across the trans-critical boundary:

$$C_D = c_{d0} + \frac{c_{d1}}{1 + e^{(v - v_c) / \Delta v}}$$

Where:
- $c_{d0} \approx 0.30$ is the baseline drag
- $c_{d1} \approx 0.15$
- $v_c$ is the critical speed threshold
