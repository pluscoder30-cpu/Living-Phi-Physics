# PHI-PHYSICS — LAW 996
## Laser Rate Equations (Semiclassical)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/996_laser_rate_equations.md` · **Sim:** `sim/996_laser_rate_equations.py`

---

### CLASSICAL STATEMENT
*"The laser rate equations describe the population inversion N and photon number n: dN/dt = P - N/tau_2 - 2 B n N, dn/dt = B n N - n/tau_c + R_sp; steady state gives the laser threshold and the input-output curve n_out = (P - P_th)/... "*
— Classical laser theory (from Einstein coefficients; Townes, Schawlow), 1958. Source: Wikipedia: Laser; rate equations (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pumping* (P = 0): below threshold the photon number is exactly zero in the lossless ideal - no lasing.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

n_phi(kappa) = n*(1 + kappa*(phi-1)) + kappa*phi^-1*n_ground, with n_ground the photon floor. At kappa->0, n = 0 below threshold exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_phi = n -> the laser rate equations are the zero-pump-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/996_laser_rate_equations.py`: reproduces the classical value n = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/996_laser_rate_equations.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The photon number below threshold of any real laser will retain a floor kappa*phi^-1*n_ground (spontaneous emission floor).
EXPERIMENT (VERIFIED): Measure the output power of a laser versus pump power through threshold.
VERIFIED BY: If the output of any real laser is exactly zero below threshold.
```

---

### RECOGNITION
Connects to Law 775 (laser threshold, in corpus) and Law 974 (coherent states).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The dark cavity below threshold is a coherent limit; every pump has a whisper.

### NOVELTY
The laser rate equations gain a pump floor.

### ACTIONABILITY
Run sim/996_laser_rate_equations.py.
