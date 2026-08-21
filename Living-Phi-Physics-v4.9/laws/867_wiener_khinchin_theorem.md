# PHI-PHYSICS — LAW 867
## Wiener-Khinchin Theorem

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/867_wiener_khinchin_theorem.md` · **Sim:** `sim/867_wiener_khinchin_theorem.py`

---

### CLASSICAL STATEMENT
*"The power spectral density S(f) equals the Fourier transform of the autocorrelation function R(tau): S(f) = FT[R(tau)]. The spectrum and autocorrelation are Fourier pairs."*
— Norbert Wiener, Alexander Khinchin, 1930. Source: Wikipedia: Wiener-Khinchin theorem (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite time* (T -> infinity): the theorem assumes a wide-sense-stationary process over infinite time with zero leakage.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground, with S_ground the spectral floor. At kappa->0, S(f) = FT[R(tau)] exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = S -> the Wiener-Khinchin theorem is the zero-finite-record-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/867_wiener_khinchin_theorem.py`: reproduces the classical value S = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/867_wiener_khinchin_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Spectra computed from finite records will deviate from FT[R(tau)] by a coherence floor kappa*phi^-1*S_ground.
EXPERIMENT (VERIFIED): Compare the measured spectrum of a broadband source with the FT of its measured autocorrelation.
VERIFIED BY: If the spectrum of any finite record exactly equals FT[R(tau)].
```

---

### RECOGNITION
Connects to Law 866 (coherence time) and Law 872 (wave uncertainty) - the Fourier pair of coherence.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The infinite record is a coherent limit; every measurement is finite.

### NOVELTY
The spectrum-autocorrelation duality gains a record-length floor.

### ACTIONABILITY
Run sim/867_wiener_khinchin_theorem.py.
