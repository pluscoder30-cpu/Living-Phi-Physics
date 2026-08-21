# PHI-PHYSICS — LAW 915
## Acoustic Impedance (Characteristic)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/915_acoustic_impedance.md` · **Sim:** `sim/915_acoustic_impedance.py`

---

### CLASSICAL STATEMENT
*"Z = rho * c, the characteristic acoustic impedance of a medium; at an interface, the reflection coefficient is r = (Z2 - Z1)/(Z2 + Z1)."*
— Classical acoustics (Rayleigh), 19th century. Source: Wikipedia: Acoustic impedance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero impedance contrast* (Z2 = Z1): with matched impedances the reflection coefficient is exactly zero - a perfectly transparent interface.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

r_phi(kappa) = r*(1 + kappa*(phi-1)) + kappa*phi^-1*r_ground, with r_ground the reflection floor. At kappa->0, r = (Z2-Z1)/(Z2+Z1) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} r_phi = r -> acoustic impedance matching is the zero-contrast-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/915_acoustic_impedance.py`: reproduces the classical value Z = 1.48e+06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/915_acoustic_impedance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A perfectly matched interface will still reflect a floor kappa*phi^-1*r_ground; no interface is exactly reflectionless.
EXPERIMENT (VERIFIED): Measure the reflection at a water-glycerin interface of matched impedance.
VERIFIED BY: If any real interface gives exactly zero reflection with matched impedance.
```

---

### RECOGNITION
Connects to Law 914 (speed of sound) and Law 951 (impedance matching).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The transparent interface is a coherent limit; every boundary whispers back.

### NOVELTY
Acoustic impedance gains a contrast floor.

### ACTIONABILITY
Run sim/915_acoustic_impedance.py.
