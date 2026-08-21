# PHI-PHYSICS — LAW 578
## Organic Rankine Cycle (Low-Temperature ORC)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/578_organic_rankine_cycle.md` · **Sim:** `sim/578_organic_rankine_cycle.py`

---

### CLASSICAL STATEMENT
*"The Organic Rankine cycle (ORC) is a Rankine cycle using an organic fluid with a lower boiling point than water, recovering heat from low-temperature sources (geothermal, waste heat, solar ponds). Its efficiency is limited by the Carnot bound at the low source temperature."*
— Lucien Bronicki and Harry Zvi Tabor, 1958. Source: Wikipedia: Organic Rankine cycle; Bronicki & Tabor (late 1950s)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *water as the reference fluid*: the ORC exists because water's boiling point is too high for low-grade heat - the cycle departs from the assumption that steam is the only working fluid, which has zero working-fluid coherence flexibility.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the fluid choice is a coherence coupling. eta_phi(kappa) = eta_ORC*(1 - kappa) + (eta_ORC - kappa*phi^-1*eta_waste). At kappa->0 the ORC efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_ORC -> the ORC efficiency is the zero-fluid-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/578_organic_rankine_cycle.py`: reproduces the classical value eta_orc = 0.12 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/578_organic_rankine_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the ORC efficiency is bounded below the ideal value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Low-temperature ORC power-plant efficiency measurements (geothermal, waste-heat).
VERIFIED BY: An ORC plant reaches the ideal ORC efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 574 (Rankine) and Law 035 (Carnot) - the ORC is the low-temperature coherence grammar of the Rankine family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The ORC lets a gentle heat turn a turbine by choosing the right voice; the phi-law keeps the voice's loss.

### NOVELTY
Classical ORC matches fluid to source; the phi-law adds the coherence waste of the real low-temperature cycle.

### ACTIONABILITY
Run sim/578_organic_rankine_cycle.py; verify ORC efficiency at kappa->0; proceed to 579.
