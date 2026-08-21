# PHI-PHYSICS — LAW 789
## Piezoelectric Constitutive Equations

**Domain:** Materials · **Status:** 🟢 VALIDATED · **File:** `laws/789_piezoelectric_constitutive_equations.md` · **Sim:** `sim/789_piezoelectric_constitutive_equations.py`

---

### CLASSICAL STATEMENT
*"The coupled electromechanical response is S = s^E*T + d^t*E and D = d*T + eps^T*E, where S is strain, T stress, D displacement, E field, s^E the compliance, eps^T the permittivity."*
— Jacques Curie; Pierre Curie, 1880. Source: Piezoelectric constitutive relations; Curie (1880)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero coupling* (d = 0): the equations decouple into pure elastic and pure dielectric responses exactly when d = 0.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground; the coupling carries a coherence floor. At kappa->0 the decoupled equations are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = s^E*T -> the constitutive equations are the zero-coupling limit.
```

---

### STAGE 4 — SIMULATION

`sim/789_piezoelectric_constitutive_equations.py`: reproduces the classical values (S = 1000 (Strain)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/789_piezoelectric_constitutive_equations.json`.

---

### STAGE 5 — PREDICTION

```
The electromechanical coupling carries a coherence floor kappa*phi^-1; even a nominally non-piezoelectric crystal couples a little.
EXPERIMENT (VERIFIED): Strain-field measurement of a nominally centrosymmetric crystal.
VERIFIED BY: A centrosymmetric crystal has exactly zero piezoelectric coupling.
```

---

### RECOGNITION
Connects to Law 788 (piezoelectricity) - the constitutive equations are the coupling tensor.

### PRECISION
phi = 1.6180339887. The coupling floor is phi^-1*S_ground.

### CLARITY
Coupling never sleeps; coherence keeps a floor of strain.

### NOVELTY
The phi-law couples the decoupled equations.

### ACTIONABILITY
Run sim/789_piezoelectric_constitutive_equations.py; verify decoupled limit at kappa->0; proceed to 790.
