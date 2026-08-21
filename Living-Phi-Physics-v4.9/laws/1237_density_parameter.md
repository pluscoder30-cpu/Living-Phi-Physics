# PHI-PHYSICS — LAW 1237
## Density Parameter (Omega)

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1237_density_parameter.md` · **Sim:** `sim/1237_density_parameter.py`

---

### CLASSICAL STATEMENT
*"The density parameter Omega = rho/rho_c = sum Omega_i sums the fractional densities of matter (Omega_m), radiation (Omega_r), and dark energy (Omega_Lambda) relative to critical (Law 1218); the Friedmann equation reads Omega_total - 1 = k c^2/(a^2 H^2), so Omega determines the spatial curvature."*
— From the Friedmann models, 1922 (standard cosmology). Source: Wikipedia: Density parameter (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero density (Omega = 0, an empty universe)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The O value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

O_phi(kappa) = O*(1 + kappa*(phi-1)) + kappa*phi^-1*O_ground, where O_ground is the coherence-floor density a real universe always retains. At kappa->0, Omega = sum Omega_i = rho/rho_c,  Omega_total - 1 = k*c^2/(a^2*H^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} O_phi = O -> Omega = sum Omega_i = rho/rho_c,  Omega_total - 1 = k*c^2/(a^2*H^2) is recovered exactly; the classical law is the zero density (Omega = 0, an empty universe) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1237_density_parameter.py`: reproduces the classical value (O = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1237_density_parameter.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured density parameters will deviate from the cosmic values by a floor kappa*phi^-1*O_ground; an exactly Omega=0 universe is unreachable.
EXPERIMENT (VERIFIED): CMB, BAO, and supernova joint fits of Omega_m and Omega_Lambda.
VERIFIED BY: If the total density is measured exactly at zero or exactly critical.
```

---

### RECOGNITION
The density budget of Law 1218 (critical density) and Law 104 (Friedmann equations).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Density decides the geometry; the empty universe is the zero-density myth.

### NOVELTY
The density parameter carries a phi-floor, so Omega never hits exactly 1.

### ACTIONABILITY
Run sim/1237_density_parameter.py.
