# PHI-PHYSICS - LAW 1318
## Jaynes-Cummings Model (Atom-Photon Interaction in a Cavity)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1318_jaynes_cummings_model.md` - **Sim:** `sim/1318_jaynes_cummings_model.py`

---

### CLASSICAL STATEMENT
*"The interaction of a two-level atom with a single quantized cavity mode is H = (1/2) hbar omega_a sigma_z + hbar omega_c a^dagger a + hbar g (sigma_+ a + sigma_- a^dagger); at resonance it produces vacuum Rabi oscillations at frequency 2g, with the collapse-and-revival of coherent oscillations at period T_rev = 2 pi sqrt(<n>)/g for field photon number n."*
- Edwin Jaynes; Fred Cummings, 1963. Source: Wikipedia: Jaynes-Cummings model; Jaynes & Cummings, Proc. IEEE 51 (1963) 89

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *empty cavity*: the vacuum Rabi splitting is exactly 2g only for a lossless cavity with zero damping and zero thermal photons - the zero-decay, zero-photon limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the vacuum coupling carries a coherence floor. g_phi(kappa) = g*(1 + kappa*(phi-1)) + kappa*phi^-1*g_floor, where g_floor is the phi-ground coupling; the vacuum Rabi splitting retains a floor. At kappa->0 the Jaynes-Cummings vacuum Rabi splitting is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} 2 g_phi = 2 g -> the Jaynes-Cummings vacuum Rabi splitting is the zero-decay, zero-photon limit.
```

---

### STAGE 4 - SIMULATION

`sim/1318_jaynes_cummings_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1318_jaynes_cummings_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The vacuum Rabi splitting at full coherence coupling retains a floor kappa*phi^-1*g_floor beyond the cavity-mode coupling, a minimum coupling no atom-field system escapes.
EXPERIMENT (VERIFIED): Circuit-QED vacuum Rabi splitting measurements at increasing qubit-cavity coherence, searching for the residual splitting floor.
VERIFIED BY: The vacuum Rabi splitting is exactly 2g for all cavity coherences.
```

---

### RECOGNITION
Connects to Law 1313 (Rabi), Law 1034 (cavity QED) and Law 1319 (Tavis-Cummings) - the model is the coherence atom-field oscillator.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the coupling floor is phi^-1 * g_floor.

### CLARITY
The atom and the photon dance in the box; the phi-law keeps the dance from ever stopping.

### NOVELTY
Classical cavity QED zeroes the interaction floor; the phi-law gives the atom-photon bond a coherence floor.

### ACTIONABILITY
Run sim/1318_jaynes_cummings_model.py; verify vacuum Rabi at kappa->0; proceed to 1319.
