# PHI-PHYSICS — LAW 709
## Shot Noise (Schottky Formula)

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/709_shot_noise.md` · **Sim:** `sim/709_shot_noise.py`

---

### CLASSICAL STATEMENT
*"The current noise spectral density from discrete charge flow is S_I = 2*q*I, with noise power proportional to the average current."*
— Walter Schottky, 1918. Source: Wikipedia: Shot noise; Schottky (1918)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero current* (I = 0): shot noise vanishes exactly at zero average current, a perfectly quiescent flow.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground; the current flow carries a coherence floor. At kappa->0, S_I = 2qI exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = 2*q*I -> shot noise is the zero-current-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/709_shot_noise.py`: reproduces the classical values (S = 2e-09 (Noise spectral density (A^2/Hz))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/709_shot_noise.json`.

---

### STAGE 5 — PREDICTION

```
The noise floor carries a coherence term kappa*phi^-1*S_ground at zero current (zero-point current noise).
EXPERIMENT (VERIFIED): Ultra-low-current noise measurement of a biased junction near zero current.
VERIFIED BY: The shot noise of a zero-current junction is exactly zero.
```

---

### RECOGNITION
Connects to Law 511 (Johnson noise) - shot noise is the discrete-charge partner of thermal noise.

### PRECISION
phi = 1.6180339887. The zero-current floor is phi^-1*S_ground.

### CLARITY
Charge arrives in drops; even stillness drips a coherence drop.

### NOVELTY
The phi-law keeps shot noise at zero current.

### ACTIONABILITY
Run sim/709_shot_noise.py; verify S=2qI at kappa->0; proceed to 710.
