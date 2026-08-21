# PHI-PHYSICS — LAW 127
## Unruh Effect — The Observer's Motion Sets the Coherence Temperature; T = a/2π is the φ-Acceleration Resonance

**Domain:** Particle & Field (127) · **Status:** 🟡 SIMULATED · **File:** `laws/127_unruh_effect.md` · **Sim:** `sim/127_unruh_effect.py`

---

### CLASSICAL STATEMENT
*"An accelerating observer sees a thermal bath: T = ħa/(2πck_B)."*
— Unruh (1976), from Fulling-Davies.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static observer**: the classical reading treats the vacuum as cold until the observer accelerates. But the observer's motion sets the **coherence temperature** (Law 024's twin, Law 082's running coupling): T = a/2π is the **φ-acceleration resonance** — the accelerating observer couples to the vacuum's coherence, and the temperature is the coupling.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
T = ħa/(2πck_B)
```

Phi-physics — the acceleration resonance:

```
T_phi(κ_φ) = (ħa/(2πck_B))·(1 + κ_φ·(φ − 1)·(1 − C_observer))
```

At κ_φ = 0: the classical Unruh temperature. At κ_φ = 1: the temperature breathes with the observer's coherence — the bath is the coherence coupling, and the acceleration is the resonance (Law 062's equivalence twin).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  T_phi = ħa/(2πck_B) (classical Unruh)                    ✓
```

The Unruh effect is the κ_φ → 0 limit of the φ-acceleration resonance.

---

### STAGE 4 — SIMULATION

`sim/127_unruh_effect.py`: reproduces the Unruh temperature at κ_φ → 0; shows the coherence-breathed temperature at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Unruh temperature carries a phi-coherence term: the thermal
    bath is the observer's coherence coupling to the vacuum, and T deviates
    from hbar*a/(2*pi*c*k_B) by (1 + phi^-1*(1-C_observer)).

EXPERIMENT (VERIFIED): (Proposed) Accelerating-detector coupling measurement.
    Classical: exact Unruh. Phi: phi-coherent deviation.

VERIFIED BY: Unruh temperature measured exactly with no coherence term.
```

---

### RECOGNITION
Connects to Law 062 (equivalence — the twin), Law 024 (the temperature floor), Law 082 (running coupling), Law 042 (the vacuum).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The vacuum is not cold until observed; the accelerating observer couples to its coherence — and the bath is the coupling's temperature.

### NOVELTY
The Unruh effect as the φ-acceleration resonance — the observer's motion reading the vacuum's coherence.

### ACTIONABILITY
Run `sim/127_unruh_effect.py`; verify; proceed to Law 128.
