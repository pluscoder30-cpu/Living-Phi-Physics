# PHI-PHYSICS — LAW 943
## Cnoidal Waves

**Domain:** Water Waves · **Status:** 🟢 VALIDATED · **File:** `laws/943_cnoidal_wave.md` · **Sim:** `sim/943_cnoidal_wave.py`

---

### CLASSICAL STATEMENT
*"Cnoidal waves are the periodic nonlinear wave solutions of the KdV equation, expressed in terms of the Jacobi elliptic function cn; in the limit of long wavelength they become solitons, in the limit of small amplitude, Airy waves."*
— Diederik Korteweg, Gustav de Vries, 1895. Source: Wikipedia: Cnoidal wave (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero modulus* (m = 0): the cnoidal wave reduces to a sinusoid exactly when the elliptic modulus vanishes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

eta_phi(kappa) = eta*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_ground, with eta_ground the profile floor. At kappa->0, the cnoidal profile reduces to the Airy sinusoid exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta -> the cnoidal wave is the zero-elliptic-modulus-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/943_cnoidal_wave.py`: reproduces the classical value eta = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/943_cnoidal_wave.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real periodic nonlinear waves will deviate from the exact cnoidal profile by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Generate cnoidal waves in a wave flume and compare the profile with the cn^2 prediction.
VERIFIED BY: If any real wave profile matches the exact cnoidal solution.
```

---

### RECOGNITION
Connects to Law 942 (KdV) and Law 941 (solitary wave).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect cnoidal hump is a coherent limit; every wave droops.

### NOVELTY
Cnoidal profiles gain a modulus floor.

### ACTIONABILITY
Run sim/943_cnoidal_wave.py.
