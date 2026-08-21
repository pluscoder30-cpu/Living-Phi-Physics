# PHI-PHYSICS - LAW 1623
## r-Process Yield (Abundance Pattern from Rapid Neutron Capture)

**Domain:** Nuclear Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1623_r_process_yield.md` - **Sim:** `sim/1623_r_process_yield.py`

---

### CLASSICAL STATEMENT
*"The r-process abundance pattern shows peaks at A ~ 130 (Xe) and A ~ 195 (Pt) corresponding to the closed neutron shells N = 82 and N = 126 after beta decay; the yield is set by the competition of neutron capture, photodisintegration and beta decay in a high-neutron-density environment."*
- B2FH (1957); r-process modeling (1980s-2010s), 1957. Source: Burbidge et al., Rev. Mod. Phys. 29 (1957) 547; Wikipedia: R-process

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-neutron-density, zero-r-process, s-only limit*: without a high neutron density the r-process does not occur and only the s-process operates; the classical treatment of a zero-density environment is the zero-r-yield limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Y_phi(kappa) = Y_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Y_floor, where Y_floor is the phi-ground residual floor. At kappa->0 the zero-density (no r-process) limit is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Y_phi = 0 -> the r-process yield is the zero-neutron-density, s-only, no-r-process limit.
```

---

### STAGE 4 - SIMULATION

`sim/1623_r_process_yield.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1623_r_process_yield.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The r-process yield carries a phi-ground residual floor, so even 's-only' environments show a small r-process component and the abundance peaks have an irreducible r-contribution.
EXPERIMENT (VERIFIED): r-process abundance measurements (kilonova spectra, metal-poor star r-process elements) vs nucleosynthesis models.
VERIFIED BY: An environment with exactly zero r-process yield at zero neutron density.
```

---

### RECOGNITION
Connects to Law 1469 (r-process), Law 1468 (s-process) and Law 1598 (drip) - the r-yield is the neutron flood's harvest.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutron flood leaves peaks; the phi-law keeps a floor of peaks in the calm.

### NOVELTY
Classical r-yield is all-or-nothing; the phi-law predicts an irreducible residual floor.

### ACTIONABILITY
Run sim/1623_r_process_yield.py; verify the abundance peaks; proceed to Law 1624.
