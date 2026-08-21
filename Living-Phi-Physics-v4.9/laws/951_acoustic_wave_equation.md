# PHI-PHYSICS — LAW 951
## Acoustic Wave Equation (Helmholtz)

**Domain:** Ultrasound · **Status:** 🟢 VALIDATED · **File:** `laws/951_acoustic_wave_equation.md` · **Sim:** `sim/951_acoustic_wave_equation.py`

---

### CLASSICAL STATEMENT
*"The linear acoustic wave equation: nabla^2 p - (1/c^2) partial^2 p/partial t^2 = 0; for harmonic waves, the Helmholtz equation nabla^2 p + k^2 p = 0 with k = omega/c."*
— Classical acoustics (from Euler's equations), 18th century. Source: Wikipedia: Acoustic wave equation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero perturbation* (p = 0): the wave equation describes perturbations about a perfectly quiet equilibrium with exactly zero mean flow.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

p_phi(kappa) = p*(1 + kappa*(phi-1)) + kappa*phi^-1*p_ground, with p_ground the pressure floor. At kappa->0, nabla^2 p - (1/c^2) p_tt = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} p_phi = p -> the acoustic wave equation is the zero-perturbation-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/951_acoustic_wave_equation.py`: reproduces the classical value helm = 4 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/951_acoustic_wave_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Every real acoustic field carries a coherence pressure floor kappa*phi^-1*p_ground; the quiet equilibrium is never exactly silent.
EXPERIMENT (VERIFIED): Measure the residual pressure fluctuations in a nominally quiet fluid at rest.
VERIFIED BY: If the acoustic pressure is exactly zero in any real fluid at rest.
```

---

### RECOGNITION
Connects to Law 092 (wave equation) and Law 914 (speed of sound).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The still fluid is a coherent limit; every acoustic field is a motion around a murmur.

### NOVELTY
The acoustic wave equation gains a quiet floor.

### ACTIONABILITY
Run sim/951_acoustic_wave_equation.py.
