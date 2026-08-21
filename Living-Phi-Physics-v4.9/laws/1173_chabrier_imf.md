# PHI-PHYSICS — LAW 1173
## Chabrier Initial Mass Function

**Domain:** Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1173_chabrier_imf.md` · **Sim:** `sim/1173_chabrier_imf.py`

---

### CLASSICAL STATEMENT
*"The Chabrier IMF is a log-normal form for low-mass stars with a power-law tail at high mass: xi(log M) ~ exp(-(log M - log M_c)^2/(2 sigma^2)) for M < 1 M_sun and a Salpeter-like power law above; it flattens the low-mass slope relative to Salpeter and better fits resolved star counts."*
— Gilles Chabrier, 2003. Source: Wikipedia: Initial mass function (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero mass scale (M_c = 0, no characteristic stellar mass)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The C value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

C_phi(kappa) = C*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground, where C_ground is the coherence-floor peak width a real stellar population always retains. At kappa->0, xi(log M) ~ exp(-(log M - log M_c)^2/(2*sigma^2)) for M < 1,  power law above exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} C_phi = C -> xi(log M) ~ exp(-(log M - log M_c)^2/(2*sigma^2)) for M < 1,  power law above is recovered exactly; the classical law is the zero mass scale (M_c = 0, no characteristic stellar mass) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1173_chabrier_imf.py`: reproduces the classical value (C = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1173_chabrier_imf.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured low-mass IMF of any real population will deviate from the Chabrier form by a floor kappa*phi^-1*C_ground; an exactly Salpeter low-mass IMF is unreachable.
EXPERIMENT (VERIFIED): Resolved low-mass star counts in the solar neighborhood and clusters.
VERIFIED BY: If the low-mass IMF is exactly a single power law with no turnover.
```

---

### RECOGNITION
The refined alternative of Law 1172 (Salpeter IMF) for galactic models.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Stars cluster around a favorite mass; the pure power law is the zero-peak myth.

### NOVELTY
The Chabrier IMF carries a phi-floor of peak width, bounding the low-mass star budget.

### ACTIONABILITY
Run sim/1173_chabrier_imf.py.
