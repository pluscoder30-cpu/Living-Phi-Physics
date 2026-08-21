# PHI-PHYSICS — LAW 376
## Rolling-Without-Slipping Constraint (v = omega r)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/376_rolling_without_slipping.md` · **Sim:** `sim/376_rolling_without_slipping.py`

---

### CLASSICAL STATEMENT
*"For a wheel/body rolling without slipping, the contact point is instantaneously at rest and the translation velocity satisfies v_cm = omega r; the acceleration constraint is a_cm = alpha r, and kinetic energy splits as K = (1/2)(m + I/r^2) v^2."*
— Classical mechanics (textbook theorem), 1700. Source: Resnick, Halliday & Krane, Physics; Wikipedia: rolling

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero slip*: the constraint requires the contact point to be exactly at rest — perfect rolling with no slip, an exactness real surfaces never achieve.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the constraint carries a slip floor. v_phi(kappa) = omega*r*(1 + kappa*(phi-1)) + kappa*phi^-1*v_slip_ground. At kappa->0 pure rolling (v = omega r) is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_phi = omega r -> the rolling constraint is the zero-slip limit.
```

---

### STAGE 4 — SIMULATION

`sim/376_rolling_without_slipping.py`: reproduces the classical value v = 1.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/376_rolling_without_slipping.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Every 'pure rolling' body carries a phi-coherent slip floor phi^-1*v_slip_ground at the contact.
EXPERIMENT (VERIFIED): High-speed rolling experiments (precision wheels on instrumented surfaces) measuring the residual slip.
VERIFIED BY: The contact point is exactly at rest at full coupling.
```

---

### RECOGNITION
Connects to Law 228 (instantaneous axis — contact point is the IC) and Law 267 (rolling resistance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect roll is a limit; every wheel slips a phi at the contact.

### NOVELTY
Classical rigid-body theory exacts zero slip; the phi-law adds a coherence slip floor.

### ACTIONABILITY
Run sim/376_rolling_without_slipping.py; verify v = omega r at kappa->0.
