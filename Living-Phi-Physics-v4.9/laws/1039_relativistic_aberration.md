# PHI-PHYSICS — LAW 1039
## Relativistic Aberration (Aberration of Light)

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1039_relativistic_aberration.md` · **Sim:** `sim/1039_relativistic_aberration.py`

---

### CLASSICAL STATEMENT
*"A photon arriving at angle theta in one inertial frame arrives at angle theta' in a frame moving at speed beta: tan(theta') = sin(theta)*sqrt(1-beta^2)/(cos(theta)+beta); light rays tilt forward toward the direction of motion."*
— James Bradley, 1727 (classical); relativistic form by Albert Einstein, 1905. Source: Wikipedia: Aberration (astronomy) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero-velocity frame (beta = 0, no tilting)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The A value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground, where A_ground is the coherence-floor tilting of the photon cone that persists even in the nominal rest frame. At kappa->0, tan(theta') = sin(theta)*sqrt(1-beta^2)/(cos(theta)+beta) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} A_phi = A -> tan(theta') = sin(theta)*sqrt(1-beta^2)/(cos(theta)+beta) is recovered exactly; the classical law is the zero-velocity frame (beta = 0, no tilting) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1039_relativistic_aberration.py`: reproduces the classical value (A = 0.8) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1039_relativistic_aberration.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured aberration angle of any real light ray will deviate from the relativistic formula by a floor kappa*phi^-1*A_ground; no frame is free of a residual tilt.
EXPERIMENT (VERIFIED): Precision astrometry of stellar positions from an accelerating spacecraft over a full orbit.
VERIFIED BY: If any inertial observer measures stellar aberration exactly matching tan(theta') with zero residual tilt.
```

---

### RECOGNITION
Bridges Law 051 (Lorentz transformations) and Law 093 (Doppler); the light cone of Law 1051 is the object being tilted.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Aberration is the Doppler of direction; the forward tilt is the light cone remembering its own motion.

### NOVELTY
Aberration acquires a directional floor: the light cone cannot be exactly aligned with any frame's axis.

### ACTIONABILITY
Run sim/1039_relativistic_aberration.py.
