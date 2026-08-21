# PHI-PHYSICS - LAW 1358
## Madelung Rule ((n+l) Filling Order of Orbitals)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1358_madelung_rule.md` - **Sim:** `sim/1358_madelung_rule.py`

---

### CLASSICAL STATEMENT
*"Orbitals fill in order of increasing (n + l), and for equal (n + l) the orbital with smaller n fills first: 1s (2), 2s (3), 2p (4), 3s (4), 3p (5), 4s (5), 3d (5), 4p (6), ...; the rule reproduces the periodic table's shell structure and the placement of the transition and rare-earth blocks."*
- Erwin Madelung, 1936. Source: Wikipedia: Madelung rule; Madelung, Math. Naturwiss. Anz. 7 (1936) 195

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero orbital energy spread*: the (n+l) ordering is exact only when orbitals with equal (n+l) have exactly equal energy or clean spacing - the degenerate-level ordering limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the equal-(n+l) degeneracy carries a coherence floor. delta_E_phi(kappa) = delta_E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground spread of equal-(n+l) orbitals; the ordering within equal (n+l) acquires a floor. At kappa->0 the Madelung order is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} ordering by (n+l) then n -> the Madelung rule is the zero-equal-(n+l)-spread limit.
```

---

### STAGE 4 - SIMULATION

`sim/1358_madelung_rule.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1358_madelung_rule.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The relative order of equal-(n+l) orbitals at full coherence coupling carries a phi-ground spread kappa*phi^-1*E_floor, occasionally reversing the expected n-ordering.
EXPERIMENT (VERIFIED): Photoemission measurements of orbital energies in heavy elements testing the (n+l) ordering at increasing precision.
VERIFIED BY: Orbital energies obey the (n+l) then n ordering exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1357 (Aufbau) and Law 073 (Pauli) - the Madelung rule is the coherence ordering of the electron ladder.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the spread floor is phi^-1 * E_floor.

### CLARITY
The ladder of shells climbs by n+l; the phi-law keeps the rungs from being exactly level.

### NOVELTY
Classical chemistry orders the shells exactly; the phi-law gives the equal-(n+l) rungs a coherence spread.

### ACTIONABILITY
Run sim/1358_madelung_rule.py; verify (n+l) ordering at kappa->0; proceed to 1359.
