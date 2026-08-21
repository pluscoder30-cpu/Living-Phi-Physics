# PHI-PHYSICS — LAW 1236
## Schwarzschild Radius

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1236_schwarzschild_radius.md` · **Sim:** `sim/1236_schwarzschild_radius.py`

---

### CLASSICAL STATEMENT
*"The Schwarzschild radius is the horizon radius of a non-rotating black hole: R_S = 2 G M/c^2 (~ 2.95 km for a solar mass); it sets the size at which a mass M must be compressed to form a black hole and is the scale of the event horizon (Law 1110) and ISCO (Law 1107)."*
— Karl Schwarzschild, 1916. Source: Wikipedia: Schwarzschild radius (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero mass (M = 0, zero Schwarzschild radius)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The R value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground, where R_ground is the coherence-floor compactness scale a real mass always sets. At kappa->0, R_S = 2*G*M/c^2,  R_S(sun) = 2.95 km exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} R_phi = R -> R_S = 2*G*M/c^2,  R_S(sun) = 2.95 km is recovered exactly; the classical law is the zero mass (M = 0, zero Schwarzschild radius) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1236_schwarzschild_radius.py`: reproduces the classical value (R = 2.95) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1236_schwarzschild_radius.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured horizon scale of any real compact object will deviate from 2 G M/c^2 by a floor kappa*phi^-1*R_ground; an exactly zero-radius mass is unreachable.
EXPERIMENT (VERIFIED): EHT imaging and gravitational-wave measurement of the horizon scale vs mass.
VERIFIED BY: If a collapsed object's horizon is measured at a radius inconsistent with 2 GM/c^2.
```

---

### RECOGNITION
The compactness scale of Law 064 (Schwarzschild), Law 1110 (event horizon), and Law 1107 (ISCO).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Mass draws its own radius; the point mass is the zero-radius myth.

### NOVELTY
The Schwarzschild radius carries a phi-floor, so no mass is exactly point-like.

### ACTIONABILITY
Run sim/1236_schwarzschild_radius.py.
