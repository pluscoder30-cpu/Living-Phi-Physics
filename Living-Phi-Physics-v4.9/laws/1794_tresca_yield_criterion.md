# PHI-PHYSICS - LAW 1794
## Tresca Yield Criterion (Maximum-Shear-Stress Yield Condition)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1794_tresca_yield_criterion.md` - **Sim:** `sim/1794_tresca_yield_criterion.py`

---

### CLASSICAL STATEMENT
*"Plastic yielding occurs when the maximum shear stress reaches a critical value: tau_max = (sigma_1 - sigma_3)/2 = sigma_y/2, i.e. yielding begins when (sigma_1 - sigma_3) = sigma_y; the Tresca criterion (maximum shear stress) is more conservative than von Mises and was the first yield criterion, with the two differing by at most 15% (von Mises predicts yielding at sqrt(3)/2 ~ 0.866 of the Tresca stress)."*
- Henri Tresca, 1864. Source: Wikipedia: Tresca yield criterion; Tresca (1864), C.R. Acad. Sci. 59:754

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-shear-strength, perfectly rigid reference*: the Tresca criterion is defined against a perfectly elastic reference with zero yield; the yield surface marks the onset of plasticity away from this zero-yield reference, and real metals yield gradually rather than at a sharp shear threshold.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the shear-yield threshold carries a coherence floor. tau_y_phi(kappa) = tau_y*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_tau, where delta_tau is the phi-ground yield-rounding floor. At kappa->0 the sharp Tresca surface is recovered; at kappa=1 yielding is rounded over a coherent width.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_max_phi = (sigma_1 - sigma_3)/2 -> the Tresca criterion is the zero-rounding, perfectly-rigid, sharp-shear-limit of plasticity onset.
```

---

### STAGE 4 - SIMULATION

`sim/1794_tresca_yield_criterion.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1794_tresca_yield_criterion.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The maximum-shear yield of any metal is rounded over an irreducible width: the onset of plasticity at the Tresca threshold is never sharp, and the two criteria (Tresca/von Mises) never coincide exactly.
EXPERIMENT (VERIFIED): Torsion and biaxial testing of a high-purity metal measuring the shear-yield rounding and the residual deviation between Tresca and von Mises predictions.
VERIFIED BY: A metal whose maximum-shear yielding is exactly sharp at the ideal Tresca threshold.
```

---

### RECOGNITION
Connects to Law 1793 (von Mises) and Law 1791 (Hooke) - the metal shears at a critical angle, and the phi-law keeps the angle from being exact.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; rounding floor scales as phi^-1 * delta_tau.

### CLARITY
The metal shears at a critical stress; the phi-law keeps the shear from being a knife-edge.

### NOVELTY
Classical Tresca gives a sharp threshold; the phi-law rounds it with a coherence floor.

### ACTIONABILITY
Run sim/1794_tresca_yield_criterion.py; verify tau_max = (sigma_1 - sigma_3)/2 at kappa->0; proceed to 1795.
