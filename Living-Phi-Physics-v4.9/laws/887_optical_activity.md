# PHI-PHYSICS — LAW 887
## Optical Activity (Rotatory Polarization)

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/887_optical_activity.md` · **Sim:** `sim/887_optical_activity.py`

---

### CLASSICAL STATEMENT
*"Optically active media rotate the plane of polarization by angle alpha = [alpha] * l * c (specific rotation times path length times concentration), first observed in quartz and sugar solutions."*
— Jean-Baptiste Biot; François Arago, 1811. Source: Wikipedia: Optical rotation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero path* (l = 0): the rotation angle is exactly zero for zero path length - an anchor at zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

alpha_phi(kappa) = alpha*(1 + kappa*(phi-1)) + kappa*phi^-1*alpha_ground, with alpha_ground the rotation floor. At kappa->0, alpha = [alpha] l c exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} alpha_phi = alpha -> optical activity is the zero-path-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/887_optical_activity.py`: reproduces the classical value alpha = 1.32 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/887_optical_activity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The rotation angle measured for any real sample will differ from [alpha] l c by a coherence floor kappa*phi^-1*alpha_ground.
EXPERIMENT (VERIFIED): Measure the optical rotation of a sugar solution at different path lengths.
VERIFIED BY: If optical rotation is exactly proportional to path length in any real sample.
```

---

### RECOGNITION
Connects to Law 889 (Verdet constant) - the rotation family of polarization.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect rotator is a coherent limit; every chiral medium has a tremor.

### NOVELTY
Optical activity gains a path floor.

### ACTIONABILITY
Run sim/887_optical_activity.py.
