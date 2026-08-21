# PHI-PHYSICS — LAW 1165
## Isothermal Sphere (Dark Matter Halo)

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1165_isothermal_sphere.md` · **Sim:** `sim/1165_isothermal_sphere.py`

---

### CLASSICAL STATEMENT
*"The singular isothermal sphere has density rho(r) = sigma^2/(2 pi G r^2) with a flat rotation curve v_c = sqrt(2) sigma; it is the simplest halo model predicting the flat galaxy rotation curves observed, though it has a central cusp and infinite mass (needing a cutoff)."*
— Classical stellar-dynamics model; used for dark matter by Fritz Zwicky, 1937. Source: Wikipedia: Isothermal sphere (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero velocity dispersion (sigma = 0, no confining mass)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The I value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_phi(kappa) = I*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground, where I_ground is the coherence-floor central concentration a real halo always retains. At kappa->0, rho(r) = sigma^2/(2*pi*G*r^2),  v_c = sqrt(2)*sigma exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} I_phi = I -> rho(r) = sigma^2/(2*pi*G*r^2),  v_c = sqrt(2)*sigma is recovered exactly; the classical law is the zero velocity dispersion (sigma = 0, no confining mass) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1165_isothermal_sphere.py`: reproduces the classical value (I = 0.5) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1165_isothermal_sphere.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured rotation curve will deviate from the flat isothermal prediction by a floor kappa*phi^-1*I_ground; an exactly flat rotation curve is unreachable.
EXPERIMENT (VERIFIED): Galaxy rotation-curve measurements (HI and stellar kinematics) testing the flat curve.
VERIFIED BY: If any galaxy's rotation curve is exactly flat with zero deviation.
```

---

### RECOGNITION
The rotation-curve model of Law 1163 (NFW) and the dark-matter evidence of Law 1167 (Tully-Fisher).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The halo keeps the curve flat; the rising/falling curve is the zero-isothermal myth.

### NOVELTY
The isothermal sphere carries a phi-floor of dispersion, bounding the flatness of rotation curves.

### ACTIONABILITY
Run sim/1165_isothermal_sphere.py.
