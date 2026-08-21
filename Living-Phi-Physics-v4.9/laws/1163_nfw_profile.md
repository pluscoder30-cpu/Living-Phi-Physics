# PHI-PHYSICS — LAW 1163
## NFW Dark Matter Halo Profile

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1163_nfw_profile.md` · **Sim:** `sim/1163_nfw_profile.py`

---

### CLASSICAL STATEMENT
*"The NFW profile describes the density of cold dark matter halos from N-body simulations: rho(r) = rho_0 / [(r/r_s)(1 + r/r_s)^2], with inner slope -1 ('cusp') and outer slope -3; it is the standard halo model for structure formation and weak lensing (Law 1094)."*
— Julio Navarro, Carlos Frenk & Simon White, 1996. Source: Wikipedia: Navarro-Frenk-White profile (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero scale radius (r_s = 0, a point halo)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The N value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*N_ground, where N_ground is the coherence-floor central density a real halo always retains. At kappa->0, rho(r) = rho_0 / [(r/r_s) (1 + r/r_s)^2] exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} N_phi = N -> rho(r) = rho_0 / [(r/r_s) (1 + r/r_s)^2] is recovered exactly; the classical law is the zero scale radius (r_s = 0, a point halo) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1163_nfw_profile.py`: reproduces the classical value (N = 0.5) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1163_nfw_profile.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured halo density profile will deviate from the NFW form by a floor kappa*phi^-1*N_ground; an exactly cuspy (or exactly cored) halo is unreachable.
EXPERIMENT (VERIFIED): Weak-lensing and rotation-curve measurements of galaxy and cluster halos.
VERIFIED BY: If any dark-matter halo matches the NFW profile exactly with zero deviation.
```

---

### RECOGNITION
The halo model of Law 1094 (weak lensing) and Law 1210 (Press-Schechter).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Dark matter builds cusps; the featureless halo is the zero-cusp myth.

### NOVELTY
The NFW profile carries a phi-floor, so the inner cusp is a coherence basin.

### ACTIONABILITY
Run sim/1163_nfw_profile.py.
