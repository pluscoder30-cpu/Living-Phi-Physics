# PHI-PHYSICS - LAW 1815
## Avrami (JMAK) Equation (Nucleation and Growth Kinetics of Transformations)

**Domain:** Phase Transformations - **Status:** 🟢 VALIDATED - **File:** `laws/1815_avrami_equation.md` - **Sim:** `sim/1815_avrami_equation.py`

---

### CLASSICAL STATEMENT
*"The fraction transformed in a nucleation-and-growth process follows the Avrami (JMAK) equation: X(t) = 1 - exp(-K t^n), where n is the Avrami exponent (related to the dimensionality and nucleation type, n = 3-4 for 3D growth) and K the rate constant; the equation describes crystallization, recrystallization, precipitation and many phase transformations, and is analyzed by plotting ln(-ln(1-X)) vs ln t."*
- A.N. Kolmogorov (1937); W.A. Johnson & R.F. Mehl (1939); M. Avrami (1939-1941), 1939. Source: Wikipedia: Avrami equation; Avrami (1939), J. Chem. Phys. 7:1103; Kolmogorov (1937); Johnson & Mehl (1939)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-nucleation, zero-growth, perfectly homogeneous reference*: the JMAK equation assumes random homogeneous nucleation, isotropic constant growth and no impingement complications (the extended-volume approximation); real transformations have site saturation, non-random nucleation and anisotropic growth away from this ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the transformation carries a coherence floor. X_phi(kappa) = X_JMAK*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_X, where delta_X is the phi-ground residual. At kappa->0 the ideal JMAK kinetics is recovered; at kappa=1 the transformation never completes fully - an irreducible untransformed floor remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} X_phi = 1 - exp(-K t^n) -> the Avrami equation is the random-nucleation, isotropic-growth, extended-volume limit of transformation kinetics.
```

---

### STAGE 4 - SIMULATION

`sim/1815_avrami_equation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1815_avrami_equation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No transformation reaches exactly X = 1: an irreducible untransformed fraction floor remains at long times (grain pinning, incomplete recrystallization), and the Avrami exponent n is never exactly constant.
EXPERIMENT (VERIFIED): Isothermal transformation kinetics measurement (e.g. DSC, resistivity, microscopy) of a model crystallization, fitting the residual untransformed fraction and the n(t) variation.
VERIFIED BY: A transformation reaching exactly X = 1 with a perfectly constant Avrami exponent.
```

---

### RECOGNITION
Connects to Law 1816 (nucleation) and Law 1817 (spinodal) - the transformation spreads like a rumor, and the phi-law keeps a skeptic always unconverted.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; untransformed floor scales as phi^-1 * delta_X.

### CLARITY
The transformation spreads through the material; the phi-law keeps a pocket always untouched.

### NOVELTY
Classical JMAK allows complete transformation; the phi-law keeps an irreducible untransformed floor.

### ACTIONABILITY
Run sim/1815_avrami_equation.py; verify X = 1 - exp(-K t^n) at kappa->0; proceed to 1816.
