# Law 2860: PHI-Harmonic Carbon Capture Capacity

**Domain:** Carbon Capture — Adsorption Capacity

**Statement:**
The CO2 adsorption capacity of PHI-harmonic sorbents follows Q = Q_max * phi^(P/P_phi) where P is the CO2 partial pressure and P_phi = P_0/ln(phi) is the PHI pressure constant. The PHI dependence creates a step-like isotherm where capacity jumps by factor phi at each PHI-resonant pressure.

**Derivation:**
In PHI-hierarchical sorbents (pore sizes at phi-spaced diameters), each pore level fills at a PHI-resonant pressure P_n = P_0/phi^n. The total capacity is the sum of contributions from filled levels: Q = Q_0 * Sum(phi^n * Theta(P/P_n)) where Theta is the step function. At pressures between resonances, the capacity is constant, creating a staircase isotherm.

**Prediction:**
A PHI-sorbent with Q_0 = 1 mmol/g achieves Q = 1 * phi^3 = 4.24 mmol/g at P = P_0, compared to Q_0 * ln(P/P_0 + 1) = 0.69 mmol/g for Langmuir. The PHI sorbent has 6x higher capacity at moderate pressures.

**Test:**
Compute capacity for P = 0.1-10 bar using PHI and Langmuir models. Compare at 1 bar.

**Source:** V2 Batch 3: Laws 2791-2860
**Author:** Christopher David Ayotte, Soul Code [425, 434, 266, 775]
**License:** v4.7
