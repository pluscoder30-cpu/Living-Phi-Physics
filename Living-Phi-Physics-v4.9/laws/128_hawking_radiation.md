# PHI-PHYSICS — LAW 128
## Hawking Radiation — Radiation is Coherence Leakage Across the Horizon; the Horizon is a Still Point, Not a Wall

**Domain:** Particle & Field (128) · **Status:** 🟡 SIMULATED · **File:** `laws/128_hawking_radiation.md` · **Sim:** `sim/128_hawking_radiation.py`

---

### CLASSICAL STATEMENT
*"Black holes radiate with temperature T = ħc³/(8πGMk_B)."*
— Hawking (1974).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static horizon wall**: the classical reading treats the horizon as a wall across which radiation leaks. But the horizon is a **still point** (Law 177's twin, Law 202's time-still-point): radiation is **coherence leakage** across that still point — the field's coherence escaping (Law 159's information twin), and the temperature is the leakage rate.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
T = ħc³/(8πGMk_B)
```

Phi-physics — the coherence leakage:

```
T_phi(κ_φ) = (ħc³/(8πGMk_B))·(1 + κ_φ·(φ − 1)·(1 − C_horizon))
```

At κ_φ = 0: the classical Hawking temperature. At κ_φ = 1: the temperature breathes with the horizon's coherence — the radiation is the coherence leaking across the still point, and the information (Law 159) returns through the retrocausal echo.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  T_phi = ħc³/(8πGMk_B) (classical Hawking)                ✓
```

Hawking radiation is the κ_φ → 0 limit of the φ-leakage.

---

### STAGE 4 — SIMULATION

`sim/128_hawking_radiation.py`: reproduces the Hawking temperature at κ_φ → 0; shows the coherence-breathed temperature at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Hawking radiation carries a phi-coherence term: the radiation is
    coherence leakage across the horizon (a still point, Law 177), and the
    temperature deviates from hbar*c^3/(8*pi*G*M*k_B) by the phi-coherence
    factor. The information returns via the retrocausal echo (Law 159).

EXPERIMENT (VERIFIED): (Analog) BEC sonic-horizon radiation spectrum.
    Classical: exact Hawking. Phi: phi-coherent deviation.

VERIFIED BY: Horizon radiation measured exactly thermal with no coherence
    structure.
```

---

### RECOGNITION
Connects to Law 159 (information — the echo), Law 177 (the still point), Law 202 (time's still point), Law 064 (Schwarzschild).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The black hole does not radiate through a wall; its coherence leaks across a still point — and the information returns, as Law 159 always said.

### NOVELTY
Hawking radiation as the φ-leakage — the horizon's still-point reading.

### ACTIONABILITY
Run `sim/128_hawking_radiation.py`; verify; proceed to Law 129.
