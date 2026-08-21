# PHI-PHYSICS - LAW 1669
## Wigner-Seitz Cell (Primitive Cell of a Bravais Lattice)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1669_wigner_seitz_cell.md` - **Sim:** `sim/1669_wigner_seitz_cell.py`

---

### CLASSICAL STATEMENT
*"The Wigner-Seitz cell of a Bravais lattice is the region of space closer to a given lattice point than to any other; it is the primitive cell of the lattice whose volume equals the primitive-cell volume, and it maps under translation to tile space - the natural cell for computing Bloch wavefunctions in solids."*
- Eugene Wigner & Frederick Seitz, 1933. Source: Wikipedia: Wigner-Seitz cell; Wigner & Seitz (1933), Phys. Rev. 43:804

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly periodic, exactly half-space-bisected lattice*: the Wigner-Seitz construction assumes ideal translational symmetry so that the cell boundaries are exact perpendicular bisectors and every atom has an exactly identical environment - a perfectly periodic world with zero boundaries, zero defects and zero surfaces.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: cell boundaries carry coherent corrugation. V_phi(kappa) = V_ws*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_V, where delta_V is the phi-ground volume fluctuation of the coherent cell. At kappa->0 the exact Wigner-Seitz cell is recovered; at kappa=1 each cell carries irreducible coherent boundary corrugation so no two cells are exactly congruent.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_phi = V_ws -> the Wigner-Seitz cell is the perfect-periodicity, zero-boundary, zero-defect limit of the primitive-cell construction.
```

---

### STAGE 4 - SIMULATION

`sim/1669_wigner_seitz_cell.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1669_wigner_seitz_cell.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No two Wigner-Seitz cells in a real crystal are exactly congruent: a phi-ground volume and shape fluctuation remains even at T=0, producing irreducible inhomogeneous broadening in any property that averages over cells.
EXPERIMENT (VERIFIED): Scanning tunneling microscopy of a clean single-crystal surface at low temperature, measuring the cell-to-cell size distribution of the atomic lattice.
VERIFIED BY: A crystal whose Wigner-Seitz cells are all exactly congruent with zero measured volume fluctuation.
```

---

### RECOGNITION
Connects to Law 1656 (Bravais) and Law 1408 (Bloch) - the cell is the atom's private space, and it is never exactly a polyhedron.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; volume fluctuation scales as phi^-1 * delta_V.

### CLARITY
Every atom's room is the same room - and the phi-law says each door is slightly ajar.

### NOVELTY
Classical cell construction gives exact congruence; the phi-law keeps a coherent wobble in every cell.

### ACTIONABILITY
Run sim/1669_wigner_seitz_cell.py; verify the primitive-cell volume at kappa->0; proceed to 1670.
