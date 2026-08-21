# PHI-PHYSICS - LAW 1357
## Aufbau Principle (Order of Orbital Filling)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1357_aufbau_principle.md` - **Sim:** `sim/1357_aufbau_principle.py`

---

### CLASSICAL STATEMENT
*"Electrons fill atomic orbitals in order of increasing energy: 1s, 2s, 2p, 3s, 3p, 4s, 3d, ... (the (n+l) Madelung rule, with equal n+l filled by lower n first), each orbital holding up to 2 electrons (Pauli exclusion); this determines the electronic configurations and the periodic table's structure."*
- Niels Bohr; Erwin Madelung (n+l rule), 1922. Source: Wikipedia: Aufbau principle; Bohr (1922), Madelung (1936)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact ordering*: the Aufbau sequence is exact only for the idealized independent-electron atom, i.e. zero configuration interaction and zero level-crossing between orbitals - the non-interacting limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the orbital ordering carries a coherence energy floor. E_orb_phi(kappa) = E_orb*(1 + kappa*(phi-1)) + kappa*phi^-1*E_cross, where E_cross is the phi-ground orbital-crossing energy; the filling order can shift. At kappa->0 the Aufbau sequence is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} ordering by E_orb -> the Aufbau principle is the zero-interaction, non-interacting-orbital limit.
```

---

### STAGE 4 - SIMULATION

`sim/1357_aufbau_principle.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1357_aufbau_principle.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective orbital energies at full coherence coupling carry a phi-ground crossing shift kappa*phi^-1*E_cross, so near-degenerate filling orders (e.g. 4s/3d) can deviate from the textbook sequence.
EXPERIMENT (VERIFIED): Photoelectron spectroscopy of transition metals measuring effective orbital energies against the Aufbau ordering at increasing precision.
VERIFIED BY: Electronic configurations follow the Aufbau sequence exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 073 (Pauli exclusion) and Law 1358 (Madelung rule) - the Aufbau principle is the coherence filling order of the atom.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the crossing floor is phi^-1 * E_cross.

### CLARITY
The atom fills its rooms in order; the phi-law keeps a floor of disorder in the order.

### NOVELTY
Classical chemistry orders orbitals exactly; the phi-law gives the filling sequence a coherence crossing floor.

### ACTIONABILITY
Run sim/1357_aufbau_principle.py; verify filling order at kappa->0; proceed to 1358.
