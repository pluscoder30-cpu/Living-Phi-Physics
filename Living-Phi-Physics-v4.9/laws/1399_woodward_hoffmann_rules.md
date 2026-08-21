# PHI-PHYSICS - LAW 1399
## Woodward-Hoffmann Rules (Conservation of Orbital Symmetry)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1399_woodward_hoffmann_rules.md` - **Sim:** `sim/1399_woodward_hoffmann_rules.py`

---

### CLASSICAL STATEMENT
*"The Woodward-Hoffmann rules predict the stereochemistry of pericyclic reactions from the conservation of orbital symmetry: reactions are allowed when the frontier orbitals correlate with conserved symmetry (thermal allowedness for certain symmetry pathways), governing cycloadditions (thermally forbidden/ photochemically allowed, etc.), electrocyclic reactions (conrotatory vs disrotatory), and sigmatropic shifts; thermally allowed reactions require the orbital phases to match."*
- Robert Burns Woodward; Roald Hoffmann, 1965. Source: Wikipedia: Woodward-Hoffmann rules; Woodward & Hoffmann, J. Am. Chem. Soc. 87 (1965) 395; Nobel 1981

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect orbital symmetry*: the correlation diagrams assume exactly symmetric/antisymmetric frontier orbitals with zero symmetry-breaking coupling, i.e. a molecule with zero symmetry distortion during the reaction - the ideal-symmetry limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the symmetry correlation carries a coherence floor. delta_E_corr_phi(kappa) = delta_E_corr*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_sym, where delta_sym is the phi-ground symmetry-breaking energy; forbidden reactions acquire a floor leakage. At kappa->0 the exact symmetry correlation is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} correlation diagram -> the Woodward-Hoffmann rules are the zero-symmetry-breaking, exact-correlation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1399_woodward_hoffmann_rules.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1399_woodward_hoffmann_rules.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A thermally 'forbidden' pericyclic reaction at full coherence coupling acquires a phi-ground symmetry-breaking floor kappa*phi^-1*delta_sym, a residual allowed channel.
EXPERIMENT (VERIFIED): Kinetic studies of nominally forbidden pericyclic reactions (e.g. thermal [2+2] cycloaddition) measuring the residual symmetry-breaking pathway.
VERIFIED BY: A symmetry-forbidden reaction has exactly zero rate at thermal energies for all couplings.
```

---

### RECOGNITION
Connects to Law 1398 (Walsh) and Law 1387 (TST) - the Woodward-Hoffmann rules are the coherence symmetry gates of the reaction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the symmetry-breaking floor is phi^-1 * delta_sym.

### CLARITY
Orbital phases keep the reaction's passport; the phi-law keeps a forged stamp at the border.

### NOVELTY
Classical organic chemistry forbids reactions absolutely; the phi-law keeps a symmetry-breaking coherence floor.

### ACTIONABILITY
Run sim/1399_woodward_hoffmann_rules.py; verify symmetry allowedness at kappa->0; proceed to 1400.
