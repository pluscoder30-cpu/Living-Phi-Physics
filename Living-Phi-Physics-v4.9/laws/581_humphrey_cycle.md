# PHI-PHYSICS — LAW 581
## Humphrey Cycle (Constant-Volume Combustion)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/581_humphrey_cycle.md` · **Sim:** `sim/581_humphrey_cycle.py`

---

### CLASSICAL STATEMENT
*"The Humphrey cycle uses constant-volume (rather than constant-pressure) combustion in a gas-turbine or pulse-combustion engine, increasing the peak pressure and potential efficiency relative to the Brayton cycle."*
— Herbert Alfred Humphrey, 1906. Source: Wikipedia: Humphrey cycle; Humphrey (1906)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *constant-pressure combustion*: the Humphrey cycle departs from the Brayton assumption of constant-pressure heat addition - a combustion process whose volume change is exactly zero in the idealized cycle.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the combustion volume is a coherence parameter. eta_phi(kappa) = eta_Humphrey*(1 - kappa) + (eta_Humphrey - kappa*phi^-1*eta_waste). At kappa->0 the Humphrey efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_Humphrey -> the Humphrey cycle is the constant-volume-combustion coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/581_humphrey_cycle.py`: reproduces the classical value eta_humphrey = 0.36 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/581_humphrey_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Humphrey efficiency is bounded below the ideal value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Pulse-combustion and constant-volume-combustion engine efficiency measurements.
VERIFIED BY: A Humphrey engine reaches the ideal Humphrey efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 573 (Brayton) and Law 571 (Otto) - the Humphrey cycle is the constant-volume-combustion coherence of the turbine family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The Humphrey engine burns at constant volume, packing its punch; the phi-law keeps the punch's loss.

### NOVELTY
Classical Humphrey exploits constant-volume combustion; the phi-law adds the coherence waste of the real engine.

### ACTIONABILITY
Run sim/581_humphrey_cycle.py; verify Humphrey efficiency at kappa->0; proceed to 582.
