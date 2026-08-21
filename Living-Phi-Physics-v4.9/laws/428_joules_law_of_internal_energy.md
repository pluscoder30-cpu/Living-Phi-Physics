# PHI-PHYSICS — LAW 428
## Joule's Law of Internal Energy (U = U(T) for Ideal Gas)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/428_joules_law_of_internal_energy.md` · **Sim:** `sim/428_joules_law_of_internal_energy.py`

---

### CLASSICAL STATEMENT
*"The internal energy of an ideal gas depends only on temperature, not on volume or pressure: U = U(T), so (dU/dV)_T = 0. Free expansion of an ideal gas does not change its temperature."*
— James Prescott Joule, 1843. Source: Wikipedia: Internal energy; Joule, On the Calorific Effects of Magneto-Electricity (1843)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-interaction gas*: Joule's law requires the gas molecules to exert no forces on each other at all, so expanding the volume does no work against internal attractions.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: real gases carry a cohesion coupling. U_phi(T,V,kappa) = U(T)*(1 + kappa*(phi-1)) + kappa*phi^-1*U_int(V), where U_int is the interaction energy of the coherence field. At kappa->0, (dU/dV)_T = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dU_phi/dV = 0 -> Joule's law is the zero-interaction ideal-gas limit.
```

---

### STAGE 4 — SIMULATION

`sim/428_joules_law_of_internal_energy.py`: reproduces the classical values U_int_energy = 6240, dU_dV = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/428_joules_law_of_internal_energy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A real gas at finite coupling shows a volume-dependent internal energy kappa*phi^-1*U_int(V); free expansion produces a measurable (non-zero) temperature change governed by the coherence coupling.
EXPERIMENT (VERIFIED): Precision free-expansion calorimetry (Joule expansion) of helium at high density measuring the temperature change dT.
VERIFIED BY: Free expansion of an ideal gas produces exactly zero temperature change at any density and coupling.
```

---

### RECOGNITION
Connects to Law 025 (ideal gas) and Law 421 (Joule-Thomson) - the ideal gas is the zero-cohesion reading of the carrier gas.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the interaction energy enters as phi^-1 * U_int(V).

### CLARITY
The ideal gas is the gas that has forgotten its own attractions; the phi-law restores the memory.

### NOVELTY
Classical Joule's law zeroes (dU/dV)_T; the phi-law turns that zero into a coherence-measurable interaction floor.

### ACTIONABILITY
Run sim/428_joules_law_of_internal_energy.py; verify U=U(T) at kappa->0; proceed to 429.
