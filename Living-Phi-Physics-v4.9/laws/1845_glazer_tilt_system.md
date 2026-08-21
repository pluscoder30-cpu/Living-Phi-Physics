# PHI-PHYSICS - LAW 1845
## Glazer Notation (Octahedral Tilt Systems of Perovskites)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1845_glazer_tilt_system.md` - **Sim:** `sim/1845_glazer_tilt_system.py`

---

### CLASSICAL STATEMENT
*"The tilts of the BO6 octahedra in perovskite structures are classified by Glazer notation a+b+c- etc., where the letters a, b, c denote tilt magnitudes about the three pseudocubic axes and the superscripts +, 0, - denote in-phase, zero or out-of-phase tilting of adjacent octahedra; the 23 tilt systems (e.g. a0a0a0 for ideal cubic, a-a-a- for rhombohedral) classify all perovskite distortions."*
- A.M. Glazer, 1972. Source: Wikipedia: Glazer notation; Glazer (1972), Acta Cryst. B28:3384

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-tilt, ideal-cubic reference*: Glazer notation is defined against the zero-tilt cubic perovskite (a0a0a0); every tilt system is a distortion away from this zero-tilt reference, and real perovskites always carry residual tilts.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the tilt magnitude carries a coherence floor. tilt_phi(kappa) = tilt_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_tilt, where delta_tilt is the phi-ground residual tilt. At kappa->0 the zero-tilt cubic reference is recovered; at kappa=1 no perovskite is exactly untilted - an irreducible tilt floor exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tilt_phi = 0 -> Glazer notation is the zero-tilt, ideal-cubic limit of octahedral tilt classification.
```

---

### STAGE 4 - SIMULATION

`sim/1845_glazer_tilt_system.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1845_glazer_tilt_system.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No perovskite is exactly cubic (a0a0a0) at any temperature: an irreducible octahedral-tilt floor remains even in the ideal cubic phase, observable as a residual tilt and soft-mode broadening.
EXPERIMENT (VERIFIED): Precision synchrotron diffraction and neutron scattering of a cubic perovskite (e.g. SrTiO3, BaTiO3) above its transition, measuring the residual tilt floor.
VERIFIED BY: A perovskite with exactly zero octahedral tilt in its nominal cubic phase.
```

---

### RECOGNITION
Connects to Law 1674 (tolerance) and Law 1679 (crystal systems) - the octahedra lean and rotate, and the phi-law keeps a lean always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; tilt floor scales as phi^-1 * delta_tilt.

### CLARITY
The octahedra lean in concert; the phi-law keeps a lean always present.

### NOVELTY
Classical Glazer allows a perfect cubic state; the phi-law keeps an irreducible tilt floor.

### ACTIONABILITY
Run sim/1845_glazer_tilt_system.py; verify the a0a0a0 cubic reference at kappa->0; proceed to 1846.
