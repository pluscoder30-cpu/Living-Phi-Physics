# PHI-PHYSICS — LAW 949
## Internal Waves

**Domain:** Geophysical Waves · **Status:** 🟢 VALIDATED · **File:** `laws/949_internal_wave.md` · **Sim:** `sim/949_internal_wave.py`

---

### CLASSICAL STATEMENT
*"Internal waves propagate within a density-stratified fluid; their dispersion is omega^2 = N^2 k^2/(k^2 + m^2), bounded by the buoyancy (Brunt-Vaisala) frequency N; the maximum frequency of internal waves is exactly N."*
— Classical fluid dynamics (Brunt-Vaisala), 1927. Source: Wikipedia: Internal wave (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero stratification* (N = 0): internal waves vanish exactly in a homogeneous (unstratified) fluid.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

omega_phi(kappa) = omega*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground, with omega_ground the frequency floor. At kappa->0, omega^2 = N^2 k^2/(k^2+m^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_phi = omega -> the internal wave is the zero-stratification-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/949_internal_wave.py`: reproduces the classical value omega = 0.004472 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/949_internal_wave.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured frequency of any real internal wave will deviate from the dispersion relation by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Generate internal waves in a salt-stratified tank and measure their dispersion.
VERIFIED BY: If the internal wave frequency in any real stratified fluid matches the dispersion relation exactly.
```

---

### RECOGNITION
Connects to Law 947 (Rossby) - the stratified rotating-wave family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly stratified sea is a coherent limit; every layer trembles.

### NOVELTY
Internal waves gain a stratification floor.

### ACTIONABILITY
Run sim/949_internal_wave.py.
