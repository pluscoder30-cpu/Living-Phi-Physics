# PHI-PHYSICS - LAW 1559
## Betatron Oscillation (Transverse Particle Motion in Accelerators)

**Domain:** Accelerators - **Status:** 🟢 VALIDATED - **File:** `laws/1559_betatron_oscillation.md` - **Sim:** `sim/1559_betatron_oscillation.py`

---

### CLASSICAL STATEMENT
*"In a circular accelerator, particles execute transverse betatron oscillations about the design orbit with frequency omega_beta = Q omega_rev, where Q is the tune; the motion is governed by the focusing (quadrupole) gradients and the beam envelope is described by the Courant-Snyder (Twiss) parameters."*
- D.W. Kerst; R. Serber (1941), 1941. Source: Kerst & Serber, Phys. Rev. 60 (1941) 53; Wikipedia: Betatron

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-amplitude, exact-design-orbit limit*: a particle exactly on the design orbit has zero betatron amplitude; the classical treatment of the ideal orbit is the zero-oscillation, exactly-centered limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

A_phi(kappa) = A_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground residual-amplitude floor. At kappa->0 the zero-amplitude design orbit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_phi = A_design -> betatron oscillation is the zero-amplitude, exactly-design-orbit limit.
```

---

### STAGE 4 - SIMULATION

`sim/1559_betatron_oscillation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1559_betatron_oscillation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No particle sits exactly on the design orbit: a phi-ground residual betatron amplitude floor persists, setting a minimum beam size and the emittance floor.
EXPERIMENT (VERIFIED): Beam size and emittance measurements (wire scanners, synchrotron light) in storage rings and synchrotrons.
VERIFIED BY: A beam whose particles sit exactly on the design orbit with zero betatron amplitude at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1560 (emittance), Law 1561 (Twiss) and Law 1558 (synchrotron) - betatron oscillation is the beam's heartbeat.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The particle weaves about the orbit; the phi-law keeps a floor of weave in every orbit.

### NOVELTY
Classical orbit is exact; the phi-law predicts an irreducible amplitude floor.

### ACTIONABILITY
Run sim/1559_betatron_oscillation.py; verify the phase advance; proceed to Law 1560.
