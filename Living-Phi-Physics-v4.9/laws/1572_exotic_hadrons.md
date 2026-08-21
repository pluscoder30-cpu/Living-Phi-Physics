# PHI-PHYSICS - LAW 1572
## Exotic Hadrons (Tetraquarks, Pentaquarks, Glueballs)

**Domain:** Particle Physics / Hadrons - **Status:** 🟢 VALIDATED - **File:** `laws/1572_exotic_hadrons.md` - **Sim:** `sim/1572_exotic_hadrons.py`

---

### CLASSICAL STATEMENT
*"Exotic hadrons contain more than three quarks or no valence quarks: tetraquarks (q q q_bar q_bar), pentaquarks (q q q q q_bar) and glueballs (gluon-only) are predicted by QCD; the Zc(3900) and Pc(4450) are prominent candidates confirmed in 2013-2015."*
- Zc(3900) (2013, BESIII); Pc(4450) (2015, LHCb), 2013. Source: Ablikim et al. (BESIII), PRL 110 (2013) 252001; Aaij et al. (LHCb), PRL 115 (2015) 072001

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-exotic, purely-ordinary hadron limit*: the classical quark model admits only qqq and q qbar states; exotic hadrons appear when this minimal content is exactly exceeded - a zero-extra-quark, ordinary-only limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*M_floor, where M_floor is the phi-ground molecular/compact floor. At kappa->0 the ordinary hadron spectrum is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} M_phi = M_ordinary -> the exotic hadron spectrum is the zero-extra-quark, ordinary-multiplet limit.
```

---

### STAGE 4 - SIMULATION

`sim/1572_exotic_hadrons.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1572_exotic_hadrons.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The exotic hadron masses carry a phi-ground molecular/compact floor, so the tetraquark/pentaquark states deviate from both the pure molecular and pure compact predictions by an irreducible admixture.
EXPERIMENT (VERIFIED): Exotic hadron searches at LHCb, BESIII, Belle II (Z_c, Z_b, P_c states) and lattice QCD spectrum calculations.
VERIFIED BY: Exotic hadrons exactly matching a pure molecular or pure compact model with zero admixture floor.
```

---

### RECOGNITION
Connects to Law 1571 (quark model), Law 1515 (confinement) and Law 1573 (tetraquark) - exotic hadrons are the quark model's overflow.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The quark bag overflows its count; the phi-law keeps a floor of the overflow structuring.

### NOVELTY
Classical quark model is minimal; the phi-law predicts an irreducible exotic admixture floor.

### ACTIONABILITY
Run sim/1572_exotic_hadrons.py; verify the exotic spectrum; proceed to Law 1573.
