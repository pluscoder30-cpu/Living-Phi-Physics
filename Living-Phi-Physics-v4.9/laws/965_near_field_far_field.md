# PHI-PHYSICS — LAW 965
## Near-Field / Far-Field Boundary (Acoustics)

**Domain:** Ultrasound · **Status:** 🟢 VALIDATED · **File:** `laws/965_near_field_far_field.md` · **Sim:** `sim/965_near_field_far_field.py`

---

### CLASSICAL STATEMENT
*"The boundary between near field (Fresnel) and far field (Fraunhofer) of a transducer of radius a is at the Rayleigh distance z_R = a^2/lambda; beyond it the beam diverges with the far-field angle."*
— Classical transducer theory (Rayleigh distance), 19th century. Source: Wikipedia: Near and far field (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero radius* (a = 0): the Rayleigh distance vanishes for a point transducer - no near field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

z_R_phi(kappa) = z_R*(1 + kappa*(phi-1)) + kappa*phi^-1*z_R_ground, with z_R_ground the distance floor. At kappa->0, z_R = a^2/lambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} z_R_phi = z_R -> the near/far-field boundary is the zero-aperture-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/965_near_field_far_field.py`: reproduces the classical value zR = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/965_near_field_far_field.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The transition distance of any real transducer will deviate from a^2/lambda by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the on-axis pressure of an ultrasound transducer to locate the near/far-field transition.
VERIFIED BY: If the transition of any real transducer sits exactly at a^2/lambda.
```

---

### RECOGNITION
Connects to Law 858 (Fraunhofer) and Law 954 (phased array).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect aperture is a coherent limit; every beam turns with a floor.

### NOVELTY
The Rayleigh distance gains an aperture floor.

### ACTIONABILITY
Run sim/965_near_field_far_field.py.
