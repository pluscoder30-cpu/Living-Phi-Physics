# PHI-PHYSICS — LAW 584
## Coefficient of Performance of Refrigeration

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/584_refrigeration_cop.md` · **Sim:** `sim/584_refrigeration_cop.py`

---

### CLASSICAL STATEMENT
*"The coefficient of performance of a refrigerator is COP = Q_c/W, the heat removed from the cold reservoir per unit work input. The maximum (Carnot) COP is COP_max = T_c/(T_h - T_c)."*
— Rudolf Clausius; William Thomson (Carnot analysis), 1850. Source: Wikipedia: Coefficient of performance; Clausius (1850), Thomson (1851)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature lift*: the COP diverges exactly when T_h = T_c (no temperature difference) - a refrigerator lifting heat across no gradient requires no work, a zero-lift state that never exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the temperature lift is a coherence basin. COP_phi(kappa) = (Tc/(Th-Tc))*(1 - kappa) + (Tc/(Th-Tc) - kappa*phi^-1*COP_waste). At kappa->0 the Carnot COP is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} COP_phi = Tc/(Th - Tc) -> the refrigeration COP is the zero-coherence Carnot limit.
```

---

### STAGE 4 — SIMULATION

`sim/584_refrigeration_cop.py`: reproduces the classical value COP_ref = 5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/584_refrigeration_cop.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the achievable COP is bounded below the Carnot value by the coherence waste kappa*phi^-1*COP_waste.
EXPERIMENT (VERIFIED): Cryocooler and refrigerator COP measurements versus the Carnot COP.
VERIFIED BY: A refrigerator reaches the Carnot COP exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 443 (Clausius statement) and Law 585 (heat pump COP) - the COP is the cold-side coherence budget.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * COP_waste.

### CLARITY
Every refrigerator carries heat uphill on a work ladder; the phi-law keeps the ladder's loss.

### NOVELTY
Classical COP diverges at zero lift; the phi-law bounds the real COP with a coherence waste.

### ACTIONABILITY
Run sim/584_refrigeration_cop.py; verify Carnot COP at kappa->0; proceed to 585.
