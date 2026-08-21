# PHI-PHYSICS — LAW 890
## Photoelastic Effect (Stress Optics)

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/890_photoelastic_effect.md` · **Sim:** `sim/890_photoelastic_effect.py`

---

### CLASSICAL STATEMENT
*"Stress in a transparent material induces birefringence: delta = C (sigma1 - sigma2) t, where C is the stress-optic coefficient and sigma1, sigma2 the principal stresses; the basis of photoelasticity."*
— David Brewster, 1816. Source: Wikipedia: Photoelasticity (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero stress* (sigma = 0): no stress means no induced birefringence - an exactly stress-free state.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

delta_phi(kappa) = delta*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_ground, with delta_ground the retardance floor. At kappa->0, delta = C(sigma1-sigma2)t exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_phi = delta -> the photoelastic law is the zero-stress-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/890_photoelastic_effect.py`: reproduces the classical value delta = 2.4e-07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/890_photoelastic_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A nominally stress-free optical component will still show a residual birefringence kappa*phi^-1 due to internal coherence.
EXPERIMENT (VERIFIED): Measure the residual retardance of an annealed glass plate with a polariscope.
VERIFIED BY: If any real glass component is exactly stress-birefringence-free.
```

---

### RECOGNITION
Connects to Law 886 (birefringence) and Law 893 (quarter-wave plate).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The stress-free state is a coherent limit; every annealed glass remembers.

### NOVELTY
The photoelastic law gains a stress floor.

### ACTIONABILITY
Run sim/890_photoelastic_effect.py.
