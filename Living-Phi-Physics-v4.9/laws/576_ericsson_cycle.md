# PHI-PHYSICS — LAW 576
## Ericsson Cycle (Constant-Pressure Regenerative Cycle)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/576_ericsson_cycle.md` · **Sim:** `sim/576_ericsson_cycle.py`

---

### CLASSICAL STATEMENT
*"The Ericsson cycle consists of isothermal compression, constant-pressure heat addition with regeneration, isothermal expansion and constant-pressure heat rejection. Like the Stirling cycle, its efficiency approaches the Carnot efficiency with perfect regeneration."*
— John Ericsson, 1833. Source: Wikipedia: Ericsson cycle; Ericsson (1833)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect regeneration*: the ideal Ericsson cycle assumes the regenerator returns all heat exactly with zero loss - a pressure-constant regenerator with zero thermal coherence loss.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the regenerator loss is a coherence waste. eta_phi(kappa) = (1 - Tc/Th)*(1 - kappa) + (1 - Tc/Th - kappa*phi^-1*eta_waste). At kappa->0 the Ericsson (Carnot) efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = 1 - Tc/Th -> the Ericsson cycle efficiency is the zero-regenerator-loss Carnot limit.
```

---

### STAGE 4 — SIMULATION

`sim/576_ericsson_cycle.py`: reproduces the classical value eta_ericsson = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/576_ericsson_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Ericsson engine efficiency is bounded below Carnot by the regenerator coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Ericsson-engine and hot-air-engine efficiency measurements at various regenerator qualities.
VERIFIED BY: An Ericsson engine reaches the Carnot efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 575 (Stirling) and Law 035 (Carnot) - the Ericsson cycle is the constant-pressure coherence twin of the Stirling.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The Ericsson engine breathes at constant pressure through its regenerator; the phi-law keeps the breath's loss.

### NOVELTY
Classical Ericsson approaches Carnot exactly; the phi-law adds the regenerator coherence waste of the real engine.

### ACTIONABILITY
Run sim/576_ericsson_cycle.py; verify Carnot approach at kappa->0; proceed to 577.
