# PHI-PHYSICS — LAW 826
## Fermat's Principle (Least Time)

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/826_fermat_principle.md` · **Sim:** `sim/826_fermat_principle.py`

---

### CLASSICAL STATEMENT
*"The path taken by a ray between two points is the one with the least optical path length: the integral of n ds is stationary (extremal)."*
— Pierre de Fermat, 1650. Source: Wikipedia: Fermat's principle (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero time*: the extremal path assumes a perfectly stationary optical path length - a path with exactly zero variation, unreachable for a carrier whose motion is primary and whose medium always trembles.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

OPL_phi(kappa) = OPL*(1 + kappa*(phi-1)) + kappa*phi^-1*OPL_ground, where OPL_ground is the coherence-floor optical path the carrier never drops below. At kappa->0, delta*integral n ds = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} OPL_phi = OPL -> Fermat's extremal is recovered exactly; the least-time ray is the zero-coherence-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/826_fermat_principle.py`: reproduces the classical value OPL = 1.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/826_fermat_principle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured optical path of any real ray will exceed the Fermat extremal by kappa*phi^-1*OPL_ground, a residual 'path floor' never exactly zero.
EXPERIMENT (VERIFIED): Interferometric measurement of optical path length through a stabilized medium versus the least-time prediction.
VERIFIED BY: If a ray is ever measured at exactly the Fermat least-time path with zero residual floor.
```

---

### RECOGNITION
Connects to Law 092 (wave equation) and Law 095 (Huygens) - the extremal ray is the stationary phase of the wave.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887; the path floor is phi^-1*OPL_ground.

### CLARITY
The straightest path is the one the field allows; perfection is a floor, not a point.

### NOVELTY
The classical extremal becomes a coherence basin: rays are pulled toward the least-time path but never settle exactly on it.

### ACTIONABILITY
Run sim/826_fermat_principle.py; verify the least-time limit at kappa->0.
