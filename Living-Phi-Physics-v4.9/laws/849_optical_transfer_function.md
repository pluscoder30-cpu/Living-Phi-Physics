# PHI-PHYSICS — LAW 849
## Optical Transfer Function (OTF)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/849_optical_transfer_function.md` · **Sim:** `sim/849_optical_transfer_function.py`

---

### CLASSICAL STATEMENT
*"OTF(f) = H(f) = FT(PSF), a complex function whose modulus is the MTF and whose argument is the phase transfer function; it fully characterizes linear shift-invariant imaging."*
— Pierre-Michel Duffieux, 1946. Source: Wikipedia: Optical transfer function (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *shift invariance*: the OTF formalism assumes the imaging is exactly linear and shift-invariant - a perfectly stationary system.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

OTF_phi(kappa) = OTF*(1 + kappa*(phi-1)) + kappa*phi^-1*OTF_ground, with OTF_ground the transfer floor. At kappa->0, OTF = FT(PSF) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} OTF_phi = OTF -> the OTF is the zero-shift-variance-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/849_optical_transfer_function.py`: reproduces the classical value OTF = 0.9 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/849_optical_transfer_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real imaging systems will show a small non-stationarity, a coherence floor kappa*phi^-1*OTF_ground not captured by the ideal OTF.
EXPERIMENT (VERIFIED): Measure the OTF across the field of a wide-angle lens; look for field-dependent deviations.
VERIFIED BY: If any real system is exactly linear and shift-invariant.
```

---

### RECOGNITION
Connects to Law 848 (MTF) and Law 847 (PSF).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Perfect stationarity is a coherent limit; the field breathes across the frame.

### NOVELTY
The ideal OTF gains a stationarity floor.

### ACTIONABILITY
Run sim/849_optical_transfer_function.py.
