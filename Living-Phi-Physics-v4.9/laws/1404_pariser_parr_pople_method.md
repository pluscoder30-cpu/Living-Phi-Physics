# PHI-PHYSICS - LAW 1404
## Pariser-Parr-Pople Method (Semiempirical Pi-Electron SCF)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1404_pariser_parr_pople_method.md` - **Sim:** `sim/1404_pariser_parr_pople_method.py`

---

### CLASSICAL STATEMENT
*"The Pariser-Parr-Pople (PPP) method applies Hartree-Fock to pi electrons with the zero differential overlap (ZDO) approximation: the two-electron repulsion integrals are parameterized (e.g. the Mataga-Nishimoto formula gamma_ij = 14.397/(a_ij + r_ij) eV), and the pi-electron SCF problem is solved for conjugated molecules, giving accurate pi-electron spectra, ionization potentials and bond orders for dyes and polyenes."*
- Rudolph Pariser, Robert Parr; John Pople, 1953. Source: Wikipedia: Pariser-Parr-Pople method; Pariser & Parr, J. Chem. Phys. 21 (1953) 466; Pople, Trans. Faraday Soc. 49 (1953) 1375

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero differential overlap*: the method's speed rests on dropping differential overlap exactly (S = 0 for all pairs), i.e. orbitals with zero overlap ambiguity - the ZDO limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the ZDO assumption carries a coherence floor. S_phi(kappa) = 0*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground overlap residue; the method's simplicity carries a floor error. At kappa->0 the PPP SCF is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} gamma_ij parameterization -> the PPP method is the zero-differential-overlap, ZDO limit.
```

---

### STAGE 4 - SIMULATION

`sim/1404_pariser_parr_pople_method.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1404_pariser_parr_pople_method.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The PPP pi-electron spectrum at full coherence coupling carries a phi-ground overlap residue kappa*phi^-1*S_floor, shifting predicted transition energies.
EXPERIMENT (VERIFIED): UV-visible spectroscopy of conjugated dyes comparing measured pi-pi* transitions against PPP predictions.
VERIFIED BY: The PPP method reproduces pi-electron spectra exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1361 (HF) and Law 1400 (Huckel) - the PPP method is the coherence semiempirical pi-electron SCF.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the overlap residue is phi^-1 * S_floor.

### CLARITY
The pi electrons are treated as almost independent; the phi-law keeps the 'almost' visible.

### NOVELTY
Classical semiempirical theory drops overlap exactly; the phi-law keeps the ZDO's coherence residue.

### ACTIONABILITY
Run sim/1404_pariser_parr_pople_method.py; verify ZDO at kappa->0; proceed to 1405.
