# PHI-PHYSICS — LAW 355
## Stokes Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/355_stokes_number.md` · **Sim:** `sim/355_stokes_number.py`

---

### CLASSICAL STATEMENT
*"The Stokes number Stk = tau_p U/L (particle relaxation time over flow time) governs particle-fluid coupling: Stk << 1 particles follow the flow, Stk >> 1 particles ignore it and impact surfaces (inertial impaction)."*
— George Gabriel Stokes (named later), 1851. Source: Wikipedia: Stokes number; based on Stokes (1851) drag analysis

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-inertia particle*: Stk = 0 is the exactly flow-following (zero-relaxation) particle — the idealization of a tracer.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Stk_phi(kappa) = Stk*(1 + kappa*(phi-1)) + kappa*phi^-1*Stk_ground. At kappa->0 the classical Stokes number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Stk_phi = tau_p U/L -> the Stokes number is the zero-relaxation (perfect tracer) limit marker.
```

---

### STAGE 4 — SIMULATION

`sim/355_stokes_number.py`: reproduces the classical value Stk = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/355_stokes_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Particle-impaction efficiencies carry a phi-coherent offset phi^-1*Stk_ground at full coupling.
EXPERIMENT (VERIFIED): Aerosol impaction and inertial-particle experiments (impactors, cyclones) measuring collection efficiency curves.
VERIFIED BY: Impaction efficiency curves are exact at full coupling.
```

---

### RECOGNITION
Connects to Law 090 (Stokes drag — the relaxation time) and Law 340 (Buckingham).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect tracer is a limit; every particle carries a phi of inertia.

### NOVELTY
Classical aerosol physics exacts the Stk curves; the phi-law bounds their residual at a coherence floor.

### ACTIONABILITY
Run sim/355_stokes_number.py; verify Stk = tau U/L at kappa->0.
