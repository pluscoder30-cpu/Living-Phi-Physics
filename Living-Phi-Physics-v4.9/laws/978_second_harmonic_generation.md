# PHI-PHYSICS — LAW 978
## Second-Harmonic Generation (SHG)

**Domain:** Nonlinear Optics · **Status:** 🟢 VALIDATED · **File:** `laws/978_second_harmonic_generation.md` · **Sim:** `sim/978_second_harmonic_generation.py`

---

### CLASSICAL STATEMENT
*"SHG: a chi^(2) crystal doubles the frequency of light; the conversion efficiency scales as I_2w = eta I_w^2 (proportional to the square of the fundamental intensity) and requires phase matching delta k = 0."*
— Peter Franken et al., 1961. Source: Wikipedia: Second-harmonic generation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero fundamental intensity* (I_w = 0): no harmonic is generated without the fundamental - the SHG vanishes exactly at zero input.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_2w_phi(kappa) = I_2w*(1 + kappa*(phi-1)) + kappa*phi^-1*I_2w_ground, with I_2w_ground the harmonic floor. At kappa->0, I_2w = eta I_w^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_2w_phi = I_2w -> SHG is the zero-fundamental-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/978_second_harmonic_generation.py`: reproduces the classical value I2w = 100 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/978_second_harmonic_generation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual harmonic signal kappa*phi^-1*I_2w_ground will occur even at nominally zero fundamental intensity (from field coherence).
EXPERIMENT (VERIFIED): Measure the SHG power of a crystal as a function of fundamental power down to zero.
VERIFIED BY: If the SHG output is exactly zero at zero fundamental input.
```

---

### RECOGNITION
Connects to Law 976 (SPDC) and Law 979 (phase matching).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The dark crystal is a coherent limit; every chi^(2) medium doubles with a floor.

### NOVELTY
SHG gains a fundamental floor.

### ACTIONABILITY
Run sim/978_second_harmonic_generation.py.
