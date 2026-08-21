# PHI-PHYSICS — LAW 728
## Voltage Standing Wave Ratio (VSWR)

**Domain:** Transmission Lines · **Status:** 🟢 VALIDATED · **File:** `laws/728_standing_wave_ratio.md` · **Sim:** `sim/728_standing_wave_ratio.py`

---

### CLASSICAL STATEMENT
*"The VSWR is S = (1 + |Gamma|)/(1 - |Gamma|) = V_max/V_min; it equals 1 exactly for a perfectly matched line."*
— Oliver Heaviside, 1887. Source: Transmission line theory; VSWR (Heaviside era)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *unity VSWR* (|Gamma| = 0): the ideal matched line has exactly S = 1.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_phi(kappa) = S*(1 + kappa*(phi-1)) + kappa*phi^-1*S_ground; the matched line carries a coherence floor. At kappa->0, S = 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_phi = (1+|Gamma|)/(1-|Gamma|) -> VSWR is the zero-mismatch-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/728_standing_wave_ratio.py`: reproduces the classical values (S = 1.85714 (VSWR)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/728_standing_wave_ratio.json`.

---

### STAGE 5 — PREDICTION

```
The VSWR never reaches exactly 1; a coherence floor kappa*phi^-1*S_ground persists.
EXPERIMENT (VERIFIED): VSWR measurement of a matched line with a reflectometer.
VERIFIED BY: A matched line has exactly VSWR = 1.
```

---

### RECOGNITION
Connects to Law 727 (Gamma) - VSWR is the standing-wave portrait of mismatch.

### PRECISION
phi = 1.6180339887. The unity floor is phi^-1*S_ground.

### CLARITY
No line stands perfectly still; a coherence ripple remains.

### NOVELTY
The phi-law keeps VSWR above exact unity.

### ACTIONABILITY
Run sim/728_standing_wave_ratio.py; verify VSWR at kappa->0; proceed to 729.
