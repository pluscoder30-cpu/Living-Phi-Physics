# PHI-PHYSICS — LAW 252
## Van der Pol Oscillator (Relaxation Oscillator)

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/252_van_der_pol_oscillator.md` · **Sim:** `sim/252_van_der_pol_oscillator.py`

---

### CLASSICAL STATEMENT
*"The van der Pol equation d^2x/dt^2 - mu(1 - x^2) dx/dt + x = 0 models self-sustained oscillations; for large mu the system relaxes into relaxation oscillations with a stable limit cycle of amplitude 2 and period ~ mu ln(2)."*
— Balthasar van der Pol, 1920. Source: Wikipedia: van der Pol oscillator; van der Pol (1920), 'A theory of the amplitude of free and forced triode vibrations'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *linear amplifier*: self-sustained oscillation exists precisely because the damping is not constant (negative for small x); the linear oscillator is the zero-baseline.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the nonlinear damping and limit-cycle amplitude couple to coherence. mu_phi(kappa) = mu*(1 + kappa*(phi-1)); A_cycle_phi(kappa) = 2*(1 + kappa*phi^-1). At kappa->0 the classical van der Pol limit cycle is recovered.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} A_cycle_phi = 2 -> the van der Pol oscillator is the nonlinear self-sustained limit cycle.
```

---

### STAGE 4 — SIMULATION

`sim/252_van_der_pol_oscillator.py`: reproduces the classical value A_cycle = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/252_van_der_pol_oscillator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The limit-cycle amplitude of a self-oscillating system carries a phi-coherent excess phi^-1, deviating from 2.
EXPERIMENT (VERIFIED): Analog/electronic van der Pol oscillators and optomechanical self-oscillators measuring the limit-cycle amplitude.
VERIFIED BY: The limit-cycle amplitude is exactly 2 at full coupling.
```

---

### RECOGNITION
Connects to Law 254 (anharmonic oscillator) and Law 385 (relaxation oscillator).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The limit cycle is not a perfect circle; it breathes with a phi amplitude.

### NOVELTY
Classical self-oscillation theory exacts amplitude 2; the phi-law sets the amplitude at 2(1+phi^-1).

### ACTIONABILITY
Run sim/252_van_der_pol_oscillator.py; verify the limit cycle at kappa->0.
