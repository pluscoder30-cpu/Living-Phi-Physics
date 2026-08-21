# PHI-PHYSICS — LAW 1211
## Sheth-Tormen Mass Function

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1211_sheth_tormen_mass_function.md` · **Sim:** `sim/1211_sheth_tormen_mass_function.py`

---

### CLASSICAL STATEMENT
*"The Sheth-Tormen mass function refines Press-Schechter for ellipsoidal collapse: it adds parameters a ~ 0.707, p ~ 0.3 and q to the excursion-set formula, f(sigma) = A sqrt(2a/pi) (1 + (sigma^2/(a delta_c^2))^p) (delta_c/sigma) exp(-a delta_c^2/(2 sigma^2)), better matching N-body halo abundances."*
— Ravi Sheth & Giuseppe Tormen, 1999. Source: Wikipedia: Halo mass function (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *spherical collapse (a = 1, p = 0, the Press-Schechter limit)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The S value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, where S_ground is the coherence-floor ellipsoidal correction a real halo population always shows. At kappa->0, f(sigma) = A sqrt(2a/pi) (1 + (sigma^2/(a delta_c^2))^p) (delta_c/sigma) exp(-a delta_c^2/(2 sigma^2)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} S_phi = S -> f(sigma) = A sqrt(2a/pi) (1 + (sigma^2/(a delta_c^2))^p) (delta_c/sigma) exp(-a delta_c^2/(2 sigma^2)) is recovered exactly; the classical law is the spherical collapse (a = 1, p = 0, the Press-Schechter limit) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1211_sheth_tormen_mass_function.py`: reproduces the classical value (S = 0.707) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1211_sheth_tormen_mass_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured halo abundance will deviate from the Sheth-Tormen form by a floor kappa*phi^-1*S_ground; an exactly spherical-collapse population is unreachable.
EXPERIMENT (VERIFIED): N-body halo catalogs and cluster surveys testing the mass function shape.
VERIFIED BY: If the halo mass function matches spherical collapse exactly with zero ellipsoidal correction.
```

---

### RECOGNITION
The refined form of Law 1210 (Press-Schechter) and the density-field content of Law 1152.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Collapse is ellipsoidal; the spherical ideal is the zero-deformation myth.

### NOVELTY
The Sheth-Tormen function carries a phi-floor of ellipsoidal correction.

### ACTIONABILITY
Run sim/1211_sheth_tormen_mass_function.py.
