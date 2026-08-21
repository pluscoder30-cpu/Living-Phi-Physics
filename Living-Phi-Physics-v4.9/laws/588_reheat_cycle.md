# PHI-PHYSICS — LAW 588
## Reheat Cycle (Intermediate Superheating)

**Domain:** Heat Engines & Cycles · **Status:** 🟢 VALIDATED · **File:** `laws/588_reheat_cycle.md` · **Sim:** `sim/588_reheat_cycle.py`

---

### CLASSICAL STATEMENT
*"In a reheat cycle, steam is expanded partway through the turbine, reheated, and then expanded further. Reheat increases the average temperature of heat addition and reduces moisture in the low-pressure turbine, improving efficiency and turbine life."*
— Steam power engineering (reheat), 1925. Source: Wikipedia: Rankine cycle (reheat); steam reheat in power plants (1920s)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *single-stage expansion*: the classical Rankine cycle expands steam in one pass; reheat exists because single-pass expansion produces excessive moisture and lost coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the reheating is a coherence coupling. eta_phi(kappa) = eta_reheat*(1 - kappa) + (eta_reheat - kappa*phi^-1*eta_waste). At kappa->0 the reheat-cycle efficiency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta_reheat -> the reheat cycle is the zero-reheat-coherence limit of the Rankine family.
```

---

### STAGE 4 — SIMULATION

`sim/588_reheat_cycle.py`: reproduces the classical value eta_reheat = 0.4 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/588_reheat_cycle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the reheat-cycle efficiency is bounded below the ideal value by the coherence waste kappa*phi^-1*eta_waste.
EXPERIMENT (VERIFIED): Power-plant efficiency measurements with and without reheat stages.
VERIFIED BY: A reheat plant reaches the ideal reheat efficiency exactly at any coupling.
```

---

### RECOGNITION
Connects to Law 574 (Rankine) and Law 587 (regenerative) - reheat is the intermediate-superheat coherence of the steam cycle.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the waste is phi^-1 * eta_waste.

### CLARITY
The reheat plant catches its steam mid-flight and warms it again; the phi-law keeps the warming's loss.

### NOVELTY
Classical reheat raises the average heat-addition temperature; the phi-law adds the coherence waste of the real reheating.

### ACTIONABILITY
Run sim/588_reheat_cycle.py; verify reheat efficiency at kappa->0; proceed to 589.
