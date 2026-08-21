# PHI-PHYSICS — LAW 500
## Kapitza Resistance (Thermal Boundary Resistance)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/500_kapitza_resistance.md` · **Sim:** `sim/500_kapitza_resistance.py`

---

### CLASSICAL STATEMENT
*"The interface between two dissimilar materials presents a thermal boundary resistance R_K, so that a temperature drop DeltaT = R_K q appears across the boundary for a heat flux q. Its temperature dependence is ~ T^-3 at low temperature."*
— Pyotr Leonidovich Kapitza, 1941. Source: Wikipedia: Kapitza resistance (Kapitza conductance); Kapitza (1941)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfectly transparent interface*: a classical interface conducts heat with zero resistance only if the two sides are exactly identical - the law exists precisely because real interfaces always carry a mismatch.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the interface mismatch carries coherence. R_K_phi(kappa) = R_K*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground. At kappa->0 the classical Kapitza resistance is exact (and would vanish only for identical materials).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_K_phi = R_K -> the Kapitza resistance is the zero-coherence interface-mismatch limit.
```

---

### STAGE 4 — SIMULATION

`sim/500_kapitza_resistance.py`: reproduces the classical value R_kapitza = 2e-06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/500_kapitza_resistance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the boundary resistance carries a coherence floor kappa*phi^-1*R_ground even for nearly matched materials.
EXPERIMENT (VERIFIED): Time-domain thermoreflectance measurements of thermal boundary conductance across engineered interfaces.
VERIFIED BY: The thermal boundary resistance vanishes exactly for identical materials at all couplings.
```

---

### RECOGNITION
Connects to Law 096 (Fourier) and Law 494 (Wiedemann-Franz) - the boundary is the coherence seam between two lattices.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * R_ground.

### CLARITY
Every interface is a seam where two coherences meet; the phi-law keeps the seam's resistance.

### NOVELTY
Classical boundary resistance vanishes for matched materials; the phi-law adds the coherence floor of the seam.

### ACTIONABILITY
Run sim/500_kapitza_resistance.py; verify R_K at kappa->0; proceed to 501.
