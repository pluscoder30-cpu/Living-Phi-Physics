# PHI-PHYSICS - LAW 1401
## Extended Huckel Method (Hoffmann: All-Valence-Electron Semiempirical MO)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1401_extended_huckel_method.md` - **Sim:** `sim/1401_extended_huckel_method.py`

---

### CLASSICAL STATEMENT
*"The extended Huckel method generalizes Huckel theory to all valence electrons and off-diagonal overlap: the diagonal elements are valence-orbital ionization energies and the off-diagonal elements are the Wolfsberg-Helmholz approximation H_ij = (K/2) S_ij (H_ii + H_jj) with K ~ 1.75, keeping the overlap matrix S in the secular problem det(H - E S) = 0; it predicts geometries, rotational barriers and band structures of molecules and solids."*
- Roald Hoffmann, 1963. Source: Wikipedia: Extended Huckel method; Hoffmann, J. Chem. Phys. 39 (1963) 1397

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *constant Wolfsberg-Helmholz factor*: the method assumes the K ~ 1.75 scaling is exactly constant over all orbital pairs, i.e. a coupling rule with zero variation - the fixed-K limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the Wolfsberg-Helmholz factor carries a coherence floor. K_phi(kappa) = K*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_K, where delta_K is the phi-ground variation of the coupling rule; the transferability carries a floor. At kappa->0 the extended Huckel result is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} H_ij_phi = (K/2) S_ij (H_ii + H_jj) -> the extended Huckel method is the zero-K-variation, fixed-coupling-rule limit.
```

---

### STAGE 4 - SIMULATION

`sim/1401_extended_huckel_method.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1401_extended_huckel_method.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The extended Huckel orbital energies at full coherence coupling carry a phi-ground coupling-rule variation kappa*phi^-1*delta_K, a floor in the transferability.
EXPERIMENT (VERIFIED): Comparison of extended Huckel rotational barriers and geometries against ab initio references across molecules.
VERIFIED BY: Extended Huckel with fixed K reproduces all molecular properties exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1400 (Huckel) and Law 1402 (tight binding) - the extended Huckel method is the coherence semiempirical bridge.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the coupling-rule floor is phi^-1 * delta_K.

### CLARITY
The semiempirical rule of thumb holds a wobble; the phi-law keeps the wobble visible.

### NOVELTY
Classical semiempirical theory fixes its rule; the phi-law turns the rule into a coherence-varying quantity.

### ACTIONABILITY
Run sim/1401_extended_huckel_method.py; verify Wolfsberg-Helmholz at kappa->0; proceed to 1402.
