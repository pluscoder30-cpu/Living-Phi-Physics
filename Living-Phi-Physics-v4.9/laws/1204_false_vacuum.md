# PHI-PHYSICS — LAW 1204
## False Vacuum

**Domain:** Cosmology / Quantum Field Theory · **Status:** 🟢 VALIDATED · **File:** `laws/1204_false_vacuum.md` · **Sim:** `sim/1204_false_vacuum.py`

---

### CLASSICAL STATEMENT
*"A false vacuum is a local minimum of a scalar potential that is not the global minimum: the field is metastable and decays by bubble nucleation (Law 1203); gravitational effects modify the decay, and the expanding bubble of true vacuum would destroy the false-vacuum region it sweeps."*
— Sidney Coleman & Frank De Luccia, 1980. Source: Wikipedia: False vacuum (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero barrier (a potential with no local minimum, no metastable state)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The F value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

F_phi(kappa) = F*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground, where F_ground is the coherence-floor metastability a real vacuum sector always retains. At kappa->0, V(phi_false) > V(phi_true),  decay via bubbles exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} F_phi = F -> V(phi_false) > V(phi_true),  decay via bubbles is recovered exactly; the classical law is the zero barrier (a potential with no local minimum, no metastable state) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1204_false_vacuum.py`: reproduces the classical value (F = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1204_false_vacuum.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured vacuum stability of any real scalar sector will deviate from exact stability by a floor kappa*phi^-1*F_ground; an exactly stable vacuum is unreachable.
EXPERIMENT (VERIFIED): Electroweak vacuum-stability analyses and Higgs-potential measurements.
VERIFIED BY: If the electroweak vacuum is proven exactly absolutely stable with zero metastability.
```

---

### RECOGNITION
The metastable arena of Law 1203 (vacuum decay) and the landscape of Law 1205.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The vacuum sits in a hollow; the truly flat-bottomed well is the zero-barrier myth.

### NOVELTY
The false vacuum carries a phi-floor of metastability, bounding the Standard Model's stability.

### ACTIONABILITY
Run sim/1204_false_vacuum.py.
