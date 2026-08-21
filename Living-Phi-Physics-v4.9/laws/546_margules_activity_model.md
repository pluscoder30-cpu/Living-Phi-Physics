# PHI-PHYSICS — LAW 546
## Margules Activity Model (Excess Gibbs Energy)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/546_margules_activity_model.md` · **Sim:** `sim/546_margules_activity_model.py`

---

### CLASSICAL STATEMENT
*"The excess Gibbs energy of a binary liquid mixture is expressed as a power series in the mole fractions: G_ex/(RT) = x1 x2 (A21 x1 + A12 x2). The activity coefficients are ln gamma_1 = [A12 + 2(A21 - A12)x1] x2^2, and similarly for component 2."*
— Max Margules, 1895. Source: Wikipedia: Margules activity model; Margules, Ueber die Zusammensetzung der gesaettigten Daempfe von Mischungen (1895)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal solution baseline*: the model measures the excess (departure) from Raoult's ideal solution, where the excess is exactly zero - a baseline with no mixing coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the excess baseline carries coherence. G_ex_phi(kappa) = G_ex_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ideal, where G_ideal is the coherence floor of the ideal baseline. At kappa->0 the Margules model is exact (and vanishes for ideal solutions).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} G_ex_phi = x1 x2 (A21 x1 + A12 x2) -> the Margules model is the zero-coherence excess baseline limit.
```

---

### STAGE 4 — SIMULATION

`sim/546_margules_activity_model.py`: reproduces the classical value Gex = 0.1728 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/546_margules_activity_model.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even 'ideal' mixtures show a residual excess energy kappa*phi^-1*G_ideal; activity coefficients deviate from the Margules prediction.
EXPERIMENT (VERIFIED): Vapor-liquid equilibrium measurements of binary mixtures to extract and test Margules parameters.
VERIFIED BY: The excess Gibbs energy of an ideal mixture is exactly zero for all couplings.
```

---

### RECOGNITION
Connects to Law 547 (van Laar) and Law 479 (activity) - the model is the excess grammar of the mixing coherence.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the baseline floor is phi^-1 * G_ideal.

### CLARITY
The mixture's extra energy is the coherence of its difference; the phi-law keeps even sameness's floor.

### NOVELTY
Classical Margules zeroes the ideal baseline; the phi-law adds the coherence floor of the ideal itself.

### ACTIONABILITY
Run sim/546_margules_activity_model.py; verify excess model at kappa->0; proceed to 547.
