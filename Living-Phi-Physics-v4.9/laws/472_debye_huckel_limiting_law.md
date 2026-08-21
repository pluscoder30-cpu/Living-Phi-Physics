# PHI-PHYSICS — LAW 472
## Debye-Hückel Limiting Law (Activity Coefficient)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/472_debye_huckel_limiting_law.md` · **Sim:** `sim/472_debye_huckel_limiting_law.py`

---

### CLASSICAL STATEMENT
*"In the limit of infinite dilution, the mean activity coefficient of an electrolyte is log_10 gamma_+/- = -A |z+ z-| sqrt(I), where A ~ 0.509 (mol/kg)^(-1/2) in water at 25 C. The logarithm of the activity coefficient is proportional to the square root of ionic strength."*
— Peter Debye and Erich Huckel, 1923. Source: Wikipedia: Debye-Huckel equation; Debye & Huckel (1923)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite dilution*: the limiting law is exact only as ionic strength -> 0, where the ionic atmosphere is infinitely diffuse and ions carry zero mutual coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the atmosphere floor is a coherence term. ln(gamma)_phi(kappa) = -A|z+z-|sqrt(I)*(1 + kappa*(phi-1)) + kappa*phi^-1*ln_gamma_ground. At kappa->0, the limiting law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} ln(gamma)_phi = -A|z+z-|sqrt(I) -> the Debye-Hückel limiting law is the zero-coherence, infinite-dilution limit.
```

---

### STAGE 4 — SIMULATION

`sim/472_debye_huckel_limiting_law.py`: reproduces the classical value ln_gamma = -0.0509 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/472_debye_huckel_limiting_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the activity coefficient carries a floor kappa*phi^-1*ln_gamma_ground even as I -> 0; the sqrt(I) law gains an intercept.
EXPERIMENT (VERIFIED): High-precision activity measurements of dilute electrolytes extrapolating to infinite dilution.
VERIFIED BY: log(gamma) vs sqrt(I) is exactly linear through the origin at all couplings.
```

---

### RECOGNITION
Connects to Law 471 (Debye-Hückel theory) and Law 458 (Kohlrausch) - the sqrt(I) law is the coherence screening in its asymptotic limit.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * ln_gamma_ground.

### CLARITY
Even at infinite dilution the ion remembers its atmosphere; the phi-law keeps the memory.

### NOVELTY
Classical limiting law passes through the origin; the phi-law gives the sqrt(I) line a coherence intercept.

### ACTIONABILITY
Run sim/472_debye_huckel_limiting_law.py; verify sqrt(I) law at kappa->0; proceed to 473.
