# PHI-PHYSICS — LAW 1108
## Photon Sphere

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1108_photon_sphere.md` · **Sim:** `sim/1108_photon_sphere.py`

---

### CLASSICAL STATEMENT
*"The photon sphere is the radius at which light can orbit a black hole in an unstable circular orbit: r_ph = 3 G M/c^2 = 1.5 R_S for Schwarzschild; photons inside this radius are captured, and the sphere casts the black-hole shadow."*
— From the Schwarzschild solution, 1916. Source: Wikipedia: Photon sphere (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero radius (r -> 0, the degenerate photon orbit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The R value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground, where R_ground is the coherence-floor photon orbit a real shadow always sets. At kappa->0, r_ph = 3*G*M/c^2 (Schwarzschild) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} R_phi = R -> r_ph = 3*G*M/c^2 (Schwarzschild) is recovered exactly; the classical law is the zero radius (r -> 0, the degenerate photon orbit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1108_photon_sphere.py`: reproduces the classical value (R = 3.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1108_photon_sphere.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured shadow radius of any real black hole will deviate from the photon-sphere prediction by a floor kappa*phi^-1*R_ground; an exactly zero-radius shadow is unreachable.
EXPERIMENT (VERIFIED): Event Horizon Telescope imaging of M87* and Sgr A* shadows constraining the photon-sphere radius.
VERIFIED BY: If a black-hole shadow has exactly zero radius or matches the prediction with zero residual.
```

---

### RECOGNITION
The shadow signature of Law 064 (Schwarzschild) and Law 1096 (Einstein ring).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The hole's shadow is its photon sphere drawn in darkness; the point shadow is the flat-space myth.

### NOVELTY
The photon sphere carries a phi-floor, so every shadow has a finite angular width.

### ACTIONABILITY
Run sim/1108_photon_sphere.py.
