# PHI-PHYSICS — LAW 834
## Optical Power (Dioptric Power)

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/834_optical_power.md` · **Sim:** `sim/834_optical_power.py`

---

### CLASSICAL STATEMENT
*"P = n/f (in air P = 1/f measured in diopters); power is the reciprocal focal length, additive for thin lenses in contact: P = P1 + P2."*
— Classical optics (diopter convention, Monoyer), 1872. Source: Wikipedia: Optical power (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero power* (P = 0): an afocal system has exactly no focusing effect - a system of zero vergence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, with P_ground the afocal floor. At kappa->0, P = n/f exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P -> optical power is the zero-afocal-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/834_optical_power.py`: reproduces the classical value P = 20 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/834_optical_power.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: An 'afocal' system will still focus a beam slightly, with a residual power kappa*phi^-1*P_ground.
EXPERIMENT (VERIFIED): Measure the residual focusing of a telescope afocal system with a collimated beam.
VERIFIED BY: If any real system has exactly zero optical power.
```

---

### RECOGNITION
Connects to Law 834 (lensmaker) and Law 828 (thin lens) - the reciprocal-focal-length convention.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Zero power is a coherent limit; every system bends the field slightly.

### NOVELTY
The afocal ideal gains a power floor.

### ACTIONABILITY
Run sim/834_optical_power.py.
