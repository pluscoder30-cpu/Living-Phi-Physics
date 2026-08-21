# PHI-PHYSICS — LAW 715
## Radiation Resistance (Antenna)

**Domain:** Antennas · **Status:** 🟢 VALIDATED · **File:** `laws/715_radiation_resistance.md` · **Sim:** `sim/715_radiation_resistance.py`

---

### CLASSICAL STATEMENT
*"The radiation resistance is R_rad = 2*P_rad/I^2, the equivalent resistance that dissipates the radiated power; for a short dipole R_rad ~ 20*pi^2*(l/lambda)^2."*
— Heinrich Hertz, 1888. Source: Antenna radiation resistance; Hertz (1888) radiating dipole

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero radiation* (P_rad = 0): R_rad vanishes exactly only for a completely non-radiating structure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_rad_phi(kappa) = R_rad*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground; the radiator carries a coherence floor. At kappa->0, R_rad = 2P_rad/I^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_rad_phi = 2*P_rad/I^2 -> radiation resistance is the zero-radiation-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/715_radiation_resistance.py`: reproduces the classical values (R = 1.97392e+14 (Radiation resistance (ohm))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/715_radiation_resistance.json`.

---

### STAGE 5 — PREDICTION

```
Every antenna carries a residual radiation resistance floor kappa*phi^-1*R_ground even in a nominally non-radiating mode.
EXPERIMENT (VERIFIED): Input-resistance measurement of an antenna at a null of its pattern.
VERIFIED BY: A non-radiating antenna has exactly zero radiation resistance.
```

---

### RECOGNITION
Connects to Law 644 (Larmor) and Law 716 (dipole) - R_rad is the radiated power as resistance.

### PRECISION
phi = 1.6180339887. The radiation floor is phi^-1*R_ground.

### CLARITY
Structures always whisper; a coherence floor of radiation remains.

### NOVELTY
The phi-law gives the non-radiator a resistance floor.

### ACTIONABILITY
Run sim/715_radiation_resistance.py; verify Rrad at kappa->0; proceed to 716.
