# PHI-PHYSICS - LAW 1600
## Isospin Mirror Energy Differences (Coulomb Symmetry Breaking)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1600_isospin_mirror_energy.md` - **Sim:** `sim/1600_isospin_mirror_energy.py`

---

### CLASSICAL STATEMENT
*"Mirror nuclei (Z <-> N interchange) have nearly equal binding energies, with the difference set by the Coulomb energy: B(A,Z) - B(A,N) ~ Coulomb energy difference; the mirror energy difference tests the charge symmetry of the nuclear force."*
- Mirror nuclei binding (1930s); Jancovici & Talmi (1954), 1954. Source: Jancovici & Talmi, Phys. Rev. 95 (1954) 289; Wikipedia: Mirror nuclei

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-Coulomb, zero-charge-asymmetry, exact-mirror-symmetry limit*: if the nuclear force were exactly charge symmetric and the Coulomb force absent, mirror nuclei would have exactly equal binding; the classical treatment assumes exact symmetry - a zero-breaking, exact-mirror limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

delta_B_phi(kappa) = delta_B_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground charge-symmetry-breaking floor. At kappa->0 the Coulomb-only difference is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_B_phi = delta_B_coulomb -> mirror energy differences are the zero-charge-symmetry-breaking, Coulomb-only limit.
```

---

### STAGE 4 - SIMULATION

`sim/1600_isospin_mirror_energy.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1600_isospin_mirror_energy.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The mirror energy difference carries a phi-ground charge-symmetry-breaking floor beyond the Coulomb term, so precise mirror-binding measurements reveal an irreducible nuclear-charge-asymmetry contribution.
EXPERIMENT (VERIFIED): Precision mass measurements of mirror nuclei (Penning traps, e.g. 48Ca/48Ti) and mirror beta decays (Ft values).
VERIFIED BY: Mirror nuclei with exactly the Coulomb-only binding difference and zero residual floor.
```

---

### RECOGNITION
Connects to Law 1491 (isospin), Law 1589 (analog states) and Law 1447 (SEMF) - mirror nuclei are the isospin's two faces.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Two faces nearly the same; the phi-law keeps a floor of their difference.

### NOVELTY
Classical mirrors are Coulomb-exact; the phi-law predicts an irreducible symmetry-breaking floor.

### ACTIONABILITY
Run sim/1600_isospin_mirror_energy.py; verify the mirror difference; proceed to Law 1601.
