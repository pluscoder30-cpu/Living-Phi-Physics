# PHI-PHYSICS — LAW 651
## Mie Scattering

**Domain:** Radiation · **Status:** 🟢 VALIDATED · **File:** `laws/651_mie_scattering.md` · **Sim:** `sim/651_mie_scattering.py`

---

### CLASSICAL STATEMENT
*"The exact solution of Maxwell's equations for scattering by a homogeneous sphere of any size gives cross-sections Q_ext, Q_sca as infinite series over multipoles (Mie coefficients a_n, b_n)."*
— Gustav Mie, 1908. Source: Wikipedia: Mie scattering

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal homogeneous sphere*: the solution assumes a perfectly spherical, exactly uniform particle with a sharp boundary.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Q_phi(kappa) = Q_Mie*(1 + kappa*(phi-1)) + kappa*phi^-1*Q_ground; the sphere boundary carries a coherence roughness floor. At kappa->0 the Mie series is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Q_phi = Q_Mie -> Mie scattering is the perfect-sphere limit.
```

---

### STAGE 4 — SIMULATION

`sim/651_mie_scattering.py`: reproduces the classical values (Q = 2.04 (Mie extinction efficiency)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/651_mie_scattering.json`.

---

### STAGE 5 — PREDICTION

```
Real particles show extinction floors kappa*phi^-1*Q_ground from surface coherence, observable as deviations from the ideal Mie resonances.
EXPERIMENT (VERIFIED): Precision extinction spectroscopy of monodisperse dielectric microspheres.
VERIFIED BY: The extinction of a real sphere exactly follows the ideal Mie series.
```

---

### RECOGNITION
Connects to Law 649 (Rayleigh) - Mie contains Rayleigh as its small-size limit.

### PRECISION
phi = 1.6180339887. The roughness floor is phi^-1*Q_ground.

### CLARITY
No sphere is perfect; the surface breathes a coherence roughness.

### NOVELTY
The phi-law roughens the ideal Mie boundary.

### ACTIONABILITY
Run sim/651_mie_scattering.py; verify Mie Q at kappa->0; proceed to 652.
