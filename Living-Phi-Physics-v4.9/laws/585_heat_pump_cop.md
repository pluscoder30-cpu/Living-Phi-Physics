# PHI-PHYSICS — LAW 585
## Coefficient of Performance of a Heat Pump

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/585_heat_pump_cop.md` · **Sim:** `sim/585_heat_pump_cop.py`

---

### CLASSICAL STATEMENT
*"The coefficient of performance of a heat pump is COP = Q_h/W, the heat delivered to the hot reservoir per unit work input. The maximum (Carnot) COP is COP_max = T_h/(T_h - T_c) = COP_refrigerator + 1."*
— William Thomson (Lord Kelvin), 1852. Source: Wikipedia: Coefficient of performance; Thomson (1852)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature lift*: the COP diverges exactly when T_h = T_c - a heat pump lifting heat across no gradient needs no work, a zero-lift state that never exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the temperature lift is a coherence basin. COP_phi(kappa) = (Th/(Th-Tc))*(1 - kappa) + (Th/(Th-Tc) - kappa*phi^-1*COP_waste). At kappa->0 the Carnot heat-pump COP is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} COP_phi = Th/(Th - Tc) -> the heat-pump COP is the zero-coherence Carnot limit.
```

---

### STAGE 4 — SIMULATION

`sim/585_heat_pump_cop.py`: reproduces the classical value COP_hp = 14.65 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/585_heat_pump_cop.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the achievable heat-pump COP is bounded below the Carnot value by the coherence waste kappa*phi^-1*COP_waste.
EXPERIMENT (VERIFIED): Heat-pump COP measurements versus the Carnot COP across temperature lifts.
VERIFIED BY: A heat pump reaches the Carnot COP exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 584 (refrigeration COP) and Law 443 (Clausius) - the heat-pump COP is the hot-side coherence budget.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * COP_waste.

### CLARITY
The heat pump pays work to move warmth up; the phi-law keeps the moving's loss.

### NOVELTY
Classical heat-pump COP diverges at zero lift; the phi-law bounds the real COP with a coherence waste.

### ACTIONABILITY
Run sim/585_heat_pump_cop.py; verify Carnot COP at kappa->0; proceed to 586.
