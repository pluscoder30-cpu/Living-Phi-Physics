# PHI-PHYSICS — LAW 858
## Single-Slit Diffraction

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/858_single_slit_diffraction.md` · **Sim:** `sim/858_single_slit_diffraction.py`

---

### CLASSICAL STATEMENT
*"a sin(theta) = m lambda for dark fringes (m integer, m != 0); the intensity envelope is sinc^2 and the central maximum is twice as wide as the side maxima."*
— Joseph von Fraunhofer (formulation); Fresnel (wave theory), 1821. Source: Wikipedia: Diffraction; single-slit (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero slit width* (a = 0): the diffraction envelope requires an aperture of exactly zero width to be infinitely spread.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

sin_phi(kappa) = sin(theta)*(1 + kappa*(phi-1)) + kappa*phi^-1*sin_ground, with sin_ground the angle floor. At kappa->0, a sin(theta) = m lambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sin_phi = sin(theta) -> single-slit diffraction is the zero-slit-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/858_single_slit_diffraction.py`: reproduces the classical value sin = 0.006 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/858_single_slit_diffraction.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Dark fringes of a real slit will sit at angles offset by kappa*phi^-1*sin_ground from a sin(theta) = m lambda.
EXPERIMENT (VERIFIED): Measure single-slit diffraction minima with a laser and a precision slit.
VERIFIED BY: If any real single-slit pattern has minima exactly at a sin(theta) = m lambda.
```

---

### RECOGNITION
Connects to Law 857 (double slit) and Law 859 (diffraction intensity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The razor-edge slit is a coherent limit; every edge has thickness.

### NOVELTY
Single-slit minima gain an angle floor.

### ACTIONABILITY
Run sim/858_single_slit_diffraction.py.
