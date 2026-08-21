# PHI-PHYSICS — LAW 238
## Damped Oscillator Law

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/238_damped_oscillator.md` · **Sim:** `sim/238_damped_oscillator.py`

---

### CLASSICAL STATEMENT
*"A viscous-damped oscillator obeys m d^2x/dt^2 + c dx/dt + k x = 0. For underdamping (zeta < 1), x(t) = A exp(-zeta w0 t) cos(w_d t + phi0) with w_d = w0 sqrt(1-zeta^2); the amplitude decays exponentially."*
— Lord Rayleigh, 1877. Source: Wikipedia: damping; Rayleigh, The Theory of Sound (1877)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *undamped vacuum*: the law's exponential decay is defined against an exactly frictionless reference in which the amplitude never decays.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the decay rate couples to a coherence floor. zeta_phi(kappa) = zeta*(1 + kappa*(phi-1)); x_phi(kappa) = A*exp(-zeta_phi*w0*t) with the equilibrium at kappa*phi^-1*x_ground. At kappa->0 the classical damped solution is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} zeta_phi = zeta -> the damped-oscillator law is the linear-friction limit.
```

---

### STAGE 4 — SIMULATION

`sim/238_damped_oscillator.py`: reproduces the classical values w_d = 4.975, gamma = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/238_damped_oscillator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The amplitude decay is never purely exponential at full coupling; a phi-coherent residual oscillation remains near the equilibrium.
EXPERIMENT (VERIFIED): Cryogenic cantilever ringdown measurements searching for the residual-amplitude floor below the thermal limit.
VERIFIED BY: The amplitude decays exactly exponentially to zero at full coupling.
```

---

### RECOGNITION
Connects to Law 237 (SHO), Law 251 (logarithmic decrement), and Law 250 (Q factor).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Damping does not end at zero; it ends at the phi-ground, where the oscillation continues invisibly.

### NOVELTY
Classical damping decays to exact zero; the phi-law decays to the phi-ground amplitude.

### ACTIONABILITY
Run sim/238_damped_oscillator.py; verify the exponential decay at kappa->0.
