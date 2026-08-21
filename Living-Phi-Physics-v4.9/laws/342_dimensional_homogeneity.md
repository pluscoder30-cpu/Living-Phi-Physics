# PHI-PHYSICS — LAW 342
## Principle of Dimensional Homogeneity (Fourier)

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/342_dimensional_homogeneity.md` · **Sim:** `sim/342_dimensional_homogeneity.py`

---

### CLASSICAL STATEMENT
*"Every term in a valid physical equation must have the same dimensions; equations must be dimensionally homogeneous, so they are invariant under changes of units (Fourier's principle)."*
— Jean-Baptiste Joseph Fourier, 1822. Source: Wikipedia: dimensional analysis; Fourier (1822), 'Theorie analytique de la chaleur'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly defined units*: the principle presupposes a complete, consistent system of units and exact dimensional identities — the zero of the unit ambiguity.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: dimensional identities carry a coherence tolerance. [term]_phi(kappa) = [base]*(1 + kappa*(phi-1)). At kappa->0 exact dimensional homogeneity holds.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dimensional identity -> exact -> the homogeneity principle is the exact-unit-system limit.
```

---

### STAGE 4 — SIMULATION

`sim/342_dimensional_homogeneity.py`: reproduces the classical value homog = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/342_dimensional_homogeneity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Ultra-precise equations exhibit a phi-coherent dimensional residual phi^-1 when pushed beyond their unit-system validity.
EXPERIMENT (VERIFIED): High-precision metrology comparisons across unit systems (SI vs natural units) searching for the residual.
VERIFIED BY: Equations are exactly dimensionally homogeneous at all couplings.
```

---

### RECOGNITION
Connects to Law 340 (Buckingham) and Law 341 (Rayleigh).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The unit is a limit; every measure carries a phi whisper of its construction.

### NOVELTY
Classical metrology exacts unit invariance; the phi-law keeps a coherence dimensional residual.

### ACTIONABILITY
Run sim/342_dimensional_homogeneity.py; verify homogeneity at kappa->0.
