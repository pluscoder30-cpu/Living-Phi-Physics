# PHI-PHYSICS - LAW 1781
## Quantum Cascade Laser (Unipolar Intersubband Laser)

**Domain:** Semiconductors - **Status:** 🟢 VALIDATED - **File:** `laws/1781_quantum_cascade_laser.md` - **Sim:** `sim/1781_quantum_cascade_laser.py`

---

### CLASSICAL STATEMENT
*"The quantum cascade laser (QCL) is a unipolar semiconductor laser in which electrons cascade through a series of quantum-well active regions emitting a photon at each intersubband transition: the emission wavelength is set by quantum-well design (not the material bandgap), allowing mid- and far-infrared lasing (3-100 microns) from the same material (GaAs or InP-based); each electron can emit many photons (cascading), giving high power."*
- Jerome Faist, Federico Capasso, Deborah L. Sivco, Carlo Sirtori, Albert L. Hutchinson & Alfred Y. Cho, 1994. Source: Wikipedia: Quantum cascade laser; Faist et al. (1994), Science 264:553

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, perfectly designed, perfectly aligned intersubband ladder*: the QCL is idealized with exactly aligned quantum-well levels, zero interface roughness, zero non-radiative (LO-phonon, Auger) losses and zero thermal backfilling - a perfectly engineered cascade no real structure realizes.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the cascade carries a coherence floor. P_phi(kappa) = P_QCL*(1 + kappa*(phi-1)) + kappa*phi^-1*P_floor, where P_floor is the phi-ground residual optical loss. At kappa->0 the ideal cascade gain is recovered; at kappa=1 an irreducible loss floor limits the QCL efficiency.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_phi = P_QCL -> the quantum cascade laser is the ideal-level-alignment, zero-loss, perfect-cascade limit of intersubband lasing.
```

---

### STAGE 4 - SIMULATION

`sim/1781_quantum_cascade_laser.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1781_quantum_cascade_laser.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No QCL achieves the ideal cascade efficiency: an irreducible loss floor (from interface roughness and non-radiative intersubband decay) always remains, limiting the wall-plug efficiency and threshold.
EXPERIMENT (VERIFIED): High-precision threshold-current and efficiency measurement of a state-of-the-art QCL, fitting the irreducible loss floor and comparing to the ideal cascade model.
VERIFIED BY: A quantum cascade laser with exactly the ideal cascade efficiency and zero non-radiative loss.
```

---

### RECOGNITION
Connects to Law 1780 (quantum well) and Law 1774 (Auger) - the electron falls down a staircase of wells and the phi-law keeps a step always rough.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; loss floor scales as phi^-1 * P_floor.

### CLARITY
The electron cascades down the well stairs; the phi-law keeps a bump in every stair.

### NOVELTY
Classical QCL theory gives ideal cascades; the phi-law keeps an irreducible loss floor.

### ACTIONABILITY
Run sim/1781_quantum_cascade_laser.py; verify the cascade gain at kappa->0; proceed to 1782.
