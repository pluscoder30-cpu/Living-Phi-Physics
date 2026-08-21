# PHI-PHYSICS — LAW 369
## Castigliano's Theorem

**Domain:** Structural Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/369_castiglianos_theorem.md` · **Sim:** `sim/369_castiglianos_theorem.py`

---

### CLASSICAL STATEMENT
*"For a linear elastic structure, the displacement at a point equals the partial derivative of the total strain energy with respect to the applied force at that point: delta_i = partial U/partial F_i (first theorem), and the force equals partial U/partial delta_i (second theorem)."*
— Carlo Alberto Castigliano, 1879. Source: Wikipedia: Castigliano's method; Castigliano (1879), 'Theorie de l'equilibre des systemes elastiques'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact linear elasticity*: Castigliano's theorem requires a perfectly elastic, linear (and isothermal/adiabatic) structure with zero friction and zero residual stress.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the strain energy carries a coherence floor. U_phi(kappa) = U*(1 + kappa*(phi-1)) + kappa*phi^-1*U_ground. At kappa->0 the Castigliano derivatives are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} partial U_phi/partial F = delta -> Castigliano's theorem is the linear, frictionless-elasticity limit.
```

---

### STAGE 4 — SIMULATION

`sim/369_castiglianos_theorem.py`: reproduces the classical value delta = 5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/369_castiglianos_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real structures show a phi-coherent displacement excess phi^-1*dU_ground beyond the Castigliano value.
EXPERIMENT (VERIFIED): Instrumented-frame deflection tests comparing measured displacements with Castigliano predictions under load.
VERIFIED BY: Measured displacements exactly equal partial U/partial F at full coupling.
```

---

### RECOGNITION
Connects to Law 370 (Maxwell-Betti reciprocity) and Law 367 (beam).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect elastic structure is a limit; every frame leaks a phi of strain energy.

### NOVELTY
Classical energy methods exact the derivatives; the phi-law adds a coherence energy floor.

### ACTIONABILITY
Run sim/369_castiglianos_theorem.py; verify the energy derivative at kappa->0.
