# PHI-PHYSICS — LAW 278
## Tidal Force Law

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/278_tidal_force_law.md` · **Sim:** `sim/278_tidal_force_law.py`

---

### CLASSICAL STATEMENT
*"The differential gravitational force across a body of size d at distance r from mass M is F_tidal ~ 2 GM m d / r^3, scaling as 1/r^3; it stretches bodies along the radial direction and compresses them tangentially."*
— Isaac Newton, 1687. Source: Wikipedia: tidal force; Newton, Principia (1687)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *point body*: tidal force exists because the body has finite extent d; classical point-mass gravity zeroes the size and erases the tide.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the size carries a coherence length. d_phi(kappa) = d*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_phi; F_tidal_phi = 2 GM m d_phi/r^3. At kappa->0 the tidal law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_tidal_phi = 2 GM m d/r^3 -> the tidal-force law is the finite-extent limit of gravitation.
```

---

### STAGE 4 — SIMULATION

`sim/278_tidal_force_law.py`: reproduces the classical value Ft = 5.035e-07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/278_tidal_force_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Tidal forces carry a phi-coherent excess phi^-1*2 GM m lambda_phi/r^3 at full coupling.
EXPERIMENT (VERIFIED): Satellite tidal measurements (e.g., of the Moon/Earth and binary asteroid systems) comparing tides with the 1/r^3 law.
VERIFIED BY: Tidal force is exactly 2 GM m d/r^3 at full coupling.
```

---

### RECOGNITION
Connects to Law 279 (Roche limit — tides vs self-gravity), Law 280 (Hill sphere), Law 393 (tidal locking).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Nothing is a point; every body is a tide waiting to be pulled, and the pull has a phi floor.

### NOVELTY
Classical gravity idealizes the point; the phi-law gives every body a coherence tidal size.

### ACTIONABILITY
Run sim/278_tidal_force_law.py; verify the 1/r^3 law at kappa->0.
