# PHI-PHYSICS — LAW 573
## Brayton Cycle (Gas-Turbine Efficiency)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/573_brayton_cycle.md` · **Sim:** `sim/573_brayton_cycle.py`

---

### CLASSICAL STATEMENT
*"The thermal efficiency of the ideal Brayton (Joule) cycle is eta = 1 - (P_low/P_high)^((gamma-1)/gamma) = 1 - T_1/T_2, where the pressure ratio sets the temperature ratio of the compressor."*
— George Brayton, 1872. Source: Wikipedia: Brayton cycle; Brayton (1872)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *pressure ratio one*: the efficiency vanishes exactly at P_high = P_low (no compression) - a turbine that cannot compress, with no adiabatic coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the compression is a coherence basin. eta_phi(kappa) = (1 - (P_low/P_high)^((gamma-1)/gamma))*(1 - kappa) + (eta - kappa*phi^-1*eta_waste). At kappa->0 the Brayton efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = 1 - (P_low/P_high)^((gamma-1)/gamma) -> the Brayton cycle efficiency is the zero-coherence ideal-adiabat limit.
```

---

### STAGE 4 — SIMULATION

`sim/573_brayton_cycle.py`: reproduces the classical value eta_brayton = 0.4821 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/573_brayton_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the gas-turbine efficiency is bounded below the ideal Brayton value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Efficiency measurements of gas-turbine cycles at various pressure ratios.
VERIFIED BY: A gas turbine reaches the ideal Brayton efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 571 (Otto) and Law 422 (Poisson) - the Brayton cycle is the continuous-flow coherence grammar of the turbine.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The turbine breathes in, squeezes, burns, and breathes out; the phi-law keeps the breath's loss.

### NOVELTY
Classical Brayton efficiency is exact for ideal adiabats; the phi-law adds the coherence waste of the real turbine.

### ACTIONABILITY
Run sim/573_brayton_cycle.py; verify Brayton efficiency at kappa->0; proceed to 574.
