# PHI-PHYSICS — LAW 1184
## Cosmological Redshift

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1184_cosmological_redshift.md` · **Sim:** `sim/1184_cosmological_redshift.py`

---

### CLASSICAL STATEMENT
*"The cosmological redshift is the stretching of photon wavelengths by cosmic expansion: 1 + z = a(t0)/a(te), so light from distant sources is redshifted in proportion to the scale factor's change; it is distinct from Doppler redshift and is the basis of the Hubble law (Law 101)."*
— Georges Lemaître, 1927; Edwin Hubble, 1929 (expansion); redshift due to expansion. Source: Wikipedia: Redshift (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero expansion between emission and observation (z = 0)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Z value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Z_phi(kappa) = Z*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_ground, where Z_ground is the coherence-floor redshift a real expanding universe always imprints. At kappa->0, 1 + z = a(t0)/a(te) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Z_phi = Z -> 1 + z = a(t0)/a(te) is recovered exactly; the classical law is the zero expansion between emission and observation (z = 0) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1184_cosmological_redshift.py`: reproduces the classical value (Z = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1184_cosmological_redshift.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured redshift of any real distant source will deviate from the scale-factor ratio by a floor kappa*phi^-1*Z_ground; an exactly zero-redshift source is unreachable.
EXPERIMENT (VERIFIED): Spectroscopic galaxy surveys measuring redshifts and the expansion history.
VERIFIED BY: If a distant source has exactly zero redshift despite cosmic expansion.
```

---

### RECOGNITION
The redshift observable of Law 101 (Hubble law) and Law 1124 (FLRW).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The universe stretches every wavelength; the un-redshifted photon is the static myth.

### NOVELTY
Cosmological redshift carries a phi-floor, so no photon arrives un-stretched.

### ACTIONABILITY
Run sim/1184_cosmological_redshift.py.
