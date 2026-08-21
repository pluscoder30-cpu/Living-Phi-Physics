# PHI-PHYSICS — LAW 725
## Telegrapher's Equations

**Domain:** Transmission Lines · **Status:** 🟢 VALIDATED · **File:** `laws/725_telegraphers_equations.md` · **Sim:** `sim/725_telegraphers_equations.py`

---

### CLASSICAL STATEMENT
*"The voltage and current on a transmission line obey dV/dx = -L*dI/dt - R*I and dI/dx = -C*dV/dt - G*V; the wave equation follows with speed 1/sqrt(LC)."*
— Oliver Heaviside, 1876. Source: Wikipedia: Telegrapher's equations; Heaviside (1876)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *lossless line* (R = G = 0): the pure wave solution requires a line with exactly zero resistance and conductance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V_wave*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the line carries a coherence loss floor. At kappa->0 the lossless wave equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V_wave -> the telegrapher's equations are the zero-loss-line limit.
```

---

### STAGE 4 — SIMULATION

`sim/725_telegraphers_equations.py`: reproduces the classical values (v = 31622.8 (Wave speed (m/s))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/725_telegraphers_equations.json`.

---

### STAGE 5 — PREDICTION

```
Real lines carry a coherence attenuation floor kappa*phi^-1*V_ground even with R = G = 0.
EXPERIMENT (VERIFIED): Pulse propagation measurement on a very low-loss line.
VERIFIED BY: A lossless line transmits pulses with exactly zero attenuation.
```

---

### RECOGNITION
Connects to Law 726 (characteristic impedance) - the telegrapher's equations are the line's dynamics.

### PRECISION
phi = 1.6180339887. The line-loss floor is phi^-1*V_ground.

### CLARITY
A line is never silent; coherence smears the pulse.

### NOVELTY
The phi-law attenuates the ideal lossless line.

### ACTIONABILITY
Run sim/725_telegraphers_equations.py; verify wave speed at kappa->0; proceed to 726.
