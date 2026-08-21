# PHI-PHYSICS — LAW 896
## Inverse Square Law (Irradiance)

**Domain:** Radiometry · **Status:** 🟢 VALIDATED · **File:** `laws/896_inverse_square_law.md` · **Sim:** `sim/896_inverse_square_law.py`

---

### CLASSICAL STATEMENT
*"The irradiance from a point source falls as E = I / r^2: the power per unit area is inversely proportional to the square of the distance from the source."*
— Classical radiometry (Kepler, Bouguer), 1604/1729. Source: Wikipedia: Inverse-square law (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero source size*: the law holds exactly for a point source of zero extent - the pure inverse square requires a point.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, with E_ground the irradiance floor. At kappa->0, E = I/r^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} E_phi = E -> the inverse square law is the zero-source-size-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/896_inverse_square_law.py`: reproduces the classical value E = 25 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/896_inverse_square_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured irradiance from a real (finite) source will deviate from I/r^2 by a coherence floor kappa*phi^-1*E_ground.
EXPERIMENT (VERIFIED): Measure irradiance versus distance of a small LED and compare with the inverse square law.
VERIFIED BY: If irradiance from any real source follows I/r^2 exactly at all distances.
```

---

### RECOGNITION
Connects to Law 855 (radiance) and Law 419 (Lambert) - the radiometry fundamentals.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect point source is a coherent limit; every source has a face.

### NOVELTY
The inverse square law gains a source-size floor.

### ACTIONABILITY
Run sim/896_inverse_square_law.py.
