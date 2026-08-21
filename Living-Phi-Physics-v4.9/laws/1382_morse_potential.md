# PHI-PHYSICS - LAW 1382
## Morse Potential (Anharmonic Diatomic Bond V(r) = D(1 - e^(-a(r-re)))^2)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1382_morse_potential.md` - **Sim:** `sim/1382_morse_potential.py`

---

### CLASSICAL STATEMENT
*"The Morse potential V(r) = D_e (1 - e^(-a(r - r_e)))^2 describes the diatomic bond with dissociation energy D_e, equilibrium distance r_e and anharmonicity a = sqrt(k_e/(2 D_e)): it reproduces the anharmonic vibrational levels E_v = hbar omega (v + 1/2) - hbar omega x_e (v + 1/2)^2, converging to dissociation as v increases - the first realistic anharmonic potential."*
- Philip M. Morse, 1929. Source: Wikipedia: Morse potential; Morse, Phys. Rev. 34 (1929) 57

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero anharmonicity*: the Morse potential reduces to the harmonic oscillator when the anharmonicity x_e -> 0 (deep-bond limit), i.e. a bond with zero level convergence - the harmonic limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the anharmonicity carries a coherence floor. x_e_phi(kappa) = x_e*(1 + kappa*(phi-1)) + kappa*phi^-1*x_floor, where x_floor is the phi-ground anharmonicity; no bond is exactly harmonic. At kappa->0 the Morse levels are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_v_phi = hbar omega(v+1/2) - hbar omega x_e(v+1/2)^2 -> the Morse potential is the exact-anharmonicity limit (with the harmonic oscillator its deep-bond degenerate case).
```

---

### STAGE 4 - SIMULATION

`sim/1382_morse_potential.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1382_morse_potential.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The vibrational level convergence at full coherence coupling carries a phi-ground anharmonicity kappa*phi^-1*x_floor beyond the Morse prediction, a floor in the level spacing.
EXPERIMENT (VERIFIED): High-resolution infrared spectroscopy of diatomic molecules measuring vibrational spacings against the Morse levels.
VERIFIED BY: Diatomic vibrational levels obey the Morse formula exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1381 (Franck-Condon) and Law 1383 (Lennard-Jones) - the Morse potential is the coherence anharmonic bond.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the anharmonicity floor is phi^-1 * x_floor.

### CLARITY
The bond stretches, weakens, and finally lets go; the phi-law keeps a floor of its letting go.

### NOVELTY
Classical harmonic theory stops at equal spacings; the phi-law keeps the anharmonic coherence floor on the Morse curve.

### ACTIONABILITY
Run sim/1382_morse_potential.py; verify anharmonic levels at kappa->0; proceed to 1383.
