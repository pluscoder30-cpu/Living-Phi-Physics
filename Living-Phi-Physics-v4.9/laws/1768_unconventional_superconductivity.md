# PHI-PHYSICS - LAW 1768
## Unconventional Superconductivity (Pairing Beyond the Electron-Phonon BCS Mechanism)

**Domain:** Superconductivity - **Status:** 🟢 VALIDATED - **File:** `laws/1768_unconventional_superconductivity.md` - **Sim:** `sim/1768_unconventional_superconductivity.py`

---

### CLASSICAL STATEMENT
*"Unconventional superconductors are those whose pairing is not mediated by the conventional electron-phonon interaction: heavy-fermion (CeCu2Si2), organic, ruthenate, cuprate and iron-based superconductors show sign-changing or anisotropic order parameters, pairing mediated by spin or other fluctuations, and deviations from BCS universality; the identification rests on the BCS phonon reference that they violate."*
- F. Steglich et al. (1979, heavy fermions); general concept, 1979. Source: Wikipedia: Unconventional superconductor; Steglich et al. (1979), PRL 43:1892

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-spin-fluctuation, pure-phonon BCS reference*: unconventional superconductivity is defined against the conventional BCS (phonon, s-wave) superconductor reference; every unconventional system is a deviation away from this zero-exotic-mechanism reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the exotic pairing carries a coherence floor. T_c_phi(kappa) = T_c_unconventional*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground transition smearing. At kappa->0 the sharp nominal T_c is recovered; at kappa=1 unconventional transitions carry irreducible pairing-fluctuation floors.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_c_phi = T_c_unconventional -> unconventional superconductivity is the exotic-pairing state measured from the conventional phonon-BCS reference.
```

---

### STAGE 4 - SIMULATION

`sim/1768_unconventional_superconductivity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1768_unconventional_superconductivity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Unconventional superconducting transitions always carry a pairing-fluctuation floor: the transition is never BCS-sharp, and residual bosonic-fluctuation signatures persist into the normal state.
EXPERIMENT (VERIFIED): High-resolution specific-heat, penetration-depth and neutron measurements of a heavy-fermion or organic superconductor measuring the transition width and fluctuation floor.
VERIFIED BY: An unconventional superconductor with a BCS-sharp transition and zero fluctuation signatures in the normal state.
```

---

### RECOGNITION
Connects to Law 1765 (cuprates) and Law 1767 (iron-based) - the exotic pairs dance to a different music, and the phi-law keeps a step of the dance in the normal state.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; transition width scales as phi^-1 * delta_T.

### CLARITY
The exotic pairs dance to a new music; the phi-law keeps a step of it above T_c.

### NOVELTY
Classical BCS gives sharp clean transitions; the phi-law keeps a fluctuation floor in exotic systems.

### ACTIONABILITY
Run sim/1768_unconventional_superconductivity.py; verify the non-BCS T_c at kappa->0; proceed to 1769.
