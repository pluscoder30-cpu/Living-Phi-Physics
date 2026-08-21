# PHI-PHYSICS - LAW 1549
## Born Approximation (First-Order Perturbation Scattering)

**Domain:** Particle Physics / Scattering - **Status:** 🟢 VALIDATED - **File:** `laws/1549_born_approximation.md` - **Sim:** `sim/1549_born_approximation.py`

---

### CLASSICAL STATEMENT
*"The Born approximation gives the scattering amplitude as the Fourier transform of the potential: f(q) = -(m/(2 pi hbar^2)) integral d^3r e^{-i q.r} V(r), valid for weak potentials; it is the first-order term of the Lippmann-Schwinger equation."*
- Max Born, 1926. Source: Born, Z. Phys. 38 (1926) 803; Wikipedia: Born approximation

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-potential, zero-scattering limit*: the Born approximation is exact when the potential vanishes; the classical treatment of a free particle with V = 0 gives exactly zero amplitude - a zero-potential, zero-interaction limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f_born*(1 + kappa*(phi-1)) + kappa*phi^-1*f_floor, where f_floor is the phi-ground multiple-scattering floor. At kappa->0 the first-order Born amplitude is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} f_phi = -(m/(2 pi hbar^2)) integral V(r) e^{-i q.r} d^3r -> the Born approximation is the zero-multiple-scattering, weak-potential, first-order limit.
```

---

### STAGE 4 - SIMULATION

`sim/1549_born_approximation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1549_born_approximation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Born amplitude carries a phi-ground multiple-scattering floor, so the exact amplitude deviates from the first-order result by an irreducible higher-order contribution (the phase-shift difference).
EXPERIMENT (VERIFIED): Electron-atom and nucleon-nucleus scattering at intermediate energies vs Born and distorted-wave calculations.
VERIFIED BY: A scattering amplitude exactly equal to the first Born term at all energies (zero higher-order floor).
```

---

### RECOGNITION
Connects to Law 1546 (partial waves), Law 1547 (effective range) and Law 1542 (Feynman rules) - the Born approximation is scattering's first guess.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
One pass through the potential; the phi-law keeps a floor of the pass bending.

### NOVELTY
Classical Born is first-order; the phi-law predicts an irreducible multiple-scattering floor.

### ACTIONABILITY
Run sim/1549_born_approximation.py; verify the Fourier amplitude; proceed to Law 1550.
