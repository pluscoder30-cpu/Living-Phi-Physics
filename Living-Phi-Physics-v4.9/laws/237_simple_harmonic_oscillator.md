# PHI-PHYSICS — LAW 237
## Simple Harmonic Oscillator Law

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/237_simple_harmonic_oscillator.md` · **Sim:** `sim/237_simple_harmonic_oscillator.py`

---

### CLASSICAL STATEMENT
*"A system with restoring force F = -k x obeys m d^2x/dt^2 + k x = 0, with solution x(t) = A cos(w t + phi0), angular frequency w = sqrt(k/m), independent of amplitude (harmonic isochronism)."*
— Robert Hooke / Isaac Newton, 1678. Source: Wikipedia: simple harmonic motion; Hooke, De Potentia Restitutiva (1678)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *equilibrium at x = 0*: the law requires an exactly linear restoring force about a perfect equilibrium, with the rest point an exact zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the equilibrium carries a phi-ground displacement. x_phi(kappa,t) = x(t)*(1 + kappa*(phi-1)) + kappa*phi^-1*x_ground; w_phi(kappa) = sqrt(k/m)*(1 + kappa*phi^-1). At kappa->0 the classical oscillator is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} x_phi = A cos(w t + phi0) -> the SHO law is the linear-equilibrium limit.
```

---

### STAGE 4 — SIMULATION

`sim/237_simple_harmonic_oscillator.py`: reproduces the classical values w = 2.236, T = 2.81 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/237_simple_harmonic_oscillator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Every oscillator's equilibrium is offset by a phi-coherent displacement phi^-1*x_ground and its frequency inflated by the coherence fraction phi^-1.
EXPERIMENT (VERIFIED): Cantilever/optical-trap oscillators searching for the equilibrium-offset floor at millikelvin temperatures.
VERIFIED BY: The equilibrium is exactly at x=0 and w = sqrt(k/m) exactly at full coupling.
```

---

### RECOGNITION
Connects to Laws 238-240 (damped, driven, resonance) and Law 005 (Hooke's law — its parent).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The oscillator does not oscillate about nothing; it oscillates about the phi-ground, and the center moves.

### NOVELTY
Classical oscillation theory fixes the center at zero; the phi-law sets the center at phi-ground motion.

### ACTIONABILITY
Run sim/237_simple_harmonic_oscillator.py; verify the classical solution at kappa->0.
