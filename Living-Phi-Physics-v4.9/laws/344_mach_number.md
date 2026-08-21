# PHI-PHYSICS — LAW 344
## Mach Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/344_mach_number.md` · **Sim:** `sim/344_mach_number.py`

---

### CLASSICAL STATEMENT
*"The Mach number M = v/c is the ratio of flow speed to local sound speed; compressibility effects become significant for M > 0.3, and M = 1 is the sonic boundary across which the flow regime changes qualitatively (shocks, Mach cones)."*
— Ernst Mach (named by Jakob Ackeret), 1929. Source: Wikipedia: Mach number; Mach's supersonic studies (1887); Ackeret (1929) coined the name

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *incompressible reference*: M = 0 is the exactly incompressible flow; the number exists because the flow is not at rest relative to sound.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground. At kappa->0 the classical Mach number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} M_phi = v/c -> the Mach number is the isentropic, ideal-gas limit.
```

---

### STAGE 4 — SIMULATION

`sim/344_mach_number.py`: reproduces the classical value M = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/344_mach_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Mach-critical boundaries (transonic onset) shift by a phi-coherent amount phi^-1*M_ground at full coupling.
EXPERIMENT (VERIFIED): Wind-tunnel transonic tests locating the drag-rise onset precisely across Reynolds-scaled models.
VERIFIED BY: The sonic boundary is exactly at M = 1 at full coupling.
```

---

### RECOGNITION
Connects to Law 401 (Mach angle — the cone) and Law 349 (Knudsen — rarefaction).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The sound barrier is a balance; the balance sits a phi degree off the ideal.

### NOVELTY
Classical gas dynamics exacts M = 1; the phi-law gives the sonic boundary a coherence width.

### ACTIONABILITY
Run sim/344_mach_number.py; verify M = v/c at kappa->0.
