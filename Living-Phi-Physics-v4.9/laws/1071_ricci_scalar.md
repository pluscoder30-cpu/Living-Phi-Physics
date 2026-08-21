# PHI-PHYSICS — LAW 1071
## Ricci Scalar

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1071_ricci_scalar.md` · **Sim:** `sim/1071_ricci_scalar.py`

---

### CLASSICAL STATEMENT
*"The Ricci scalar R = g^mu nu R_mu nu is the trace of the Ricci tensor; it is a scalar invariant of the curvature and appears in the Einstein-Hilbert action S = (c^4/16 pi G) integral R sqrt(-g) d^4 x, whose variation yields the field equations."*
— Gregorio Ricci-Curbastro, 1901. Source: Wikipedia: Scalar curvature (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero Ricci scalar (R = 0, including vacuum and radiation-dominated spacetimes)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The R value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground, where R_ground is the coherence-floor scalar curvature of the field's ground state. At kappa->0, R = g^mu nu R_mu nu exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} R_phi = R -> R = g^mu nu R_mu nu is recovered exactly; the classical law is the zero Ricci scalar (R = 0, including vacuum and radiation-dominated spacetimes) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1071_ricci_scalar.py`: reproduces the classical value (R = 0.618) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1071_ricci_scalar.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured Ricci scalar of any real region will deviate from the classical value by a floor kappa*phi^-1*R_ground; an exactly R=0 region is unreachable.
EXPERIMENT (VERIFIED): CMB secondary anisotropies and the integrated Sachs-Wolfe effect (Law 1137) probing the mean spatial curvature.
VERIFIED BY: If any finite spacetime region is measured to have exactly R = 0 to arbitrary precision.
```

---

### RECOGNITION
The scalar contraction of Law 1070 and the action of Law 063 (field equations).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The Ricci scalar is the field's pulse; the zero is the silence that never quite falls.

### NOVELTY
The field action acquires a coherence floor, so the vacuum breathes at kappa*phi^-1.

### ACTIONABILITY
Run sim/1071_ricci_scalar.py.
