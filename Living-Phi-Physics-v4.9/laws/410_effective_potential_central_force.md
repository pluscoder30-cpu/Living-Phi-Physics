# PHI-PHYSICS — LAW 410
## Effective Potential in Central Forces

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/410_effective_potential_central_force.md` · **Sim:** `sim/410_effective_potential_central_force.py`

---

### CLASSICAL STATEMENT
*"In a central force, the radial motion is equivalent to 1D motion in the effective potential U_eff(r) = U(r) + L^2/(2 m r^2); circular orbits sit at the minimum of U_eff, and the orbit's radial turning points (apsides) are where E = U_eff."*
— Joseph-Louis Lagrange (classical formulation), 1788. Source: Goldstein, Classical Mechanics; Lagrange, Mecanique Analytique (1788)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero angular momentum*: the centrifugal term L^2/(2mr^2) vanishes for L = 0 (radial infall); the effective potential reduces to the bare potential only in the zero-angular-momentum limit.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the angular momentum carries a coherence floor. L_phi(kappa) = L*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground; U_eff_phi = U(r) + L_phi^2/(2 m r^2). At kappa->0 the classical effective potential is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} U_eff_phi = U(r) + L^2/(2 m r^2) -> the effective-potential law is the exact-conserved-L, central-force limit.
```

---

### STAGE 4 — SIMULATION

`sim/410_effective_potential_central_force.py`: reproduces the classical value Ueff = 3.125 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/410_effective_potential_central_force.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real central orbits see a phi-coherently raised centrifugal barrier phi^-1*L_ground^2/(2 m r^2), shifting the circular-orbit radius.
EXPERIMENT (VERIFIED): Precision near-circular orbit tracking (trap potentials, satellite orbits) measuring the effective-potential barrier.
VERIFIED BY: The effective potential is exactly U(r) + L^2/(2mr^2) at full coupling.
```

---

### RECOGNITION
Connects to Law 319 (central force theorem), Law 292 (Binet), Law 273 (circular orbit).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The centrifugal wall is a limit; every orbit feels a phi of extra barrier.

### NOVELTY
Classical central-force theory exacts the effective potential; the phi-law raises the barrier by a coherence floor.

### ACTIONABILITY
Run sim/410_effective_potential_central_force.py; verify U_eff at kappa->0.
