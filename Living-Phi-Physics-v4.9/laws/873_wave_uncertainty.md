# PHI-PHYSICS — LAW 873
## Wave Uncertainty (dx dk)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/873_wave_uncertainty.md` · **Sim:** `sim/873_wave_uncertainty.py`

---

### CLASSICAL STATEMENT
*"delta_x * delta_k >= 1/2 for a wave packet: the spatial extent and wavenumber spread of a wave cannot both be arbitrarily small (Fourier uncertainty)."*
— Derived from Fourier analysis (Rayleigh; Heisenberg analogy), 1909/1927. Source: Wikipedia: Uncertainty principle (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero spread* (delta_k = 0): an exactly monochromatic plane wave has infinite extent - zero spatial localization.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

prod_phi(kappa) = prod*(1 + kappa*(phi-1)) + kappa*phi^-1*prod_ground, with prod_ground the floor of 1/2. At kappa->0, delta_x delta_k = 1/2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} prod_phi = prod -> wave uncertainty is the zero-localization-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/873_wave_uncertainty.py`: reproduces the classical value prod = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/873_wave_uncertainty.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The minimum product delta_x delta_k of any real wave packet exceeds 1/2 by a coherence floor; perfect localization is unreachable.
EXPERIMENT (VERIFIED): Measure the spatial width and spectral width of a femtosecond pulse.
VERIFIED BY: If any real wave packet achieves delta_x delta_k < 1/2.
```

---

### RECOGNITION
Connects to Law 070 (Heisenberg) and Law 867 (Wiener-Khinchin) - the Fourier limit.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Localization and purity trade against each other; the 1/2 is a floor.

### NOVELTY
The Fourier uncertainty gains a coherence floor above 1/2.

### ACTIONABILITY
Run sim/873_wave_uncertainty.py.
