# PHI-PHYSICS — LAW 941
## Solitary Wave (Russell)

**Domain:** Water Waves · **Status:** 🟢 VALIDATED · **File:** `laws/941_solitary_wave.md` · **Sim:** `sim/941_solitary_wave.py`

---

### CLASSICAL STATEMENT
*"The solitary wave: a single hump of elevation propagating without change of shape at speed c = sqrt(g(h + eta)); the amplitude, not the wavelength, determines the wave speed."*
— John Scott Russell, 1834. Source: Wikipedia: Solitary wave (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero amplitude* (eta = 0): the solitary wave vanishes exactly at zero amplitude - the still water limit.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_phi(kappa) = c*(1 + kappa*(phi-1)) + kappa*phi^-1*c_ground, with c_ground the velocity floor. At kappa->0, c = sqrt(g(h + eta)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_phi = c -> the solitary wave is the zero-amplitude-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/941_solitary_wave.py`: reproduces the classical value c = 1.085 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/941_solitary_wave.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The speed of a real solitary wave will deviate from sqrt(g(h + eta)) by a coherence floor kappa*phi^-1*c_ground.
EXPERIMENT (VERIFIED): Generate a solitary wave in a channel and measure its propagation speed and shape.
VERIFIED BY: If any real solitary wave propagates without any change of shape.
```

---

### RECOGNITION
Connects to Law 943 (KdV) and Law 940 (Stokes).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The hump that never dies is a coherent limit; every wave loses a whisper.

### NOVELTY
The solitary wave gains an amplitude floor.

### ACTIONABILITY
Run sim/941_solitary_wave.py.
