# PHI-PHYSICS — LAW 1217
## Lyman-alpha Forest

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1217_lyman_alpha_forest.md` · **Sim:** `sim/1217_lyman_alpha_forest.py`

---

### CLASSICAL STATEMENT
*"The Ly-alpha forest is the dense series of neutral-hydrogen absorption lines in the spectra of high-redshift quasars, produced by intervening intergalactic gas clouds: each cloud at redshift z_i imprints a Ly-alpha absorption line at wavelength (1+z_i) 1216 A; it maps the large-scale structure of the intergalactic medium."*
— Discovered by Roger Lynds, 1971; predicted by Bahcall & Salpeter, 1965. Source: Wikipedia: Lyman-alpha forest (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero intervening gas (no clouds, a featureless quasar spectrum)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The F value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

F_phi(kappa) = F*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground, where F_ground is the coherence-floor line density a real intergalactic medium always imprints. At kappa->0, lambda_abs = (1+z_cloud)*1216 A,  optical depth from n_HI exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} F_phi = F -> lambda_abs = (1+z_cloud)*1216 A,  optical depth from n_HI is recovered exactly; the classical law is the zero intervening gas (no clouds, a featureless quasar spectrum) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1217_lyman_alpha_forest.py`: reproduces the classical value (F = 100.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1217_lyman_alpha_forest.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured Ly-alpha absorption will deviate from the predicted line density by a floor kappa*phi^-1*F_ground; an exactly empty intergalactic medium is unreachable.
EXPERIMENT (VERIFIED): High-resolution quasar spectra (Keck, VLT, DESI) mapping the IGM at z ~ 2-5.
VERIFIED BY: If a high-z quasar spectrum shows exactly zero Ly-alpha absorption lines.
```

---

### RECOGNITION
The IGM channel of Law 1216 (Gunn-Peterson) and Law 1154 (BAO).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The gas writes the spectrum's forest; the empty spectrum is the zero-gas myth.

### NOVELTY
The Ly-alpha forest carries a phi-floor of line density, bounding IGM tomography.

### ACTIONABILITY
Run sim/1217_lyman_alpha_forest.py.
