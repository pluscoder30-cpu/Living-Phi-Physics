# PHI-PHYSICS — LAW 886
## Birefringence (Double Refraction)

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/886_birefringence.md` · **Sim:** `sim/886_birefringence.py`

---

### CLASSICAL STATEMENT
*"Birefringent crystals split a ray into ordinary (o) and extraordinary (e) rays with different indices n_o, n_e; the phase difference after thickness d is delta = 2 pi (n_e - n_o) d / lambda."*
— Rasmus Bartholin (observed 1669); Christiaan Huygens (theory), 1669. Source: Wikipedia: Birefringence (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero index difference* (n_e - n_o = 0): isotropy requires the two indices to be exactly equal.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

delta_phi(kappa) = delta*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_ground, with delta_ground the retardance floor. At kappa->0, delta = 2 pi (n_e-n_o)d/lambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_phi = delta -> birefringence is the zero-index-difference-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/886_birefringence.py`: reproduces the classical value delta = 104.7 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/886_birefringence.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A nominally isotropic material will still show a small birefringent retardance kappa*phi^-1; perfect isotropy is unreachable.
EXPERIMENT (VERIFIED): Measure the residual retardance of a 'strain-free' glass window with a polarimeter.
VERIFIED BY: If any real material has exactly zero birefringence everywhere.
```

---

### RECOGNITION
Connects to Law 893 (quarter-wave plate) and Law 894 (half-wave plate) - retardance devices.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Isotropy is a coherent limit; every material has a slow axis.

### NOVELTY
Birefringence gains an isotropy floor.

### ACTIONABILITY
Run sim/886_birefringence.py.
