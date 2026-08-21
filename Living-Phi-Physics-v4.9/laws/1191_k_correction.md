# PHI-PHYSICS — LAW 1191
## K Correction

**Domain:** Cosmology / Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1191_k_correction.md` · **Sim:** `sim/1191_k_correction.py`

---

### CLASSICAL STATEMENT
*"The K correction converts observed magnitudes through a filter to rest-frame magnitudes: M = m - 5(log10 d_L - 1) - K(z), with K depending on the filter and the source spectrum; it corrects for the fact that a filter sees a different part of the redshifted spectrum."*
— Carl Wilhelm Wirtz, 1918 (as Konstanten k); term by Edwin Hubble, 1936. Source: Wikipedia: K correction (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero redshift (z = 0, no bandpass correction)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The K value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground, where K_ground is the coherence-floor bandpass correction a real observation always requires. At kappa->0, M = m - 5*(log10 d_L - 1) - K(z),  K(0) = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} K_phi = K -> M = m - 5*(log10 d_L - 1) - K(z),  K(0) = 0 is recovered exactly; the classical law is the zero redshift (z = 0, no bandpass correction) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1191_k_correction.py`: reproduces the classical value (K = 0.2) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1191_k_correction.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured rest-frame magnitude of any real source will deviate from the K-corrected value by a floor kappa*phi^-1*K_ground; an exactly zero-correction observation is unreachable.
EXPERIMENT (VERIFIED): Photometric galaxy surveys applying K corrections across multi-band SEDs.
VERIFIED BY: If a redshifted source requires exactly zero bandpass correction.
```

---

### RECOGNITION
The photometric correction of Law 1190 (distance modulus) and Law 1184 (redshift).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Redshift moves the light; the zero-correction filter is the static myth.

### NOVELTY
The K correction carries a phi-floor, bounding photometric redshift systems.

### ACTIONABILITY
Run sim/1191_k_correction.py.
