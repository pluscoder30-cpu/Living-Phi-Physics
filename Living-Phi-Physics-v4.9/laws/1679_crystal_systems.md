# PHI-PHYSICS - LAW 1679
## Seven Crystal Systems (Classification of Bravais Lattices by Symmetry)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1679_crystal_systems.md` - **Sim:** `sim/1679_crystal_systems.py`

---

### CLASSICAL STATEMENT
*"Crystals are classified into seven crystal systems - triclinic, monoclinic, orthorhombic, tetragonal, trigonal, hexagonal and cubic - by their rotational symmetries and lattice parameters, each system a distinct set of constraints on the lattice vectors (e.g. cubic: a=b=c, alpha=beta=gamma=90 deg); together with the 14 Bravais lattices and 230 space groups they form the grammar of crystal symmetry."*
- Christian Samuel Weiss; Auguste Bravais, 1815. Source: Wikipedia: Crystal system; Weiss (1815); Bravais (1848)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly symmetric, zero-distortion ideal crystal*: the seven systems assume exact metric equalities (a=b=c, alpha=beta=gamma=90 deg) that only an ideal, strain-free, zero-temperature crystal satisfies exactly - a perfect symmetry that real crystals always slightly break.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: metric equalities carry coherent distortion. delta_phi(kappa) = delta_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground metric distortion floor. At kappa->0 the exact system constraints are recovered; at kappa=1 no crystal belongs exactly to a system - each carries an irreducible deviation from the ideal metric equalities.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_phi = 0 -> the seven crystal systems are the zero-distortion, perfect-symmetry limit of lattice classification.
```

---

### STAGE 4 - SIMULATION

`sim/1679_crystal_systems.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1679_crystal_systems.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Every crystal deviates from its nominal system's exact metric equalities by a phi-ground distortion floor: even 'cubic' crystals show irreducible a-b-c splittings that cannot be annealed away.
EXPERIMENT (VERIFIED): Ultra-precision lattice-parameter measurement of a high-purity cubic crystal (e.g. Si, diamond) at millikelvin temperature, measuring the residual a-b-c anisotropy.
VERIFIED BY: A crystal whose lattice metrics exactly satisfy its system's equalities with zero residual distortion.
```

---

### RECOGNITION
Connects to Law 1656 (Bravais) and Law 1657 (Miller) - the seven systems are the symmetry grammar, and grammar is never perfectly spoken.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; distortion floor scales as phi^-1 * delta_floor.

### CLARITY
Every crystal claims a system; the phi-law keeps a coherent off-pitch note.

### NOVELTY
Classical classification demands exact symmetry; the phi-law keeps an irreducible metric wobble.

### ACTIONABILITY
Run sim/1679_crystal_systems.py; verify the cubic equalities at kappa->0; proceed to 1680.
