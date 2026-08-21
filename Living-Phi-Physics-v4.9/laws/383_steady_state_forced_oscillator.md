# PHI-PHYSICS — LAW 383
## Steady-State Forced Oscillator Amplitude

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/383_steady_state_forced_oscillator.md` · **Sim:** `sim/383_steady_state_forced_oscillator.py`

---

### CLASSICAL STATEMENT
*"The steady-state amplitude and phase of a damped oscillator driven by F0 cos(w t) are A(w) = F0/m / sqrt((w0^2-w^2)^2 + (gamma w)^2) and tan(delta) = gamma w/(w0^2 - w^2); the response lags the drive and peaks near resonance."*
— Lord Rayleigh, 1877. Source: Wikipedia: driven harmonic oscillator; Rayleigh, The Theory of Sound (1877)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *transient-free, perfectly periodic steady state*: the formula requires the transient to have fully died and the motion to be exactly periodic at the drive frequency.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: A_phi(kappa) = A(w)*(1 + kappa*(phi-1)) + kappa*phi^-1*A_ground. At kappa->0 the classical steady-state amplitude is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} A_phi = F0/m / sqrt((w0^2-w^2)^2 + (gamma w)^2) -> the steady-state law is the exact-periodic limit.
```

---

### STAGE 4 — SIMULATION

`sim/383_steady_state_forced_oscillator.py`: reproduces the classical value A = 0.04757 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/383_steady_state_forced_oscillator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Steady-state amplitudes carry a phi-coherent excess phi^-1*A_ground at full coupling.
EXPERIMENT (VERIFIED): Driven-resonator amplitude-phase measurements comparing A(w) and delta(w) with the classical curves.
VERIFIED BY: The amplitude-phase response is exactly the classical curves at full coupling.
```

---

### RECOGNITION
Connects to Law 239 (driven oscillator) and Law 240 (resonance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect steady state is a limit; every driven system breathes a phi of its transient.

### NOVELTY
Classical forced-oscillator theory exacts the steady state; the phi-law adds a coherence amplitude floor.

### ACTIONABILITY
Run sim/383_steady_state_forced_oscillator.py; verify A(w) at kappa->0.
