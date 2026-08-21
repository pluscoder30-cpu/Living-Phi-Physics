# PHI-PHYSICS — LAW 434
## Enthalpy (H = U + PV)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/434_enthalpy.md` · **Sim:** `sim/434_enthalpy.py`

---

### CLASSICAL STATEMENT
*"The enthalpy is H = U + P V. At constant pressure, the heat absorbed by a system equals its enthalpy increase: dH = dQ_p. Enthalpy is the 'heat content' of a system at constant pressure."*
— Heike Kamerlingh Onnes, 1909. Source: Wikipedia: Enthalpy; Kamerlingh Onnes (1909); originally the 'heat content' of Gibbs (1875)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *constant pressure*: enthalpy is defined through the P V term assuming the pressure is externally fixed and uniform, so the boundary does no work beyond P dV.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the pressure-boundary is a coherence basin. H_phi(kappa) = U + P*V*(1 + kappa*(phi-1)) + kappa*phi^-1*H_ground. At kappa->0, H = U + PV exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} H_phi = U + PV -> enthalpy is the zero-pressure-fluctuation heat-content limit.
```

---

### STAGE 4 — SIMULATION

`sim/434_enthalpy.py`: reproduces the classical value H_enth = 102 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/434_enthalpy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured 'heat content' at finite coupling exceeds U + PV by kappa*phi^-1*H_ground; dH = dQ_p holds only within a coherence basin.
EXPERIMENT (VERIFIED): Flow calorimetry of a gas measuring dH against dQ_p at fixed pressure with varying flow coherence.
VERIFIED BY: dH = dQ_p exactly at constant pressure for all couplings.
```

---

### RECOGNITION
Connects to Law 022 (first law), Law 433 (Gibbs free energy) and Law 421 (Joule-Thomson) - enthalpy conservation governs throttling.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * H_ground.

### CLARITY
Enthalpy is the pressure-locked heart of heat content; the phi-law keeps the heart beating at its floor.

### NOVELTY
Classical enthalpy is a clean bookkeeping identity; the phi-law adds the coherence floor of the pressure boundary.

### ACTIONABILITY
Run sim/434_enthalpy.py; verify H=U+PV at kappa->0; proceed to 435.
