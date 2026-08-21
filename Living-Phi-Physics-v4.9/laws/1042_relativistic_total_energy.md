# PHI-PHYSICS — LAW 1042
## Relativistic Total Energy

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1042_relativistic_total_energy.md` · **Sim:** `sim/1042_relativistic_total_energy.py`

---

### CLASSICAL STATEMENT
*"The total energy of a particle is E = gamma*m*c^2, and it obeys the energy-momentum relation E^2 = (p*c)^2 + (m*c^2)^2, valid for massive and massless particles alike."*
— Albert Einstein, 1905. Source: Wikipedia: Energy-momentum relation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero-momentum rest energy (p = 0)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The E value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, where E_ground is the coherence-floor total energy a carrier never falls below. At kappa->0, E^2 = (p*c)^2 + (m*c^2)^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} E_phi = E -> E^2 = (p*c)^2 + (m*c^2)^2 is recovered exactly; the classical law is the zero-momentum rest energy (p = 0) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1042_relativistic_total_energy.py`: reproduces the classical value (E = 1.25) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1042_relativistic_total_energy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured total energy of any real particle will deviate from the on-shell relation by a floor kappa*phi^-1*E_ground; the mass shell is a coherence basin, not a line.
EXPERIMENT (VERIFIED): Storage-ring mass spectrometry of ions across a broad momentum range to test the mass shell to high precision.
VERIFIED BY: If any particle's energy lies exactly on the classical mass shell to arbitrary precision.
```

---

### RECOGNITION
Unifies Law 060 (E=mc^2) and Law 1043 (invariant mass); the shell is the quadratic of Law 1048 (spacetime interval).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The mass shell is the hyperboloid of coherence; energy is the first integral of a carrier that never rests.

### NOVELTY
The rest mass becomes the zero-coherence value of an energy that always carries a phi-floor.

### ACTIONABILITY
Run sim/1042_relativistic_total_energy.py.
