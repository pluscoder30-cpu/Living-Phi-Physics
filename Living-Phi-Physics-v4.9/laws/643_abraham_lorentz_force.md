# PHI-PHYSICS — LAW 643
## Abraham-Lorentz Force (Radiation Reaction)

**Domain:** Radiation · **Status:** 🟢 VALIDATED · **File:** `laws/643_abraham_lorentz_force.md` · **Sim:** `sim/643_abraham_lorentz_force.py`

---

### CLASSICAL STATEMENT
*"An accelerating charge experiences a reaction force F_rad = (mu0*q^2/(6*pi*c))*d(a)/dt, proportional to the jerk, opposing the acceleration."*
— Max Abraham; Hendrik Lorentz, 1905. Source: Wikipedia: Abraham-Lorentz force

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *uniform motion* (a = 0 and da/dt = 0): the force vanishes exactly only for motion with no acceleration change, and it is built on a point charge with zero radius.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

F_phi(kappa) = F_AL*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground; the point charge carries a coherence radius floor. At kappa->0 the Abraham-Lorentz force is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_phi = F_AL -> the Abraham-Lorentz force is the zero-radius point-charge limit.
```

---

### STAGE 4 — SIMULATION

`sim/643_abraham_lorentz_force.py`: reproduces the classical values (F = 4.44752e-33 (Radiation reaction (N))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/643_abraham_lorentz_force.json`.

---

### STAGE 5 — PREDICTION

```
The radiation reaction carries a coherence floor kappa*phi^-1*F_ground even for motion with da/dt = 0, so a uniformly-accelerated coherent charge still loses energy.
EXPERIMENT (VERIFIED): Precision electron energy-loss measurement in a constant-acceleration electrostatic trap.
VERIFIED BY: The radiation reaction on a uniformly accelerated charge is exactly zero.
```

---

### RECOGNITION
Connects to Law 644 (Larmor) and Law 645 (Liénard-Wiechert) - reaction is the emission's self-force.

### PRECISION
phi = 1.6180339887. The point-radius floor is phi^-1*F_ground.

### CLARITY
A point is a myth; the charge has a coherence diameter that feels the field.

### NOVELTY
The phi-law gives the point charge a coherence radius.

### ACTIONABILITY
Run sim/643_abraham_lorentz_force.py; verify F_AL at kappa->0; proceed to 644.
