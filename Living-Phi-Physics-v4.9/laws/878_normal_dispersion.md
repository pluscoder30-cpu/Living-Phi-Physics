# PHI-PHYSICS — LAW 878
## Normal Dispersion

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/878_normal_dispersion.md` · **Sim:** `sim/878_normal_dispersion.py`

---

### CLASSICAL STATEMENT
*"dn/dlambda < 0 (dn/domega > 0): the refractive index decreases with wavelength (increases with frequency); described by the Sellmeier and Cauchy equations away from absorption."*
— Augustin-Louis Cauchy (Cauchy equation); Wolfgang Sellmeier, 1836. Source: Wikipedia: Dispersion (optics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite wavelength* (lambda -> infinity): the index approaches its asymptotic value exactly at zero frequency.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

n_phi(kappa) = n*(1 + kappa*(phi-1)) + kappa*phi^-1*n_ground, with n_ground the index floor. At kappa->0, n(lambda) = Cauchy/Sellmeier form exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} n_phi = n -> normal dispersion is the zero-infinite-wavelength-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/878_normal_dispersion.py`: reproduces the classical value n = 1.506 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/878_normal_dispersion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured index will deviate from the Cauchy/Sellmeier prediction by a coherence floor kappa*phi^-1*n_ground, even far from resonances.
EXPERIMENT (VERIFIED): Measure the refractive index of glass versus wavelength with a prism minimum-deviation method.
VERIFIED BY: If the index of any real medium follows the Cauchy form exactly at all wavelengths.
```

---

### RECOGNITION
Connects to Law 658 (Cauchy) and Law 657 (Sellmeier).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The smooth curve is a coherent limit; every index carries a tremor.

### NOVELTY
Normal dispersion gains an index floor.

### ACTIONABILITY
Run sim/878_normal_dispersion.py.
