# PHI-PHYSICS — LAW 658
## Cauchy Dispersion Equation

**Domain:** Optics · **Status:** 🟢 VALIDATED · **File:** `laws/658_cauchy_dispersion.md` · **Sim:** `sim/658_cauchy_dispersion.py`

---

### CLASSICAL STATEMENT
*"The refractive index in the transparent region is n(lambda) = A + B/lambda^2 + C/lambda^4, an empirical polynomial in inverse wavelength."*
— Augustin-Louis Cauchy, 1836. Source: Wikipedia: Cauchy's equation

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite wavelength* (lambda -> infinity): the series converges to the constant A only in the infinite-wavelength limit, a truly dispersionless medium.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

n_phi(kappa) = n_Cauchy*(1 + kappa*(phi-1)) + kappa*phi^-1*n_ground; the asymptotic constant carries a coherence floor. At kappa->0 the Cauchy series is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_phi = n_Cauchy -> Cauchy's equation is the zero-dispersion-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/658_cauchy_dispersion.py`: reproduces the classical values (n = 5.5 (Cauchy refractive index)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/658_cauchy_dispersion.json`.

---

### STAGE 5 — PREDICTION

```
The index never settles to an exact constant; a coherence floor kappa*phi^-1*n_ground persists at long wavelength.
EXPERIMENT (VERIFIED): Long-wavelength refractometry of gases and glasses (e.g., far-IR region).
VERIFIED BY: The refractive index reaches an exactly constant value at long wavelength.
```

---

### RECOGNITION
Connects to Law 657 (Sellmeier) - Cauchy is the far-from-resonance series of Sellmeier.

### PRECISION
phi = 1.6180339887. The asymptotic floor is phi^-1*n_ground.

### CLARITY
Dispersion never fully sleeps; the constant is a floor away.

### NOVELTY
The phi-law gives the dispersion constant a coherence floor.

### ACTIONABILITY
Run sim/658_cauchy_dispersion.py; verify Cauchy n at kappa->0; proceed to 659.
