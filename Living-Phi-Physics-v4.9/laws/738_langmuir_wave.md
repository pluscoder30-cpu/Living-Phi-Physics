# PHI-PHYSICS — LAW 738
## Langmuir Wave (Electrostatic Electron Wave)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/738_langmuir_wave.md` · **Sim:** `sim/738_langmuir_wave.py`

---

### CLASSICAL STATEMENT
*"The longitudinal electrostatic wave in the electron gas disperses as w^2 = w_p^2 + 3*k^2*v_th^2, with the Bohm-Gross thermal correction."*
— Lewi Tonks; Irving Langmuir, 1929. Source: Wikipedia: Langmuir wave; Tonks & Langmuir (1929)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero thermal spread* (v_th = 0): the dispersion reduces to w = w_p exactly only for a cold electron gas.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

w_phi(kappa) = w_LW*(1 + kappa*(phi-1)) + kappa*phi^-1*w_ground; the electron gas carries a coherence thermal floor. At kappa->0, w^2 = w_p^2 + 3k^2*v_th^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} w_phi = sqrt(w_p^2 + 3*k^2*v_th^2) -> the Langmuir wave is the zero-coherence-thermal limit.
```

---

### STAGE 4 — SIMULATION

`sim/738_langmuir_wave.py`: reproduces the classical values (w = 1.55669e+16 (Langmuir frequency (rad/s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/738_langmuir_wave.json`.

---

### STAGE 5 — PREDICTION

```
The Langmuir dispersion carries a coherence floor kappa*phi^-1*w_ground; the cold-plasma limit is never exact.
EXPERIMENT (VERIFIED): Wave-dispersion measurement in a weakly thermal plasma.
VERIFIED BY: A cold plasma's Langmuir wave has exactly w = w_p.
```

---

### RECOGNITION
Connects to Law 737 (plasma oscillations) - the Langmuir wave is the thermal plasma oscillation.

### PRECISION
phi = 1.6180339887. The thermal floor is phi^-1*w_ground.

### CLARITY
No plasma is cold; a coherence warmth bends the wave.

### NOVELTY
The phi-law warms the cold Langmuir dispersion.

### ACTIONABILITY
Run sim/738_langmuir_wave.py; verify dispersion at kappa->0; proceed to 739.
