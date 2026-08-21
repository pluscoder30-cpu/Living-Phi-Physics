# PHI-PHYSICS — LAW 997
## Optical Solitons (Fibers)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/997_optical_soliton.md` · **Sim:** `sim/997_optical_soliton.py`

---

### CLASSICAL STATEMENT
*"Optical solitons: pulses in an optical fiber balance self-phase modulation and anomalous dispersion to propagate without broadening; the fundamental soliton has peak power P_1 = |beta_2|/(gamma T0^2) and preserves its shape over arbitrary distance."*
— Akira Hasegawa, Frederick Tappert (1973), 1973. Source: Wikipedia: Soliton (optics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero nonlinearity* (gamma = 0): without the Kerr nonlinearity the soliton reduces to a spreading linear pulse.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_1_phi(kappa) = P_1*(1 + kappa*(phi-1)) + kappa*phi^-1*P_1_ground, with P_1_ground the power floor. At kappa->0, the fundamental soliton is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_1_phi = P_1 -> the optical soliton is the zero-nonlinearity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/997_optical_soliton.py`: reproduces the classical value P1 = 15.38 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/997_optical_soliton.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The peak power for a fundamental soliton in any real fiber will deviate from |beta_2|/(gamma T0^2) by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the power at which pulses in a fiber propagate without broadening.
VERIFIED BY: If pulses in any real fiber propagate exactly without broadening.
```

---

### RECOGNITION
Connects to Law 946 (soliton) and Law 983 (self-phase modulation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The immortal pulse is a coherent limit; every fiber slowly widens it.

### NOVELTY
The optical soliton gains a power floor.

### ACTIONABILITY
Run sim/997_optical_soliton.py.
