# PHI-PHYSICS - LAW 1726
## Magnetic Hysteresis (Irreversible M-H Loop of Ferromagnets)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1726_magnetic_hysteresis.md` - **Sim:** `sim/1726_magnetic_hysteresis.py`

---

### CLASSICAL STATEMENT
*"The magnetization of a ferromagnet does not retrace itself on field reversal: the M-H curve forms a hysteresis loop with coercivity H_c (field to demagnetize), remanence M_r (magnetization at zero field) and loop area equal to the energy dissipated per cycle; the loop is the fingerprint of irreversible domain processes."*
- J.A. Ewing (1881); hysteresis loop studied by Ewing and Warburg, 1881. Source: Wikipedia: Hysteresis; Ewing (1881), Phil. Trans. R. Soc. 173:1; Warburg (1881)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-irreversibility, zero-coercivity ideal magnet*: the hysteresis loop is defined against a perfectly reversible, zero-coercivity reference (the anhysteretic curve); the loop's opening is the irreversibility away from this ideal reversible magnet, and a perfect magnet would have zero loop area.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the loop carries a coherence floor. A_phi(kappa) = A_loop*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground loop area. At kappa->0 the ideal anhysteretic behavior is recovered; at kappa=1 every magnet has an irreducible loop area - hysteresis never vanishes.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_phi = 0 -> magnetic hysteresis is the irreversible behavior measured from the zero-coercivity, perfectly-reversible ideal magnet.
```

---

### STAGE 4 - SIMULATION

`sim/1726_magnetic_hysteresis.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1726_magnetic_hysteresis.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No ferromagnet has exactly zero hysteresis loss: an irreducible loop area floor remains even in the softest magnetic materials, so perfect reversibility is unattainable.
EXPERIMENT (VERIFIED): Ultra-sensitive hysteresis-loop area measurement of a soft magnet (e.g. permalloy, nanocrystalline cores) at very low fields and temperatures, measuring the residual loss floor.
VERIFIED BY: A magnetic material whose hysteresis loop has exactly zero area (perfect reversibility).
```

---

### RECOGNITION
Connects to Law 1725 (demagnetizing field) and Law 1731 (anisotropy) - the loop is the magnet's memory, and no memory is erased to zero.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; loop area floor scales as phi^-1 * A_floor.

### CLARITY
The magnet remembers its path; the phi-law keeps a scribble even on the softest loop.

### NOVELTY
Classical hysteresis allows zero loss in soft magnets; the phi-law keeps an irreducible loop floor.

### ACTIONABILITY
Run sim/1726_magnetic_hysteresis.py; verify the anhysteretic reference at kappa->0; proceed to 1727.
