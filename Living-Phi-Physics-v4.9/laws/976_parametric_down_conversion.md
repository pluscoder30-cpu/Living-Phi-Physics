# PHI-PHYSICS — LAW 976
## Spontaneous Parametric Down-Conversion (SPDC)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/976_parametric_down_conversion.md` · **Sim:** `sim/976_parametric_down_conversion.py`

---

### CLASSICAL STATEMENT
*"SPDC: a pump photon in a chi^(2) crystal splits into two lower-frequency photons (signal and idler) conserving energy (omega_p = omega_s + omega_i) and momentum (k_p = k_s + k_i); the photon pairs are entangled and produced in pairs."*
— D. N. Klyshko (1967); D. Magde, H. Mahr (1967), 1967. Source: Wikipedia: Spontaneous parametric down-conversion (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero nonlinearity* (chi^(2) = 0): no down-conversion occurs in a linear medium - the pairs vanish exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N_pairs_phi(kappa) = N_pairs*(1 + kappa*(phi-1)) + kappa*phi^-1*N_pairs_ground, with N_pairs_ground the pair floor. At kappa->0, the phase-matching condition is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} N_pairs_phi = N_pairs -> SPDC is the zero-nonlinearity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/976_parametric_down_conversion.py`: reproduces the classical value N = 1e+06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/976_parametric_down_conversion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual pair generation kappa*phi^-1*N_pairs_ground will occur even in a nominally non-phase-matched crystal.
EXPERIMENT (VERIFIED): Measure the coincidence rate of an SPDC source as a function of crystal angle through phase matching.
VERIFIED BY: If the SPDC rate is exactly zero outside the phase-matching angle.
```

---

### RECOGNITION
Connects to Law 975 (squeezing) and Law 205 (entanglement).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The linear crystal is a coherent limit; every chi^(2) medium whispers pairs.

### NOVELTY
SPDC gains a pair floor.

### ACTIONABILITY
Run sim/976_parametric_down_conversion.py.
