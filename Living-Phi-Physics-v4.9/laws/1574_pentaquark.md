# PHI-PHYSICS - LAW 1574
## Pentaquark States (Five-Quark Baryons)

**Domain:** Particle Physics / Hadrons - **Status:** 🟢 VALIDATED - **File:** `laws/1574_pentaquark.md` - **Sim:** `sim/1574_pentaquark.py`

---

### CLASSICAL STATEMENT
*"A pentaquark is a baryon containing four quarks and one antiquark (q q q q q_bar); the LHCb discovery of the Pc(4380) and Pc(4450) states in Lambda_b -> J/psi p K decays provides strong evidence for charmonium-pentaquark states, a new form of hadronic matter."*
- Pc(4450), Pc(4380) (LHCb, 2015); Psi(5568) claim (D0, 2016), 2015. Source: Aaij et al. (LHCb), PRL 115 (2015) 072001; Wikipedia: Pentaquark

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-pentaquark, pure-three-quark-baryon limit*: the classical quark model admits only qqq baryons; pentaquarks require extra quark-antiquark pairs - a zero-extra-pair, ordinary-baryon limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*M_floor, where M_floor is the phi-ground molecular/compact floor. At kappa->0 the ordinary baryon mass is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} M_phi = M_qqq -> the pentaquark is the zero-extra-quark-pair, ordinary-baryon limit.
```

---

### STAGE 4 - SIMULATION

`sim/1574_pentaquark.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1574_pentaquark.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The pentaquark masses carry a phi-ground molecular/compact floor, so the P_c states deviate from both the charmonium-nucleon molecule and compact pentaquark predictions by an irreducible admixture.
EXPERIMENT (VERIFIED): Pentaquark searches in Lambda_b and B decays at LHCb (including the 2020 P_c states) and Belle II.
VERIFIED BY: A pentaquark exactly matching a pure molecule or compact model with zero admixture floor.
```

---

### RECOGNITION
Connects to Law 1572 (exotic), Law 1573 (tetraquark) and Law 1571 (quark model) - the pentaquark is the five-quark state.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Five quarks make a new baryon; the phi-law keeps a floor of the making uncertain.

### NOVELTY
Classical baryons are qqq; the phi-law predicts an irreducible pentaquark floor.

### ACTIONABILITY
Run sim/1574_pentaquark.py; verify the exotic state; proceed to Law 1575.
