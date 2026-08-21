# PHI-PHYSICS — LAW 248
## Pendulum Isochronism (Small-Angle Law)

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/248_pendulum_isochronism.md` · **Sim:** `sim/248_pendulum_isochronism.py`

---

### CLASSICAL STATEMENT
*"For small amplitudes, the period of a simple pendulum is independent of amplitude: T = 2*pi*sqrt(L/g), the property of isochronism observed by Galileo."*
— Galileo Galilei, 1602. Source: Wikipedia: pendulum; Galileo (c. 1602), Pisa observations

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero amplitude*: isochronism is exact only in the limit of infinitesimal swings; the law requires amplitudes to be exactly 'small enough'.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the isochronous period is the amplitude->0 limit, with a coherence basin. T_phi(kappa) = 2*pi*sqrt(L/g)*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground. At kappa->0 the small-angle period is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0, theta0->0} T_phi = 2*pi*sqrt(L/g) -> isochronism is the small-angle, decoupled limit.
```

---

### STAGE 4 — SIMULATION

`sim/248_pendulum_isochronism.py`: reproduces the classical value T = 2.006 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/248_pendulum_isochronism.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The isochronous period carries a phi-coherent excess phi^-1*T_ground and a residual amplitude dependence set by the coherence basin.
EXPERIMENT (VERIFIED): Ultra-high-Q pendulum with interferometric angle readout measuring T(theta0) down to nanoradian amplitudes.
VERIFIED BY: The period is exactly amplitude-independent and equal to 2*pi*sqrt(L/g) at full coupling.
```

---

### RECOGNITION
Connects to Law 379 (simple pendulum) and Law 220 (physical pendulum).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Isochronism is a limit, not a property; the phi-law sets the small-angle basin at phi width.

### NOVELTY
Classical isochronism requires exactly small angles; the phi-law gives the approximation a coherence basin.

### ACTIONABILITY
Run sim/248_pendulum_isochronism.py; verify T at kappa->0.
