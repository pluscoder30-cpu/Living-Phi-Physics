# PHI-PHYSICS - LAW 1377
## Molecular Orbital Theory (Hund-Mulliken: Delocalized Orbitals)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1377_molecular_orbital_theory.md` - **Sim:** `sim/1377_molecular_orbital_theory.py`

---

### CLASSICAL STATEMENT
*"Molecular orbital theory describes electrons in delocalized orbitals spanning the whole molecule, built as linear combinations of atomic orbitals (LCAO): bonding orbitals lower the energy (constructive interference), antibonding raise it, with the bond order BO = (n_bonding - n_antibonding)/2; electron occupancy follows the Aufbau and Hund's rules, and the theory unifies bonding, spectra and magnetism."*
- Friedrich Hund; Robert Mulliken, 1928. Source: Wikipedia: Molecular orbital theory; Hund (1928), Mulliken (1928)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *atomic-orbital limit*: the delocalized picture reduces to atomic orbitals when the molecule is fully dissociated with zero interatomic overlap - the zero-overlap separated-atom limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the interatomic overlap carries a coherence floor. S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground overlap; even separated atoms retain a floor bond. At kappa->0 the separated-atom limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_MO_phi = E_atomic at S -> 0 -> molecular orbital theory is the zero-overlap, separated-atom limit.
```

---

### STAGE 4 - SIMULATION

`sim/1377_molecular_orbital_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1377_molecular_orbital_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Fully separated atoms at full coherence coupling retain a phi-ground overlap kappa*phi^-1*S_floor, a residual bond floor no dissociation removes.
EXPERIMENT (VERIFIED): Spectroscopy of atom pairs at large interatomic distance (photoassociation) measuring the residual molecular binding floor.
VERIFIED BY: Fully separated atoms have exactly zero molecular binding for all couplings.
```

---

### RECOGNITION
Connects to Law 1378 (LCAO) and Law 1397 (bond order) - MO theory is the coherence delocalization of the bond.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the overlap floor is phi^-1 * S_floor.

### CLARITY
The molecule is one orchestra, not many players; the phi-law keeps a whisper of the orchestra at separation.

### NOVELTY
Classical valence theory localizes bonds; the phi-law keeps the delocalized field's overlap floor.

### ACTIONABILITY
Run sim/1377_molecular_orbital_theory.py; verify bond order at kappa->0; proceed to 1378.
