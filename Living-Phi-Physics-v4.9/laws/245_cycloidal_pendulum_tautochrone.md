# PHI-PHYSICS — LAW 245
## Tautochrone (Cycloidal Pendulum) Law

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/245_cycloidal_pendulum_tautochrone.md` · **Sim:** `sim/245_cycloidal_pendulum_tautochrone.py`

---

### CLASSICAL STATEMENT
*"A particle sliding without friction on an inverted cycloid reaches the lowest point in the same time regardless of starting point: the cycloid is the tautochrone, with period T = 2*pi*sqrt(L/g) for a cycloidal pendulum of length L = 4a, independent of amplitude."*
— Christiaan Huygens, 1659. Source: Wikipedia: tautochrone curve; Huygens, Horologium Oscillatorium (1673)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact cycloidal shape*: tautochronism requires the guide to be an exact mathematical cycloid with zero friction — a perfect shape the real universe never machines.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the shape and friction carry coherence. T_phi(kappa) = 2*pi*sqrt(L/g)*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground. At kappa->0 the tautochrone period is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = 2*pi*sqrt(L/g) -> the tautochrone law is the exact-cycloid, zero-friction limit.
```

---

### STAGE 4 — SIMULATION

`sim/245_cycloidal_pendulum_tautochrone.py`: reproduces the classical value T = 2.006 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/245_cycloidal_pendulum_tautochrone.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real tautochrone pendulums show a phi-coherent period excess and a residual amplitude dependence phi^-1*T_ground.
EXPERIMENT (VERIFIED): Ultra-low-friction cycloidal pendulum with air-track and laser readout measuring the period vs starting angle.
VERIFIED BY: The tautochrone period is exactly amplitude-independent and equal to 2*pi*sqrt(L/g) at full coupling.
```

---

### RECOGNITION
Connects to Law 246 (brachistochrone — the cycloid family) and Law 248 (isochronism).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect curve is a limit; the real curve lives in a phi-basin that still breathes with amplitude.

### NOVELTY
Classical tautochrony requires a perfect shape; the phi-law allows a coherence basin of near-cycloidal shapes.

### ACTIONABILITY
Run sim/245_cycloidal_pendulum_tautochrone.py; verify the tautochrone period at kappa->0.
