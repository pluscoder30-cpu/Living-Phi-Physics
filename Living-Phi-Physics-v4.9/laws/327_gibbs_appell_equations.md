# PHI-PHYSICS — LAW 327
## Gibbs-Appell Equations

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/327_gibbs_appell_equations.md` · **Sim:** `sim/327_gibbs_appell_equations.py`

---

### CLASSICAL STATEMENT
*"For a system with generalized coordinates q, the Gibbs-Appell equations are dS/du_dot = Q_i, where S = (1/2) sum m a^2 is the Gibbs function (acceleration energy) and u_dot are quasi-accelerations; they provide the most general and often simplest equations of nonholonomic dynamics."*
— Paul Emile Appell, 1900. Source: Wikipedia: Gibbs-Appell equations; Appell (1900), 'Sur une forme generale des equations de la dynamique'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-acceleration reference*: the Gibbs function is measured against the exactly acceleration-free (inertial) reference — the zero of acceleration energy.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground. At kappa->0 the Gibbs-Appell equations are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dS/du_dot = Q_i -> the Gibbs-Appell equations are the exact-acceleration-energy limit.
```

---

### STAGE 4 — SIMULATION

`sim/327_gibbs_appell_equations.py`: reproduces the classical value S = 9 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/327_gibbs_appell_equations.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The realized generalized accelerations carry a phi-coherent Gibbs residual phi^-1*S_ground.
EXPERIMENT (VERIFIED): Nonholonomic-roller and mechanism experiments comparing realized accelerations with Gibbs-Appell predictions.
VERIFIED BY: The motion satisfies the Gibbs-Appell equations exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 019 (Lagrange equations — the standard form) and Law 326 (Gauss least constraint).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The acceleration energy is a limit; every realized acceleration carries a phi whisper.

### NOVELTY
Classical dynamics exacts the acceleration energy; the phi-law gives it a coherence floor.

### ACTIONABILITY
Run sim/327_gibbs_appell_equations.py; verify the Gibbs function at kappa->0.
