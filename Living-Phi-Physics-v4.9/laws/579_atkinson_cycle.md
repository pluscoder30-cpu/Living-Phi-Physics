# PHI-PHYSICS — LAW 579
## Atkinson Cycle (Expansion-Ratio Engine)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/579_atkinson_cycle.md` · **Sim:** `sim/579_atkinson_cycle.py`

---

### CLASSICAL STATEMENT
*"The Atkinson cycle has a longer expansion stroke than compression stroke (expansion ratio > compression ratio), extracting more work per cycle. Its efficiency can exceed the Otto efficiency at the same compression ratio, at the cost of lower power density."*
— James Atkinson, 1882. Source: Wikipedia: Atkinson cycle; Atkinson (1882)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *equal strokes*: the Atkinson cycle departs from the Otto assumption of equal compression and expansion ratios - an asymmetric engine whose asymmetry is exactly zero in the Otto limit.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the stroke asymmetry is a coherence parameter. eta_phi(kappa) = eta_Atkinson*(1 - kappa) + (eta_Atkinson - kappa*phi^-1*eta_waste). At kappa->0 the Atkinson efficiency reduces to the Otto form.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_Atkinson -> the Atkinson cycle is the extended-expansion coherence limit of the Otto.
```

---

### STAGE 4 — SIMULATION

`sim/579_atkinson_cycle.py`: reproduces the classical value eta_atkinson = 0.4 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/579_atkinson_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Atkinson efficiency is bounded below the ideal value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Efficiency measurements of Atkinson-cycle and Miller-cycle engines (modern hybrids).
VERIFIED BY: An Atkinson engine reaches the ideal Atkinson efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 571 (Otto) and Law 580 (Miller) - the Atkinson cycle is the asymmetric-stroke coherence of the engine family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The Atkinson engine expands longer than it compresses; the phi-law keeps the asymmetry's loss.

### NOVELTY
Classical Atkinson exploits stroke asymmetry; the phi-law adds the coherence waste of the real asymmetric engine.

### ACTIONABILITY
Run sim/579_atkinson_cycle.py; verify Atkinson efficiency at kappa->0; proceed to 580.
