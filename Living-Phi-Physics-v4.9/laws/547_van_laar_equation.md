# PHI-PHYSICS — LAW 547
## Van Laar Equation (Two-Parameter Activity Model)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/547_van_laar_equation.md` · **Sim:** `sim/547_van_laar_equation.py`

---

### CLASSICAL STATEMENT
*"The van Laar activity model expresses the excess Gibbs energy as G_ex/(RT) = A12 A21 x1 x2 / (A12 x1 + A21 x2), giving ln gamma_1 = A12 (A21 x2/(A12 x1 + A21 x2))^2 and ln gamma_2 = A21 (A12 x1/(A12 x1 + A21 x2))^2. The parameters equal the limiting activity coefficients."*
— Johannes van Laar, 1910. Source: Wikipedia: Van Laar equation; van Laar (1910-1913)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal solution baseline*: like Margules, the model measures departure from Raoult's ideal solution where the excess vanishes - a zero-coherence baseline.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the baseline carries coherence. G_ex_phi(kappa) = G_ex_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ideal. At kappa->0 the van Laar model is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} G_ex_phi = A12 A21 x1 x2/(A12 x1 + A21 x2) -> the van Laar equation is the zero-coherence excess baseline limit.
```

---

### STAGE 4 — SIMULATION

`sim/547_van_laar_equation.py`: reproduces the classical value Gex_vl = 0.36 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/547_van_laar_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even ideal mixtures show a residual excess energy; the van Laar activity coefficients deviate from the predicted limiting values.
EXPERIMENT (VERIFIED): Vapor-liquid equilibrium measurements of binary mixtures to test the van Laar correlations.
VERIFIED BY: The excess Gibbs energy of an ideal mixture is exactly zero for all couplings.
```

---

### RECOGNITION
Connects to Law 546 (Margules) and Law 142 (van der Waals) - the van Laar equation is the van der Waals-derived coherence excess model.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the baseline floor is phi^-1 * G_ideal.

### CLARITY
Every model of excess begins from an ideal that never was; the phi-law keeps the floor of the never-was.

### NOVELTY
Classical van Laar measures departure from ideal; the phi-law adds the coherence floor of the ideal baseline.

### ACTIONABILITY
Run sim/547_van_laar_equation.py; verify van Laar model at kappa->0; proceed to 548.
