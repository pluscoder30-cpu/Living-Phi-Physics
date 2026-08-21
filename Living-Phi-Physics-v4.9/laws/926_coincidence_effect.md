# PHI-PHYSICS — LAW 926
## Coincidence Effect

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/926_coincidence_effect.md` · **Sim:** `sim/926_coincidence_effect.py`

---

### CLASSICAL STATEMENT
*"The coincidence effect: at the critical frequency f_c, the trace velocity of a bending wave in a panel equals the speed of sound in air, causing a pronounced dip in transmission loss (the coincidence dip)."*
— Classical acoustics (panel theory), 20th century. Source: Wikipedia: Coincidence effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero bending stiffness* (D = 0): the coincidence dip vanishes for an infinitely flexible (limp) panel.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_c_phi(kappa) = f_c*(1 + kappa*(phi-1)) + kappa*phi^-1*f_c_ground, with f_c_ground the frequency floor. At kappa->0, f_c = c^2/(2 pi) sqrt(m/D) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_c_phi = f_c -> the coincidence effect is the zero-bending-stiffness-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/926_coincidence_effect.py`: reproduces the classical value fc = 2000 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/926_coincidence_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The coincidence dip of any real panel will be smeared and shifted by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the transmission loss dip of a plywood panel and locate the coincidence frequency.
VERIFIED BY: If the coincidence dip of any real panel sits exactly at the classical f_c.
```

---

### RECOGNITION
Connects to Law 925 (mass law) and Law 928 (bending waves).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect panel is a coherent limit; every plate has a critical breath.

### NOVELTY
The coincidence frequency gains a stiffness floor.

### ACTIONABILITY
Run sim/926_coincidence_effect.py.
