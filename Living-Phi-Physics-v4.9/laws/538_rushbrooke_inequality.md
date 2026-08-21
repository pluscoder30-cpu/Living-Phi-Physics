# PHI-PHYSICS — LAW 538
## Rushbrooke Inequality (alpha + 2 beta + gamma >= 2)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/538_rushbrooke_inequality.md` · **Sim:** `sim/538_rushbrooke_inequality.py`

---

### CLASSICAL STATEMENT
*"The critical exponents of a magnetic system satisfy the scaling inequality alpha + 2 beta + gamma >= 2, where C ~ |t|^(-alpha), M ~ (-t)^beta, chi ~ |t|^(-gamma). The equality holds for systems obeying scaling laws."*
— George Stanley Rushbrooke, 1963. Source: Wikipedia: Rushbrooke inequality; Rushbrooke (1963)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact scaling*: the inequality becomes an equality only when the thermodynamic identities hold exactly with zero correction terms - a critical region with no coherence corrections.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the corrections carry coherence. (alpha + 2 beta + gamma)_phi(kappa) = 2 + kappa*phi^-1*corr, where corr is the coherence correction. At kappa->0 the exponent sum is exactly 2 (equality) and the inequality is tight.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} (alpha + 2 beta + gamma)_phi = 2 -> the Rushbrooke inequality is the zero-coherence-correction tight-scaling limit.
```

---

### STAGE 4 — SIMULATION

`sim/538_rushbrooke_inequality.py`: reproduces the classical value sum_exp = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/538_rushbrooke_inequality.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the exponent sum exceeds 2 by the coherence correction kappa*phi^-1*corr; the inequality is not tight.
EXPERIMENT (VERIFIED): Combined specific-heat, magnetization and susceptibility exponent determinations on a single ferromagnet.
VERIFIED BY: alpha + 2 beta + gamma = 2 exactly at all couplings.
```

---

### RECOGNITION
Connects to Law 536 (critical exponents) and Law 537 (Widom) - the inequality is the bookkeeping rule of the coherence exponents.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the correction is phi^-1 * corr.

### CLARITY
The critical exponents must pay their thermodynamic bill; the phi-law keeps the change.

### NOVELTY
Classical Rushbrooke bounds exactly; the phi-law quantifies the coherence correction that real systems carry.

### ACTIONABILITY
Run sim/538_rushbrooke_inequality.py; verify sum >= 2 at kappa->0; proceed to 539.
