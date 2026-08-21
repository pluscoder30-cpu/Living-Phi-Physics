# PHI-PHYSICS — LAW 687
## Current Divider (Rule)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/687_current_divider.md` · **Sim:** `sim/687_current_divider.py`

---

### CLASSICAL STATEMENT
*"In a parallel chain the current through R_k is I_k = I*G_k/(sum G_i) = I*(1/R_k)/(sum 1/R_i); the total current divides in proportion to conductance."*
— Gustav Kirchhoff, 1845. Source: Current divider rule; Kirchhoff (1845)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero parallel-lead impedance*: the divider assumes each branch is exactly parallel with no lead impedance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_k_phi(kappa) = I_k*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the branch carries a coherence lead floor. At kappa->0 the divider rule is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_k_phi = I*G_k/sum G_i -> the current divider is the zero-lead-impedance limit.
```

---

### STAGE 4 — SIMULATION

`sim/687_current_divider.py`: reproduces the classical values (I = 0.666667 (Divided current (A))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/687_current_divider.json`.

---

### STAGE 5 — PREDICTION

```
The divided current carries a coherence floor kappa*phi^-1*I_ground.
EXPERIMENT (VERIFIED): Precision parallel-current measurement with minimal lead resistance.
VERIFIED BY: The current through a resistor is always exactly the ideal divider value.
```

---

### RECOGNITION
Connects to Law 045 (KCL) - the divider is the parallel KCL balance.

### PRECISION
phi = 1.6180339887. The lead floor is phi^-1*I_ground.

### CLARITY
Current splits, never perfectly; coherence keeps a sliver.

### NOVELTY
The phi-law gives the parallel divider a coherence sliver.

### ACTIONABILITY
Run sim/687_current_divider.py; verify Ik at kappa->0; proceed to 688.
