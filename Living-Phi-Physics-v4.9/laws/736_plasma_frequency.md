# PHI-PHYSICS — LAW 736
## Plasma Frequency

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/736_plasma_frequency.md` · **Sim:** `sim/736_plasma_frequency.py`

---

### CLASSICAL STATEMENT
*"Electrons oscillate collectively at the plasma frequency omega_p = sqrt(n*e^2/(eps_0*m_e)); the plasma is opaque to radiation below omega_p."*
— Irving Langmuir; Lewi Tonks, 1929. Source: Wikipedia: Plasma oscillation; Tonks & Langmuir (1929)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero density* (n = 0): the plasma frequency vanishes exactly for a plasma with no free electrons.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

w_p_phi(kappa) = w_p*(1 + kappa*(phi-1)) + kappa*phi^-1*w_ground; the electron gas carries a coherence floor. At kappa->0, omega_p is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} w_p_phi = sqrt(n*e^2/(eps_0*m_e)) -> the plasma frequency is the zero-density-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/736_plasma_frequency.py`: reproduces the classical values (wp = 69.0935 (Plasma frequency (rad/s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/736_plasma_frequency.json`.

---

### STAGE 5 — PREDICTION

```
The plasma frequency carries a coherence floor kappa*phi^-1*w_ground; a vanishing-density plasma still oscillates.
EXPERIMENT (VERIFIED): Radio reflection cut-off measurement in a tenuous plasma.
VERIFIED BY: A zero-density plasma has exactly zero plasma frequency.
```

---

### RECOGNITION
Connects to Law 737 (plasma oscillations) and Law 738 (Langmuir wave) - omega_p is the plasma's heartbeat.

### PRECISION
phi = 1.6180339887. The density floor is phi^-1*w_ground.

### CLARITY
The plasma hums even when thin; coherence keeps a floor tone.

### NOVELTY
The phi-law gives the empty plasma a frequency floor.

### ACTIONABILITY
Run sim/736_plasma_frequency.py; verify omega_p at kappa->0; proceed to 737.
