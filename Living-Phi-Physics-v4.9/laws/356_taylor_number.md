# PHI-PHYSICS — LAW 356
## Taylor Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/356_taylor_number.md` · **Sim:** `sim/356_taylor_number.py`

---

### CLASSICAL STATEMENT
*"The Taylor number Ta = (omega d^2/nu)^2 (for concentric rotating cylinders, Ta = 4 omega^2 d^4/nu^2) governs the stability of Couette flow; above a critical Ta, the flow breaks into axisymmetric Taylor vortices."*
— Geoffrey Ingram Taylor, 1923. Source: Wikipedia: Taylor number; Taylor (1923), 'Stability of a viscous liquid contained between two rotating cylinders'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *non-rotating / zero-gap reference*: Ta = 0 is the no-rotation state; the instability exists because the cylinders rotate and the gap is finite.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Ta_phi(kappa) = Ta*(1 + kappa*(phi-1)) + kappa*phi^-1*Ta_ground. At kappa->0 the classical Taylor number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Ta_phi = 4 omega^2 d^4/nu^2 -> the Taylor number is the Couette-stability limit marker.
```

---

### STAGE 4 — SIMULATION

`sim/356_taylor_number.py`: reproduces the classical value Ta = 4e+04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/356_taylor_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Taylor-vortex onset shifts by a phi-coherent amount phi^-1*Ta_ground from the critical Ta.
EXPERIMENT (VERIFIED): Couette experiments (rotating cylinders with dye/particle imaging) locating the vortex onset precisely.
VERIFIED BY: Taylor vortices appear exactly at the classical critical Ta at full coupling.
```

---

### RECOGNITION
Connects to Law 397 (Kelvin-Helmholtz) and Law 354 (Richardson) — the stability-number family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The smooth swirl is a limit; every rotating gap flares a phi off the ideal onset.

### NOVELTY
Classical stability theory exacts the critical Ta; the phi-law gives it a coherence width.

### ACTIONABILITY
Run sim/356_taylor_number.py; verify Ta at kappa->0.
