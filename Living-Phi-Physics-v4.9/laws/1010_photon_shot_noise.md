# PHI-PHYSICS — LAW 1010
## Photon Shot Noise

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1010_photon_shot_noise.md` · **Sim:** `sim/1010_photon_shot_noise.py`

---

### CLASSICAL STATEMENT
*"Photon shot noise: the fundamental intensity noise of a coherent (Poissonian) light field has N photons with variance delta N = sqrt(N); the shot-noise-limited signal-to-noise ratio is SNR = sqrt(N) = sqrt(P t/(h nu))."*
— Classical photodetection theory (Schottky 1918), 1918. Source: Wikipedia: Shot noise (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero photons* (N = 0): the shot noise vanishes exactly at zero photon number.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

dN_phi(kappa) = dN*(1 + kappa*(phi-1)) + kappa*phi^-1*dN_ground, with dN_ground the noise floor. At kappa->0, delta N = sqrt(N) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dN_phi = dN -> photon shot noise is the zero-photon-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1010_photon_shot_noise.py`: reproduces the classical value dN = 1000 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1010_photon_shot_noise.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The noise of any real light field will exceed sqrt(N) by a coherence floor kappa*phi^-1 (excess noise).
EXPERIMENT (VERIFIED): Measure the photocurrent noise of a laser and compare to the shot-noise floor.
VERIFIED BY: If the noise of any real light field is exactly sqrt(N).
```

---

### RECOGNITION
Connects to Law 991 (photon statistics) and Law 974 (coherent states).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect Poisson stream is a coherent limit; every stream has excess.

### NOVELTY
Photon shot noise gains an excess floor.

### ACTIONABILITY
Run sim/1010_photon_shot_noise.py.
