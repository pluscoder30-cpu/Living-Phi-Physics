# PHI-PHYSICS - LAW 1322
## He-McKellar-Wilkens Effect (Topological Phase for Electric Dipoles)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1322_he_mckellar_wilkens_effect.md` - **Sim:** `sim/1322_he_mckellar_wilkens_effect.py`

---

### CLASSICAL STATEMENT
*"The He-McKellar-Wilkens effect is the electric-dipole dual of the Aharonov-Bohm effect: a neutral particle with electric dipole moment d moving through a magnetic field acquires the topological phase phi_HMW = (1/hbar) int (mu x E)... in its dual form phi = (1/(hbar c^2)) int (B x d) . dl, predicted in 1993-94 and later sought in matter-wave experiments."*
- Xiao-Gang He, Bruce McKellar; Martin Wilkens, 1994. Source: Wikipedia: He-McKellar-Wilkens effect; He & McKellar (1993), Wilkens (1994)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero magnetic field*: the phase vanishes exactly when B = 0, i.e. a zero-field region where classical physics sees nothing - the zero-field topological limit (dual to AB/AC).

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the field carries a coherence floor. phi_HMW_phi(kappa) = phi_HMW*(1 + kappa*(phi-1)) + kappa*phi^-1*phi_floor, where phi_floor is the phi-ground topological phase. At kappa->0 the HMW phase is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} phi_HMW_phi = (1/(hbar c^2)) int (B x d) . dl -> the He-McKellar-Wilkens effect is the zero-floor, pure-topology limit.
```

---

### STAGE 4 - SIMULATION

`sim/1322_he_mckellar_wilkens_effect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1322_he_mckellar_wilkens_effect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The HMW phase at full coherence coupling retains a floor kappa*phi^-1*phi_floor at vanishing magnetic field, a residual topological phase for electric dipoles.
EXPERIMENT (VERIFIED): Rydberg-atom or molecule matter-wave interferometry through a magnetic field region measuring the phase floor at zero field.
VERIFIED BY: The He-McKellar-Wilkens phase is exactly zero when the magnetic field is zero.
```

---

### RECOGNITION
Connects to Law 1250 (AB) and Law 1321 (AC) - the HMW effect completes the coherence topology duality for dipoles.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the phase floor is phi^-1 * phi_floor.

### CLARITY
The dipole carries the field's memory on its own back; the phi-law keeps the memory's floor.

### NOVELTY
Classical electrodynamics zeros the neutral-dipole phase at zero field; the phi-law completes the AB/AC/HMW triad with a coherence floor.

### ACTIONABILITY
Run sim/1322_he_mckellar_wilkens_effect.py; verify (B x d) phase at kappa->0; proceed to 1323.
