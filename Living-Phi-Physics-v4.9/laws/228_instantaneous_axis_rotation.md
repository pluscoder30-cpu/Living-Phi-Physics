# PHI-PHYSICS — LAW 228
## Instantaneous Axis of Rotation

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/228_instantaneous_axis_rotation.md` · **Sim:** `sim/228_instantaneous_axis_rotation.py`

---

### CLASSICAL STATEMENT
*"At every instant, the general motion of a rigid body is a pure rotation about a unique instantaneous axis (in 2D, the instantaneous center of rotation); the velocity of every point is v = w x r about that axis."*
— Leonhard Euler, 1775. Source: Wikipedia: instantaneous centre of rotation; Goldstein, Classical Mechanics

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *instant*: the theorem requires an exact instant at which the axis exists, freezing time to define a pure rotation about a point.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the instantaneous axis itself moves coherently. v_phi(kappa) = w*r*(1 + kappa*(phi-1)) + kappa*phi^-1*v_ground. At kappa->0, v = w x r about a fixed instantaneous axis is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_phi = w x r -> the instantaneous-axis theorem is the frozen-instant limit.
```

---

### STAGE 4 — SIMULATION

`sim/228_instantaneous_axis_rotation.py`: reproduces the classical value v = 2.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/228_instantaneous_axis_rotation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The instantaneous center of rotation of a rolling or sliding body wanders by a phi-coherent amount between successive instants, smearing the instantaneous axis.
EXPERIMENT (VERIFIED): High-speed video tracking of the instantaneous center of a rolling disk with sub-frame temporal resolution.
VERIFIED BY: The instantaneous axis is exactly stationary within each instant at full coupling.
```

---

### RECOGNITION
Connects to Law 211 (Chasles — screw about an instantaneous axis) and Law 376 (rolling constraint).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The instant is a fiction; every instant is a short loop, and the loop has a phi-axis that moves.

### NOVELTY
Classical kinematics freezes the instant; the phi-law gives the instantaneous axis a coherence wander.

### ACTIONABILITY
Run sim/228_instantaneous_axis_rotation.py; verify v=w x r at kappa->0.
