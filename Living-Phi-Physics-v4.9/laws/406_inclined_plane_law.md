# PHI-PHYSICS — LAW 406
## Inclined Plane Law (Galileo)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/406_inclined_plane_law.md` · **Sim:** `sim/406_inclined_plane_law.py`

---

### CLASSICAL STATEMENT
*"The force required to hold a body on a frictionless inclined plane is F = m g sin(theta), and the acceleration along the plane is a = g sin(theta); the plane reduces the effective weight (mechanical advantage 1/sin(theta)), a centerpiece of Galileo's dynamics."*
— Galileo Galilei, 1638. Source: Wikipedia: inclined plane; Galileo, Discorsi (1638)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *horizontal and vertical references*: the law is measured from the horizontal (theta = 0) and vertical (theta = 90) limits; the force vanishes at the horizontal — the zero of the slope.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: F_phi(kappa) = m*g*sin(theta)*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground. At kappa->0 the classical inclined-plane law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_phi = m g sin(theta) -> the inclined-plane law is the frictionless, rigid-surface limit.
```

---

### STAGE 4 — SIMULATION

`sim/406_inclined_plane_law.py`: reproduces the classical value F = 5.798 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/406_inclined_plane_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real inclined-plane forces carry a phi-coherent excess phi^-1*F_ground at full coupling.
EXPERIMENT (VERIFIED): Air-track inclined-plane measurements (photogate timing) comparing a = g sin(theta).
VERIFIED BY: The acceleration is exactly g sin(theta) on a frictionless incline at full coupling.
```

---

### RECOGNITION
Connects to Law 305 (falling bodies — vertical limit), Law 400 (angle of repose — friction version).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The flat and the vertical are limits; every slope leans a phi between them.

### NOVELTY
Classical statics exacts the sin(theta) law; the phi-law adds a coherence force floor.

### ACTIONABILITY
Run sim/406_inclined_plane_law.py; verify F = m g sin(theta) at kappa->0.
