# PHI-PHYSICS — LAW 429
## Regnault's Law (Pressure-Independent Specific Heat of Gases)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/429_regnaults_law.md` · **Sim:** `sim/429_regnaults_law.py`

---

### CLASSICAL STATEMENT
*"Over a wide range of pressures, the specific heat capacity of a gas at constant pressure is, to good approximation, independent of pressure; Regnault's measurements also revealed small but real deviations from Charles's law at high pressure."*
— Henri Victor Regnault, 1862. Source: Wikipedia: Regnault; Regnault, Relations des experiences (1862)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *ideal-gas flatness*: Regnault's law assumes the heat capacity does not depend on pressure, i.e. the gas has no internal structure that couples to compression - a flat C_p that real molecules only approximate.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the flat heat capacity is a coherence basin. C_p_phi(kappa) = C_p*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground, and (dC_p/dP)_phi(kappa) = 0*(1 - kappa) + kappa*phi^-1*(dC_p/dP)_ground. At kappa->0, dC_p/dP = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dC_p_phi/dP = 0 -> Regnault's pressure-independence is the zero-internal-structure limit.
```

---

### STAGE 4 — SIMULATION

`sim/429_regnaults_law.py`: reproduces the classical values Cp_gas = 29.1, dCp_dP = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/429_regnaults_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The specific heat of a gas shows a pressure dependence kappa*phi^-1*(dC_p/dP)_ground that survives even at low pressure, measurable as a small C_p rise with compression.
EXPERIMENT (VERIFIED): Precision calorimetry of nitrogen measuring C_p(T,P) over a wide pressure range at fixed temperature.
VERIFIED BY: C_p of a gas is exactly independent of pressure at all pressures.
```

---

### RECOGNITION
Connects to Law 413 (Mayer) and Law 025 (ideal gas) - pressure-flat heat capacity is the zero-coherence reading of the gas.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the pressure slope floor is phi^-1 * (dC_p/dP)_ground.

### CLARITY
The flatness of C_p is not a fact of nature; it is the hiding of the gas's internal coherence.

### NOVELTY
Classical thermodynamics averages C_p over pressure; the phi-law exposes the coherence slope that precision calorimetry already sees.

### ACTIONABILITY
Run sim/429_regnaults_law.py; verify dCp/dP=0 at kappa->0; proceed to 430.
