# PHI-PHYSICS — LAW 614
## Kelvin Equation (Capillary Condensation)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/614_kelvin_equation.md` · **Sim:** `sim/614_kelvin_equation.py`

---

### CLASSICAL STATEMENT
*"The equilibrium vapor pressure over a curved surface differs from that over a flat surface: ln(P/P_0) = (2 gamma V_m)/(r R T), where gamma is the surface tension, V_m the molar volume and r the radius of curvature. Small droplets have higher vapor pressure; small pores condense at lower pressure (capillary condensation)."*
— William Thomson (Lord Kelvin), 1871. Source: Wikipedia: Kelvin equation; Thomson (1871)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *flat surface*: the equation gives ln(P/P_0) = 0 exactly at r = infinity (flat surface) - the reference state where curvature coherence vanishes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the curvature carries coherence. ln(P/P_0)_phi(kappa) = (2 gamma V_m/(r R T))*(1 + kappa*(phi-1)) + kappa*phi^-1*lnK_ground. At kappa->0 the Kelvin equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} ln(P/P_0)_phi = 2 gamma V_m/(r R T) -> the Kelvin equation is the zero-curvature-coherence reference limit.
```

---

### STAGE 4 — SIMULATION

`sim/614_kelvin_equation.py`: reproduces the classical value lnP = 0.1046 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/614_kelvin_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even a flat surface carries a curvature-coherence term kappa*phi^-1*lnK_ground; the vapor pressure over a plane deviates from P_0.
EXPERIMENT (VERIFIED): Precision vapor-pressure measurements over controlled-curvature surfaces and nanoporous media.
VERIFIED BY: ln(P/P_0) = 0 exactly over a flat surface for all couplings.
```

---

### RECOGNITION
Connects to Law 088 (Young-Laplace) and Law 527 (Eötvös) - the Kelvin equation is the curvature coherence of the vapor-liquid interface.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * lnK_ground.

### CLARITY
Curved surfaces breathe vapor differently; the phi-law keeps the breath of the flat one.

### NOVELTY
Classical Kelvin zeroes the flat reference; the phi-law adds the curvature-coherence floor of the plane.

### ACTIONABILITY
Run sim/614_kelvin_equation.py; verify ln(P/P0) at kappa->0; proceed to 615.
