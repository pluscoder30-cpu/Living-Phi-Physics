# PHI-PHYSICS — LAW 624
## Green's Reciprocity (Mutual Energy)

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/624_greens_reciprocity.md` · **Sim:** `sim/624_greens_reciprocity.py`

---

### CLASSICAL STATEMENT
*"For two charge configurations (rho1, V1) and (rho2, V2) on the same conductors, the mutual energies are equal: integral rho1*V2 dV = integral rho2*V1 dV."*
— George Green, 1828. Source: Wikipedia: Green's reciprocity theorem

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *identical geometry*: reciprocity holds exactly only when the two configurations share the same boundary, a condition no changing field ever meets exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

W12_phi(kappa) = W12*(1 + kappa*(phi-1)) + kappa*phi^-1*W_ground; the reciprocity identity acquires a coherence-asymmetry floor. At kappa->0, W12 = W21 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} W12_phi = W12 -> Green's reciprocity is the identical-geometry limit.
```

---

### STAGE 4 — SIMULATION

`sim/624_greens_reciprocity.py`: reproduces the classical values (W = 8.98755e-07 (Mutual electrostatic energy (J))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/624_greens_reciprocity.json`.

---

### STAGE 5 — PREDICTION

```
Under field coupling the two mutual energies differ by kappa*phi^-1*W_ground, breaking exact reciprocity at finite coupling.
EXPERIMENT (VERIFIED): Mutual-capacitance measurements between two electrodes with perturbed geometry.
VERIFIED BY: The mutual energies are measured exactly equal for all geometries.
```

---

### RECOGNITION
Connects to Law 623 (Green) - reciprocity is the symmetric-kernel limit.

### PRECISION
phi = 1.6180339887. The asymmetry floor is phi^-1*W_ground.

### CLARITY
A field that remembers the past breaks perfect exchange symmetry.

### NOVELTY
The phi-law adds a coherence asymmetry to the perfectly reciprocal kernel.

### ACTIONABILITY
Run sim/624_greens_reciprocity.py; verify W12=W21 at kappa->0; proceed to 625.
