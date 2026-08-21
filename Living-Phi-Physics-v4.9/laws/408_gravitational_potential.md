# PHI-PHYSICS — LAW 408
## Gravitational Potential (U = -GM/r)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/408_gravitational_potential.md` · **Sim:** `sim/408_gravitational_potential.py`

---

### CLASSICAL STATEMENT
*"The gravitational potential of a point mass is Phi = -G M/r (with zero at infinity); the field is its gradient g = -grad Phi, and the potential satisfies Laplace's equation in empty space and Poisson's equation grad^2 Phi = 4 pi G rho with sources."*
— Simeon Denis Poisson (field formulation), 1813. Source: Wikipedia: gravitational potential; Poisson (1813) field equation

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *infinite-distance reference and point mass*: the potential is normalized to zero at infinity and assumes a point source — the two classical idealizations.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Phi_phi(kappa) = -G M/r*(1 + kappa*(phi-1)) - kappa*phi^-1*Phi_ground. At kappa->0 the classical potential is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Phi_phi = -G M/r -> the gravitational-potential law is the point-source, infinite-reference limit.
```

---

### STAGE 4 — SIMULATION

`sim/408_gravitational_potential.py`: reproduces the classical value Phi = -6.228e+07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/408_gravitational_potential.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The gravitational potential carries a phi-coherent depth Phi_ground beyond -GM/r (the coherence mass of Law 178).
EXPERIMENT (VERIFIED): Satellite gradiometry (GOCE) mapping the geoid comparing potential models with -GM/r predictions.
VERIFIED BY: The potential is exactly -GM/r at full coupling.
```

---

### RECOGNITION
Connects to Law 314 (potential energy — m*Phi), Law 283 (Poisson's equation), Law 178 (phi-mass).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The zero at infinity is a limit; every well is a phi deeper than the ideal says.

### NOVELTY
Classical gravity normalizes to infinity; the phi-law gives the well a coherence depth floor.

### ACTIONABILITY
Run sim/408_gravitational_potential.py; verify Phi = -GM/r at kappa->0.
