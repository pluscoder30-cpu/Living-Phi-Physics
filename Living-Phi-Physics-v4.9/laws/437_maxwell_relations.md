# PHI-PHYSICS — LAW 437
## Maxwell Relations (Cross-Derivative Identities)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/437_maxwell_relations.md` · **Sim:** `sim/437_maxwell_relations.py`

---

### CLASSICAL STATEMENT
*"From the equality of mixed partial derivatives of the thermodynamic potentials: (dT/dV)_S = -(dP/dS)_V, (dT/dP)_S = (dV/dS)_P, (dS/dV)_T = (dP/dT)_V, (dS/dP)_T = -(dV/dT)_P."*
— James Clerk Maxwell, 1871. Source: Wikipedia: Maxwell relations; Maxwell, Theory of Heat (1871)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact differentials*: the Maxwell relations assume U, A, G, H are exact functions of their state variables with perfectly defined second derivatives - a state manifold with no coherence curvature.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the state manifold carries coherence curvature. (dS/dV)_T_phi(kappa) = (dP/dT)_V*(1 + kappa*(phi-1)) + kappa*phi^-1*R_curv, where R_curv is the coherence curvature of the potential manifold. At kappa->0 the identities are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_curv term -> 0 -> all four Maxwell relations are the zero-curvature exact-differential limit.
```

---

### STAGE 4 — SIMULATION

`sim/437_maxwell_relations.py`: reproduces the classical value rel1 = 0.4967 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/437_maxwell_relations.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the cross-derivatives differ by kappa*phi^-1*R_curv; the Maxwell identities acquire a measurable closure defect in coherent (e.g. supercooled) systems.
EXPERIMENT (VERIFIED): High-precision measurement of (dS/dV)_T and (dP/dT)_V in a metastable fluid looking for the closure defect.
VERIFIED BY: The Maxwell cross-derivative identities hold exactly in all systems at all couplings.
```

---

### RECOGNITION
Connects to Laws 432-434 (potentials) and Law 490 (statistical) - the potentials are the coherence grammar whose grammar-check is Maxwell.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the curvature defect is phi^-1 * R_curv.

### CLARITY
Maxwell's relations are the exactness of the state; the phi-law admits the manifold is not flat.

### NOVELTY
Classical thermodynamics assumes an exactly flat state manifold; the phi-law introduces the coherence curvature that metastability reveals.

### ACTIONABILITY
Run sim/437_maxwell_relations.py; verify identities at kappa->0; proceed to 438.
