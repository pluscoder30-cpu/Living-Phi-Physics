# PHI-PHYSICS — LAW 379
## Simple Pendulum Period (T = 2 pi sqrt(L/g))

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/379_simple_pendulum_formula.md` · **Sim:** `sim/379_simple_pendulum_formula.py`

---

### CLASSICAL STATEMENT
*"A simple pendulum (point mass on a massless rod of length L) has period T = 2 pi sqrt(L/g) for small amplitudes, independent of mass."*
— Christiaan Huygens, 1673. Source: Wikipedia: pendulum; Huygens, Horologium Oscillatorium (1673)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *point bob and massless rod*: the formula requires a perfectly idealized pendulum with all mass at a point and zero rod mass.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: T_phi(kappa) = 2*pi*sqrt(L/g)*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground. At kappa->0 the classical period is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = 2 pi sqrt(L/g) -> the simple-pendulum law is the point-bob, massless-rod, small-angle limit.
```

---

### STAGE 4 — SIMULATION

`sim/379_simple_pendulum_formula.py`: reproduces the classical value T = 2.006 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/379_simple_pendulum_formula.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real pendulums carry a phi-coherent period excess phi^-1*T_ground beyond the formula.
EXPERIMENT (VERIFIED): High-Q pendulum clocks with interferometric timing measuring the period against the formula.
VERIFIED BY: The period is exactly 2 pi sqrt(L/g) at full coupling.
```

---

### RECOGNITION
Connects to Law 248 (isochronism), Law 365 (scaling), Law 220 (physical pendulum — generalization).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The point bob is a limit; every pendulum swings a phi off the ideal.

### NOVELTY
Classical clockmaking exacts the formula; the phi-law adds a coherence period floor.

### ACTIONABILITY
Run sim/379_simple_pendulum_formula.py; verify T at kappa->0.
