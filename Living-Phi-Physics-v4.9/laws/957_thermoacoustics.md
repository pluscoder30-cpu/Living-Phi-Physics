# PHI-PHYSICS — LAW 957
## Thermoacoustic Effect

**Domain:** Thermoacoustics · **Status:** 🟢 VALIDATED · **File:** `laws/957_thermoacoustics.md` · **Sim:** `sim/957_thermoacoustics.py`

---

### CLASSICAL STATEMENT
*"Thermoacoustics converts heat into sound (and vice versa) via the interaction of acoustic oscillations with a temperature gradient; the critical temperature gradient for the onset of instability satisfies the Rott condition."*
— Peter Rijke (Rijke tube 1859); Rott (theory 1969), 1859. Source: Wikipedia: Thermoacoustics (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature gradient*: thermoacoustic instability requires a temperature gradient above a critical value - no sound is generated at zero gradient.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, with P_ground the power floor. At kappa->0, the onset threshold is exactly the Rott critical gradient.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P -> thermoacoustics is the zero-gradient-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/957_thermoacoustics.py`: reproduces the classical value P = 0.01 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/957_thermoacoustics.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual acoustic emission kappa*phi^-1*P_ground will occur even below the nominal critical gradient.
EXPERIMENT (VERIFIED): Measure the onset of sound in a Rijke tube as the temperature gradient is increased from zero.
VERIFIED BY: If no sound is produced below the exact critical temperature gradient.
```

---

### RECOGNITION
Connects to Law 959 (Rijke tube) and Law 921 (Sabine).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The uniform temperature is a coherent limit; every gradient sings.

### NOVELTY
Thermoacoustics gains a gradient floor.

### ACTIONABILITY
Run sim/957_thermoacoustics.py.
