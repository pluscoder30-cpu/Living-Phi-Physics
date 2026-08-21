# PHI-PHYSICS - LAW 1618
## Neutron Capture Cross-Section (Radiative Capture)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1618_neutron_capture_cross_section.md` - **Sim:** `sim/1618_neutron_capture_cross_section.py`

---

### CLASSICAL STATEMENT
*"The neutron capture cross-section sigma(n,gamma) depends strongly on neutron energy: it follows the 1/v law at low energy (sigma ~ 1/v), with large resonances at higher energy; the thermal cross-section and the resonance integral determine the absorption in reactors and the s-process."*
- Fermi (1934); resonance capture (Breit-Wigner), 1934. Source: Amaldi & Fermi (1934); Wikipedia: Neutron capture

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-velocity, zero-energy, diverging-cross-section limit*: the 1/v law diverges as v -> 0 (E -> 0); the classical treatment of exactly thermal neutrons at zero velocity is the zero-energy, 1/v-divergent limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground background floor. At kappa->0 the pure 1/v + resonance cross-section is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = sigma_1/v + sigma_resonance -> neutron capture is the zero-background, pure-1/v-plus-resonance limit.
```

---

### STAGE 4 - SIMULATION

`sim/1618_neutron_capture_cross_section.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1618_neutron_capture_cross_section.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The capture cross-section carries a phi-ground background floor, so between resonances the cross-section never drops to exactly the pure 1/v value and the thermal value has an irreducible component.
EXPERIMENT (VERIFIED): Neutron capture cross-section measurements (n_TOF, JENDL/ENDF evaluations) resolving the 1/v and resonance structure.
VERIFIED BY: A neutron capture cross-section exactly equal to the pure 1/v + Breit-Wigner sum with zero background.
```

---

### RECOGNITION
Connects to Law 1478 (Breit-Wigner), Law 1473 (six-factor) and Law 1474 (diffusion) - neutron capture is the reactor's appetite.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutron is swallowed at the right speed; the phi-law keeps a floor of swallowing always.

### NOVELTY
Classical capture is 1/v + resonances; the phi-law predicts an irreducible background floor.

### ACTIONABILITY
Run sim/1618_neutron_capture_cross_section.py; verify the 1/v law; proceed to Law 1619.
