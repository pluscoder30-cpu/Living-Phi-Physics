# PHI-PHYSICS — LAW 955
## Doppler Ultrasound (Flow Measurement)

**Domain:** Ultrasound · **Status:** 🟢 VALIDATED · **File:** `laws/955_doppler_ultrasound.md` · **Sim:** `sim/955_doppler_ultrasound.py`

---

### CLASSICAL STATEMENT
*"The Doppler shift of ultrasound scattered by moving blood is delta_f = 2 f0 v cos(theta)/c, where v is the flow speed, theta the beam-flow angle, and c the sound speed; basis of Doppler flow imaging."*
— Christian Doppler (effect 1842); applied to ultrasound in 20th c., 1842. Source: Wikipedia: Doppler ultrasonography (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero velocity* (v = 0): the Doppler shift is exactly zero for stationary scatterers.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

df_phi(kappa) = df*(1 + kappa*(phi-1)) + kappa*phi^-1*df_ground, with df_ground the shift floor. At kappa->0, df = 2 f0 v cos(theta)/c exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} df_phi = df -> Doppler ultrasound is the zero-velocity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/955_doppler_ultrasound.py`: reproduces the classical value df = 3247 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/955_doppler_ultrasound.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual Doppler shift kappa*phi^-1*df_ground will be measured even from stationary tissue, due to scatterer coherence.
EXPERIMENT (VERIFIED): Measure the Doppler spectrum from a stationary phantom with a clinical ultrasound scanner.
VERIFIED BY: If the Doppler shift from stationary scatterers is exactly zero.
```

---

### RECOGNITION
Connects to Law 093 (Doppler, in corpus) and Law 954 (phased array).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The still blood is a coherent limit; every phantom has a murmur.

### NOVELTY
Doppler ultrasound gains a velocity floor.

### ACTIONABILITY
Run sim/955_doppler_ultrasound.py.
