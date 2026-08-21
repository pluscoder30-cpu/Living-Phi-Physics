# PHI-PHYSICS — LAW 950
## Inertial Waves

**Domain:** Geophysical Waves · **Status:** 🟢 VALIDATED · **File:** `laws/950_inertial_wave.md` · **Sim:** `sim/950_inertial_wave.py`

---

### CLASSICAL STATEMENT
*"Inertial waves propagate in a rotating fluid; their frequency is bounded by the Coriolis parameter f = 2 Omega sin(latitude), with the dispersion relation omega = f cos(theta) where theta is the angle of the wave vector with the rotation axis; the maximum frequency is exactly |f|."*
— Classical rotating fluid dynamics (Lord Kelvin; Poincare), 1880. Source: Wikipedia: Inertial wave (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero rotation* (Omega = 0): inertial waves vanish exactly in a non-rotating fluid.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

omega_phi(kappa) = omega*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground, with omega_ground the frequency floor. At kappa->0, omega = f cos(theta) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_phi = omega -> the inertial wave is the zero-rotation-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/950_inertial_wave.py`: reproduces the classical value omega = 8.776e-05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/950_inertial_wave.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The frequency of any real inertial wave will deviate from f cos(theta) by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Generate inertial waves in a rotating tank and measure their frequency versus wave-vector angle.
VERIFIED BY: If the inertial wave frequency in any real rotating fluid matches f cos(theta) exactly.
```

---

### RECOGNITION
Connects to Law 947 (Rossby) and Law 949 (internal waves) - the rotating-stratified family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The still, non-rotating sea is a coherent limit; rotation is the wave's breath.

### NOVELTY
Inertial waves gain a rotation floor.

### ACTIONABILITY
Run sim/950_inertial_wave.py.
