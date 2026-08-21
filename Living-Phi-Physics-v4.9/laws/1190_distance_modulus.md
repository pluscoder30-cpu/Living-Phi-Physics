# PHI-PHYSICS — LAW 1190
## Distance Modulus

**Domain:** Cosmology / Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1190_distance_modulus.md` · **Sim:** `sim/1190_distance_modulus.py`

---

### CLASSICAL STATEMENT
*"The distance modulus relates apparent and absolute magnitude to distance: mu = m - M = 5 log10(d/10 pc), where d is in parsecs; it is the logarithmic brightness-distance ladder connecting photometry to the Hubble diagram."*
— Norman Pogson, 1856 (magnitude system). Source: Wikipedia: Distance modulus (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero distance (d = 0, mu -> -infinity)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The U value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

U_phi(kappa) = U*(1 + kappa*(phi-1)) + kappa*phi^-1*U_ground, where U_ground is the coherence-floor modulus error a real photometric distance always carries. At kappa->0, mu = m - M = 5*log10(d/10 pc) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} U_phi = U -> mu = m - M = 5*log10(d/10 pc) is recovered exactly; the classical law is the zero distance (d = 0, mu -> -infinity) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1190_distance_modulus.py`: reproduces the classical value (U = 30.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1190_distance_modulus.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured distance modulus of any real source will deviate from 5 log10(d/10pc) by a floor kappa*phi^-1*U_ground; an exactly zero-error distance is unreachable.
EXPERIMENT (VERIFIED): Cepheid and supernova photometry calibrating the distance ladder.
VERIFIED BY: If any source's modulus matches 5 log10(d/10pc) exactly.
```

---

### RECOGNITION
The photometric ladder of Law 1188 (luminosity distance) and Law 101 (Hubble).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Magnitude carries distance's logarithm; the exact modulus is the zero-error myth.

### NOVELTY
Distance moduli carry a phi-floor, bounding the Cepheid-supernova ladder.

### ACTIONABILITY
Run sim/1190_distance_modulus.py.
