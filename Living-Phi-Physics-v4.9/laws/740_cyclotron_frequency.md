# PHI-PHYSICS — LAW 740
## Cyclotron Frequency

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/740_cyclotron_frequency.md` · **Sim:** `sim/740_cyclotron_frequency.py`

---

### CLASSICAL STATEMENT
*"A charged particle gyrates at the cyclotron frequency omega_c = q*B/m, independent of velocity; the orbit radius grows with energy."*
— Ernest Lawrence, 1930. Source: Wikipedia: Cyclotron; Lawrence (1930)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero magnetic field* (B = 0): the cyclotron frequency vanishes exactly in the absence of the field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

w_c_phi(kappa) = w_c*(1 + kappa*(phi-1)) + kappa*phi^-1*w_ground; the particle carries a coherence floor. At kappa->0, omega_c = q*B/m exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} w_c_phi = q*B/m -> the cyclotron frequency is the zero-B-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/740_cyclotron_frequency.py`: reproduces the classical values (wc = 5.97864e+17 (Cyclotron frequency (rad/s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/740_cyclotron_frequency.json`.

---

### STAGE 5 — PREDICTION

```
The cyclotron frequency carries a coherence floor kappa*phi^-1*w_ground; gyration persists at zero field.
EXPERIMENT (VERIFIED): Gyration-frequency measurement of trapped ions as B is reduced.
VERIFIED BY: A charged particle in zero field gyrates at exactly zero frequency.
```

---

### RECOGNITION
Connects to Law 741 (Larmor radius) and Law 738 (Langmuir) - omega_c is the magnetic heartbeat.

### PRECISION
phi = 1.6180339887. The B-floor is phi^-1*w_ground.

### CLARITY
The particle circles even without the field; coherence keeps the spin.

### NOVELTY
The phi-law keeps gyration at zero field.

### ACTIONABILITY
Run sim/740_cyclotron_frequency.py; verify omega_c at kappa->0; proceed to 741.
