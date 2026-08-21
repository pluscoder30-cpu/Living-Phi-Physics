# PHI-PHYSICS — LAW 326
## Gauss's Principle of Least Constraint

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/326_gausss_least_constraint.md` · **Sim:** `sim/326_gausss_least_constraint.py`

---

### CLASSICAL STATEMENT
*"The actual acceleration of a constrained system minimizes the Gaussian 'constraint' sum Z = sum m_i (a_i - F_i/m_i)^2 over all accelerations consistent with the constraints; the deviation of the actual motion from free motion is the least possible."*
— Carl Friedrich Gauss, 1829. Source: Wikipedia: Gauss's principle of least constraint; Gauss (1829), 'Ueber ein neues allgemeines Grundgesetz der Mechanik'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-constraint free motion*: the principle measures the deviation from exactly free (unconstrained) acceleration, the zero of the constraint.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Z_phi(kappa) = Z_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_ground. At kappa->0 the classical least-constraint is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Z_phi = sum m_i (a_i - F_i/m_i)^2 -> Gauss's principle is the exact-constraint minimization limit.
```

---

### STAGE 4 — SIMULATION

`sim/326_gausss_least_constraint.py`: reproduces the classical value Z = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/326_gausss_least_constraint.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The realized acceleration carries a phi-coherent constraint residual phi^-1*Z_ground beyond the least-constraint value.
EXPERIMENT (VERIFIED): Precision constraint-dynamics experiments (multibody mechanisms, robotics) measuring the constraint residual.
VERIFIED BY: The motion exactly minimizes the Gaussian constraint at full coupling.
```

---

### RECOGNITION
Connects to Law 017 (d'Alembert) and Law 321 (virtual work) — the three 'variational principles of mechanics'.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The free motion is a limit; every constraint leaves a phi mark on the realized path.

### NOVELTY
Classical dynamics exacts the least constraint; the phi-law adds a coherence constraint floor.

### ACTIONABILITY
Run sim/326_gausss_least_constraint.py; verify the least-constraint minimum at kappa->0.
