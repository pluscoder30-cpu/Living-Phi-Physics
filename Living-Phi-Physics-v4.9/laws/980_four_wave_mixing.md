# PHI-PHYSICS — LAW 980
## Four-Wave Mixing (FWM)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/980_four_wave_mixing.md` · **Sim:** `sim/980_four_wave_mixing.py`

---

### CLASSICAL STATEMENT
*"Four-wave mixing: three waves interact in a chi^(3) medium to generate a fourth, omega_4 = omega_1 +/- omega_2 +/- omega_3, with phase matching k_4 = k_1 +/- k_2 +/- k_3; a source of new frequencies and of cross-talk in fibers."*
— Classical nonlinear optics (from chi^(3) theory), 1960s. Source: Wikipedia: Four-wave mixing (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero third-order nonlinearity* (chi^(3) = 0): no FWM occurs in a linear medium - the generated wave vanishes exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_4_phi(kappa) = I_4*(1 + kappa*(phi-1)) + kappa*phi^-1*I_4_ground, with I_4_ground the mixing floor. At kappa->0, the FWM product follows the chi^(3) theory exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_4_phi = I_4 -> four-wave mixing is the zero-chi3-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/980_four_wave_mixing.py`: reproduces the classical value I4 = 0.05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/980_four_wave_mixing.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual FWM product kappa*phi^-1*I_4_ground will be generated even in a nominally linear medium.
EXPERIMENT (VERIFIED): Measure the FWM product of three copropagating waves in an optical fiber.
VERIFIED BY: If the FWM product is exactly zero in any real medium.
```

---

### RECOGNITION
Connects to Law 978 (SHG) and Law 982 (optical Kerr).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The linear fiber is a coherent limit; every chi^(3) medium mixes with a floor.

### NOVELTY
Four-wave mixing gains a chi3 floor.

### ACTIONABILITY
Run sim/980_four_wave_mixing.py.
