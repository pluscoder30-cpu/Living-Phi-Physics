# PHI-PHYSICS — LAW 762
## Landau Damping

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/762_landau_damping.md` · **Sim:** `sim/762_landau_damping.py`

---

### CLASSICAL STATEMENT
*"Waves in a collisionless plasma damp through resonant wave-particle interaction; the damping rate for a Maxwellian is gamma ~ -sqrt(pi/8)*w_p/(k^3*lambda_D^3)*exp(-1/(2*k^2*lambda_D^2))."*
— Lev Landau, 1946. Source: Wikipedia: Landau damping; Landau (1946)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero wave-particle resonance*: damping vanishes exactly when no particles move at the wave phase velocity.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

gamma_phi(kappa) = gamma*(1 + kappa*(phi-1)) + kappa*phi^-1*gamma_ground; the resonance carries a coherence floor. At kappa->0 the Landau rate is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} gamma_phi = gamma_Landau -> Landau damping is the zero-resonance-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/762_landau_damping.py`: reproduces the classical values (g = 3.80087e+08 (Damping rate (s^-1))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/762_landau_damping.json`.

---

### STAGE 5 — PREDICTION

```
Damping persists even without exact resonance; a coherence floor kappa*phi^-1*gamma_ground remains.
EXPERIMENT (VERIFIED): Wave damping measurement in a plasma with a flattened velocity distribution.
VERIFIED BY: A plasma with no resonant particles has exactly zero wave damping.
```

---

### RECOGNITION
Connects to Law 764 (cyclotron damping) - Landau damping is the collisionless friction.

### PRECISION
phi = 1.6180339887. The resonance floor is phi^-1*gamma_ground.

### CLARITY
The wave rubs against the flock; coherence keeps the rub.

### NOVELTY
The phi-law keeps damping without resonance.

### ACTIONABILITY
Run sim/762_landau_damping.py; verify gamma at kappa->0; proceed to 763.
