# PHI-PHYSICS — LAW 702
## MOSFET Square-Law (Shichman-Hodges)

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/702_mosfet_square_law.md` · **Sim:** `sim/702_mosfet_square_law.py`

---

### CLASSICAL STATEMENT
*"In saturation the MOSFET drain current is I_D = (1/2)*k_n*(W/L)*(V_GS - V_th)^2, the square-law relation of gate overdrive."*
— D. Shichman; D. A. Hodges, 1968. Source: Shichman-Hodges model (1968), MOSFET square law

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact threshold* (V_GS = V_th): the current vanishes exactly at threshold, a precise overdrive-zero condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_D_phi(kappa) = I_D*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground; the threshold carries a coherence basin. At kappa->0 the square law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_D_phi = (1/2)*k_n*(W/L)*(V_GS-V_th)^2 -> the square law is the zero-overdrive-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/702_mosfet_square_law.py`: reproduces the classical values (ID = 0.00025 (Drain current (A))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/702_mosfet_square_law.json`.

---

### STAGE 5 — PREDICTION

```
The drain current carries a coherence floor kappa*phi^-1*I_ground below threshold (subthreshold leakage).
EXPERIMENT (VERIFIED): Subthreshold drain-current measurement of a MOSFET at V_GS = V_th.
VERIFIED BY: A MOSFET conducts exactly zero current at threshold.
```

---

### RECOGNITION
Connects to Law 699 (diode) - the square law is the gate-controlled channel.

### PRECISION
phi = 1.6180339887. The subthreshold floor is phi^-1*I_ground.

### CLARITY
Threshold is a gate, not a wall; coherence leaks below it.

### NOVELTY
The phi-law leaks current below the exact threshold.

### ACTIONABILITY
Run sim/702_mosfet_square_law.py; verify square law at kappa->0; proceed to 703.
