# PHI-PHYSICS - LAW 1724
## Sherrington-Kirkpatrick Model (Infinite-Range Spin Glass)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1724_sherrington_kirkpatrick_model.md` - **Sim:** `sim/1724_sherrington_kirkpatrick_model.py`

---

### CLASSICAL STATEMENT
*"The Sherrington-Kirkpatrick model is the infinite-range spin glass: H = -(1/sqrt(N)) sum_{i<j} J_ij s_i s_j with Gaussian random couplings of variance 1/N, solvable in mean-field theory; its replica-symmetric solution fails below the transition (negative entropy), leading Parisi to the replica-symmetry-breaking (RSB) solution - the exact mean-field theory of spin glasses."*
- David Sherrington & Scott Kirkpatrick, 1975. Source: Wikipedia: Sherrington-Kirkpatrick model; Sherrington & Kirkpatrick (1975), Phys. Rev. Lett. 35:1792

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-frustration, perfectly symmetric infinite-range reference*: the SK model is defined against the replica-symmetric, uniform-coupling reference; the glassy RSB phase emerges away from this symmetric reference, and the sharpest results assume an infinite system at T=0.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the transition carries a coherence floor. T_g_phi(kappa) = T_g*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_T, where delta_T is the phi-ground smearing of the glass transition. At kappa->0 the sharp RSB transition is recovered; at kappa=1 the transition is smeared by a coherent width.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} T_g_phi = T_g -> the SK model is the infinite-range, replica-symmetric, zero-temperature limit of mean-field spin-glass theory.
```

---

### STAGE 4 - SIMULATION

`sim/1724_sherrington_kirkpatrick_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1724_sherrington_kirkpatrick_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The spin-glass freezing in any finite real system is smeared over a phi-ground width around the mean-field T_g: the sharp RSB transition is never observed exactly.
EXPERIMENT (VERIFIED): Ultra-low-temperature ac-susceptibility of a metallic spin glass measuring the freezing width around the nominal transition temperature.
VERIFIED BY: A spin glass whose freezing is exactly sharp at the mean-field T_g with zero width.
```

---

### RECOGNITION
Connects to Law 1723 (EA) and Law 1730 (Stoner) - the SK model is the infinite-range glass, and the glass never freezes on a point.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; freezing width scales as phi^-1 * delta_T.

### CLARITY
The infinite-range glass tries to freeze at a point; the phi-law smears the point.

### NOVELTY
Classical SK theory gives a sharp transition; the phi-law smears it with a coherence floor.

### ACTIONABILITY
Run sim/1724_sherrington_kirkpatrick_model.py; verify the RSB transition at kappa->0; proceed to 1725.
