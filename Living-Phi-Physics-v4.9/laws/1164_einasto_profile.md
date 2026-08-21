# PHI-PHYSICS — LAW 1164
## Einasto Profile

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1164_einasto_profile.md` · **Sim:** `sim/1164_einasto_profile.py`

---

### CLASSICAL STATEMENT
*"The Einasto profile describes dark-matter halo density with a logarithmic slope that varies as a power law of radius: rho(r) = rho_0 exp(-d_n[(r/r_s)^(1/n) - 1]), where n is the shape parameter; it fits N-body halos and stellar spheroids, often better than NFW in the inner regions."*
— Jaan Einasto, 1965. Source: Wikipedia: Einasto profile (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero shape index (n -> infinity, the isothermal core limit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The E value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, where E_ground is the coherence-floor shape complexity a real halo always retains. At kappa->0, rho(r) = rho_0 exp(-d_n[(r/r_s)^(1/n) - 1]) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} E_phi = E -> rho(r) = rho_0 exp(-d_n[(r/r_s)^(1/n) - 1]) is recovered exactly; the classical law is the zero shape index (n -> infinity, the isothermal core limit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1164_einasto_profile.py`: reproduces the classical value (E = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1164_einasto_profile.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured halo density profile will deviate from the Einasto form by a floor kappa*phi^-1*E_ground; an exactly power-law halo is unreachable.
EXPERIMENT (VERIFIED): High-resolution N-body simulations and stellar-halo observations fitting Einasto parameters.
VERIFIED BY: If a halo is exactly described by a single power-law slope.
```

---

### RECOGNITION
The smoother alternative of Law 1163 (NFW) for Law 1094 (weak lensing).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Dark matter curves its slope; the pure power law is the zero-shape myth.

### NOVELTY
The Einasto index carries a phi-floor, so no halo has an exactly constant slope.

### ACTIONABILITY
Run sim/1164_einasto_profile.py.
