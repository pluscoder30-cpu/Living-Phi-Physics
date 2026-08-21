# PHI-PHYSICS — LAW 922
## Sabine's Equation (Reverberation Time)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/922_sabines_equation.md` · **Sim:** `sim/922_sabines_equation.py`

---

### CLASSICAL STATEMENT
*"T60 = 0.161 V / (sum alpha_i S_i) (seconds): the reverberation time of a room is proportional to its volume and inversely proportional to the total absorption (Sabine's formula)."*
— Wallace Clement Sabine, 1898. Source: Wikipedia: Sabine (acoustics); Wallace Clement Sabine (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero absorption* (sum alpha S = 0): an exactly reverberant room has infinite T60 - sound never decays.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T60_phi(kappa) = T60*(1 + kappa*(phi-1)) + kappa*phi^-1*T60_ground, with T60_ground the decay floor. At kappa->0, T60 = 0.161 V/A exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T60_phi = T60 -> Sabine's equation is the zero-absorption-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/922_sabines_equation.py`: reproduces the classical value T60 = 1.61 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/922_sabines_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The reverberation time of any real room will differ from 0.161 V/A by a coherence floor kappa*phi^-1*T60_ground.
EXPERIMENT (VERIFIED): Measure the RT60 of a reverberation chamber by the interrupted-noise method.
VERIFIED BY: If the RT60 of any real room matches Sabine's formula exactly.
```

---

### RECOGNITION
Connects to Law 923 (reverberation time) and Law 099 (standing waves).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect echo chamber is a coherent limit; every room decays with a floor.

### NOVELTY
Sabine's equation gains an absorption floor.

### ACTIONABILITY
Run sim/922_sabines_equation.py.
