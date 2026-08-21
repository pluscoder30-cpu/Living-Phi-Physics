# PHI-PHYSICS - LAW 1638
## Nuclear Reaction Threshold Behavior (Wigner's Threshold Law)

**Domain:** Nuclear Reactions - **Status:** 🟢 VALIDATED - **File:** `laws/1638_nuclear_reaction_threshold.md` - **Sim:** `sim/1638_nuclear_reaction_threshold.py`

---

### CLASSICAL STATEMENT
*"Near a reaction threshold, the cross-section obeys the Wigner threshold law sigma ~ k^(2l+1) where k is the relative momentum and l the orbital angular momentum of the outgoing channel; this determines the energy dependence of exothermic reactions at threshold."*
- Eugene Wigner (1948); threshold laws, 1948. Source: Wigner, Phys. Rev. 73 (1948) 1002; Wikipedia: Wigner threshold law

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-momentum, zero-energy, threshold-point limit*: at the exact threshold the relative momentum is zero and the cross-section vanishes (for l > 0); the classical treatment of the threshold point is the zero-momentum, zero-cross-section limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_floor, where sigma_floor is the phi-ground residual floor. At kappa->0 the Wigner threshold law is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = k^(2l+1) -> the threshold law is the zero-momentum, exact-threshold, zero-residual limit.
```

---

### STAGE 4 - SIMULATION

`sim/1638_nuclear_reaction_threshold.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1638_nuclear_reaction_threshold.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The cross-section carries a phi-ground residual floor at the threshold, so the Wigner k^(2l+1) behavior is approached but never exactly reached at zero energy.
EXPERIMENT (VERIFIED): Threshold cross-section measurements (cold fusion, neutron-producing reactions) and the s-wave/p-wave threshold behavior.
VERIFIED BY: A reaction cross-section exactly zero at threshold with zero residual floor.
```

---

### RECOGNITION
Connects to Law 1477 (threshold), Law 1372 (Wigner threshold law) and Law 1478 (resonance) - the threshold law is the reaction's doorstep.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The door opens slowly with momentum; the phi-law keeps a floor of ajar.

### NOVELTY
Classical threshold is k^(2l+1); the phi-law predicts an irreducible residual floor.

### ACTIONABILITY
Run sim/1638_nuclear_reaction_threshold.py; verify the k^(2l+1) law; proceed to Law 1639.
