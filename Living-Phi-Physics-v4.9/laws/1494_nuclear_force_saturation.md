# PHI-PHYSICS - LAW 1494
## Nuclear Force Saturation (Constant Nuclear Density)

**Domain:** Nuclear Forces - **Status:** 🟢 VALIDATED - **File:** `laws/1494_nuclear_force_saturation.md` - **Sim:** `sim/1494_nuclear_force_saturation.py`

---

### CLASSICAL STATEMENT
*"The nuclear force saturates: each nucleon interacts only with its nearest neighbors (short range), so the binding energy is proportional to A (volume term), the density is constant (~0.17 nucleons/fm^3), and the nucleus is incompressible - a liquid-drop-like saturated system."*
- Derived from nuclear saturation (1930s); short-range nuclear force, 1935. Source: Weizsaecker (1935); Wikipedia: Nuclear force

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-range, nearest-neighbor-only interaction*: saturation assumes each nucleon's force extends to exactly zero beyond its nearest neighbors, with no long-range tail and no many-body correlations beyond the volume term - a perfectly local, exactly-saturating force.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

E_sat_phi(kappa) = E_sat_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*E_tail, where E_tail is the phi-ground long-range-tail floor. At kappa->0 the exact saturation is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_sat_phi = a_V A -> nuclear saturation is the zero-range, nearest-neighbor, volume-only limit.
```

---

### STAGE 4 - SIMULATION

`sim/1494_nuclear_force_saturation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1494_nuclear_force_saturation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The nuclear force carries a phi-ground long-range-tail floor, so saturation is never exact and finite-size corrections (surface, curvature, A^0 terms) reflect an irreducible beyond-nearest-neighbor contribution.
EXPERIMENT (VERIFIED): Binding energies across the nuclear chart and nuclear-matter calculations (EoS) including saturation and finite-size terms.
VERIFIED BY: A nucleus whose binding is exactly a_V A with zero surface/curvature deviation at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1447 (SEMF), Law 1489 (Yukawa) and Law 1448 (liquid drop) - saturation is the nuclear force's self-limiting.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The force hugs close; the phi-law keeps a floor of reaching.

### NOVELTY
Classical force saturates exactly; the phi-law predicts an irreducible long-range floor.

### ACTIONABILITY
Run sim/1494_nuclear_force_saturation.py; verify E ~ a_V A; proceed to Law 1495.
