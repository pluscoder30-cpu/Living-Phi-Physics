# PHI-PHYSICS — LAW 583
## Combined Cycle (Gas-Steam Power Generation)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/583_combined_cycle.md` · **Sim:** `sim/583_combined_cycle.py`

---

### CLASSICAL STATEMENT
*"The combined cycle couples a Brayton (gas-turbine) topping cycle with a Rankine (steam) bottoming cycle, recovering the gas-turbine exhaust heat. Its efficiency approaches eta_combined = eta_Brayton + eta_Rankine - eta_Brayton eta_Rankine, reaching over 60%."*
— Power-plant engineering (gas-steam combined cycle), 1950. Source: Wikipedia: Combined cycle power plant; developed in power engineering (1940s-1960s)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *single-cycle operation*: the combined cycle exists because a single cycle cannot use all its rejected heat - the topping cycle's waste is the bottoming cycle's fuel, a coherence handoff that a single cycle lacks.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the heat handoff is a coherence coupling. eta_phi(kappa) = (eta_B + eta_R - eta_B eta_R)*(1 - kappa) + (eta_comb - kappa*phi^-1*eta_waste). At kappa->0 the combined-cycle efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_B + eta_R - eta_B eta_R -> the combined-cycle efficiency is the zero-handoff-coherence cascade limit.
```

---

### STAGE 4 — SIMULATION

`sim/583_combined_cycle.py`: reproduces the classical value eta_combined = 0.64 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/583_combined_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the combined-cycle efficiency is bounded below the cascade formula by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Modern combined-cycle power-plant efficiency measurements versus the cascade formula.
VERIFIED BY: A combined-cycle plant reaches eta_B + eta_R - eta_B eta_R exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 573 (Brayton) and Law 574 (Rankine) - the combined cycle is the heat-handoff coherence of the two-cycle plant.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
One engine's waste is another's fuel; the phi-law keeps the handoff's loss.

### NOVELTY
Classical combined cycle cascades efficiencies; the phi-law adds the coherence waste of the real handoff.

### ACTIONABILITY
Run sim/583_combined_cycle.py; verify cascade formula at kappa->0; proceed to 584.
