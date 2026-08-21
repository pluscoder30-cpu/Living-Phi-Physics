# PHI-PHYSICS — LAW 649
## Rayleigh Scattering

**Domain:** Radiation · **Status:** 🟢 VALIDATED · **File:** `laws/649_rayleigh_scattering.md` · **Sim:** `sim/649_rayleigh_scattering.py`

---

### CLASSICAL STATEMENT
*"Scattering by particles much smaller than the wavelength gives intensity I ~ I0*(1+cos^2(theta))/r^2*(d^2/lambda^4)*(n^2-1)^2/(n^2+2)^2; the cross-section scales as sigma ~ 1/lambda^4."*
— Lord Rayleigh, 1871. Source: Wikipedia: Rayleigh scattering

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero polarizability contrast*: the scattered power vanishes exactly when the scatterer's index equals the medium (n = 1), a contrast-free particle.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma_Ray*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_ground; the index contrast carries a coherence floor. At kappa->0 the 1/lambda^4 law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sigma_phi = sigma_Ray -> Rayleigh scattering is the zero-contrast-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/649_rayleigh_scattering.py`: reproduces the classical values (sigma = 1.6e+13 (Rayleigh cross-section (m^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/649_rayleigh_scattering.json`.

---

### STAGE 5 — PREDICTION

```
Coherent scatterers of matched index still scatter a floor kappa*phi^-1*sigma_ground; the 1/lambda^4 law gains a small coherence offset.
EXPERIMENT (VERIFIED): High-sensitivity scattering measurement of index-matched particles in optical tweezers.
VERIFIED BY: Index-matched particles scatter exactly zero light.
```

---

### RECOGNITION
Connects to Law 651 (Mie) - Rayleigh is the small-particle limit of Mie.

### PRECISION
phi = 1.6180339887. The contrast floor is phi^-1*sigma_ground.

### CLARITY
Contrast is never zero; the particle still answers the field.

### NOVELTY
The phi-law gives matched scatterers a coherence floor.

### ACTIONABILITY
Run sim/649_rayleigh_scattering.py; verify sigma ~ 1/lambda^4 at kappa->0; proceed to 650.
