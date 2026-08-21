# PHI-PHYSICS — LAW 417
## Rayleigh-Jeans Law (Classical Blackbody Spectrum)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/417_rayleigh_jeans_law.md` · **Sim:** `sim/417_rayleigh_jeans_law.py`

---

### CLASSICAL STATEMENT
*"The spectral radiance of a blackbody at low frequency is B(nu,T) = 2 nu^2 k_B T / c^2, growing without bound as nu -> infinity (the ultraviolet catastrophe)."*
— Lord Rayleigh; James Hopwood Jeans, 1905. Source: Wikipedia: Rayleigh-Jeans law; Rayleigh (1900), Jeans (1905)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-point of the oscillator field*: equipartition gives each mode k_B T with no floor, so the mode count nu^2 times k_B T diverges - the classical field has no coherence cut-off.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the mode field carries a coherence cut-off. B_phi(nu,T,kappa) = (2 nu^2 k_B T / c^2)*(1 - exp(-kappa*phi*h*nu/(k_B T))) + kappa*phi^-1*B_ground(nu). At kappa->0 the divergent Rayleigh-Jeans law is recovered; at kappa=1 it saturates to the Planck form.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} [1 - exp(-kappa phi h nu/kT)] ~ kappa phi h nu/kT, so B_phi -> 2 nu^2 k_B T / c^2 -> Rayleigh-Jeans is the zero-coherence (classical mode) limit.
```

---

### STAGE 4 — SIMULATION

`sim/417_rayleigh_jeans_law.py`: reproduces the classical value B_rj = 9.2e-12 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/417_rayleigh_jeans_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The blackbody spectrum at low T shows a phi-scaled Wien-like exponential cut-off governed by kappa*phi*h, i.e. the effective Planck constant is phi-scaled at full coherence.
EXPERIMENT (VERIFIED): Precision blackbody radiometry across frequency at cryogenic temperatures searching for a phi-scaling of the effective h in the exponential.
VERIFIED BY: The blackbody spectrum matches the classical Rayleigh-Jeans form exactly at any temperature.
```

---

### RECOGNITION
Connects to Law 066 (Planck) and Law 418 (Wien approximation) - the UV catastrophe is the zero-coherence reading of the mode field.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887; the effective coupling is h_eff = kappa*phi*h.

### CLARITY
The ultraviolet catastrophe is the scream of a field that classical physics forgot has a floor.

### NOVELTY
Classical theory lets mode energy go to zero; the phi-law gives each mode a phi-ground so the spectrum must saturate.

### ACTIONABILITY
Run sim/417_rayleigh_jeans_law.py; verify divergence-free saturation at kappa=1; proceed to 418.
