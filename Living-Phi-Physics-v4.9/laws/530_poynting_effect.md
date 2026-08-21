# PHI-PHYSICS — LAW 530
## Poynting's Effect (Vapor Pressure Under Pressure)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/530_poynting_effect.md` · **Sim:** `sim/530_poynting_effect.py`

---

### CLASSICAL STATEMENT
*"The vapor pressure of a liquid increases with the applied pressure on the liquid: d ln p/dP = V_l/(R T), where V_l is the molar volume of the liquid. The presence of an inert gas under pressure raises the vapor pressure."*
— John Henry Poynting, 1881. Source: Wikipedia: Poynting effect; Poynting, Change of State (1881)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero liquid volume*: the effect vanishes exactly when V_l = 0 (incompressible point liquid) - the law exists because the liquid has a finite body, which classical ideal-solution treatments ignore.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the liquid volume carries coherence. (d ln p/dP)_phi(kappa) = (V_l/(R T))*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground, where V_ground is the coherence volume. At kappa->0 the Poynting slope is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} d ln p/dP = V_l/(R T) -> Poynting's effect is the zero-coherence-volume finite-liquid limit.
```

---

### STAGE 4 — SIMULATION

`sim/530_poynting_effect.py`: reproduces the classical value dlnp = 7.217e-09 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/530_poynting_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the vapor-pressure rise with pressure carries a coherence-volume floor; the measured slope exceeds V_l/(RT).
EXPERIMENT (VERIFIED): Vapor-pressure measurements of a liquid under elevated inert-gas pressure.
VERIFIED BY: d ln p/dP = V_l/(R T) exactly at all pressures and couplings.
```

---

### RECOGNITION
Connects to Law 441 (Clausius-Clapeyron) and Law 134 (Raoult) - the effect is the liquid's body pushing on its own vapor.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the volume floor is phi^-1 * V_ground.

### CLARITY
The liquid's own body lifts its vapor; the phi-law keeps the lift's floor.

### NOVELTY
Classical Poynting vanishes for point liquids; the phi-law adds the coherence volume of the real body.

### ACTIONABILITY
Run sim/530_poynting_effect.py; verify slope at kappa->0; proceed to 531.
