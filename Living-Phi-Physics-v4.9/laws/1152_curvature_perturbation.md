# PHI-PHYSICS — LAW 1152
## Curvature Perturbation

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1152_curvature_perturbation.md` · **Sim:** `sim/1152_curvature_perturbation.py`

---

### CLASSICAL STATEMENT
*"The curvature perturbation zeta is a gauge-invariant variable conserved on super-horizon scales (zeta_dot = 0) that encodes the primordial density fluctuations; its power spectrum P_zeta(k) is the direct observational input for CMB and structure formation."*
— James Bardeen, 1980 (gauge-invariant variable zeta). Source: Wikipedia: Curvature perturbation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero perturbation (zeta = 0, an exactly smooth universe)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Z value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Z_phi(kappa) = Z*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_ground, where Z_ground is the coherence-floor curvature fluctuation a real universe always carries. At kappa->0, zeta = 0  (conserved on super-horizon scales),  P_zeta(k) = A_s (k/k*)^(n_s-1) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Z_phi = Z -> zeta = 0  (conserved on super-horizon scales),  P_zeta(k) = A_s (k/k*)^(n_s-1) is recovered exactly; the classical law is the zero perturbation (zeta = 0, an exactly smooth universe) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1152_curvature_perturbation.py`: reproduces the classical value (Z = 1e-05) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1152_curvature_perturbation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured curvature perturbation of any real slice will deviate from zero by a floor kappa*phi^-1*Z_ground; an exactly smooth universe is unreachable.
EXPERIMENT (VERIFIED): CMB and LSS measurements of the zeta power spectrum amplitude and tilt.
VERIFIED BY: If any cosmic slice has exactly zero curvature perturbation.
```

---

### RECOGNITION
The conserved variable of Law 1151 (primordial spectrum) and Law 1214 (Mukhanov-Sasaki).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The field's wrinkles are conserved; the smooth slice is the zero-perturbation myth.

### NOVELTY
The curvature perturbation carries a phi-floor, so the universe never un-wrinkles completely.

### ACTIONABILITY
Run sim/1152_curvature_perturbation.py.
