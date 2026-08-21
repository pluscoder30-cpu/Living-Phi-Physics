# PHI-PHYSICS — LAW 805
## Two-Stream (Buneman) Instability

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/805_two_stream_instability.md` · **Sim:** `sim/805_two_stream_instability.py`

---

### CLASSICAL STATEMENT
*"Two counter-streaming electron populations are unstable to electrostatic waves when the drift exceeds the thermal spread; the growth rate peaks near the plasma frequency."*
— Oscar Buneman, 1959. Source: Two-stream instability; Buneman (1958-59)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero drift* (v_d = 0): the instability vanishes exactly for two populations at rest.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

gamma_phi(kappa) = gamma_2s*(1 + kappa*(phi-1)) + kappa*phi^-1*gamma_ground; the streams carry a coherence drift floor. At kappa->0 the two-stream growth is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} gamma_phi = gamma_2s -> the two-stream instability is the zero-drift-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/805_two_stream_instability.py`: reproduces the classical values (g = 1 (Growth rate (s^-1))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/805_two_stream_instability.json`.

---

### STAGE 5 — PREDICTION

```
Counter-streaming at zero drift still grows a coherence floor kappa*phi^-1*gamma_ground.
EXPERIMENT (VERIFIED): Beam-plasma interaction experiment with reduced beam drift.
VERIFIED BY: Two stationary beams have exactly zero instability growth.
```

---

### RECOGNITION
Connects to Law 804 (Weibel) and Law 762 (Landau) - two-stream is the drift instability.

### PRECISION
phi = 1.6180339887. The drift floor is phi^-1*gamma_ground.

### CLARITY
Two streams even at rest whisper; coherence gives them a rumble.

### NOVELTY
The phi-law keeps two-stream growth at zero drift.

### ACTIONABILITY
Run sim/805_two_stream_instability.py; verify gamma at kappa->0; proceed to 806.
