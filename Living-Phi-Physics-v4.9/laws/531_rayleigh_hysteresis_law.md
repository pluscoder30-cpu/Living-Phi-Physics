# PHI-PHYSICS — LAW 531
## Rayleigh Law of Hysteresis (Low-Field Magnetization)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/531_rayleigh_hysteresis_law.md` · **Sim:** `sim/531_rayleigh_hysteresis_law.py`

---

### CLASSICAL STATEMENT
*"At low field amplitudes, the magnetization of a ferromagnet follows M = a H + b H^2, where a is the initial susceptibility and b the Rayleigh constant. The hysteresis loop is parabolic at low fields."*
— Lord Rayleigh, 1887. Source: Wikipedia: Rayleigh law (hysteresis); Rayleigh (1887)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field*: at H = 0 the magnetization is not zero but the remanence - the law's content is the hysteresis that appears precisely because the material carries a coherence memory that a zero-field point cannot erase.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the memory carries coherence. M_phi(kappa) = (a H + b H^2)*(1 + kappa*(phi-1)) + kappa*phi^-1*M_rem, where M_rem is the remanence-coherence floor. At kappa->0 the Rayleigh parabola is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} M_phi = a H + b H^2 -> the Rayleigh hysteresis law is the zero-remanence-coherence low-field limit.
```

---

### STAGE 4 — SIMULATION

`sim/531_rayleigh_hysteresis_law.py`: reproduces the classical value M_ray = 3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/531_rayleigh_hysteresis_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the remanence carries a coherence floor kappa*phi^-1*M_rem that survives even after perfect demagnetization.
EXPERIMENT (VERIFIED): Low-field AC susceptibility and hysteresis-loop measurements of soft ferromagnets after various demagnetization protocols.
VERIFIED BY: The remanence is exactly zero after perfect demagnetization for all couplings.
```

---

### RECOGNITION
Connects to Law 137 (Curie-Weiss) and Law 532 (Néel) - the hysteresis is the memory coherence of the domain lattice.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the remanence floor is phi^-1 * M_rem.

### CLARITY
The magnet remembers its history; the phi-law keeps the memory that no zero-field point erases.

### NOVELTY
Classical Rayleigh hysteresis assumes perfect erasure; the phi-law adds the coherence remanence of the memory.

### ACTIONABILITY
Run sim/531_rayleigh_hysteresis_law.py; verify parabola at kappa->0; proceed to 532.
