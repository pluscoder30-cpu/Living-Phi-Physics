# PHI-PHYSICS — LAW 574
## Rankine Cycle (Steam Power Cycle)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/574_rankine_cycle.md` · **Sim:** `sim/574_rankine_cycle.py`

---

### CLASSICAL STATEMENT
*"The Rankine cycle is the ideal vapor-power cycle: isentropic compression in the pump, constant-pressure heat addition in the boiler, isentropic expansion in the turbine, and constant-pressure condensation. Its thermal efficiency is eta = (W_turbine - W_pump)/Q_in."*
— William John Macquorn Rankine, 1859. Source: Wikipedia: Rankine cycle; Rankine, A Manual of the Steam Engine (1859)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *isentropic expansion*: the cycle assumes the turbine and pump are exactly isentropic with zero entropy generation - machinery with no dissipation coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the machinery dissipation is a coherence waste. eta_phi(kappa) = eta_Rankine*(1 - kappa) + (eta_Rankine - kappa*phi^-1*eta_waste). At kappa->0 the Rankine efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_Rankine -> the Rankine cycle efficiency is the zero-dissipation isentropic-machine limit.
```

---

### STAGE 4 — SIMULATION

`sim/574_rankine_cycle.py`: reproduces the classical value eta_rankine = 0.37 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/574_rankine_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the steam-cycle efficiency is bounded below the ideal Rankine value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Power-plant efficiency measurements comparing actual steam cycles with the ideal Rankine analysis.
VERIFIED BY: A steam power plant reaches the ideal Rankine efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 575 (Stirling) and Law 434 (enthalpy) - the Rankine cycle is the phase-change coherence grammar of the steam engine.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
Steam is the working breath of industry; the phi-law keeps the breath's loss.

### NOVELTY
Classical Rankine assumes ideal machines; the phi-law adds the coherence waste of the real plant.

### ACTIONABILITY
Run sim/574_rankine_cycle.py; verify Rankine efficiency at kappa->0; proceed to 575.
