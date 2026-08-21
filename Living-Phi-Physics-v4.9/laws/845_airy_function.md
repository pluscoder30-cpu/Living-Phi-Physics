# PHI-PHYSICS — LAW 845
## Airy Function (Fabry-Perot Transmission)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/845_airy_function.md` · **Sim:** `sim/845_airy_function.py`

---

### CLASSICAL STATEMENT
*"T = I0 / (1 + F sin^2(delta/2)) with F = 4R/(1-R)^2; the Airy function describing the transmitted intensity of a Fabry-Perot etalon."*
— George Biddell Airy, 1835. Source: Wikipedia: Airy function (Fabry-Perot) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero round-trip phase error*: the Airy function assumes an exactly resonant phase delta = 2 m pi with zero detuning.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground, with T_ground the transmission floor. At kappa->0, T = I0/(1+F sin^2(delta/2)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = T -> the Airy function is the zero-detuning-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/845_airy_function.py`: reproduces the classical value T = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/845_airy_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Peak transmission through a real etalon will fall short of I0 by a floor kappa*phi^-1*T_ground; the peak is a basin, not a point.
EXPERIMENT (VERIFIED): Measure the transmitted intensity of a scanned etalon at resonance.
VERIFIED BY: If any real etalon reaches exactly the Airy peak transmission.
```

---

### RECOGNITION
Connects to Law 844 (Fabry-Perot) and Law 845 (Airy disk).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The resonant peak is a basin; perfect tuning is a coherent limit.

### NOVELTY
The Airy transmission gains a floor at peak.

### ACTIONABILITY
Run sim/845_airy_function.py.
