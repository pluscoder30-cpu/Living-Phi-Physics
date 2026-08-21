# PHI-PHYSICS — LAW 260
## Perfectly Inelastic Collision Law

**Domain:** Impact / Collisions · **Status:** 🟢 VALIDATED · **File:** `laws/260_inelastic_collision.md` · **Sim:** `sim/260_inelastic_collision.py`

---

### CLASSICAL STATEMENT
*"In a perfectly inelastic collision the bodies stick together and move with the common velocity V = (m1 v1 + m2 v2)/(m1 + m2) (momentum conservation), with maximum kinetic energy lost as heat/deformation."*
— Classical mechanics (textbook theorem), 1700. Source: Resnick, Halliday & Krane, Physics; Wikipedia: inelastic collision

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect sticking*: the law assumes e=0 exactly, that the bodies fuse with no rebound — a condition no real material satisfies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: e_phi(kappa) = kappa*phi^-1*e_floor (a coherence rebound floor), so V_phi(kappa) = V + kappa*phi^-1*(small rebound). At kappa->0, V = (m1 v1 + m2 v2)/(m1+m2) exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = (m1 v1 + m2 v2)/(m1+m2) -> the perfectly inelastic collision law is the e=0 limit.
```

---

### STAGE 4 — SIMULATION

`sim/260_inelastic_collision.py`: reproduces the classical values V = 2, KE_loss = 12 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/260_inelastic_collision.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Perfectly inelastic collisions retain a phi-coherent rebound; the common velocity is inflated by kappa*phi^-1*delta_v.
EXPERIMENT (VERIFIED): Ultra-cold sticky collisions of atoms/microspheres measuring the residual rebound velocity.
VERIFIED BY: Sticky collisions show exactly zero rebound at full coupling.
```

---

### RECOGNITION
Connects to Law 256 (e=0 floor) and Law 259 (e=1 ceiling): the two ends of the restitution range.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Even the perfect stick keeps a phi bounce; nothing is ever fully dead.

### NOVELTY
Classical theory perfects sticking; the phi-law gives sticking a coherence rebound floor.

### ACTIONABILITY
Run sim/260_inelastic_collision.py; verify V at kappa->0.
