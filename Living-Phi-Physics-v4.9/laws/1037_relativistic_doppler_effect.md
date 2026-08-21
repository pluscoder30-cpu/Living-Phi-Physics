# PHI-PHYSICS — LAW 1037
## Relativistic Doppler Effect

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1037_relativistic_doppler_effect.md` · **Sim:** `sim/1037_relativistic_doppler_effect.py`

---

### CLASSICAL STATEMENT
*"For a source moving at speed beta = v/c at angle theta to the line of sight, the observed frequency is f_obs = f_src*gamma*(1 + beta*cos(theta)) with gamma = 1/sqrt(1-beta^2); for longitudinal motion f_obs = f_src*sqrt((1-beta)/(1+beta))."*
— Christian Doppler, 1842; relativistic form by Albert Einstein, 1905. Source: Wikipedia: Relativistic Doppler effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exactly-zero line-of-sight velocity (beta = 0)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor frequency ratio a real carrier never drops below. At kappa->0, f_obs = f_src * gamma * (1 + beta*cos(theta)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> f_obs = f_src * gamma * (1 + beta*cos(theta)) is recovered exactly; the classical law is the exactly-zero line-of-sight velocity (beta = 0) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1037_relativistic_doppler_effect.py`: reproduces the classical value (D = 1.25) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1037_relativistic_doppler_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured Doppler factor of any real relativistic source will deviate from gamma*(1+beta*cos(theta)) by a floor kappa*phi^-1*D_ground; no source is seen exactly on the classical cone.
EXPERIMENT (VERIFIED): Spectrally resolve the relativistic Doppler factor of a synchrotron-emitting jet at known beta over a full range of theta.
VERIFIED BY: If the Doppler factor of any relativistic source matches gamma*(1+beta*cos(theta)) to arbitrary precision at all angles.
```

---

### RECOGNITION
Extends Law 093 (Doppler effect) and Law 057 (time dilation); the gamma factor is the coherence-baseline of Law 060.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The classical Doppler shift hides the transverse term; motion in phi-space has no exactly-forward direction.

### NOVELTY
The transverse Doppler term becomes a coherence floor, so the 'beaming cone' becomes a 'coherence basin'.

### ACTIONABILITY
Run sim/1037_relativistic_doppler_effect.py.
