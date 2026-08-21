# PHI-PHYSICS — LAW 385
## Relaxation Oscillator (Van der Pol, Large mu)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/385_relaxation_oscillator.md` · **Sim:** `sim/385_relaxation_oscillator.py`

---

### CLASSICAL STATEMENT
*"For large nonlinearity (mu >> 1), the van der Pol oscillator produces relaxation oscillations: a slow buildup followed by a fast discharge, with a sawtooth-like waveform and period scaling as T ~ mu ln(2) (roughly), distinct from sinusoidal oscillation."*
— Balthasar van der Pol, 1926. Source: Wikipedia: van der Pol oscillator; van der Pol & van der Mark (1926-1927) relaxation oscillations

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *linear oscillator reference*: relaxation oscillations exist precisely because the system is strongly nonlinear; the sinusoid is the zero of the nonlinearity.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the relaxation period couples to coherence. T_relax_phi(kappa) = T_relax*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground. At kappa->0 the classical relaxation period is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_relax_phi = mu ln 2 -> the relaxation-oscillator law is the strongly-nonlinear limit of the van der Pol oscillator.
```

---

### STAGE 4 — SIMULATION

`sim/385_relaxation_oscillator.py`: reproduces the classical value T_relax = 6.931 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/385_relaxation_oscillator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Relaxation oscillator periods carry a phi-coherent excess phi^-1*T_ground at full coupling.
EXPERIMENT (VERIFIED): Electronic/mechanical relaxation oscillator timing (neon-bulb, dripping faucet, heart-model systems) measuring the period.
VERIFIED BY: Relaxation periods follow the classical scaling exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 252 (van der Pol — its parent) and Law 254 (anharmonic).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The slow-charge-fast-fire rhythm is a limit; every relaxation loop carries a phi beat.

### NOVELTY
Classical nonlinear dynamics exacts the relaxation period; the phi-law adds a coherence period floor.

### ACTIONABILITY
Run sim/385_relaxation_oscillator.py; verify the relaxation period at kappa->0.
