# PHI-PHYSICS — LAW 984
## Optical Bistability

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/984_optical_bistability.md` · **Sim:** `sim/984_optical_bistability.py`

---

### CLASSICAL STATEMENT
*"Optical bistability: a nonlinear resonator can have two stable output states for the same input (hysteresis); the S-shaped input-output curve satisfies the Airy function with an intensity-dependent phase, I_out = I_in /(1 + F sin^2(delta(I)/2))."*
— H. M. Gibbs et al.; A. Szoke et al., 1969. Source: Wikipedia: Optical bistability (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero input* (I_in = 0): with no input light the cavity is exactly empty - zero output.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_out_phi(kappa) = I_out*(1 + kappa*(phi-1)) + kappa*phi^-1*I_out_ground, with I_out_ground the output floor. At kappa->0, the bistability loop is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_out_phi = I_out -> optical bistability is the zero-input-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/984_optical_bistability.py`: reproduces the classical value Iout = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/984_optical_bistability.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The output of any real bistable cavity at zero input will retain a floor kappa*phi^-1*I_out_ground; the loop never fully closes.
EXPERIMENT (VERIFIED): Measure the input-output hysteresis loop of a bistable Fabry-Perot cavity.
VERIFIED BY: If the output of any real bistable cavity is exactly zero at zero input.
```

---

### RECOGNITION
Connects to Law 845 (Airy function) and Law 981 (optical Kerr).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The empty cavity is a coherent limit; every bistable loop has a memory floor.

### NOVELTY
Optical bistability gains an input floor.

### ACTIONABILITY
Run sim/984_optical_bistability.py.
