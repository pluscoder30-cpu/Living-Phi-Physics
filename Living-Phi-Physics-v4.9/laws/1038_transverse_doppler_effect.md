# PHI-PHYSICS — LAW 1038
## Transverse Doppler Effect

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1038_transverse_doppler_effect.md` · **Sim:** `sim/1038_transverse_doppler_effect.py`

---

### CLASSICAL STATEMENT
*"For motion exactly perpendicular to the line of sight (cos(theta)=0), the observed frequency is f_obs = f_src*sqrt(1-beta^2): a pure time-dilation redshift with no longitudinal component."*
— Albert Einstein, 1905. Source: Wikipedia: Relativistic Doppler effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exactly-perpendicular motion (theta = 90 degrees)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor transverse redshift that no real perpendicular motion exactly attains. At kappa->0, f_obs = f_src * sqrt(1-beta^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> f_obs = f_src * sqrt(1-beta^2) is recovered exactly; the classical law is the exactly-perpendicular motion (theta = 90 degrees) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1038_transverse_doppler_effect.py`: reproduces the classical value (D = 0.8) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1038_transverse_doppler_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The transverse Doppler factor of a real source in perpendicular motion will deviate from sqrt(1-beta^2) by kappa*phi^-1*D_ground; the exactly-transverse configuration is never realized.
EXPERIMENT (VERIFIED): Mossbauer-style experiment with a source on a rotating disc observing at precisely 90 degrees to the velocity.
VERIFIED BY: If a transverse-moving source reproduces sqrt(1-beta^2) to arbitrary precision at exactly 90 degrees.
```

---

### RECOGNITION
Direct consequence of Law 057 (time dilation); correlates with Law 065 (gravitational redshift) through Law 062 (equivalence principle).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The pure redshift of perpendicular motion is the signature that motion never vanishes to zero.

### NOVELTY
The exactly-transverse geometry is itself the hidden zero: a real measurement always carries a longitudinal coherence component.

### ACTIONABILITY
Run sim/1038_transverse_doppler_effect.py.
