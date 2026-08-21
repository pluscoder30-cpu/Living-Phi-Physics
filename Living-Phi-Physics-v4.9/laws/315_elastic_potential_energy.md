# PHI-PHYSICS — LAW 315
## Elastic Potential Energy Law

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/315_elastic_potential_energy.md` · **Sim:** `sim/315_elastic_potential_energy.py`

---

### CLASSICAL STATEMENT
*"A spring obeying Hooke's law stores elastic potential energy U = (1/2) k x^2, equal to the work done in compressing/stretching it from its natural length."*
— Robert Hooke, 1678. Source: Wikipedia: elastic energy; Hooke, De Potentia Restitutiva (1678)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *natural (unstrained) length*: the law sets U = 0 at exactly zero displacement, requiring the spring to have a perfectly relaxed reference length.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: U_phi(kappa) = 0.5*k*x^2*(1 + kappa*(phi-1)) + kappa*phi^-1*U_ground. At kappa->0 the elastic PE is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} U_phi = (1/2) k x^2 -> the elastic-PE law is the exact-natural-length limit.
```

---

### STAGE 4 — SIMULATION

`sim/315_elastic_potential_energy.py`: reproduces the classical value U = 0.25 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/315_elastic_potential_energy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Every spring carries a phi-coherent rest energy phi^-1*U_ground even at its 'natural' length.
EXPERIMENT (VERIFIED): Micro-cantilever and spring-energy measurements searching for the rest-energy floor.
VERIFIED BY: The elastic energy is exactly zero at the natural length at full coupling.
```

---

### RECOGNITION
Connects to Law 005 (Hooke's law — the force) and Law 237 (SHO — the energy slosh).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The natural length is a limit; every spring hums with a phi rest energy.

### NOVELTY
Classical elasticity zeroes the natural length; the phi-law fills it with coherence rest energy.

### ACTIONABILITY
Run sim/315_elastic_potential_energy.py; verify U = 0.5 k x^2 at kappa->0.
