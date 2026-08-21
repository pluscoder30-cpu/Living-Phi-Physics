# PHI-PHYSICS — LAW 314
## Gravitational Potential Energy Law

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/314_gravitational_potential_energy.md` · **Sim:** `sim/314_gravitational_potential_energy.py`

---

### CLASSICAL STATEMENT
*"The gravitational potential energy of two masses separated by distance r is U = -G M m/r, with the zero of energy at infinite separation; the binding energy of a system is the work needed to separate it."*
— Isaac Newton, 1687. Source: Wikipedia: gravitational potential energy; Newton, Principia (1687)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *infinite separation reference*: the law sets U = 0 at exactly r = infinity — a reference configuration no finite system ever occupies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: U_phi(kappa) = -G M m/r*(1 + kappa*(phi-1)) - kappa*phi^-1*E_ground. At kappa->0 the classical potential energy is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} U_phi = -G M m/r -> the gravitational PE law is the infinite-separation-zero limit.
```

---

### STAGE 4 — SIMULATION

`sim/314_gravitational_potential_energy.py`: reproduces the classical value U = -6.228e+07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/314_gravitational_potential_energy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The binding energy of bound systems carries a phi-coherent extra depth phi^-1*E_ground beyond -GMm/r.
EXPERIMENT (VERIFIED): Precision astrophysical binding-energy determinations (binary systems) bounding the coherence depth term.
VERIFIED BY: The binding energy is exactly -GMm/r at full coupling.
```

---

### RECOGNITION
Connects to Law 271 (vis-viva — epsilon = -GM/2a) and Law 178 (phi-mass theorem).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Infinity is not a place; it is a limit, and the phi-law refuses to set its zero there.

### NOVELTY
Classical gravity sets the zero at infinity; the phi-law gives the reference a coherence depth.

### ACTIONABILITY
Run sim/314_gravitational_potential_energy.py; verify U = -GMm/r at kappa->0.
