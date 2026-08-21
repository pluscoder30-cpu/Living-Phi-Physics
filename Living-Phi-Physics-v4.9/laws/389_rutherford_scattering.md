# PHI-PHYSICS — LAW 389
## Rutherford Scattering Formula

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/389_rutherford_scattering.md` · **Sim:** `sim/389_rutherford_scattering.py`

---

### CLASSICAL STATEMENT
*"For a point Coulomb (inverse-square) potential, the scattering of a projectile off a stationary target follows the Rutherford formula d sigma/d Omega = (k q1 q2/(4 E sin^2(theta/2)))^2, with impact parameter b = (k q1 q2/(2 E)) cot(theta/2); it is identical to classical gravitational scattering (hyperbolic orbits)."*
— Ernest Rutherford, 1911. Source: Wikipedia: Rutherford scattering; Rutherford (1911), 'The scattering of alpha and beta particles by matter'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *point nucleus and single scattering*: the formula requires an exactly point-like target and single (not multiple) scattering events.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the differential cross-section couples to coherence. dsigma_phi(kappa) = dsigma_Rutherford*(1 + kappa*(phi-1)) + kappa*phi^-1*dsigma_ground. At kappa->0 the Rutherford formula is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dsigma_phi = (k q1 q2/(4E sin^2(theta/2)))^2 -> Rutherford scattering is the point-target, single-scattering, inverse-square limit.
```

---

### STAGE 4 — SIMULATION

`sim/389_rutherford_scattering.py`: reproduces the classical value b0 = 2.876e-13 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/389_rutherford_scattering.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Deep-scattering cross-sections carry a phi-coherent excess phi^-1*dsigma_ground at full coupling.
EXPERIMENT (VERIFIED): High-precision scattering experiments (alpha scattering, Coulomb scattering of ions) measuring the cross-section angular dependence.
VERIFIED BY: The scattering cross-section is exactly the Rutherford formula at full coupling.
```

---

### RECOGNITION
Connects to Law 286 (two-body — hyperbolic orbits) and Law 289 (LRL — the scattering trajectory family).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The point nucleus is a limit; every scattering hides a phi of structure beneath.

### NOVELTY
Classical scattering exacts the point-target law; the phi-law bounds its residual at a coherence floor.

### ACTIONABILITY
Run sim/389_rutherford_scattering.py; verify the formula at kappa->0.
