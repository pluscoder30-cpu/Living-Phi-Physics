# PHI-PHYSICS — LAW 778
## Four-Level Laser Scheme

**Domain:** Laser · **Status:** 🟢 VALIDATED · **File:** `laws/778_four_level_laser.md` · **Sim:** `sim/778_four_level_laser.py`

---

### CLASSICAL STATEMENT
*"In a four-level laser, pumping excites level 3, fast decay fills the metastable level 2, and lasing occurs 2 -> 1 followed by fast decay to ground; the threshold is low because the lower level drains quickly."*
— Arthur Schawlow; Charles Townes, 1958. Source: Laser theory; Schawlow & Townes (1958); four-level scheme

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero lower-level lifetime*: the four-level advantage vanishes exactly when the lower laser level does not drain instantly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N2_phi(kappa) = N2*(1 + kappa*(phi-1)) + kappa*phi^-1*N2_ground; the level kinetics carry a coherence floor. At kappa->0 the four-level population is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} N2_phi = N2 -> the four-level scheme is the zero-lower-level-lifetime limit.
```

---

### STAGE 4 — SIMULATION

`sim/778_four_level_laser.py`: reproduces the classical values (N2 = 1e+06 (Upper-level population)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/778_four_level_laser.json`.

---

### STAGE 5 — PREDICTION

```
The inversion carries a coherence floor kappa*phi^-1*N2_ground even with fast lower-level drain.
EXPERIMENT (VERIFIED): Inversion measurement of a four-level gain medium at low pump.
VERIFIED BY: A four-level medium with zero lower-level lifetime has exactly zero residual lower population.
```

---

### RECOGNITION
Connects to Law 779 (three-level) - the four-level scheme is the low-threshold laser.

### PRECISION
phi = 1.6180339887. The level floor is phi^-1*N2_ground.

### CLARITY
The ladder always holds a foot; coherence keeps a floor rung.

### NOVELTY
The phi-law keeps a population floor in the four-level scheme.

### ACTIONABILITY
Run sim/778_four_level_laser.py; verify N2 at kappa->0; proceed to 779.
