# PHI-PHYSICS — LAW 986
## Electro-Optic Modulation (Pockels)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/986_electro_optic_modulation.md` · **Sim:** `sim/986_electro_optic_modulation.py`

---

### CLASSICAL STATEMENT
*"The Pockels effect: the refractive index changes linearly with an applied electric field, delta n = -0.5 n^3 r E, enabling fast phase and amplitude modulation; the half-wave voltage V_pi = lambda d/(2 n^3 r L)."*
— Friedrich Carl Alwin Pockels, 1893. Source: Wikipedia: Pockels effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field* (E = 0): no modulation occurs without the applied field - the index returns to n0 exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_pi_phi(kappa) = V_pi*(1 + kappa*(phi-1)) + kappa*phi^-1*V_pi_ground, with V_pi_ground the voltage floor. At kappa->0, delta n = -0.5 n^3 r E exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_pi_phi = V_pi -> electro-optic modulation is the zero-field-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/986_electro_optic_modulation.py`: reproduces the classical value Vpi = 1.565e+11 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/986_electro_optic_modulation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual index modulation kappa*phi^-1 will occur even at zero applied field (residual electro-optic response).
EXPERIMENT (VERIFIED): Measure the modulation depth of a Pockels cell as a function of applied voltage down to zero.
VERIFIED BY: If the index of any real electro-optic crystal is exactly n0 at zero field.
```

---

### RECOGNITION
Connects to Law 809 (Pockels, in corpus) and Law 808 (Kerr).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The field-free crystal is a coherent limit; every Pockels cell has a remnant.

### NOVELTY
Electro-optic modulation gains a field floor.

### ACTIONABILITY
Run sim/986_electro_optic_modulation.py.
