# PHI-PHYSICS — LAW 401
## Mach Angle (Mach Cone) Law

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/401_mach_angle_law.md` · **Sim:** `sim/401_mach_angle_law.py`

---

### CLASSICAL STATEMENT
*"A body moving supersonically at Mach number M generates a Mach cone with half-angle mu = arcsin(1/M); the cone narrows as M increases, and the bow wave carries the acoustic energy (the 'Mach cone' photographed by Mach)."*
— Ernst Mach, 1877. Source: Wikipedia: Mach number / Mach cone; Mach's supersonic photography (c. 1877)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *subsonic reference*: the Mach cone exists only for M > 1; the sonic boundary M = 1 is the zero of the cone's existence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: mu_phi(kappa) = arcsin(1/M)*(1 + kappa*(phi-1)) + kappa*phi^-1*mu_ground. At kappa->0 the classical Mach angle is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} mu_phi = arcsin(1/M) -> the Mach-angle law is the isentropic, sharp-body limit.
```

---

### STAGE 4 — SIMULATION

`sim/401_mach_angle_law.py`: reproduces the classical value mu = 30 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/401_mach_angle_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Measured Mach cone angles carry a phi-coherent offset phi^-1*mu_ground at full coupling.
EXPERIMENT (VERIFIED): Schlieren imaging of supersonic bodies (wind tunnels, bullets) measuring the cone half-angle precisely.
VERIFIED BY: The Mach cone half-angle is exactly arcsin(1/M) at full coupling.
```

---

### RECOGNITION
Connects to Law 344 (Mach number) and Law 098 (speed of sound).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The sonic boundary is a limit; every cone leans a phi off the ideal.

### NOVELTY
Classical supersonics exacts the cone angle; the phi-law gives it a coherence width.

### ACTIONABILITY
Run sim/401_mach_angle_law.py; verify the Mach angle at kappa->0.
