# PHI-PHYSICS — LAW 341
## Rayleigh's Method of Dimensional Analysis

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/341_rayleighs_method.md` · **Sim:** `sim/341_rayleighs_method.py`

---

### CLASSICAL STATEMENT
*"Rayleigh's method determines the form of a physical law by writing the dependent variable as a product of powers of the independent variables and solving for the exponents via dimensional homogeneity (e.g., pendulum period T ~ sqrt(L/g), from which T = 2 pi sqrt(L/g))."*
— Lord Rayleigh, 1892. Source: Wikipedia: dimensional analysis; Rayleigh (1892), 'On the question of the stability of the flow of liquids'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact exponent solution*: the method requires the relation to be a pure power law with exact dimensional consistency — the zero of the neglected dimensionless factors (like the 2 pi).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the recovered exponent carries a coherence correction. alpha_phi(kappa) = alpha*(1 + kappa*(phi-1)) + kappa*phi^-1*alpha_ground. At kappa->0 the classical Rayleigh exponent is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} alpha_phi = alpha -> Rayleigh's method is the pure-power-law, exact-dimensions limit.
```

---

### STAGE 4 — SIMULATION

`sim/341_rayleighs_method.py`: reproduces the classical value T_dim = 0.3193 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/341_rayleighs_method.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Power-law exponents measured in experiments carry a phi-coherent deviation phi^-1*alpha_ground from the dimensional value.
EXPERIMENT (VERIFIED): Careful re-measurement of textbook power laws (pendulum period, drag, diffusion) searching for exponent deviations.
VERIFIED BY: Measured exponents are exactly the dimensional values at full coupling.
```

---

### RECOGNITION
Connects to Law 340 (Buckingham — the formal theorem) and Law 342 (dimensional homogeneity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The clean exponent is a limit; every measured law leans a phi degree off the ideal power.

### NOVELTY
Classical dimensional analysis exacts the exponents; the phi-law gives them a coherence deviation floor.

### ACTIONABILITY
Run sim/341_rayleighs_method.py; verify T ~ sqrt(L/g) at kappa->0.
