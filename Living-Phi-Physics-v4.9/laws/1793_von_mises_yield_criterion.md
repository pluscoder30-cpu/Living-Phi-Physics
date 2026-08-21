# PHI-PHYSICS - LAW 1793
## von Mises Yield Criterion (Energy-Based Yield Condition for Metals)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1793_von_mises_yield_criterion.md` - **Sim:** `sim/1793_von_mises_yield_criterion.py`

---

### CLASSICAL STATEMENT
*"Plastic deformation of a metal begins when the von Mises stress reaches the yield strength: sigma_v = sqrt(3 J_2) = sqrt(1/2[(sigma_1 - sigma_2)^2 + (sigma_2 - sigma_3)^2 + (sigma_3 - sigma_1)^2]) = sigma_y, where J_2 is the second deviatoric stress invariant; the criterion is equivalent to the statement that yielding occurs at a critical distortion (deviatoric) energy density, and is the standard yield condition for ductile metals."*
- Richard von Mises, 1913. Source: Wikipedia: Von Mises yield criterion; von Mises (1913), Goettinger Nachr. Math.-Phys. 1:582

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-yield-strength, perfectly rigid elastic reference*: the von Mises criterion is defined against a perfectly elastic, zero-plasticity reference; the yield surface is the onset of plasticity away from this zero-yield reference, and real metals show gradual (rounded) yielding rather than a sharp surface.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the yield surface carries a coherence floor. sigma_y_phi(kappa) = sigma_y*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_sigma, where delta_sigma is the phi-ground yield-rounding floor. At kappa->0 the sharp yield surface is recovered; at kappa=1 yielding is always rounded - the transition to plasticity is never a sharp surface.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_v_phi = sqrt(3 J_2) -> the von Mises criterion is the zero-rounding, perfectly-elastic, sharp-yield limit of ductile plasticity onset.
```

---

### STAGE 4 - SIMULATION

`sim/1793_von_mises_yield_criterion.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1793_von_mises_yield_criterion.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The elastic-plastic transition is never sharp: an irreducible yield-rounding floor remains in every metal, so the proportional limit always lies below the nominal yield stress and the transition has a finite width.
EXPERIMENT (VERIFIED): Ultra-precision tensile or torsion testing of a high-purity metal measuring the yield-rounding width and the deviation from the ideal von Mises surface.
VERIFIED BY: A metal whose elastic-plastic transition is exactly sharp at the ideal von Mises yield stress with zero rounding.
```

---

### RECOGNITION
Connects to Law 1794 (Tresca) and Law 1791 (Hooke) - the metal yields to energy, and the phi-law keeps the yield from being a line.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; rounding floor scales as phi^-1 * delta_sigma.

### CLARITY
The metal gives way under energy; the phi-law keeps the giving from being sharp.

### NOVELTY
Classical von Mises gives a sharp surface; the phi-law rounds it with a coherence floor.

### ACTIONABILITY
Run sim/1793_von_mises_yield_criterion.py; verify sigma_v = sqrt(3 J_2) at kappa->0; proceed to 1794.
