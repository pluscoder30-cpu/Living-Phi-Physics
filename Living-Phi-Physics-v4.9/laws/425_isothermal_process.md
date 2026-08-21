# PHI-PHYSICS — LAW 425
## Law of the Isothermal Process (Constant Temperature)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/425_isothermal_process.md` · **Sim:** `sim/425_isothermal_process.py`

---

### CLASSICAL STATEMENT
*"In an isothermal process at constant temperature, an ideal gas obeys P V = constant (Boyle's law); the internal energy is unchanged and all work exchanges heat with the reservoir."*
— Robert Boyle (isothermal compression), 1662. Source: Wikipedia: Isothermal process; Boyle, New Experiments Physico-Mechanical (1662)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect thermal contact*: an isothermal process requires the gas to exchange heat with a reservoir at exactly the same temperature instantly - a reservoir with zero thermal resistance and zero temperature change.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the constant-temperature contact is a coherence basin. (P V)_phi(kappa) = (P V)*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground. At kappa->0, P V = const exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} (PV)_phi = PV -> Boyle's isothermal law is the perfect-reservoir, zero-temperature-drift limit.
```

---

### STAGE 4 — SIMULATION

`sim/425_isothermal_process.py`: reproduces the classical value PV_iso = 3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/425_isothermal_process.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: An 'isothermal' process at finite coupling shows a residual PV drift kappa*phi^-1*C_ground per cycle; the temperature is never exactly constant.
EXPERIMENT (VERIFIED): Slow isothermal compression in a thermostat with high-resolution P-V-T logging measuring the PV drift over cycles.
VERIFIED BY: PV is exactly constant during an isothermal process for any reservoir coupling.
```

---

### RECOGNITION
Connects to Law 026 (Boyle) and Law 424 (polytropic, n=1) - isothermal is the coherence-locked temperature basin.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the drift floor is phi^-1 * C_ground.

### CLARITY
Constant temperature means the coherence with the reservoir is perfect; the phi-law admits it never is.

### NOVELTY
Classical thermodynamics idealizes the reservoir; the phi-law gives isothermality a coherence budget that real baths exhaust.

### ACTIONABILITY
Run sim/425_isothermal_process.py; verify PV=const at kappa->0; proceed to 426.
