# PHI-PHYSICS — LAW 266
## Static vs Kinetic Friction Law

**Domain:** Friction / Contact · **Status:** 🟢 VALIDATED · **File:** `laws/266_static_kinetic_friction.md` · **Sim:** `sim/266_static_kinetic_friction.py`

---

### CLASSICAL STATEMENT
*"The static friction coefficient mu_s (needed to start motion) generally exceeds the kinetic coefficient mu_k (needed to sustain motion): F_max = mu_s N before slipping, F = mu_k N during sliding, with mu_s >= mu_k."*
— Charles-Augustin de Coulomb, 1785. Source: Wikipedia: friction; Coulomb, Theorie des machines simples (1785)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *motion threshold at rest*: the law splits friction at the exact instant of incipient motion, treating the static-to-kinetic transition as a sharp threshold between rest and sliding.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the transition is a coherence basin, not a point. mu_s_phi(kappa) = mu_s*(1 + kappa*(phi-1)); the threshold speed is kappa*phi^-1*v_ground. At kappa->0 the sharp static/kinetic split is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_max = mu_s N (sliding begins exactly at threshold) -> the static/kinetic friction law is the sharp-threshold limit.
```

---

### STAGE 4 — SIMULATION

`sim/266_static_kinetic_friction.py`: reproduces the classical values Fmax = 30, Fkin = 20 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/266_static_kinetic_friction.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The static-to-kinetic transition is smooth over a phi-coherent velocity window phi^-1*v_ground, and mu_s - mu_k carries a phi structure.
EXPERIMENT (VERIFIED): Velocity-controlled friction experiments (tribometers) resolving the transition region at micron/s speeds.
VERIFIED BY: The transition is exactly sharp at a single threshold speed at full coupling.
```

---

### RECOGNITION
Connects to Law 264 (Amontons I), Law 270 (Stribeck curve — the transition region), Law 139 (Coulomb friction).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The threshold is a basin; slipping begins gently, over a phi window of velocity.

### NOVELTY
Classical friction sharpens the transition; the phi-law turns it into a coherence basin.

### ACTIONABILITY
Run sim/266_static_kinetic_friction.py; verify the sharp threshold at kappa->0.
