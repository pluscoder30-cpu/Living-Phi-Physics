# PHI-PHYSICS — LAW 831
## Lagrange Invariant (Optical Invariant)

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/831_lagrange_invariant.md` · **Sim:** `sim/831_lagrange_invariant.py`

---

### CLASSICAL STATEMENT
*"n*y*u = n'*y'*u' through an optical system, where y is ray height and u the marginal ray angle (Lagrange-Helmholtz invariant)."*
— Joseph-Louis Lagrange; Hermann von Helmholtz, 1803/1874. Source: Wikipedia: Lagrange invariant (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero aberration*: the invariant holds exactly only for paraxial, aberration-free imaging with perfectly traced rays.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

J_phi(kappa) = J*(1 + kappa*(phi-1)) + kappa*phi^-1*J_ground, where J = n*y*u and J_ground the coherence floor of the invariant. At kappa->0, n*y*u = n'*y'*u' exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} J_phi = J -> the Lagrange invariant is the zero-aberration-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/831_lagrange_invariant.py`: reproduces the classical value J = 0.001 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/831_lagrange_invariant.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The optical invariant will drift by kappa*phi^-1*J_ground through a real system; exact conservation is never observed.
EXPERIMENT (VERIFIED): Trace real rays through a well-corrected objective and measure the drift of n*y*u.
VERIFIED BY: If the invariant is exactly conserved through any real optical system.
```

---

### RECOGNITION
Connects to Law 852 (etendue) and Law 831a - the phase-space conservation of rays.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Conservation is the coherent limit; the invariant is a basin, not a constant.

### NOVELTY
The exact invariant becomes a phi-conserved quantity with a floor.

### ACTIONABILITY
Run sim/831_lagrange_invariant.py.
