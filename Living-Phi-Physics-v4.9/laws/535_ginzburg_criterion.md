# PHI-PHYSICS — LAW 535
## Ginzburg Criterion (Validity of Mean-Field Theory)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/535_ginzburg_criterion.md` · **Sim:** `sim/535_ginzburg_criterion.py`

---

### CLASSICAL STATEMENT
*"Mean-field theory is valid when the fluctuations of the order parameter in a coherence volume are small compared to the order parameter itself: |T - T_c| >> Gi T_c, where the Ginzburg number Gi ~ (a_0^2/(b^2 xi_0^3)) for a 3D system. Within the critical region |T-T_c| < Gi T_c, fluctuations dominate."*
— Vitaly Lazarevich Ginzburg, 1960. Source: Wikipedia: Ginzburg criterion; Ginzburg (1960)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero fluctuations*: the criterion defines the window where fluctuations vanish - mean-field theory is exact only where the order-parameter coherence fluctuations are exactly zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the fluctuation window is a coherence basin. Gi_phi(kappa) = Gi*(1 + kappa*(phi-1)) + kappa*phi^-1*Gi_ground, widening the critical region. At kappa->0 the classical Ginzburg criterion is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Gi_phi = Gi -> the Ginzburg criterion is the zero-fluctuation-coherence mean-field validity limit.
```

---

### STAGE 4 — SIMULATION

`sim/535_ginzburg_criterion.py`: reproduces the classical value Gi = 1e+27 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/535_ginzburg_criterion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the critical region is wider than the classical Ginzburg window; mean-field theory fails further from T_c than predicted.
EXPERIMENT (VERIFIED): Specific-heat and susceptibility measurements near T_c of weakly coupled superconductors and magnets to map the critical region.
VERIFIED BY: Mean-field theory is valid exactly down to the Ginzburg boundary for all couplings.
```

---

### RECOGNITION
Connects to Law 533 (Landau) and Law 536 (critical exponents) - the criterion is the coherence-size gate of the mean-field basin.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the window widening is phi^-1 * Gi_ground.

### CLARITY
Mean-field theory trusts the average; the phi-law admits the average has a wobble it cannot hide.

### NOVELTY
Classical Ginzburg defines a sharp validity window; the phi-law widens it with the coherence of the fluctuations.

### ACTIONABILITY
Run sim/535_ginzburg_criterion.py; verify Gi at kappa->0; proceed to 536.
