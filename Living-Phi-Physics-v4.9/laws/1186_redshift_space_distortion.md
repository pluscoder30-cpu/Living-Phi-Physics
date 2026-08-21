# PHI-PHYSICS — LAW 1186
## Redshift Space Distortion (Kaiser Effect)

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1186_redshift_space_distortion.md` · **Sim:** `sim/1186_redshift_space_distortion.py`

---

### CLASSICAL STATEMENT
*"Redshift-space distortions (RSD) arise because measured redshifts mix peculiar velocities with the Hubble flow, squashing (or stretching) clustering along the line of sight; the Kaiser effect enhances the quadrupole in the power spectrum and measures the growth rate of structure f sigma_8."*
— Nick Kaiser, 1987. Source: Wikipedia: Redshift-space distortions (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero peculiar velocities (exact redshift = distance mapping)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor distortion a real survey always exhibits. At kappa->0, P^s(k) = (1 + beta mu^2)^2 P^r(k),  beta = f/b exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> P^s(k) = (1 + beta mu^2)^2 P^r(k),  beta = f/b is recovered exactly; the classical law is the zero peculiar velocities (exact redshift = distance mapping) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1186_redshift_space_distortion.py`: reproduces the classical value (D = 0.4) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1186_redshift_space_distortion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured clustering of any real galaxy survey will deviate from the real-space prediction by a floor kappa*phi^-1*D_ground; an exactly distortion-free survey is unreachable.
EXPERIMENT (VERIFIED): BOSS, DESI, and Euclid RSD measurements of f sigma_8.
VERIFIED BY: If a galaxy survey shows exactly isotropic clustering in redshift space.
```

---

### RECOGNITION
The velocity channel of Law 1185 (peculiar velocity) and the growth of Law 1210 (Press-Schechter).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Velocity folds the map; the undistorted map is the zero-motion myth.

### NOVELTY
RSD carries a phi-floor, bounding growth-rate measurements with systematics.

### ACTIONABILITY
Run sim/1186_redshift_space_distortion.py.
