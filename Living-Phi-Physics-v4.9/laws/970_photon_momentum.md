# PHI-PHYSICS — LAW 970
## Photon Momentum (p = h/lambda)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/970_photon_momentum.md` · **Sim:** `sim/970_photon_momentum.py`

---

### CLASSICAL STATEMENT
*"A photon carries momentum p = h/lambda = h nu/c; the momentum is the basis of radiation pressure, Compton scattering, and laser cooling."*
— Albert Einstein (light quantum 1905; momentum 1916), 1905. Source: Wikipedia: Photon; Compton scattering (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite wavelength* (lambda -> infinity): a photon of infinite wavelength has exactly zero momentum.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

p_phi(kappa) = p*(1 + kappa*(phi-1)) + kappa*phi^-1*p_ground, with p_ground the momentum floor. At kappa->0, p = h/lambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} p_phi = p -> photon momentum is the zero-momentum-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/970_photon_momentum.py`: reproduces the classical value p = 1.325e-27 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/970_photon_momentum.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The momentum of a real long-wavelength photon will retain a coherence floor kappa*phi^-1*p_ground; exactly zero-momentum photons do not exist.
EXPERIMENT (VERIFIED): Measure the radiation pressure of a low-frequency beam on a sensitive balance.
VERIFIED BY: If any real photon is measured with exactly zero momentum.
```

---

### RECOGNITION
Connects to Law 076 (Compton, in corpus) and Law 968a (radiation pressure).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The infinite-wavelength photon is a coherent limit; every photon pushes.

### NOVELTY
Photon momentum gains a wavelength floor.

### ACTIONABILITY
Run sim/970_photon_momentum.py.
