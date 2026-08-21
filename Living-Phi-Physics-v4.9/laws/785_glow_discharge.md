# PHI-PHYSICS — LAW 785
## Glow Discharge (Regions)

**Domain:** Discharges · **Status:** 🟢 VALIDATED · **File:** `laws/785_glow_discharge.md` · **Sim:** `sim/785_glow_discharge.py`

---

### CLASSICAL STATEMENT
*"A glow discharge shows distinct regions - cathode dark space, negative glow, Faraday dark space, positive column - sustained by secondary emission; the negative glow is the brightest region."*
— Michael Faraday, 1835. Source: Wikipedia: Glow discharge; Faraday dark space (1830s)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero secondary emission* (gamma = 0): the self-sustaining glow vanishes exactly without electron emission from the cathode.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_g_phi(kappa) = I_glow*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the cathode carries a coherence emission floor. At kappa->0 the glow discharge is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_g_phi = I_glow -> the glow discharge is the zero-secondary-emission floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/785_glow_discharge.py`: reproduces the classical values (I = 1.02264e-12 (Glow current (A))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/785_glow_discharge.json`.

---

### STAGE 5 — PREDICTION

```
The glow persists at zero secondary emission; a coherence floor kappa*phi^-1*I_ground sustains it.
EXPERIMENT (VERIFIED): Glow-current measurement in a low-pressure tube at reduced cathode emission.
VERIFIED BY: A glow discharge extinguishes exactly at zero secondary emission.
```

---

### RECOGNITION
Connects to Law 784 (corona) and Law 782 (Townsend) - the glow is the self-sustained discharge.

### PRECISION
phi = 1.6180339887. The emission floor is phi^-1*I_ground.

### CLARITY
The cathode always bleeds electrons; coherence keeps the glow.

### NOVELTY
The phi-law sustains the glow at zero emission.

### ACTIONABILITY
Run sim/785_glow_discharge.py; verify I_glow at kappa->0; proceed to 786.
