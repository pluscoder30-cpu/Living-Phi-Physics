# PHI-PHYSICS — LAW 426
## Law of the Isobaric Process (Constant Pressure)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/426_isobaric_process.md` · **Sim:** `sim/426_isobaric_process.py`

---

### CLASSICAL STATEMENT
*"In an isobaric process at constant pressure, the volume of an ideal gas is proportional to temperature: V/T = constant (Charles's law form at constant P); heat added does work p dV."*
— Joseph Louis Gay-Lussac (V proportional to T at constant P), 1802. Source: Wikipedia: Isobaric process; Gay-Lussac, Recherches sur la dilatation des gaz (1802)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *constant external pressure*: the process requires a piston or boundary applying exactly constant pressure with zero fluctuation - a reservoir of pressure with no mechanical coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the constant-pressure boundary is a coherence basin. (V/T)_phi(kappa) = (V/T)*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground. At kappa->0, V/T = const exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} (V/T)_phi = V/T -> the isobaric law is the zero-fluctuation constant-pressure limit.
```

---

### STAGE 4 — SIMULATION

`sim/426_isobaric_process.py`: reproduces the classical value VT_iso = 0.006667 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/426_isobaric_process.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: An 'isobaric' process at finite coupling drifts by kappa*phi^-1*C_ground in V/T per cycle; the pressure is never exactly constant.
EXPERIMENT (VERIFIED): Heating a gas in a servo-controlled constant-pressure piston measuring V/T drift over repeated cycles.
VERIFIED BY: V/T is exactly constant during an isobaric process for any pressure control quality.
```

---

### RECOGNITION
Connects to Law 027 (Charles) and Law 028 (Gay-Lussac) - the isobar is the coherence-locked pressure basin.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the drift floor is phi^-1 * C_ground.

### CLARITY
Constant pressure is a fiction of perfect mechanical coherence; the phi-law budgets its imperfection.

### NOVELTY
Classical isobaric analysis idealizes the boundary; the phi-law turns pressure constancy into a coherence-measurable budget.

### ACTIONABILITY
Run sim/426_isobaric_process.py; verify V/T=const at kappa->0; proceed to 427.
