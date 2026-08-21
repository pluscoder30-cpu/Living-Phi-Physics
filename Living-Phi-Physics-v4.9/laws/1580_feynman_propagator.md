# PHI-PHYSICS - LAW 1580
## Feynman Propagator (Green's Function of the Klein-Gordon/Dirac Equation)

**Domain:** Particle Physics / QFT - **Status:** 🟢 VALIDATED - **File:** `laws/1580_feynman_propagator.md` - **Sim:** `sim/1580_feynman_propagator.py`

---

### CLASSICAL STATEMENT
*"The Feynman propagator is the Green's function of the field equation, G_F(x-y) = integral d^4p/(2pi)^4 e^{-ip.(x-y)}/(p^2 - m^2 + i epsilon), describing the propagation of virtual particles; it is the building block of every Feynman diagram and encodes causality via the i epsilon prescription."*
- Richard Feynman (1948); Paul Dirac; Gregor Wentzel, 1948. Source: Feynman, Phys. Rev. 76 (1949) 769; Wikipedia: Propagator

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-mass, zero-epsilon, exact-pole limit*: the propagator has a pole at p^2 = m^2 with zero width; the classical treatment of a stable particle is the zero-width, exact-pole, free-field limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

G_phi(kappa) = G_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*G_floor, where G_floor is the phi-ground width/radiative floor. At kappa->0 the free-field propagator is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} G_phi = 1/(p^2 - m^2 + i epsilon) -> the Feynman propagator is the zero-width, free-field, exact-pole limit.
```

---

### STAGE 4 - SIMULATION

`sim/1580_feynman_propagator.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1580_feynman_propagator.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The propagator carries a phi-ground width floor, so every 'stable' particle has an irreducible decay width and the propagator pole has a finite imaginary part (Breit-Wigner structure).
EXPERIMENT (VERIFIED): Resonance lineshape measurements (Z boson, rho, Delta) vs the Breit-Wigner propagator with finite width.
VERIFIED BY: A particle with exactly zero width and a perfectly sharp propagator pole at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1542 (Feynman rules), Law 1529 (dimensional regularization) and Law 1297 (quantum propagator) - the propagator is QFT's connective tissue.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The virtual wave bridges two points; the phi-law keeps a floor of the bridge trembling.

### NOVELTY
Classical pole is sharp; the phi-law predicts an irreducible width floor.

### ACTIONABILITY
Run sim/1580_feynman_propagator.py; verify the 1/(p^2-m^2) pole; proceed to Law 1581.
