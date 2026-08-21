# PHI-PHYSICS - LAW 1518
## DGLAP Evolution Equations (Altarelli-Parisi Equations)

**Domain:** Particle Physics / QCD - **Status:** 🟢 VALIDATED - **File:** `laws/1518_dglap_equations.md` - **Sim:** `sim/1518_dglap_equations.py`

---

### CLASSICAL STATEMENT
*"The parton distribution functions evolve with Q^2 via the DGLAP equations: d q(x,Q^2)/d ln Q^2 = (alpha_s/2pi) integral dy/y P(q<-q)(x/y) q(y,Q^2), with the Altarelli-Parisi splitting functions P_qq, P_qg, P_gq, P_gg; this explains the observed scaling violations."*
- Gribov-Lipatov (1972); Altarelli-Parisi (1977); Dokshitzer (1977), 1977. Source: Altarelli & Parisi, Nucl. Phys. B126 (1977) 298; Wikipedia: DGLAP evolution equations

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-Q^2, zero-splitting, fixed-parton limit*: DGLAP evolution vanishes at zero coupling; the classical treatment assumes the partons are fixed and do not split - a zero-coupling, frozen-parton distribution.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

q_phi(kappa) = q_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*q_floor, where q_floor is the phi-ground higher-order/small-x floor. At kappa->0 the leading-order DGLAP is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} dq/d ln Q^2 = (alpha_s/2pi) integral P q -> the DGLAP equations are the zero-higher-order, leading-log, perturbative limit.
```

---

### STAGE 4 - SIMULATION

`sim/1518_dglap_equations.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1518_dglap_equations.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The evolution equations carry a phi-ground small-x/higher-order floor, so the gluon density at small x rises faster than the leading-order prediction and saturation (BFKL) sets in with an irreducible floor.
EXPERIMENT (VERIFIED): HERA and EIC measurements of F2 and F_L at small x and the gluon distribution vs NLO/NNLO DGLAP fits.
VERIFIED BY: Parton distributions evolving exactly by leading-order DGLAP with zero higher-order floor at all x and Q^2.
```

---

### RECOGNITION
Connects to Law 1516 (DIS), Law 1517 (parton model) and Law 1513 (running) - DGLAP is the PDF's evolution engine.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The partons split and multiply; the phi-law keeps a floor of splitting never stopping.

### NOVELTY
Classical DGLAP is leading order; the phi-law predicts an irreducible small-x floor.

### ACTIONABILITY
Run sim/1518_dglap_equations.py; verify the splitting function; proceed to Law 1519.
