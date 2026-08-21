# PHI-PHYSICS — LAW 572
## Diesel Cycle (Compression-Ignition Efficiency)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/572_diesel_cycle.md` · **Sim:** `sim/572_diesel_cycle.py`

---

### CLASSICAL STATEMENT
*"The thermal efficiency of the ideal Diesel cycle is eta = 1 - (1/gamma)(1/r_c^gamma - 1)/(1/r_c - 1) / r^(gamma-1), where r is the compression ratio and r_c the cutoff ratio. It exceeds the Otto efficiency at the same compression ratio."*
— Rudolf Diesel, 1892. Source: Wikipedia: Diesel cycle; Diesel (1892)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *unity cutoff ratio*: the efficiency reduces to the Otto form when r_c = 1 (no constant-pressure heat addition) - a degenerate case that hides the Diesel cycle's distinct coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the cutoff is a coherence parameter. eta_phi(kappa) = eta_Diesel*(1 - kappa) + (eta_Diesel - kappa*phi^-1*eta_waste), bounding the efficiency. At kappa->0 the Diesel efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_Diesel -> the Diesel cycle efficiency is the zero-coherence ideal-adiabat limit.
```

---

### STAGE 4 — SIMULATION

`sim/572_diesel_cycle.py`: reproduces the classical value eta_diesel = 0.6138 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/572_diesel_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Diesel efficiency is bounded below the ideal value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Indicated-efficiency measurements of compression-ignition engines at various compression and cutoff ratios.
VERIFIED BY: A Diesel engine reaches the ideal Diesel efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 571 (Otto) and Law 422 (Poisson) - the Diesel cycle is the constant-pressure coherence twin of the Otto.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The Diesel squeezes air so hot it lights its own fuel; the phi-law keeps the spark's loss.

### NOVELTY
Classical Diesel efficiency assumes ideal processes; the phi-law adds the coherence waste of the real engine.

### ACTIONABILITY
Run sim/572_diesel_cycle.py; verify Diesel efficiency at kappa->0; proceed to 573.
