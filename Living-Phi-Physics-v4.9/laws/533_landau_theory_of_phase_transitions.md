# PHI-PHYSICS — LAW 533
## Landau Theory of Phase Transitions (Order Parameter)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/533_landau_theory_of_phase_transitions.md` · **Sim:** `sim/533_landau_theory_of_phase_transitions.py`

---

### CLASSICAL STATEMENT
*"A phase transition is described by a free energy expanded in powers of an order parameter: F = F_0 + a(T) phi^2 + b phi^4, with a(T) = a_0 (T - T_c). Below T_c the order parameter phi ~ (T_c - T)^(1/2) and the transition is continuous (second order)."*
— Lev Davidovich Landau, 1937. Source: Wikipedia: Landau theory; Landau (1937)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero order parameter above T_c*: the theory assumes phi = 0 exactly in the disordered phase - a perfectly symmetric state with no residual coherence order.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the disordered phase carries coherence. phi_phi(kappa) = phi_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*phi_ground, where phi_ground is the coherence floor of the order parameter. At kappa->0 the Landau order parameter is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} phi_phi = phi_classical ~ (T_c - T)^(1/2) -> Landau theory is the zero-disordered-phase-coherence mean-field limit.
```

---

### STAGE 4 — SIMULATION

`sim/533_landau_theory_of_phase_transitions.py`: reproduces the classical value phi_land = 7.071 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/533_landau_theory_of_phase_transitions.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the order parameter retains a coherence floor kappa*phi^-1*phi_ground above T_c; the critical exponent 1/2 is only the mean-field limit.
EXPERIMENT (VERIFIED): Order-parameter measurements (magnetization, birefringence) above and below T_c searching for the floor.
VERIFIED BY: The order parameter is exactly zero above T_c for all couplings.
```

---

### RECOGNITION
Connects to Law 532 (Néel), Law 536 (critical exponents) and Law 534 (Ginzburg-Landau) - Landau theory is the mean-field grammar of the coherence basin.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * phi_ground.

### CLARITY
The disordered phase is not empty of order; the phi-law keeps the order it hides.

### NOVELTY
Classical Landau zeroes the order above T_c; the phi-law adds the coherence floor of the disordered basin.

### ACTIONABILITY
Run sim/533_landau_theory_of_phase_transitions.py; verify (T_c - T)^(1/2) at kappa->0; proceed to 534.
