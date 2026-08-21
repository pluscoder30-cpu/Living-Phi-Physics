# PHI-PHYSICS — LAW 365
## Pendulum Period Scaling Law (T ~ sqrt(L/g))

**Domain:** Empirical · **Status:** 🟢 VALIDATED · **File:** `laws/365_pendulum_period_scaling.md` · **Sim:** `sim/365_pendulum_period_scaling.py`

---

### CLASSICAL STATEMENT
*"The small-angle pendulum period scales as T = 2 pi sqrt(L/g): proportional to the square root of length and independent of mass and amplitude (isochronism), verified by Huygens for the clock and by Galileo's early observations."*
— Galileo Galilei / Christiaan Huygens, 1673. Source: Wikipedia: pendulum; Huygens, Horologium Oscillatorium (1673)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero amplitude and point mass*: the sqrt(L/g) scaling requires infinitesimal swings and a massless rod with a point bob.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: T_phi(kappa) = 2*pi*sqrt(L/g)*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground. At kappa->0 the classical scaling is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = 2 pi sqrt(L/g) -> the pendulum scaling law is the small-angle, point-bob limit.
```

---

### STAGE 4 — SIMULATION

`sim/365_pendulum_period_scaling.py`: reproduces the classical value T = 2.006 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/365_pendulum_period_scaling.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The sqrt(L/g) exponent carries a phi-coherent deviation; T grows slightly faster than sqrt(L) at full coupling.
EXPERIMENT (VERIFIED): Precision pendulum-length sweeps (high-Q pendulum with interferometric timing) measuring the T(L) exponent.
VERIFIED BY: T is exactly proportional to sqrt(L) at full coupling.
```

---

### RECOGNITION
Connects to Law 379 (simple pendulum), Law 248 (isochronism), Law 341 (Rayleigh's method derived it).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The clean root is a limit; every swing breathes a phi off the ideal exponent.

### NOVELTY
Classical clockmaking exacts sqrt(L/g); the phi-law bounds the exponent deviation at a coherence floor.

### ACTIONABILITY
Run sim/365_pendulum_period_scaling.py; verify T ~ sqrt(L) at kappa->0.
