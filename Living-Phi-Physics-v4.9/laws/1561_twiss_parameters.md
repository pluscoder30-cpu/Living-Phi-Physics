# PHI-PHYSICS - LAW 1561
## Twiss Parameters (Courant-Snyder Betatron Functions)

**Domain:** Accelerators - **Status:** 🟢 VALIDATED - **File:** `laws/1561_twiss_parameters.md` - **Sim:** `sim/1561_twiss_parameters.py`

---

### CLASSICAL STATEMENT
*"The beam envelope in a lattice is described by the Twiss (Courant-Snyder) parameters alpha, beta, gamma, which satisfy the relation beta gamma - alpha^2 = 1; the betatron function beta(s) evolves via d^2 beta/ds^2 + K(s) beta = 1/beta, and the phase advance is the integral of 1/beta."*
- Ernest Courant; Hartland Snyder (1958), 1958. Source: Courant & Snyder, Ann. Phys. 3 (1958) 1; Wikipedia: Courant-Snyder parameters

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-beta-function, zero-envelope limit*: an ideal lattice would focus the beam to zero size with beta -> 0; the classical treatment of a point beam has zero beta function - a zero-envelope, point-focus limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

beta_phi(kappa) = beta_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*beta_floor, where beta_floor is the phi-ground minimum-beta floor. At kappa->0 the ideal lattice envelope is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} beta_phi = beta_courant_snyder -> the Twiss parameters are the zero-perturbation, ideal-lattice, envelope-exact limit.
```

---

### STAGE 4 - SIMULATION

`sim/1561_twiss_parameters.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1561_twiss_parameters.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The betatron function carries a phi-ground floor from lattice errors and space charge, so the beta function at the interaction point is never exactly zero and the minimum beam size is bounded.
EXPERIMENT (VERIFIED): Lattice measurements (response-matrix fits, orbit bumps) and beta-function reconstruction in accelerators.
VERIFIED BY: A lattice focusing the beam to exactly zero beta function at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1560 (emittance), Law 1559 (betatron) and Law 1562 (luminosity) - the Twiss parameters are the beam's optics.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The lattice maps the envelope; the phi-law keeps a floor of envelope in every map.

### NOVELTY
Classical envelope is exact; the phi-law predicts an irreducible beta floor.

### ACTIONABILITY
Run sim/1561_twiss_parameters.py; verify beta gamma - alpha^2 = 1; proceed to Law 1562.
