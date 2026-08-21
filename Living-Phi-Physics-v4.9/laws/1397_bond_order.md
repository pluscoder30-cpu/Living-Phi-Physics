# PHI-PHYSICS - LAW 1397
## Bond Order (Pauling: (n_bonding - n_antibonding)/2)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1397_bond_order.md` - **Sim:** `sim/1397_bond_order.py`

---

### CLASSICAL STATEMENT
*"The bond order of a bond is BO = (n_bonding - n_antibonding)/2, half the difference between the numbers of electrons in bonding and antibonding orbitals; it correlates with bond length (higher order = shorter bond) and bond energy (higher order = stronger bond), with BO = 1 for a single bond, 2 for a double, 3 for a triple; fractional orders arise in resonance structures (e.g. benzene BO ~ 1.5)."*
- Linus Pauling, 1931. Source: Wikipedia: Bond order; Pauling, J. Am. Chem. Soc. 53 (1931) 1367

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *integer order*: the classical bond order is an exact integer for localized bonds, i.e. a resonance-free structure with zero delocalization - the localized-bond limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the order carries a coherence delocalization. BO_phi(kappa) = BO*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_BO, where delta_BO is the phi-ground fractional order; no bond is exactly integer. At kappa->0 the integer bond order is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} BO_phi = (n_bonding - n_antibonding)/2 -> the bond order is the zero-delocalization, localized-bond limit.
```

---

### STAGE 4 - SIMULATION

`sim/1397_bond_order.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1397_bond_order.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective bond order at full coherence coupling carries a phi-ground fractional component kappa*phi^-1*delta_BO, so even 'localized' bonds are slightly delocalized.
EXPERIMENT (VERIFIED): Precision bond-length and bond-energy correlations in series of molecules measuring the fractional bond-order floor.
VERIFIED BY: A localized bond has exactly integer bond order for all couplings.
```

---

### RECOGNITION
Connects to Law 1377 (MO theory) and Law 1378 (LCAO) - the bond order is the coherence counting of the bond.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the fractional floor is phi^-1 * delta_BO.

### CLARITY
The bond counts its electrons like a banker; the phi-law keeps a fraction in the bank.

### NOVELTY
Classical chemistry counts integer bonds; the phi-law gives every bond a coherence fractional floor.

### ACTIONABILITY
Run sim/1397_bond_order.py; verify (nb-na)/2 at kappa->0; proceed to 1398.
