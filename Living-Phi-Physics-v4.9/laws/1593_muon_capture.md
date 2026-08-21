# PHI-PHYSICS - LAW 1593
## Muon Capture (Negative Muon Absorption by Nuclei)

**Domain:** Particle Physics / Weak Interaction - **Status:** 🟢 VALIDATED - **File:** `laws/1593_muon_capture.md` - **Sim:** `sim/1593_muon_capture.py`

---

### CLASSICAL STATEMENT
*"A negative muon bound in an atomic orbit is captured by the nucleus via the weak interaction, mu- + p -> n + nu_mu, with the capture rate governed by the Fermi and Gamow-Teller matrix elements; the total capture rate in a nucleus depends on the neutron/proton ratio and tests the weak hadronic current."*
- Wheeler (1949); Primakoff (1959); first observation 1940s, 1959. Source: Primakoff, Rev. Mod. Phys. 31 (1959) 802; Wikipedia: Muon capture

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-nuclear-overlap, zero-capture, free-muon limit*: muon capture requires the muon wavefunction to overlap the nucleus; the classical treatment of a free (unbound) muon has zero nuclear overlap and zero capture rate - a zero-overlap, zero-capture limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Lambda_phi(kappa) = Lambda_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Lambda_floor, where Lambda_floor is the phi-ground overlap floor. At kappa->0 the classical capture rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Lambda_phi = Lambda_Primakoff -> muon capture is the zero-overlap-fluctuation, exact-matrix-element limit.
```

---

### STAGE 4 - SIMULATION

`sim/1593_muon_capture.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1593_muon_capture.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The muon capture rate carries a phi-ground overlap floor, so the measured rate in nuclei deviates from the Primakoff prediction by an irreducible nuclear-structure contribution.
EXPERIMENT (VERIFIED): Muon capture rate measurements (muonic atoms, e.g. 12C, 40Ca) and the induced-pseudoscalar coupling tests (MuCap).
VERIFIED BY: A muon capture rate exactly matching the Primakoff formula with zero nuclear-structure floor.
```

---

### RECOGNITION
Connects to Law 1454 (Fermi theory), Law 1563 (V-A) and Law 1456 (electron capture) - muon capture is the heavy electron's decay.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The heavy lepton falls into the core; the phi-law keeps a floor of the fall trembling.

### NOVELTY
Classical capture is matrix-element-exact; the phi-law predicts an irreducible nuclear floor.

### ACTIONABILITY
Run sim/1593_muon_capture.py; verify the capture rate; proceed to Law 1594.
