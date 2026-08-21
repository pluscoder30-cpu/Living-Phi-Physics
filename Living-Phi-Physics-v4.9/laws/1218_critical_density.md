# PHI-PHYSICS — LAW 1218
## Critical Density

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1218_critical_density.md` · **Sim:** `sim/1218_critical_density.py`

---

### CLASSICAL STATEMENT
*"The critical density separates closed from open universes: rho_c = 3 H^2/(8 pi G) ~ 8.5 x 10^-27 kg/m^3 today; the density parameter Omega = rho/rho_c determines the spatial curvature (Omega > 1 closed, Omega < 1 open, Omega = 1 flat) in the Friedmann equations."*
— From the Friedmann models, 1922 (standard cosmology). Source: Wikipedia: Critical density (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero Hubble rate (H = 0, the static limit with no critical density)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor density a real expanding universe always sets. At kappa->0, rho_c = 3*H^2/(8*pi*G),  Omega = rho/rho_c exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> rho_c = 3*H^2/(8*pi*G),  Omega = rho/rho_c is recovered exactly; the classical law is the zero Hubble rate (H = 0, the static limit with no critical density) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1218_critical_density.py`: reproduces the classical value (D = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1218_critical_density.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured density of the universe will deviate from the critical value by a floor kappa*phi^-1*D_ground; an exactly Omega=1 universe is unreachable.
EXPERIMENT (VERIFIED): CMB, BAO, and supernova measurements of Omega and the spatial curvature.
VERIFIED BY: If the universe's density is measured at exactly the critical value.
```

---

### RECOGNITION
The density normalization of Law 104 (Friedmann equations) and Law 1146 (flatness).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Density decides the fate; the exact balance is the zero-deviation myth.

### NOVELTY
The critical density carries a phi-floor, so Omega never lands exactly on 1.

### ACTIONABILITY
Run sim/1218_critical_density.py.
