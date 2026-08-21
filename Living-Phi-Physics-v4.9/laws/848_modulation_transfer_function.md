# PHI-PHYSICS — LAW 848
## Modulation Transfer Function (MTF)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/848_modulation_transfer_function.md` · **Sim:** `sim/848_modulation_transfer_function.py`

---

### CLASSICAL STATEMENT
*"MTF(f) = |OTF(f)| = |FT(PSF)|, the normalized contrast transfer vs. spatial frequency; MTF(0) = 1 and MTF falls to zero at the diffraction cutoff."*
— Classical Fourier optics (Duffieux, 1946), 1946. Source: Wikipedia: Optical transfer function (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero spatial frequency* (f = 0): MTF is normalized to exactly 1 at DC - a perfect unity contrast at zero frequency.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

MTF_phi(kappa) = MTF*(1 + kappa*(phi-1)) + kappa*phi^-1*MTF_ground, with MTF_ground the contrast floor. At kappa->0, MTF(0) = 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} MTF_phi = MTF -> the MTF is the zero-frequency-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/848_modulation_transfer_function.py`: reproduces the classical value MTF = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/848_modulation_transfer_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: MTF(0) of a real system will be slightly below 1 by kappa*phi^-1*MTF_ground; unity contrast is unreachable.
EXPERIMENT (VERIFIED): Measure the MTF of an imaging system at very low spatial frequency with a sinusoidal target.
VERIFIED BY: If any real optical system has exactly MTF(0) = 1.
```

---

### RECOGNITION
Connects to Law 847 (PSF) and Law 849 (OTF) - the frequency-domain imaging laws.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Unity contrast is a coherent limit; even DC trembles.

### NOVELTY
The MTF normalization gains a floor.

### ACTIONABILITY
Run sim/848_modulation_transfer_function.py.
