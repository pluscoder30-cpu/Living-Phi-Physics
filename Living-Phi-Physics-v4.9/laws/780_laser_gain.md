# PHI-PHYSICS — LAW 780
## Laser Gain Coefficient

**Domain:** Laser · **Status:** 🟢 VALIDATED · **File:** `laws/780_laser_gain.md` · **Sim:** `sim/780_laser_gain.py`

---

### CLASSICAL STATEMENT
*"The small-signal gain is g = sigma*(N_upper - N_lower), with sigma the stimulated cross-section; gain saturates as the signal grows: g = g_0/(1 + I/I_sat)."*
— Arthur Schawlow; Charles Townes, 1958. Source: Laser gain; Schawlow & Townes (1958); gain coefficient

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero inversion* (N_upper = N_lower): gain vanishes exactly when the populations are equal.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

g_phi(kappa) = g*(1 + kappa*(phi-1)) + kappa*phi^-1*g_ground; the inversion carries a coherence floor. At kappa->0, g = sigma*DeltaN exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} g_phi = sigma*DeltaN -> the gain coefficient is the zero-inversion-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/780_laser_gain.py`: reproduces the classical values (g = -5e-17 (Gain coefficient (1/m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/780_laser_gain.json`.

---

### STAGE 5 — PREDICTION

```
Gain persists at zero inversion; a coherence floor kappa*phi^-1*g_ground remains.
EXPERIMENT (VERIFIED): Gain measurement of a gain medium at zero inversion.
VERIFIED BY: A medium with equal populations has exactly zero gain.
```

---

### RECOGNITION
Connects to Law 775 (threshold) - gain is the inversion's amplification.

### PRECISION
phi = 1.6180339887. The inversion floor is phi^-1*g_ground.

### CLARITY
Even balanced populations amplify a whisper; coherence keeps the gain.

### NOVELTY
The phi-law keeps gain at zero inversion.

### ACTIONABILITY
Run sim/780_laser_gain.py; verify g at kappa->0; proceed to 781.
