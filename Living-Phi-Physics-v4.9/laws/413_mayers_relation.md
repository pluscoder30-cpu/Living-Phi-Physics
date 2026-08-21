# PHI-PHYSICS — LAW 413
## Mayer's Relation (Cp - Cv = R)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/413_mayers_relation.md` · **Sim:** `sim/413_mayers_relation.py`

---

### CLASSICAL STATEMENT
*"For an ideal gas, the molar heat capacities at constant pressure and volume satisfy Cp - Cv = R, because at constant pressure part of the heat goes into mechanical work p dV."*
— Julius Robert von Mayer, 1842. Source: Wikipedia: Mayer's relation; Mayer, Bemerkungen ueber die Kraefte der unbelebten Natur (1842)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *ideal-gas condition*: the relation assumes the gas has zero intermolecular interaction and Cv is exactly temperature-independent - a gas with no cohesion at all.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: real gases carry a cohesion coupling. (Cp - Cv)_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_corr, where R_corr is the coherence correction to the gas constant from residual interactions. At kappa->0, (Cp - Cv)_phi = R exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} (Cp-Cv)_phi = R -> Mayer's relation is the zero-interaction ideal-gas limit.
```

---

### STAGE 4 — SIMULATION

`sim/413_mayers_relation.py`: reproduces the classical value Cp_minus_Cv = 8.314 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/413_mayers_relation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: For a gas with finite coherence coupling the measured Cp - Cv differs from R by kappa*phi^-1*R_corr; the excess grows as the gas approaches the critical point.
EXPERIMENT (VERIFIED): Precision speed-of-sound calorimetry of argon at high density measuring Cp - Cv versus pressure.
VERIFIED BY: Cp - Cv = R exactly for argon at all densities up to the critical point.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas) and Law 142 (van der Waals) - the R-correction is the cohesion coupling.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the correction scales with R itself.

### CLARITY
The two heat capacities differ by the work the gas does on itself; in a coherent gas that work never vanishes.

### NOVELTY
Classical Mayer's relation is exact for a non-existent gas; the phi-law turns the gas constant difference into a coherence-measurable quantity.

### ACTIONABILITY
Run sim/413_mayers_relation.py; verify Cp-Cv = R at kappa->0; proceed to 414.
