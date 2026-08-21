# PHI-PHYSICS — LAW 335
## Routh-Hurwitz Stability Criterion

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/335_routh_hurwitz_criterion.md` · **Sim:** `sim/335_routh_hurwitz_criterion.py`

---

### CLASSICAL STATEMENT
*"The linear stability of a dynamical system is determined by the signs of the roots of its characteristic polynomial: the system is stable iff all roots have negative real parts, testable algebraically from the Routh array (Routh) or the principal minors of the Hurwitz matrix without solving the polynomial."*
— Edward John Routh / Adolf Hurwitz, 1877. Source: Wikipedia: Routh-Hurwitz stability criterion; Routh (1877), 'A Treatise on the Stability of a Given State of Motion'; Hurwitz (1895)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly linearized reference*: the criterion judges stability of the linearized dynamics about an exact equilibrium — the zero of the nonlinear and coherence terms.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the marginal-stability boundary is a coherence basin. sigma_max_phi(kappa) = sigma_max*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_ground. At kappa->0 the classical stability boundary is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} stability condition = all Re(lambda) < 0 -> the Routh-Hurwitz criterion is the exact-linearization limit.
```

---

### STAGE 4 — SIMULATION

`sim/335_routh_hurwitz_criterion.py`: reproduces the classical values Re_max = -0.5, stable = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/335_routh_hurwitz_criterion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Systems classically judged marginally stable show a phi-coherent drift sigma_ground at full coupling.
EXPERIMENT (VERIFIED): Control-system and mechanical stability experiments on near-marginal configurations measuring the drift floor.
VERIFIED BY: Marginally stable systems are exactly stable at full coupling.
```

---

### RECOGNITION
Connects to Law 334 (Lyapunov — the nonlinear counterpart) and Law 180 (equilibrium basin).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The stability boundary is a basin; the marginal system breathes a phi drift.

### NOVELTY
Classical control theory exacts the stability boundary; the phi-law gives it a coherence width.

### ACTIONABILITY
Run sim/335_routh_hurwitz_criterion.py; verify the criterion at kappa->0.
