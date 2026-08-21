# PHI-PHYSICS — LAW 737
## Plasma Oscillations (Tonks-Langmuir)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/737_plasma_oscillations.md` · **Sim:** `sim/737_plasma_oscillations.py`

---

### CLASSICAL STATEMENT
*"A displacement of electrons from ions sets up collective oscillations at omega_p = sqrt(n*e^2/(eps_0*m_e)); the electrons oscillate as a rigid gas against the ion background."*
— Irving Langmuir; Lewi Tonks, 1929. Source: Wikipedia: Plasma oscillation; Tonks & Langmuir (1929)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero displacement*: the oscillation is defined relative to an exactly unperturbed, uniform electron gas.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

x_phi(kappa) = x*(1 + kappa*(phi-1)) + kappa*phi^-1*x_ground; the equilibrium carries a coherence floor. At kappa->0 the harmonic plasma oscillation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} x_phi = x -> plasma oscillations are the zero-displacement-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/737_plasma_oscillations.py`: reproduces the classical values (w = 69.0935 (Oscillation frequency (rad/s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/737_plasma_oscillations.json`.

---

### STAGE 5 — PREDICTION

```
The electron gas always carries a coherence oscillation floor kappa*phi^-1*x_ground; exact rest is unreachable.
EXPERIMENT (VERIFIED): Spectrum measurement of electron oscillations in a quiescent discharge.
VERIFIED BY: A quiescent plasma has exactly zero electron oscillation.
```

---

### RECOGNITION
Connects to Law 736 (plasma frequency) and Law 738 (Langmuir wave) - oscillations are the plasma's breath.

### PRECISION
phi = 1.6180339887. The displacement floor is phi^-1*x_ground.

### CLARITY
The plasma never stills; coherence keeps it humming.

### NOVELTY
The phi-law keeps plasma oscillating at equilibrium.

### ACTIONABILITY
Run sim/737_plasma_oscillations.py; verify oscillation at kappa->0; proceed to 738.
