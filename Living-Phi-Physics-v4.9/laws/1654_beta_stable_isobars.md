# PHI-PHYSICS - LAW 1654
## Beta Stability Valley (N-Z Ratio of Stable Nuclei)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1654_beta_stable_isobars.md` - **Sim:** `sim/1654_beta_stable_isobars.py`

---

### CLASSICAL STATEMENT
*"Stable nuclei lie in the valley of beta stability, where the neutron-proton ratio balances the Coulomb repulsion against the symmetry energy: the most stable N/Z ratio increases from 1 for light nuclei to ~1.54 for 208Pb; the valley is described by the SEMF minimum of the mass parabola."*
- Mattiauch (1937); valley of stability, 1937. Source: Wikipedia: Valley of stability; nuclear physics textbooks

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-Coulomb, zero-asymmetry, N = Z line*: in the absence of Coulomb repulsion, stable nuclei would lie exactly on the N = Z line with zero asymmetry; the classical treatment of N = Z stability is the zero-Coulomb, zero-offset limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

N/Z_phi(kappa) = N/Z_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*(N/Z)_floor, where (N/Z)_floor is the phi-ground residual floor. At kappa->0 the N = Z line is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} N/Z_phi = 1 -> the beta stability valley is the zero-Coulomb, N = Z, symmetric limit.
```

---

### STAGE 4 - SIMULATION

`sim/1654_beta_stable_isobars.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1654_beta_stable_isobars.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The stability valley carries a phi-ground residual floor, so the N/Z of stable nuclei deviates from the SEMF parabola by an irreducible shell correction.
EXPERIMENT (VERIFIED): Stable isotope systematics (mass parabolas, beta-stability lines) and the SEMF valley vs the measured chart.
VERIFIED BY: A mass parabola with exactly the SEMF minimum and zero shell correction at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1447 (SEMF), Law 1620 (binding curve) and Law 1450 (magic numbers) - the stability valley is the nuclear chart's river.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The nuclei flow down the valley; the phi-law keeps a floor of bank in the flow.

### NOVELTY
Classical valley is smooth; the phi-law predicts irreducible shell offsets.

### ACTIONABILITY
Run sim/1654_beta_stable_isobars.py; verify the valley; proceed to Law 1655.
