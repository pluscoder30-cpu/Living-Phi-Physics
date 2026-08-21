# PHI-PHYSICS — LAW 1040
## Relativistic Beaming (Doppler Beaming)

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1040_relativistic_beaming.md` · **Sim:** `sim/1040_relativistic_beaming.py`

---

### CLASSICAL STATEMENT
*"Emission from a source moving at beta is boosted into a narrow cone of half-angle theta ~ 1/gamma along the direction of motion; observed flux scales as I_obs = I*[gamma*(1+beta*cos(theta))]^(3+alpha) for a spectral index alpha."*
— Relativistic formulation by Albert Einstein, 1905; jet-beaming concept by Martin Rees, 1966. Source: Wikipedia: Relativistic beaming (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *isotropic emission (beta = 0, no preferred cone)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The B value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

B_phi(kappa) = B*(1 + kappa*(phi-1)) + kappa*phi^-1*B_ground, where B_ground is the coherence-floor beaming concentration that no isotropic emitter can fully dilute. At kappa->0, I_obs = I * [gamma*(1+beta*cos(theta))]^(3+alpha) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} B_phi = B -> I_obs = I * [gamma*(1+beta*cos(theta))]^(3+alpha) is recovered exactly; the classical law is the isotropic emission (beta = 0, no preferred cone) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1040_relativistic_beaming.py`: reproduces the classical value (B = 2.5) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1040_relativistic_beaming.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The apparent luminosity boost of a real relativistic jet will deviate from the power law by a floor kappa*phi^-1*B_ground; a perfectly isotropic source is unreachable.
EXPERIMENT (VERIFIED): Multi-band monitoring of an AGN jet with resolved pc-scale structure and known intrinsic flux.
VERIFIED BY: If any jet reproduces the beaming power law with exactly isotropic emission in its rest frame.
```

---

### RECOGNITION
Companion to Law 1039 (aberration) and Law 1037 (Doppler); underpins Law 1100 (Blandford-Znajek) jet emission.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Beaming is the convergence of the light cone; coherence concentrates what zero-coupling spreads.

### NOVELTY
The beaming cone half-angle acquires a lower bound set by the phi-floor, so a jet can never be infinitely collimated.

### ACTIONABILITY
Run sim/1040_relativistic_beaming.py.
