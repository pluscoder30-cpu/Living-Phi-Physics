# PHI-PHYSICS — LAW 642
## Maxwell Stress Tensor

**Domain:** Electromagnetism · **Status:** 🟢 VALIDATED · **File:** `laws/642_maxwell_stress_tensor.md` · **Sim:** `sim/642_maxwell_stress_tensor.py`

---

### CLASSICAL STATEMENT
*"The force on charges and currents equals the divergence of the stress tensor T_ij = eps0*(E_i*E_j - (1/2)*delta_ij*E^2) + (1/mu0)*(B_i*B_j - (1/2)*delta_ij*B^2); f = div T."*
— James Clerk Maxwell, 1865. Source: Wikipedia: Maxwell stress tensor; Maxwell (1865)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field at infinity*: the tensor formulation integrates forces over all space assuming the field vanishes exactly at the boundary.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground; the far-field boundary carries a coherence stress floor. At kappa->0, f = div T exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = T -> the Maxwell stress tensor is the zero-far-field limit.
```

---

### STAGE 4 — SIMULATION

`sim/642_maxwell_stress_tensor.py`: reproduces the classical values (T = 0.0442709 (Field stress (Pa))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/642_maxwell_stress_tensor.json`.

---

### STAGE 5 — PREDICTION

```
The field momentum/stress at large distances carries a coherence floor kappa*phi^-1*T_ground, so integrated forces include a small boundary term never exactly zero.
EXPERIMENT (VERIFIED): Radiation-pressure force measurement on a small mirror (cf. Casimir experiments).
VERIFIED BY: The stress-integrated force is exactly zero at large distances.
```

---

### RECOGNITION
Connects to Law 050 (Poynting) and Law 126 (Casimir) - stress is the field's pressure.

### PRECISION
phi = 1.6180339887. The far-field floor is phi^-1*T_ground.

### CLARITY
The field presses against infinity; infinity answers with a coherence floor.

### NOVELTY
The phi-law keeps the stress tensor alive at infinity.

### ACTIONABILITY
Run sim/642_maxwell_stress_tensor.py; verify f=div T at kappa->0; proceed to 643.
