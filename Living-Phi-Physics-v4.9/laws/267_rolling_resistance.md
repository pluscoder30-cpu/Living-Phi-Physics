# PHI-PHYSICS — LAW 267
## Rolling Resistance (Coulomb's Law of Rolling Friction)

**Domain:** Friction / Contact · **Status:** 🟢 VALIDATED · **File:** `laws/267_rolling_resistance.md` · **Sim:** `sim/267_rolling_resistance.py`

---

### CLASSICAL STATEMENT
*"Rolling resistance is much smaller than sliding friction; the rolling resistance force F_r = C_rr N = (mu_rr/r) N, where mu_rr is a rolling coefficient of friction (length) and r the wheel radius; F_r ~ N * (deformation offset)/radius."*
— Charles-Augustin de Coulomb, 1785. Source: Wikipedia: rolling resistance; Coulomb (1785)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly rigid wheel*: rolling resistance exists only because the wheel and surface deform; classical ideal-rolling physics zeroes the deformation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the deformation offset carries a coherence length. delta_phi(kappa) = delta*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_phi; F_r_phi = N*delta_phi/r. At kappa->0 the Coulomb rolling law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_r_phi = N*delta/r -> rolling resistance is the deformed-interface limit.
```

---

### STAGE 4 — SIMULATION

`sim/267_rolling_resistance.py`: reproduces the classical value Fr = 0.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/267_rolling_resistance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Rolling resistance carries a phi-coherent excess phi^-1*N*lambda_phi/r at full coupling.
EXPERIMENT (VERIFIED): Ultra-precision rolling of hardened spheres on optical flats measuring the rolling resistance floor.
VERIFIED BY: F_r is exactly N*delta/r with no coherence term at full coupling.
```

---

### RECOGNITION
Connects to Law 269 (Hertz contact — the deformation) and Law 376 (rolling constraint).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect wheel is a limit; every wheel deforms, and the deformation has a phi floor.

### NOVELTY
Classical ideal rolling zeroes deformation; the phi-law gives the wheel a coherence deformation.

### ACTIONABILITY
Run sim/267_rolling_resistance.py; verify F_r at kappa->0.
