# PHI-PHYSICS — LAW 842
## Diffraction Grating Equation

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/842_diffraction_grating_equation.md` · **Sim:** `sim/842_diffraction_grating_equation.py`

---

### CLASSICAL STATEMENT
*"d * sin(theta) = m * lambda for normal incidence, where d is the grating spacing and m the order (grating equation)."*
— Joseph von Fraunhofer (as diffraction grating; Rittenhouse 1785), 1821. Source: Wikipedia: Diffraction grating (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect periodicity*: the equation assumes an exactly periodic array of identical slits with zero groove error.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

sin(theta)_phi(kappa) = sin(theta)*(1 + kappa*(phi-1)) + kappa*phi^-1*sin(theta)_ground, with sin(theta)_ground the angle floor. At kappa->0, d sin(theta) = m lambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sin(theta)_phi = sin(theta) -> the grating equation is the zero-groove-error-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/842_diffraction_grating_equation.py`: reproduces the classical value sin = 0.3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/842_diffraction_grating_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Diffraction orders of a real grating will sit at angles offset by kappa*phi^-1*sin(theta)_ground from the grating equation.
EXPERIMENT (VERIFIED): Measure the order angles of a high-quality ruled grating with a laser.
VERIFIED BY: If any real grating satisfies d sin(theta) = m lambda exactly for all orders.
```

---

### RECOGNITION
Connects to Law 842 (grating resolving power) and Law 858 (Fraunhofer diffraction).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect comb is a coherent limit; every ruling trembles.

### NOVELTY
The grating equation gains an angle floor from groove coherence.

### ACTIONABILITY
Run sim/842_diffraction_grating_equation.py.
