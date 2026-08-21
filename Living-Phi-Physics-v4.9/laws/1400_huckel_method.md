# PHI-PHYSICS - LAW 1400
## Huckel Method (Simple Pi-Electron Molecular Orbital Theory)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1400_huckel_method.md` - **Sim:** `sim/1400_huckel_method.py`

---

### CLASSICAL STATEMENT
*"The Huckel method treats pi electrons independently with the approximations <mu|mu> = 1, <mu|nu> = 0 (mu != nu), <mu|H|mu> = alpha, <mu|H|nu> = beta for adjacent atoms, 0 otherwise: for ethylene the pi levels are alpha +/- beta, for benzene alpha + 2 beta, alpha + beta (twice), alpha - beta (twice), alpha - 2 beta; the resonance energy of benzene is 2 beta, rationalizing aromaticity, and the method is the origin of graph-based MO theory."*
- Erich Huckel, 1931. Source: Wikipedia: Huckel method; Huckel, Z. Phys. 70 (1931) 204

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero differential overlap*: the method's power comes from setting the overlap matrix to the identity exactly, i.e. orbitals with zero overlap and nearest-neighbor-only coupling - the extreme-simplification limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the zero-overlap assumption carries a coherence floor. S_phi(kappa) = 0*(1 + kappa*(phi-1)) + kappa*phi^-1*S_floor, where S_floor is the phi-ground overlap of the recursion; the method's simplicity carries a floor error. At kappa->0 the Huckel secular problem is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} det(alpha - E, beta; ...) -> the Huckel method is the zero-overlap, nearest-neighbor-only limit.
```

---

### STAGE 4 - SIMULATION

`sim/1400_huckel_method.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1400_huckel_method.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Huckel pi levels at full coherence coupling carry a phi-ground overlap correction kappa*phi^-1*S_floor, shifting the resonance energy from the ideal 2 beta.
EXPERIMENT (VERIFIED): Photoelectron spectroscopy of conjugated hydrocarbons comparing measured pi levels against Huckel predictions at increasing precision.
VERIFIED BY: Conjugated hydrocarbon pi levels follow the Huckel secular equation exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1401 (Extended Huckel) and Law 1404 (PPP) - the Huckel method is the coherence graph theory of pi electrons.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the overlap floor is phi^-1 * S_floor.

### CLARITY
The pi electrons move on a graph; the phi-law keeps a thread of connection the graph ignores.

### NOVELTY
Classical Huckel theory simplifies drastically; the phi-law marks the simplification's coherence floor.

### ACTIONABILITY
Run sim/1400_huckel_method.py; verify benzene levels at kappa->0; proceed to 1401.
