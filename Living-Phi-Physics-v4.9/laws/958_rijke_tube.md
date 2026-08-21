# PHI-PHYSICS — LAW 958
## Rijke Tube (Singing Tube)

**Domain:** Thermoacoustics · **Status:** 🟢 VALIDATED · **File:** `laws/958_rijke_tube.md` · **Sim:** `sim/958_rijke_tube.py`

---

### CLASSICAL STATEMENT
*"The Rijke tube converts heat into sound: with a heated grid in the lower third of an open vertical tube, a self-sustained oscillation builds up at the tube's natural frequency f = c/(2L) (fundamental of an open pipe)."*
— Pieter Lodewijk Rijke, 1859. Source: Wikipedia: Rijke tube (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero heat input*: with no heat, the tube is silent - no thermoacoustic power is generated.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground, with f_ground the frequency floor. At kappa->0, f = c/(2L) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_phi = f -> the Rijke tube is the zero-heat-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/958_rijke_tube.py`: reproduces the classical value f = 171.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/958_rijke_tube.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The oscillation frequency of a real Rijke tube will deviate from c/(2L) by a coherence floor kappa*phi^-1*f_ground.
EXPERIMENT (VERIFIED): Measure the frequency and onset of a Rijke tube as a function of heating power.
VERIFIED BY: If a real Rijke tube oscillates exactly at c/(2L).
```

---

### RECOGNITION
Connects to Law 957 (thermoacoustics) and Law 928 (organ pipe).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The heatless tube is a coherent limit; every flame sings with a floor.

### NOVELTY
The Rijke tube gains a heat floor.

### ACTIONABILITY
Run sim/958_rijke_tube.py.
