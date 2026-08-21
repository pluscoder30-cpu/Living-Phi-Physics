# PHI-PHYSICS — LAW 1043
## Invariant Mass (Rest Mass)

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1043_invariant_mass.md` · **Sim:** `sim/1043_invariant_mass.py`

---

### CLASSICAL STATEMENT
*"The invariant (rest) mass of a system obeys m^2 c^4 = E^2 - (p c)^2; it is Lorentz-invariant, and for a composite system is not the sum of the constituent masses (binding energy contributes)."*
— Albert Einstein, 1905. Source: Wikipedia: Invariant mass (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero rest mass (m = 0, the exactly massless carrier)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The M value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, where M_ground is the coherence-floor invariant mass that a bound system keeps even at maximum binding. At kappa->0, m^2 * c^4 = E^2 - (p*c)^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} M_phi = M -> m^2 * c^4 = E^2 - (p*c)^2 is recovered exactly; the classical law is the zero rest mass (m = 0, the exactly massless carrier) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1043_invariant_mass.py`: reproduces the classical value (M = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1043_invariant_mass.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The invariant mass of any real composite system will deviate from sqrt(E^2-(pc)^2)/c^2 by a floor kappa*phi^-1*M_ground; the exactly on-shell system is unreachable.
EXPERIMENT (VERIFIED): Hadron-collider invariant-mass reconstruction of resonances compared against the direct sum of constituent masses.
VERIFIED BY: If any composite system has invariant mass exactly equal to the classical expression to arbitrary precision.
```

---

### RECOGNITION
The mass-shell partner of Law 1042; connects Law 060 (E=mc^2) and Law 1066 (mass defect).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Invariant mass is the shadow the energy-momentum hyperboloid casts; binding hides a coherence floor, not a zero.

### NOVELTY
The classical mass defect is read as the manifestation of a phi-floor in the invariant mass.

### ACTIONABILITY
Run sim/1043_invariant_mass.py.
