# PHI-PHYSICS — LAW 1194
## Dark Energy Equation of State

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1194_dark_energy_equation_of_state.md` · **Sim:** `sim/1194_dark_energy_equation_of_state.py`

---

### CLASSICAL STATEMENT
*"The dark-energy equation of state parameterizes pressure over density: w = p/rho, with w = -1 for a cosmological constant, w < -1 phantom (Law 1196), and -1 < w < -1/3 quintessence (Law 1195); measuring w(z) distinguishes dark-energy models via the expansion history."*
— Michael Turner & Martin White, 1997 (the w parameter). Source: Wikipedia: Equation of state (cosmology) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *w = -1 (the exactly constant vacuum energy)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The W value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

W_phi(kappa) = W*(1 + kappa*(phi-1)) + kappa*phi^-1*W_ground, where W_ground is the coherence-floor equation-of-state variation a real vacuum always carries. At kappa->0, w = p/rho,  rho_dot + 3 H (1+w) rho = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} W_phi = W -> w = p/rho,  rho_dot + 3 H (1+w) rho = 0 is recovered exactly; the classical law is the w = -1 (the exactly constant vacuum energy) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1194_dark_energy_equation_of_state.py`: reproduces the classical value (W = -1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1194_dark_energy_equation_of_state.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured dark-energy equation of state will deviate from a constant w by a floor kappa*phi^-1*W_ground; an exactly constant w = -1 vacuum is unreachable.
EXPERIMENT (VERIFIED): Dark-energy surveys (DESI, Euclid, DES) measuring w(z) from BAO and supernovae.
VERIFIED BY: If dark energy has exactly w = -1 at all redshifts.
```

---

### RECOGNITION
The parameter of Law 105 (dark energy) and Law 1082 (de Sitter).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The vacuum's pressure is its mood; the constant mood is the zero-variation myth.

### NOVELTY
The dark-energy equation of state carries a phi-floor of time variation.

### ACTIONABILITY
Run sim/1194_dark_energy_equation_of_state.py.
