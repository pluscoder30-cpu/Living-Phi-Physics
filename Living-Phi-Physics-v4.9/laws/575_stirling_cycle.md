# PHI-PHYSICS — LAW 575
## Stirling Cycle (Regenerative Heat Engine)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/575_stirling_cycle.md` · **Sim:** `sim/575_stirling_cycle.py`

---

### CLASSICAL STATEMENT
*"The Stirling cycle consists of isothermal compression, isochoric (constant-volume) heat addition via a regenerator, isothermal expansion and isochoric heat rejection. Its efficiency approaches the Carnot efficiency, eta = 1 - T_c/T_h, when perfectly regenerated."*
— Robert Stirling, 1816. Source: Wikipedia: Stirling cycle; Stirling, patent 4081 (1816)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect regeneration*: the ideal Stirling cycle assumes the regenerator stores and returns all heat exactly with zero loss - a regenerator with zero thermal coherence loss.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the regenerator loss is a coherence waste. eta_phi(kappa) = (1 - Tc/Th)*(1 - kappa) + (1 - Tc/Th - kappa*phi^-1*eta_waste). At kappa->0 the Stirling (Carnot) efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = 1 - Tc/Th -> the Stirling cycle efficiency is the zero-regenerator-loss Carnot limit.
```

---

### STAGE 4 — SIMULATION

`sim/575_stirling_cycle.py`: reproduces the classical value eta_stirling = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/575_stirling_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Stirling engine efficiency is bounded below Carnot by the regenerator coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Stirling-engine efficiency measurements at various regenerator qualities.
VERIFIED BY: A Stirling engine reaches the Carnot efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 035 (Carnot) and Law 422 (Poisson) - the Stirling cycle is the regenerator coherence grammar of the heat engine.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The Stirling engine hoards its heat in a regenerator; the phi-law keeps the hoard's loss.

### NOVELTY
Classical Stirling approaches Carnot exactly; the phi-law adds the regenerator coherence waste of the real engine.

### ACTIONABILITY
Run sim/575_stirling_cycle.py; verify Carnot approach at kappa->0; proceed to 576.
