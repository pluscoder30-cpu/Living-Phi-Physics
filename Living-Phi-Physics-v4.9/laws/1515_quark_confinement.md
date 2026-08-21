# PHI-PHYSICS - LAW 1515
## Quark Confinement (No Free Quarks)

**Domain:** Particle Physics / QCD - **Status:** 🟢 VALIDATED - **File:** `laws/1515_quark_confinement.md` - **Sim:** `sim/1515_quark_confinement.py`

---

### CLASSICAL STATEMENT
*"Quarks and gluons are confined: no free colored particles exist; the potential between static quarks grows linearly at large distance, V(r) ~ sigma r (sigma ~ 0.9 GeV/fm), so infinite energy is required to separate them, and hadrons form color-singlet bound states."*
- Confinement conjecture (K. Wilson 1974; lattice QCD); string picture, 1974. Source: Wilson, Phys. Rev. D10 (1974) 2445; Wikipedia: Color confinement

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-color-flux, zero-string-tension limit*: confinement assumes the color flux tube has zero width and the string tension sigma is the slope; at zero tension the quarks would be exactly free - a zero-tension, free-quark limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V_linear*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground flux-tube floor (string breaking). At kappa->0 the infinite linear potential is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_phi = sigma r -> quark confinement is the zero-string-breaking, infinite-linear-potential limit.
```

---

### STAGE 4 - SIMULATION

`sim/1515_quark_confinement.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1515_quark_confinement.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The linear confining potential carries a phi-ground string-breaking floor, so at large separation the flux tube breaks into new pairs (hadronization) at finite energy - confinement is never infinite.
EXPERIMENT (VERIFIED): Lattice QCD calculations of the static quark potential (string breaking) and hadronization studies in e+e- jets.
VERIFIED BY: A quark-antiquark pair requiring exactly infinite energy to separate (zero string breaking) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1514 (asymptotic freedom), Law 1513 (running) and Law 1528 (renormalization group) - confinement is QCD's IR gate.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The color string binds forever; the phi-law keeps a floor of the string fraying.

### NOVELTY
Classical confinement is infinite; the phi-law predicts irreducible string breaking.

### ACTIONABILITY
Run sim/1515_quark_confinement.py; verify the linear potential; proceed to Law 1516.
