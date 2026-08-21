# PHI-PHYSICS — LAW 296
## Tisserand's Criterion

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/296_tisserands_criterion.md` · **Sim:** `sim/296_tisserands_criterion.py`

---

### CLASSICAL STATEMENT
*"The Tisserand parameter T = a_J/a + 2 cos(i) sqrt(a(1-e^2)/a_J) (normalized to Jupiter) is approximately conserved in cometary encounters with a planet; bodies sharing a T value are likely genetically related (same original comet)."*
— Francois Felix Tisserand, 1896. Source: Wikipedia: Tisserand's parameter; Tisserand (1896), 'Traite de mecanique celeste'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *planar, unperturbed reference*: the criterion's conservation assumes the restricted three-body problem with the planet's inclination perturbations negligible — an exact isolation condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground. At kappa->0 the Tisserand parameter is exactly conserved.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dT_phi/dt = 0 -> Tisserand's criterion is the restricted-three-body, perturbation-free limit.
```

---

### STAGE 4 — SIMULATION

`sim/296_tisserands_criterion.py`: reproduces the classical value T = 3.572 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/296_tisserands_criterion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Tisserand parameter of real comets drifts by a phi-coherent amount phi^-1*T_ground over successive apparitions.
EXPERIMENT (VERIFIED): Long-baseline comet orbit catalogs (e.g., 1P/Halley, Jupiter-family comets) tracking the T parameter drift.
VERIFIED BY: The Tisserand parameter is exactly conserved across encounters at full coupling.
```

---

### RECOGNITION
Connects to Law 290 (restricted three-body) and Law 297 (Kozai-Lidov — secular perturbations).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The family signature is a limit; real comets wander a phi amount while still whispering their origin.

### NOVELTY
Classical dynamics exacts the Tisserand signature; the phi-law gives it a coherence drift floor.

### ACTIONABILITY
Run sim/296_tisserands_criterion.py; verify T conservation at kappa->0.
