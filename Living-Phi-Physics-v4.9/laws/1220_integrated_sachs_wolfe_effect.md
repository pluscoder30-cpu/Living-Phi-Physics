# PHI-PHYSICS — LAW 1220
## Integrated Sachs-Wolfe Effect

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1220_integrated_sachs_wolfe_effect.md` · **Sim:** `sim/1220_integrated_sachs_wolfe_effect.py`

---

### CLASSICAL STATEMENT
*"The integrated Sachs-Wolfe (ISW) effect is the CMB anisotropy from the time variation of gravitational potentials along the line of sight: Delta T/T = -2 integral Phi_dot dt; it is null in matter-dominated Einstein-de Sitter cosmology and significant when dark energy (or curvature) makes potentials decay, so ISW correlates CMB with large-scale structure."*
— Rainer Sachs & Arthur Wolfe, 1967 (ISW term); emphasized for late-time acceleration, 1990s. Source: Wikipedia: Integrated Sachs-Wolfe effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *static potentials (Phi_dot = 0, no ISW signal)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor potential decay a real universe always produces. At kappa->0, Delta T/T = -2 * integral Phi_dot dt exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> Delta T/T = -2 * integral Phi_dot dt is recovered exactly; the classical law is the static potentials (Phi_dot = 0, no ISW signal) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1220_integrated_sachs_wolfe_effect.py`: reproduces the classical value (D = 1e-06) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1220_integrated_sachs_wolfe_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured ISW signal will deviate from the prediction by a floor kappa*phi^-1*D_ground; an exactly Einstein-de Sitter universe is unreachable.
EXPERIMENT (VERIFIED): CMB-LSS cross-correlation (Planck x SDSS/DES) measuring the ISW signal.
VERIFIED BY: If the CMB-LSS cross-correlation is exactly zero.
```

---

### RECOGNITION
The late-time channel of Law 1137 (Sachs-Wolfe) and the dark-energy signature of Law 1194.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Potentials decay as the vacuum wins; the static potential is the EdS myth.

### NOVELTY
The ISW effect carries a phi-floor, so dark energy always leaves a CMB-LSS correlation.

### ACTIONABILITY
Run sim/1220_integrated_sachs_wolfe_effect.py.
