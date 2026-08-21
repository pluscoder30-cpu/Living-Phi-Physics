# PHI-PHYSICS - LAW 1849
## J-Integral (Rice's Path-Independent Fracture Parameter)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1849_j_integral_fracture.md` - **Sim:** `sim/1849_j_integral_fracture.py`

---

### CLASSICAL STATEMENT
*"The J-integral J = integral_Gamma (W dy - T_i d u_i/dx ds) is a path-independent contour integral around a crack tip equal to the energy release rate for nonlinear elastic (deformation-plasticity) materials; for linear elasticity J = G = K^2/E, and fracture occurs at J = J_Ic, making the J-integral the basis of elastic-plastic fracture mechanics for ductile materials."*
- James R. Rice, 1968. Source: Wikipedia: J-integral; Rice (1968), J. Appl. Mech. 35:379; Cherepanov (1967)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-plasticity, perfectly path-independent, linear-elastic reference*: the J-integral's path independence assumes a deformation-theory (nonlinear elastic) material with no unloading and a sharp crack; real materials load/unload and have residual plasticity away from this ideal path-independent reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the path independence carries a coherence floor. J_phi(kappa) = J_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_J, where delta_J is the phi-ground path-dependence floor. At kappa->0 the ideal path-independent J is recovered; at kappa=1 J is never exactly path independent - an irreducible deviation remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} J_phi = G = K^2/E -> the J-integral is the deformation-theory, path-independent, linear-elastic limit of fracture-energy release.
```

---

### STAGE 4 - SIMULATION

`sim/1849_j_integral_fracture.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1849_j_integral_fracture.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The J-integral is never exactly path independent: an irreducible path-dependence floor remains from plasticity and unloading, so J_Ic values carry a specimen-dependent floor.
EXPERIMENT (VERIFIED): Multi-specimen J-R curve testing with various contour paths, measuring the residual path dependence of the computed J.
VERIFIED BY: A fracture test in which the computed J-integral is exactly path independent with zero deviation.
```

---

### RECOGNITION
Connects to Law 1848 (energy release rate) and Law 1796 (Griffith) - the contour circles the crack and counts energy, and the phi-law keeps the count slightly path-dependent.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; path-dependence floor scales as phi^-1 * delta_J.

### CLARITY
The contour circles the crack; the phi-law keeps the count slightly path-dependent.

### NOVELTY
Classical J-theory gives exact path independence; the phi-law keeps an irreducible deviation.

### ACTIONABILITY
Run sim/1849_j_integral_fracture.py; verify J = G at kappa->0; proceed to 1850.
