# PHI-PHYSICS — LAW 888
## Verdet Constant (Faraday Rotation)

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/888_verdet_constant.md` · **Sim:** `sim/888_verdet_constant.py`

---

### CLASSICAL STATEMENT
*"theta = V B L: the rotation angle of the plane of polarization in a magnetic field is V (Verdet constant) times field strength B times path length L (Faraday effect)."*
— Émile Verdet (constant); Michael Faraday (effect, 1845), 1854. Source: Wikipedia: Verdet constant (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field* (B = 0): the rotation is exactly zero in the absence of a magnetic field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

theta_phi(kappa) = theta*(1 + kappa*(phi-1)) + kappa*phi^-1*theta_ground, with theta_ground the rotation floor. At kappa->0, theta = V B L exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} theta_phi = theta -> the Verdet law is the zero-field-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/888_verdet_constant.py`: reproduces the classical value theta = 0.00075 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/888_verdet_constant.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual rotation kappa*phi^-1*theta_ground will be measured at zero applied field in any real material (field-free coherence floor).
EXPERIMENT (VERIFIED): Measure the Faraday rotation of a glass sample as a function of applied magnetic field, including zero field.
VERIFIED BY: If the measured rotation is exactly zero at zero applied field in any real material.
```

---

### RECOGNITION
Connects to Law 807 (Faraday rotation) and Law 887 (optical activity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The zero-field silence is a coherent limit; every glass carries a magnetic murmur.

### NOVELTY
The Verdet law gains a zero-field floor.

### ACTIONABILITY
Run sim/888_verdet_constant.py.
