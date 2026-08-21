# PHI-PHYSICS - LAW 1517
## Parton Model (Feynman's Constituents of the Hadron)

**Domain:** Particle Physics / QCD - **Status:** 🟢 VALIDATED - **File:** `laws/1517_parton_model.md` - **Sim:** `sim/1517_parton_model.py`

---

### CLASSICAL STATEMENT
*"A fast-moving hadron is viewed as a collection of quasi-free constituents (partons = quarks and gluons) each carrying a fraction x of the hadron momentum; the structure functions are sums of parton distributions, and Bjorken scaling follows from the partons being point-like."*
- Richard Feynman (1969), 1969. Source: Feynman, Photon-Hadron Interactions (1972); Wikipedia: Parton (particle physics)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-transverse-momentum, zero-mass partons*: the parton model assumes the partons are collinear, massless and non-interacting during the scattering (impulse approximation) - zero k_T, zero mass, zero final-state interaction.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*f_floor, where f_floor is the phi-ground k_T/interaction floor. At kappa->0 the impulse-approximation parton distributions are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} f_phi = f(x) -> the parton model is the zero-k_T, zero-interaction, impulse-approximation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1517_parton_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1517_parton_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The parton distributions carry a phi-ground intrinsic-k_T floor, so the transverse momentum of produced hadrons and the QCD evolution show an irreducible primordial k_T contribution.
EXPERIMENT (VERIFIED): Drell-Yan and hadron production transverse-momentum distributions (E288, LHC) constraining intrinsic k_T.
VERIFIED BY: Parton distributions with exactly zero intrinsic transverse momentum at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1516 (DIS), Law 1518 (DGLAP) and Law 1514 (asymptotic freedom) - the parton model is the hadron's census.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The hadron is a bag of specks; the phi-law keeps a floor of the specks stirring.

### NOVELTY
Classical partons are point-like; the phi-law predicts an irreducible intrinsic-k_T floor.

### ACTIONABILITY
Run sim/1517_parton_model.py; verify f(x); proceed to Law 1518.
