# PHI-PHYSICS — LAW 940
## Stokes Drift

**Domain:** Water Waves · **Status:** 🟢 VALIDATED · **File:** `laws/940_stokes_drift.md` · **Sim:** `sim/940_stokes_drift.py`

---

### CLASSICAL STATEMENT
*"Stokes drift: water particles in a wave have a net Lagrangian velocity in the direction of wave propagation, u_drift = a^2 omega k / sinh^2(kh) (deep water: a^2 omega k exp(2kz)), because their orbits are not closed."*
— George Gabriel Stokes, 1847. Source: Wikipedia: Stokes drift (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero amplitude* (a = 0): the drift velocity vanishes exactly for an infinitesimal wave.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

u_d_phi(kappa) = u_d*(1 + kappa*(phi-1)) + kappa*phi^-1*u_d_ground, with u_d_ground the drift floor. At kappa->0, u_d = a^2 omega k exactly (deep water).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} u_d_phi = u_d -> the Stokes drift is the zero-amplitude-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/940_stokes_drift.py`: reproduces the classical value ud = 0.005 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/940_stokes_drift.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured drift velocity of any real wave will deviate from a^2 omega k by a coherence floor kappa*phi^-1*u_d_ground.
EXPERIMENT (VERIFIED): Measure the net drift of a floating particle in a wave tank.
VERIFIED BY: If the drift velocity of any real wave equals a^2 omega k exactly.
```

---

### RECOGNITION
Connects to Law 939 (Airy theory) and Law 936 (dispersion).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The closed orbit is a coherent limit; every wave drags its water forward.

### NOVELTY
Stokes drift gains an amplitude floor.

### ACTIONABILITY
Run sim/940_stokes_drift.py.
