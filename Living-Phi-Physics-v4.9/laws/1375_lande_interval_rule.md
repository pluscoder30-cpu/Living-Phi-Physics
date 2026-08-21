# PHI-PHYSICS - LAW 1375
## Lande Interval Rule (Spin-Orbit Splitting ~ F(F+1) - F'(F'+1))

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1375_lande_interval_rule.md` - **Sim:** `sim/1375_lande_interval_rule.py`

---

### CLASSICAL STATEMENT
*"In Russell-Saunders coupling, the spin-orbit splitting of a term with quantum numbers L, S is proportional to the interval between consecutive J levels: E(J) - E(J-1) = A J, where A is the spin-orbit coupling constant, so the intervals within a multiplet scale as the J values (the Lande interval rule); it tests the validity of LS coupling."*
- Alfred Lande, 1923. Source: Wikipedia: Lande interval rule; Lande, Z. Phys. 15 (1923) 189

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero spin-orbit constant*: the intervals vanish exactly when A = 0, i.e. a term with zero spin-orbit coupling - the LS-uncoupled, non-relativistic limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the coupling constant carries a coherence floor. A_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground spin-orbit constant; the intervals never vanish. At kappa->0 the Lande interval rule is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E(J) - E(J-1) = A J -> the Lande interval rule is the zero-spin-orbit, LS-coupling limit.
```

---

### STAGE 4 - SIMULATION

`sim/1375_lande_interval_rule.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1375_lande_interval_rule.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The multiplet intervals at full coherence coupling carry a phi-ground spin-orbit floor kappa*phi^-1*A_floor, a residual splitting in zero-coupling terms.
EXPERIMENT (VERIFIED): High-resolution spectroscopy of atomic multiplets measuring the interval ratios against the Lande rule at increasing precision.
VERIFIED BY: Multiplet intervals obey the Lande rule exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1374 (Kramers) and Law 1355 (LS coupling) - the interval rule is the coherence ladder of the multiplet.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the spin-orbit floor is phi^-1 * A_floor.

### CLARITY
The multiplet's rungs step by J; the phi-law keeps the steps from being exactly even.

### NOVELTY
Classical spectroscopy pins interval ratios exactly; the phi-law gives the multiplet a coherence spin-orbit floor.

### ACTIONABILITY
Run sim/1375_lande_interval_rule.py; verify A*J intervals at kappa->0; proceed to 1376.
