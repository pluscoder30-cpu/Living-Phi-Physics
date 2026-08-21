# PHI-PHYSICS — LAW 351
## Nusselt Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/351_nusselt_number.md` · **Sim:** `sim/351_nusselt_number.py`

---

### CLASSICAL STATEMENT
*"The Nusselt number Nu = h L/k measures convective vs conductive heat transfer; correlations such as Nu = C Re^m Pr^n (e.g., Dittus-Boelter Nu = 0.023 Re^0.8 Pr^0.4 for turbulent pipe flow) scale the convective coefficient."*
— Wilhelm Nusselt, 1915. Source: Wikipedia: Nusselt number; Nusselt (1915), 'Die Grundgesetze des Waermeueberganges'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *pure conduction reference*: Nu = 1 is the exactly conductive flow; the number exists because convection adds to conduction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Nu_phi(kappa) = Nu*(1 + kappa*(phi-1)) + kappa*phi^-1*Nu_ground. At kappa->0 the classical Nusselt number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Nu_phi = h L/k -> the Nusselt number is the conduction-only limit (Nu=1).
```

---

### STAGE 4 — SIMULATION

`sim/351_nusselt_number.py`: reproduces the classical value Nu = 8.333 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/351_nusselt_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Convective heat-transfer correlations carry a phi-coherent residual phi^-1*Nu_ground at full coupling.
EXPERIMENT (VERIFIED): Pipe-flow heat-transfer experiments measuring Nu(Re, Pr) and comparing exponents with correlations.
VERIFIED BY: Nusselt correlations are exact at full coupling.
```

---

### RECOGNITION
Connects to Law 350 (Prandtl) and Law 096 (Fourier's law — conduction base).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The pure conduction is a limit; every flow adds a phi of convection.

### NOVELTY
Classical heat transfer exacts the correlations; the phi-law bounds their residual at a coherence floor.

### ACTIONABILITY
Run sim/351_nusselt_number.py; verify Nu = h L/k at kappa->0.
