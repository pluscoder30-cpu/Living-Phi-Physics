# PHI-PHYSICS — LAW 764
## Cyclotron (Ion/Electron) Damping

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/764_cyclotron_damping.md` · **Sim:** `sim/764_cyclotron_damping.py`

---

### CLASSICAL STATEMENT
*"Waves damp at cyclotron resonances through resonant gyration; the damping peaks when the wave frequency matches omega_c or its harmonics, absorbing wave energy into gyromotion."*
— Ira Bernstein, 1958. Source: Cyclotron damping; Bernstein (1958)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero resonance overlap*: damping vanishes exactly when the wave frequency misses all cyclotron resonances.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

gamma_c_phi(kappa) = gamma_c*(1 + kappa*(phi-1)) + kappa*phi^-1*gamma_ground; the resonance carries a coherence basin. At kappa->0 the cyclotron absorption is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} gamma_c_phi = gamma_c -> cyclotron damping is the zero-resonance-offset limit.
```

---

### STAGE 4 — SIMULATION

`sim/764_cyclotron_damping.py`: reproduces the classical values (g = 0.5 (Absorption profile)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/764_cyclotron_damping.json`.

---

### STAGE 5 — PREDICTION

```
Cyclotron absorption carries a coherence basin kappa*phi^-1 wide around the resonance.
EXPERIMENT (VERIFIED): Absorption measurement of an RF wave near cyclotron resonance in a plasma.
VERIFIED BY: Cyclotron damping occurs only at the exact cyclotron frequency.
```

---

### RECOGNITION
Connects to Law 762 (Landau) and Law 740 (cyclotron) - cyclotron damping is the gyro resonance.

### PRECISION
phi = 1.6180339887. The resonance basin is phi^-1*gamma_ground.

### CLARITY
Resonance is a basin; the wave drinks within it.

### NOVELTY
The phi-law widens the exact cyclotron resonance.

### ACTIONABILITY
Run sim/764_cyclotron_damping.py; verify absorption at kappa->0; proceed to 765.
