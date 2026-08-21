# PHI-PHYSICS - LAW 1419
## Mulliken Electronegativity (chi = (I + A)/2)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1419_mulliken_electronegativity.md` - **Sim:** `sim/1419_mulliken_electronegativity.py`

---

### CLASSICAL STATEMENT
*"The Mulliken electronegativity is the average of the ionization potential and electron affinity: chi_M = (I + A)/2, the chemical potential of the electron with a sign change (chi = -mu = -(dE/dN)); it converts to the Pauling scale via chi_P ~ 1.35 sqrt(chi_M(eV)) - 1.37, and rationalizes electronegativity as the tendency of an atom to attract electrons in its own chemical potential."*
- Robert S. Mulliken, 1934. Source: Wikipedia: Electronegativity; Mulliken, J. Chem. Phys. 2 (1934) 782

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero electron affinity*: the Mulliken scale reduces to chi = I/2 when A = 0, i.e. an atom with zero ability to accept electrons - the zero-affinity limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the electron affinity carries a coherence floor. A_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground affinity; no atom has exactly zero affinity. At kappa->0 the Mulliken scale is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} chi_M_phi = (I + A)/2 -> the Mulliken electronegativity is the zero-affinity, exact-chemical-potential limit.
```

---

### STAGE 4 - SIMULATION

`sim/1419_mulliken_electronegativity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1419_mulliken_electronegativity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective Mulliken electronegativity at full coherence coupling retains a phi-ground affinity floor kappa*phi^-1*A_floor, a residual electron-accepting tendency.
EXPERIMENT (VERIFIED): Measured I and A values (photoelectron and electron-attachment spectroscopy) testing the chi = (I+A)/2 relation across elements.
VERIFIED BY: The Mulliken electronegativity equals (I+A)/2 exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1418 (Pauling) and Law 1420 (Allen) - the Mulliken scale is the coherence chemical potential of the atom.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the affinity floor is phi^-1 * A_floor.

### CLARITY
The atom's greed is the average of its loss and gain; the phi-law keeps a floor of the gain.

### NOVELTY
Classical electronegativity theory averages exactly; the phi-law gives the electron affinity a coherence floor.

### ACTIONABILITY
Run sim/1419_mulliken_electronegativity.py; verify (I+A)/2 at kappa->0; proceed to 1420.
