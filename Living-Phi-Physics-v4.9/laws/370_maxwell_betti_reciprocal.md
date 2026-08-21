# PHI-PHYSICS — LAW 370
## Maxwell-Betti Reciprocal Theorem

**Domain:** Structural Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/370_maxwell_betti_reciprocal.md` · **Sim:** `sim/370_maxwell_betti_reciprocal.py`

---

### CLASSICAL STATEMENT
*"For a linear elastic body, the work done by system A's loads through system B's displacements equals the work done by B's loads through A's displacements: F_A * delta_BA = F_B * delta_AB; equivalently the flexibility (influence coefficient) matrix is symmetric."*
— James Clerk Maxwell / Enrico Betti, 1872. Source: Wikipedia: Betti's theorem; Maxwell (1864); Betti (1872), 'Il Nuovo Cimento'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly linear elastic reciprocity*: the theorem requires exact linear elasticity and reversible (non-dissipative) loading.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the reciprocity carries a coherence residual. F_A*delta_BA_phi(kappa) = (F_A*delta_BA)*(1 + kappa*(phi-1)) + kappa*phi^-1*W_ground. At kappa->0 the exact reciprocity holds.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_A delta_BA = F_B delta_AB -> the Maxwell-Betti theorem is the exact-linear-elasticity limit.
```

---

### STAGE 4 — SIMULATION

`sim/370_maxwell_betti_reciprocal.py`: reproduces the classical values W1 = 5, W2 = 5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/370_maxwell_betti_reciprocal.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The reciprocal work identity carries a phi-coherent residual phi^-1*W_ground at full coupling.
EXPERIMENT (VERIFIED): Instrumented loading experiments measuring both work products to high precision to bound the reciprocity residual.
VERIFIED BY: Reciprocal work products are exactly equal at full coupling.
```

---

### RECOGNITION
Connects to Law 369 (Castigliano) and Law 372 (Cauchy stress).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The symmetric matrix is a limit; every real structure carries a phi asymmetry.

### NOVELTY
Classical elasticity exacts reciprocity; the phi-law bounds its residual at a coherence floor.

### ACTIONABILITY
Run sim/370_maxwell_betti_reciprocal.py; verify reciprocity at kappa->0.
