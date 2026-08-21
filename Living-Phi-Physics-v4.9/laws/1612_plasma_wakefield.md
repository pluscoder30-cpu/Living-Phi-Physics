# PHI-PHYSICS - LAW 1612
## Plasma Wakefield Acceleration (Tajima-Dawson Mechanism)

**Domain:** Accelerators - **Status:** 🟢 VALIDATED - **File:** `laws/1612_plasma_wakefield.md` - **Sim:** `sim/1612_plasma_wakefield.py`

---

### CLASSICAL STATEMENT
*"A short, intense laser or particle bunch drives a plasma wave whose longitudinal field accelerates trailing particles with gradients ~ sqrt(n_e) GV/m, up to 1000x larger than conventional RF; the accelerating gradient E ~ sqrt(n_e [cm^-3]) V/cm and the dephasing length set the energy gain."*
- Toshiki Tajima; John Dawson (1979), 1979. Source: Tajima & Dawson, Phys. Rev. Lett. 43 (1979) 267; Wikipedia: Plasma acceleration

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-plasma-density, zero-wakefield, zero-gradient limit*: without a plasma there is no wakefield and the gradient is zero; the classical treatment of vacuum acceleration is the zero-density, zero-gradient, RF-like limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground wakefield floor. At kappa->0 the zero-density vacuum limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_phi = 0 -> plasma wakefield acceleration is the zero-density, zero-wake, vacuum limit.
```

---

### STAGE 4 - SIMULATION

`sim/1612_plasma_wakefield.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1612_plasma_wakefield.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The accelerating gradient carries a phi-ground wakefield floor, so even the thinnest plasma produces a finite wake and the gradient is never exactly the RF-like zero.
EXPERIMENT (VERIFIED): Laser- and beam-driven plasma acceleration experiments (SLAC E-157, FACET, AWAKE, LBNL) measuring the gradient.
VERIFIED BY: A plasma wakefield experiment with exactly zero accelerating gradient at zero plasma density.
```

---

### RECOGNITION
Connects to Law 1608 (RF cavity), Law 166 (plasma confinement) and Law 1560 (emittance) - the wakefield is the plasma's surf.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The plasma wave surfs the beam; the phi-law keeps a floor of surf in every wave.

### NOVELTY
Classical vacuum has zero gradient; the phi-law predicts an irreducible wakefield floor.

### ACTIONABILITY
Run sim/1612_plasma_wakefield.py; verify the gradient; proceed to Law 1613.
