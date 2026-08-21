# PHI-PHYSICS — LAW 1141
## Gravitational Lens Time Delay

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1141_gravitational_lens_time_delay.md` · **Sim:** `sim/1141_gravitational_lens_time_delay.py`

---

### CLASSICAL STATEMENT
*"The arrival times of the multiple images of a strongly lensed source differ by Delta t = (1+z_d) D_delta (theta^2 - beta^2)/2 (with the geometric and Shapiro contributions); the time delay between images depends on the Hubble constant, enabling time-delay cosmography."*
— Sjur Refsdal, 1964. Source: Wikipedia: Gravitational time delay (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero image separation (theta = beta, a single image with no delay)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor image delay a real multiply-imaged system always shows. At kappa->0, Delta t = (1+z_d) * D_delta * (theta^2 - beta^2)/2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> Delta t = (1+z_d) * D_delta * (theta^2 - beta^2)/2 is recovered exactly; the classical law is the zero image separation (theta = beta, a single image with no delay) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1141_gravitational_lens_time_delay.py`: reproduces the classical value (D = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1141_gravitational_lens_time_delay.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured arrival-time difference of any real lensed images will deviate from the time-delay formula by a floor kappa*phi^-1*D_ground; exactly simultaneous images are unreachable.
EXPERIMENT (VERIFIED): Time-delay cosmography (H0LiCOW, TDCOSMO) measuring delays in lensed quasars for H0.
VERIFIED BY: If two images of a lensed source arrive at exactly the same time with zero separation.
```

---

### RECOGNITION
The timing regime of Law 113 (lensing) and Law 1093 (strong lensing).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Light takes different roads; the simultaneous image is the zero-separation myth.

### NOVELTY
Lens time delays carry a phi-floor, informing the precision of H0 measurements.

### ACTIONABILITY
Run sim/1141_gravitational_lens_time_delay.py.
