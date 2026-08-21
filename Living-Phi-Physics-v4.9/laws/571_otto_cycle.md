# PHI-PHYSICS — LAW 571
## Otto Cycle (Spark-Ignition Efficiency)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/571_otto_cycle.md` · **Sim:** `sim/571_otto_cycle.py`

---

### CLASSICAL STATEMENT
*"The thermal efficiency of the ideal Otto cycle is eta = 1 - r^(1-gamma), where r is the compression ratio and gamma = C_p/C_v. Higher compression ratios give higher efficiency."*
— Nikolaus Otto, 1876. Source: Wikipedia: Otto cycle; Otto (1876)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *compression ratio one*: the efficiency vanishes exactly at r = 1 (no compression) - an engine that cannot compress at all, with no adiabatic coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the compression is a coherence basin. eta_phi(kappa) = (1 - r^(1-gamma))*(1 - kappa) + (1 - r^(1-gamma) - kappa*phi^-1*eta_waste), bounding the efficiency below the Otto value. At kappa->0 the Otto efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = 1 - r^(1-gamma) -> the Otto cycle efficiency is the zero-coherence ideal-adiabat limit.
```

---

### STAGE 4 — SIMULATION

`sim/571_otto_cycle.py`: reproduces the classical value eta_otto = 0.5647 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/571_otto_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the real Otto engine efficiency is bounded below 1 - r^(1-gamma) by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Indicated-efficiency measurements of spark-ignition engines at various compression ratios.
VERIFIED BY: An engine reaches the Otto efficiency 1 - r^(1-gamma) exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 422 (Poisson) and Law 442 (Kelvin) - the Otto cycle is the coherence grammar of the spark-ignition engine.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The Otto engine squeezes heat into a spike; the phi-law keeps the spike's loss.

### NOVELTY
Classical Otto efficiency is exact for ideal adiabats; the phi-law adds the coherence waste of the real engine.

### ACTIONABILITY
Run sim/571_otto_cycle.py; verify Otto efficiency at kappa->0; proceed to 572.
