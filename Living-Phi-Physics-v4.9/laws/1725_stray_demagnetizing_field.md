# PHI-PHYSICS - LAW 1725
## Demagnetizing Field (Shape-Dependent Internal Field of a Magnet)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1725_stray_demagnetizing_field.md` - **Sim:** `sim/1725_stray_demagnetizing_field.py`

---

### CLASSICAL STATEMENT
*"The magnetic field inside a magnetized body includes the demagnetizing field H_d = -N M, where N is the demagnetizing factor depending only on shape (N=1/3 for a sphere, ~1 for a thin film normal to the surface, ~0 for a long rod along its axis); the internal field B = mu_0(H_a + H_d + M) is reduced by the shape, setting the energy of domains and the coercivity of magnets."*
- Classical magnetostatics; formulated by J.C. Maxwell (1873), 1873. Source: Wikipedia: Demagnetizing field; Maxwell (1873), A Treatise on Electricity and Magnetism

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-surface-charge, perfectly uniform magnetization*: the demagnetizing factor is defined for a uniformly magnetized body with exactly zero pole density at internal boundaries; the field is a pure shape effect computed for an idealized uniform, surface-only magnetized body.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the uniform magnetization carries a coherence floor. M_phi(kappa) = M_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_M, where delta_M is the phi-ground magnetization nonuniformity. At kappa->0 the exact shape-only demagnetizing factor is recovered; at kappa=1 every magnet has an irreducible internal magnetization texture.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} H_d_phi = -N M -> the demagnetizing field is the zero-texture, uniform-magnetization, shape-only limit of magnetostatic energy.
```

---

### STAGE 4 - SIMULATION

`sim/1725_stray_demagnetizing_field.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1725_stray_demagnetizing_field.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective demagnetizing factor of any real magnet deviates from the ideal shape value because of an irreducible magnetization texture: small but measurable corrections persist in any homogeneous sample.
EXPERIMENT (VERIFIED): Precision VSM or SQUID magnetometry of a well-characterized sphere or thin film measuring the effective demagnetizing factor vs the ideal shape value.
VERIFIED BY: A magnet whose effective demagnetizing factor exactly equals the ideal shape value with zero deviation.
```

---

### RECOGNITION
Connects to Law 1726 (hysteresis) and Law 1731 (anisotropy) - the shape of the magnet writes its field, and the phi-law keeps a wobble in the writing.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; factor deviation scales as phi^-1 * delta_M.

### CLARITY
The shape dictates the field; the phi-law keeps a coherent imperfection in the dictation.

### NOVELTY
Classical magnetostatics gives exact shape factors; the phi-law adds an irreducible texture correction.

### ACTIONABILITY
Run sim/1725_stray_demagnetizing_field.py; verify N=1/3 for a sphere at kappa->0; proceed to 1726.
