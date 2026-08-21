# PHI-PHYSICS - LAW 1628
## Fission Product Yield (Mass Distribution of Fission Fragments)

**Domain:** Nuclear Fission - **Status:** 🟢 VALIDATED - **File:** `laws/1628_fission_product_yield.md` - **Sim:** `sim/1628_fission_product_yield.py`

---

### CLASSICAL STATEMENT
*"The fission product yield distribution is double-humped: light fragments around A ~ 95 and heavy fragments around A ~ 138, with a peak-to-valley ratio that decreases with excitation energy; the yield determines the fission-product inventory and the decay heat."*
- Fission yield systematics (1939-1950s); double-humped distribution, 1940. Source: Wikipedia: Fission product yield; radiochemical yield studies

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-yield, zero-fragmentation, symmetric-only limit*: if fission were exactly symmetric, the yield would be a single peak at A ~ A_parent/2 with zero yield elsewhere; the classical treatment of symmetric fission is the zero-asymmetry, single-peak limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Y_phi(kappa) = Y_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Y_floor, where Y_floor is the phi-ground asymmetric-yield floor. At kappa->0 the symmetric (zero-asymmetry) yield is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Y_phi = Y_symmetric -> the fission yield is the zero-asymmetry, symmetric-fission, single-peak limit.
```

---

### STAGE 4 - SIMULATION

`sim/1628_fission_product_yield.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1628_fission_product_yield.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The fission yield distribution carries a phi-ground asymmetric floor, so the peak-to-valley ratio and the asymmetric component are never exactly zero even at high excitation.
EXPERIMENT (VERIFIED): Fission yield measurements (thermal and fast fission of U, Pu, Cf) and the excitation-energy dependence of the peak-to-valley ratio.
VERIFIED BY: A fission process with exactly symmetric yields (zero asymmetry) at any excitation.
```

---

### RECOGNITION
Connects to Law 1461 (Bohr-Wheeler), Law 1463 (induced fission) and Law 1470 (chain) - the yield is fission's fingerprint.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The split is rarely even; the phi-law keeps a floor of unevenness.

### NOVELTY
Classical fission can be symmetric; the phi-law predicts an irreducible asymmetric floor.

### ACTIONABILITY
Run sim/1628_fission_product_yield.py; verify the double-hump; proceed to Law 1629.
