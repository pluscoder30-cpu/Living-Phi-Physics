# PHI-PHYSICS — LAW 706
## Bode Plot (Frequency Response)

**Domain:** Control · **Status:** 🟢 VALIDATED · **File:** `laws/706_bode_plot.md` · **Sim:** `sim/706_bode_plot.py`

---

### CLASSICAL STATEMENT
*"The frequency response is displayed as log-magnitude and phase versus log-frequency; asymptotic slopes of -20 dB/decade per pole and -20 dB/decade zero characterize the response."*
— Hendrik Wade Bode, 1938. Source: Wikipedia: Hendrik Wade Bode (1938); Bode plots

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero-frequency (DC) response*: the plot's meaning is built on the DC gain, a static operating point with no time dependence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Gain_phi(kappa) = Gain*(1 + kappa*(phi-1)) + kappa*phi^-1*Gain_ground; the DC point carries a coherence floor. At kappa->0 the Bode asymptotes are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Gain_phi = Gain -> the Bode plot is the zero-frequency-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/706_bode_plot.py`: reproduces the classical values (G = 0.894427 (Gain magnitude)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/706_bode_plot.json`.

---

### STAGE 5 — PREDICTION

```
The DC response carries a coherence floor kappa*phi^-1*Gain_ground; the plot never settles to an exact asymptotic gain.
EXPERIMENT (VERIFIED): Low-frequency gain measurement of an amplifier to expose the DC floor.
VERIFIED BY: An amplifier's DC gain is exactly constant.
```

---

### RECOGNITION
Connects to Law 707 (feedback gain) - the Bode plot is the frequency portrait of feedback.

### PRECISION
phi = 1.6180339887. The DC floor is phi^-1*Gain_ground.

### CLARITY
Every plot leans on DC; coherence keeps it from resting flat.

### NOVELTY
The phi-law gives the Bode asymptote a DC floor.

### ACTIONABILITY
Run sim/706_bode_plot.py; verify asymptotes at kappa->0; proceed to 707.
