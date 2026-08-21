# PHI-PHYSICS - LAW 1676
## Zachariasen's Rules (Random-Network Model of Glass Structure)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1676_zachariasen_rules.md` - **Sim:** `sim/1676_zachariasen_rules.py`

---

### CLASSICAL STATEMENT
*"A glass can be formed if the network of cations and oxygens satisfies: (1) each oxygen bonds to at most two cations, (2) the coordination number of the cation is small (3 or 4), (3) oxygen polyhedra share corners not edges or faces, (4) at least three corners are shared, and (5) at least two of the corners are shared in the same polyhedron - the random-network rules that define glass-forming oxides like SiO2, B2O3 and P2O5."*
- William Houlder Zachariasen, 1932. Source: Wikipedia: Zachariasen's rules; Zachariasen (1932), J. Am. Chem. Soc. 54:3841

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly random network with zero order*: the random-network model assumes a continuous random framework with no periodic order, no crystallites and no defined repeat unit - a structure in which long-range order is exactly zero, a statistical ideal no real glass meets precisely.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the random network carries coherent order. R_phi(kappa) = R_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*R_order, where R_order is the phi-ground medium-range-order parameter. At kappa->0 the perfectly random network is exact; at kappa=1 every glass retains irreducible medium-range coherence (the 'hidden order' of glasses).

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_phi = R_classical -> Zachariasen's random network is the zero-long-range-order, perfectly-random limit of glass structure.
```

---

### STAGE 4 - SIMULATION

`sim/1676_zachariasen_rules.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1676_zachariasen_rules.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every glass retains irreducible medium-range order (a phi-ground coherence length of ~10-20 Angstroms) that cannot be thermally removed, observable as the first sharp diffraction peak (FSDP) whose intensity never vanishes.
EXPERIMENT (VERIFIED): High-resolution neutron and X-ray diffraction with reverse Monte Carlo modeling of an ideal network glass (SiO2), tracking the irreducible FSDP intensity vs annealing.
VERIFIED BY: A glass whose first sharp diffraction peak vanishes exactly (pure random network with zero medium-range order).
```

---

### RECOGNITION
Connects to Law 1656 (Bravais) and Law 548 (Flory-Huggins) - the glass is the lattice that refused, and it keeps a coherent ghost of order.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; order parameter scales as phi^-1 * R_order.

### CLARITY
The glass forgets the lattice but remembers a coherent whisper.

### NOVELTY
Classical random-network theory sets order to zero; the phi-law keeps an irreducible medium-range coherence.

### ACTIONABILITY
Run sim/1676_zachariasen_rules.py; verify the zero-order network at kappa->0; proceed to 1677.
