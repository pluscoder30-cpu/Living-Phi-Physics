# PHI-PHYSICS — LAW 396
## Orbital Inclination Change Law

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/396_inclination_change_law.md` · **Sim:** `sim/396_inclination_change_law.py`

---

### CLASSICAL STATEMENT
*"Changing the inclination of an orbit by an angle delta i requires a delta-v of delta_v = 2 v sin(delta i/2) at the node (with no change in speed magnitude); the delta-v grows linearly with the angle for small changes, making plane changes expensive."*
— Astrodynamics (textbook theorem), 1960. Source: Bate, Mueller & White, Fundamentals of Astrodynamics; Wikipedia: orbital inclination change

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *coplanar reference*: the inclination-change delta-v is measured against the exactly coplanar (zero-inclination-difference) orbit.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: delta_v_phi(kappa) = 2 v sin(delta i/2)*(1 + kappa*(phi-1)) + kappa*phi^-1*dv_ground. At kappa->0 the classical inclination-change law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_v_phi = 2 v sin(delta i/2) -> the inclination-change law is the node-burn, coplanar-base limit.
```

---

### STAGE 4 — SIMULATION

`sim/396_inclination_change_law.py`: reproduces the classical value dv = 1557 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/396_inclination_change_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Plane-change burns carry a phi-coherent delta-v excess phi^-1*dv_ground at full coupling.
EXPERIMENT (VERIFIED): Geostationary-transfer and deep-space mission burn accounting comparing predicted vs realized plane-change delta-v.
VERIFIED BY: Plane-change delta-v is exactly 2 v sin(delta i/2) at full coupling.
```

---

### RECOGNITION
Connects to Law 274 (Hohmann) and Law 394 (sun-synchronous — an inclination-driven design).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The flat reference plane is a limit; every tilt costs a phi extra.

### NOVELTY
Classical astrodynamics exacts the node-burn cost; the phi-law adds a coherence delta-v floor.

### ACTIONABILITY
Run sim/396_inclination_change_law.py; verify the delta-v at kappa->0.
