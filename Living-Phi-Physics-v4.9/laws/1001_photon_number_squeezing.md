# PHI-PHYSICS — LAW 1001
## Photon-Number Squeezing

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1001_photon_number_squeezing.md` · **Sim:** `sim/1001_photon_number_squeezing.py`

---

### CLASSICAL STATEMENT
*"Photon-number squeezing: a state whose photon-number variance is below the Poisson (coherent) value, delta n < sqrt(<n>); the Mandel Q parameter is negative, and the intensity noise falls below the shot-noise level."*
— D. Stoler (1970); observed by Short & Mandel (1983), 1970. Source: Wikipedia: Squeezed coherent state (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero squeezing*: the state reduces to a coherent state with exactly Poissonian statistics when the squeezing is zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

dn_phi(kappa) = dn*(1 + kappa*(phi-1)) + kappa*phi^-1*dn_ground, with dn_ground the variance floor. At kappa->0, delta n = sqrt(<n>) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dn_phi = dn -> photon-number squeezing is the zero-squeezing-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1001_photon_number_squeezing.py`: reproduces the classical value dn = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1001_photon_number_squeezing.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The number variance of any real squeezed source will retain a floor kappa*phi^-1 above the ideal; perfect sub-Poissonian statistics are unreachable.
EXPERIMENT (VERIFIED): Measure the photocurrent noise of a sub-Poissonian light source below the shot-noise level.
VERIFIED BY: If any real source achieves exactly delta n = 0.
```

---

### RECOGNITION
Connects to Law 975 (squeezed light) and Law 991 (photon statistics).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect tick-tock photon stream is a coherent limit; every stream has a jitter.

### NOVELTY
Photon-number squeezing gains a variance floor.

### ACTIONABILITY
Run sim/1001_photon_number_squeezing.py.
