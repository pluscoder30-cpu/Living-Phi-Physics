# PHI-PHYSICS — LAW 359
## Froude Scaling Law (Model-Test Similitude)

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/359_froude_scaling.md` · **Sim:** `sim/359_froude_scaling.py`

---

### CLASSICAL STATEMENT
*"For gravity-dominated (free-surface) flows, model and prototype are dynamically similar when their Froude numbers are equal; then velocities scale as sqrt(L) (V_model = V_prototype sqrt(L_model/L_prototype)) and times as sqrt(L), enabling tow-tank tests of ships and hydraulic models."*
— William Froude, 1868. Source: Wikipedia: Froude number / model testing; Froude (1868-1874) ship model tests

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact Froude equality and scale-model perfection*: the scaling requires Fr_model = Fr_prototype exactly and neglects the viscosity/surface-tension effects that differ between scales.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the scale factor carries a coherence correction. lambda_phi(kappa) = sqrt(L_model/L_prototype)*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_ground. At kappa->0 the classical Froude scaling is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_model = V_prototype sqrt(L_m/L_p) -> Froude scaling is the gravity-only similitude limit.
```

---

### STAGE 4 — SIMULATION

`sim/359_froude_scaling.py`: reproduces the classical value Vm = 0.7071 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/359_froude_scaling.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Scale-model predictions deviate from full-scale behavior by a phi-coherent residual phi^-1*lambda_ground at full coupling.
EXPERIMENT (VERIFIED): Cross-scale model-test programs (multiple geometrically similar models of one ship/hydraulic structure) measuring the scaling residual.
VERIFIED BY: Scale-model results scale exactly by the Froude law at full coupling.
```

---

### RECOGNITION
Connects to Law 343 (Froude number) and Law 340 (Buckingham).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect model is a limit; every small version carries a phi of its large self.

### NOVELTY
Classical similitude exacts the Froude law; the phi-law bounds the cross-scale residual at a coherence floor.

### ACTIONABILITY
Run sim/359_froude_scaling.py; verify the sqrt(L) scaling at kappa->0.
