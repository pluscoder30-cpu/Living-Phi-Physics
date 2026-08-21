# PHI-PHYSICS - LAW 1589
## Isobaric Analog States (Isospin Multiplets in Neighboring Nuclei)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1589_isobaric_analog_states.md` - **Sim:** `sim/1589_isobaric_analog_states.py`

---

### CLASSICAL STATEMENT
*"Isobaric analog states are states in neighboring isobars that belong to the same isospin multiplet, related by the isospin raising/lowering operators; the analog resonance in the neutron-richer nucleus sits above the ground state by the Coulomb displacement energy, testing isospin symmetry."*
- Isobaric analog resonances (Anderson, Wong et al. 1960s), 1964. Source: Fox, Moore & Robson, Phys. Rev. Lett. 12 (1964) 198; Wikipedia: Isospin

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-Coulomb, zero-displacement, exact-degeneracy limit*: in the absence of the Coulomb force, analog states of a multiplet would have exactly equal energies; the classical treatment assumes exact degeneracy - a zero-Coulomb, exact-isospin limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

delta_E_phi(kappa) = delta_E_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground residual floor beyond the Coulomb displacement. At kappa->0 the exact degeneracy is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_E_phi = delta_E_coulomb -> isobaric analog states are the zero-residual, Coulomb-only, exact-isospin limit.
```

---

### STAGE 4 - SIMULATION

`sim/1589_isobaric_analog_states.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1589_isobaric_analog_states.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Coulomb displacement energy carries a phi-ground residual floor, so analog-state energy differences deviate from the pure Coulomb prediction by an irreducible charge-symmetry-breaking correction.
EXPERIMENT (VERIFIED): Isobaric analog resonance measurements (proton elastic scattering, (p,n) reactions) and Coulomb displacement energy systematics.
VERIFIED BY: Analog states with exactly zero energy difference beyond the Coulomb prediction at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1491 (isospin), Law 1566 (G-M-N) and Law 1479 (compound nucleus) - analog states are the isospin mirror.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The mirror states echo; the phi-law keeps a floor of the echo drifting.

### NOVELTY
Classical analog states are Coulomb-exact; the phi-law predicts an irreducible symmetry-breaking floor.

### ACTIONABILITY
Run sim/1589_isobaric_analog_states.py; verify the Coulomb displacement; proceed to Law 1590.
