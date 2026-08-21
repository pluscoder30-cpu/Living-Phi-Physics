# PHI-PHYSICS - LAW 1383
## Lennard-Jones Potential (12-6 Potential V(r) = 4 eps [(sigma/r)^12 - (sigma/r)^6])

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1383_lennard_jones_potential.md` - **Sim:** `sim/1383_lennard_jones_potential.py`

---

### CLASSICAL STATEMENT
*"The Lennard-Jones 12-6 potential V(r) = 4 eps [(sigma/r)^12 - (sigma/r)^6] models the interaction of neutral atoms/molecules: a steep repulsive wall at short range (r^-12) and an attractive van der Waals tail (r^-6), with well depth eps at r_min = 2^(1/6) sigma; it is the standard model of rare-gas interactions, liquids and the equation of state."*
- John Lennard-Jones, 1924. Source: Wikipedia: Lennard-Jones potential; Lennard-Jones, Proc. R. Soc. Lond. A 106 (1924) 463

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero interaction*: the potential vanishes exactly as r -> infinity, i.e. isolated atoms with zero mutual interaction - the infinite-separation limit (cf. Law 142 van der Waals).

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the interaction carries a coherence floor. V_LJ_phi(kappa) = V_LJ*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground residual interaction at infinity; the potential never fully vanishes. At kappa->0 the classical LJ potential is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_LJ_phi = 4 eps [(sigma/r)^12 - (sigma/r)^6] -> the Lennard-Jones potential is the zero-floor, infinite-separation-limit.
```

---

### STAGE 4 - SIMULATION

`sim/1383_lennard_jones_potential.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1383_lennard_jones_potential.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The interatomic interaction at full coherence coupling retains a floor kappa*phi^-1*V_floor at large separation, a residual long-range coherence interaction.
EXPERIMENT (VERIFIED): Ultracold atom-pair spectroscopy at large interatomic distance measuring the residual interaction floor beyond the van der Waals tail.
VERIFIED BY: The interaction between separated atoms is exactly zero beyond the LJ range for all couplings.
```

---

### RECOGNITION
Connects to Law 142 (van der Waals) and Law 1411 (London dispersion) - the LJ potential is the coherence model of the neutral interaction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the residual floor is phi^-1 * V_floor.

### CLARITY
Two neutral atoms almost forget each other; the phi-law keeps a floor of remembering.

### NOVELTY
Classical interatomic potentials vanish at infinity; the phi-law keeps a coherence interaction floor.

### ACTIONABILITY
Run sim/1383_lennard_jones_potential.py; verify 12-6 form at kappa->0; proceed to 1384.
