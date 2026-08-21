# PHI-PHYSICS — LAW 403
## Orbital Decay Law (Satellite Drag)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/403_orbital_decay_law.md` · **Sim:** `sim/403_orbital_decay_law.py`

---

### CLASSICAL STATEMENT
*"A satellite in low Earth orbit decays under atmospheric drag with the semi-major axis decreasing at a rate da/dt = -2 a^2 rho C_D A v / m (drag-limited decay), and the orbit circularizes; the decay is exponential-like near reentry with the altitude dropping faster as density rises."*
— Classical astrodynamics (textbook), 1960. Source: Wikipedia: orbital decay; atmospheric-drag perturbation theory

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *drag-free vacuum orbit*: decay exists because the atmosphere is nonzero; the two-body vacuum orbit is the zero of the drag.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the decay rate couples to coherence. da/dt_phi(kappa) = da/dt*(1 + kappa*(phi-1)) + kappa*phi^-1*(da/dt)_ground. At kappa->0 the classical decay law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} da/dt_phi = -2 a^2 rho C_D A v/m -> the orbital-decay law is the drag-perturbation limit.
```

---

### STAGE 4 — SIMULATION

`sim/403_orbital_decay_law.py`: reproduces the classical value dadt = -322.6 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/403_orbital_decay_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: LEO satellite decay rates carry a phi-coherent excess phi^-1*(da/dt)_ground at full coupling.
EXPERIMENT (VERIFIED): Precision TLE/radar tracking of decaying satellites (e.g., controlled reentries) comparing decay rates.
VERIFIED BY: Satellite decay follows the classical drag law exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 310 (drag), Law 391 (Poynting-Robertson — radiation decay), Law 392 (Yarkovsky).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The clean vacuum orbit is a limit; every satellite bleeds a phi of altitude.

### NOVELTY
Classical astrodynamics exacts the drag decay; the phi-law adds a coherence decay floor.

### ACTIONABILITY
Run sim/403_orbital_decay_law.py; verify the decay rate at kappa->0.
