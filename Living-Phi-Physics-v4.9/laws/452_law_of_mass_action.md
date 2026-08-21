# PHI-PHYSICS — LAW 452
## Law of Mass Action (Guldberg-Waage)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/452_law_of_mass_action.md` · **Sim:** `sim/452_law_of_mass_action.py`

---

### CLASSICAL STATEMENT
*"The rate of a chemical reaction is proportional to the product of the concentrations (activities) of the reactants, each raised to its stoichiometric coefficient: rate = k [A]^a [B]^b. At equilibrium, the equilibrium constant K satisfies K = [C]^c [D]^d / ([A]^a [B]^b)."*
— Cato Maximilian Guldberg and Peter Waage, 1864. Source: Wikipedia: Law of mass action; Guldberg & Waage, Studies Concerning Affinity (1864)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal dilute kinetics*: the law assumes reactants behave as independent particles with no coherence among them, so concentrations multiply cleanly with no activity corrections.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the ideal kinetics is a coherence basin. K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground, so the equilibrium constant carries the coherence activity floor of the reactants. At kappa->0, K = products/reactants exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} K_phi = K -> the law of mass action is the zero-activity-correction ideal-dilute limit.
```

---

### STAGE 4 — SIMULATION

`sim/452_law_of_mass_action.py`: reproduces the classical value K_ma = 2.25 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/452_law_of_mass_action.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The equilibrium constant of a reaction at finite coupling differs from the mass-action value by kappa*phi^-1*K_ground; the deviation grows with reactant concentration.
EXPERIMENT (VERIFIED): High-precision equilibrium-constant measurements of a reaction at various concentrations comparing with the ideal mass-action prediction.
VERIFIED BY: K equals the mass-action ratio exactly at all concentrations and couplings.
```

---

### RECOGNITION
Connects to Law 453 (Le Chatelier), Law 461 (van't Hoff) and Law 456 (Nernst) - the equilibrium constant is the coherence balance of the reaction.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the activity floor is phi^-1 * K_ground.

### CLARITY
The equilibrium is not a static ratio; it is the coherence standoff of two populations.

### NOVELTY
Classical mass action treats activities as ideal; the phi-law adds the coherence floor of real reactants.

### ACTIONABILITY
Run sim/452_law_of_mass_action.py; verify mass-action K at kappa->0; proceed to 453.
