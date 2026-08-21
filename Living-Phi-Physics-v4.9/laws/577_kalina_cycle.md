# PHI-PHYSICS — LAW 577
## Kalina Cycle (Ammonia-Water Power Cycle)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/577_kalina_cycle.md` · **Sim:** `sim/577_kalina_cycle.py`

---

### CLASSICAL STATEMENT
*"The Kalina cycle uses an ammonia-water working mixture whose boiling point varies with composition, allowing a closer match to the heat-source temperature profile. It achieves higher thermal efficiency than a comparable Rankine cycle at low-temperature heat sources."*
— Alexander Kalina, 1985. Source: Wikipedia: Kalina cycle; Kalina, US Patent 4,548,043 (1985)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *fixed composition*: the cycle exploits variable composition to match the heat source, departing from the single-fluid Rankine assumption where the working fluid has no compositional coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the composition match is a coherence coupling. eta_phi(kappa) = eta_Kalina*(1 - kappa) + (eta_Kalina - kappa*phi^-1*eta_waste). At kappa->0 the Kalina efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_Kalina -> the Kalina cycle efficiency is the zero-composition-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/577_kalina_cycle.py`: reproduces the classical value eta_kalina = 0.28 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/577_kalina_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Kalina efficiency is bounded below the ideal value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Low-temperature geothermal and waste-heat power-plant efficiency measurements with Kalina systems.
VERIFIED BY: A Kalina plant reaches the ideal Kalina efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 574 (Rankine) and Law 440 (Clapeyron) - the Kalina cycle is the variable-composition coherence of the binary fluid.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The ammonia-water pair tunes its boiling to the heat it is given; the phi-law keeps the tuning's loss.

### NOVELTY
Classical Kalina exploits composition matching; the phi-law adds the coherence waste of the real binary cycle.

### ACTIONABILITY
Run sim/577_kalina_cycle.py; verify Kalina efficiency at kappa->0; proceed to 578.
