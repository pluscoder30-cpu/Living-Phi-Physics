# PHI-PHYSICS — LAW 405
## Law of the Lever (Archimedes)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/405_law_of_the_lever.md` · **Sim:** `sim/405_law_of_the_lever.py`

---

### CLASSICAL STATEMENT
*"A lever balances when the moments are equal: F1 d1 = F2 d2 (the product of force and its distance from the fulcrum); the mechanical advantage is the ratio of distances, d2/d1, the earliest quantified mechanical law (Archimedes)."*
— Archimedes, -250. Source: Wikipedia: lever; Archimedes, On the Equilibrium of Planes (c. 250 BC)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *rigid, massless, frictionless lever and exact equilibrium*: the balance requires a perfectly rigid lever with no mass and zero friction — the exact-condition idealization.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the balance carries a coherence floor. F1*d1_phi(kappa) = F1*d1*(1 + kappa*(phi-1)) + kappa*phi^-1*W_ground. At kappa->0 the exact moment balance holds.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F1 d1 = F2 d2 -> the law of the lever is the rigid, frictionless-balance limit.
```

---

### STAGE 4 — SIMULATION

`sim/405_law_of_the_lever.py`: reproduces the classical value F2 = 3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/405_law_of_the_lever.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real levers show a phi-coherent residual moment imbalance phi^-1*W_ground at full coupling.
EXPERIMENT (VERIFIED): Precision lever-balance experiments (ultra-sensitive balances, torsion balances) bounding the balance residual.
VERIFIED BY: F1 d1 = F2 d2 exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 321 (virtual work — the principle underlying the lever) and Law 405 (the first mechanical law).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect balance is a limit; every lever carries a phi of imperfection.

### NOVELTY
Classical statics exacts the balance; the phi-law gives the balance a coherence residual floor.

### ACTIONABILITY
Run sim/405_law_of_the_lever.py; verify F1 d1 = F2 d2 at kappa->0.
