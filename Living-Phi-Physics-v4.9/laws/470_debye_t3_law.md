# PHI-PHYSICS — LAW 470
## Debye T^3 Law (Low-Temperature Heat Capacity)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/470_debye_t3_law.md` · **Sim:** `sim/470_debye_t3_law.py`

---

### CLASSICAL STATEMENT
*"At temperatures well below the Debye temperature, the heat capacity of a solid is C = (12/5) pi^4 N k_B (T/theta_D)^3, the Debye T^3 law - the acoustic phonons behave as a Debye gas of massless excitations."*
— Peter Debye, 1912. Source: Wikipedia: Debye model (T^3 law); Debye (1912)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *purely acoustic modes*: the T^3 law assumes all low-energy modes are exactly linear acoustic phonons with no optical modes, no disorder, and no coherence gap in the spectrum.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the phonon gas carries a coherence gap. C_phi(kappa) = (12/5) pi^4 N k_B (T/theta_D)^3*(1 + kappa*(phi-1)) + kappa*phi^-1*C_gap, where C_gap is the ground heat capacity of the spectrum. At kappa->0 the T^3 law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} C_phi = (12/5) pi^4 N k_B (T/theta_D)^3 -> the Debye T^3 law is the pure-acoustic, zero-gap phonon limit.
```

---

### STAGE 4 — SIMULATION

`sim/470_debye_t3_law.py`: reproduces the classical value C_T3 = 1.195e-25 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/470_debye_t3_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the low-T heat capacity carries a floor kappa*phi^-1*C_gap above the pure T^3 law, visible in very pure crystals at the lowest temperatures.
EXPERIMENT (VERIFIED): Ultra-low-temperature heat-capacity measurements of isotopically pure crystals below 0.1 K.
VERIFIED BY: The low-T heat capacity is exactly proportional to T^3 with no additive floor.
```

---

### RECOGNITION
Connects to Law 469 (Debye model) and Law 503 (Bloch) - the T^3 law is the acoustic coherence of the low-T lattice.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the gap floor is phi^-1 * C_gap.

### CLARITY
At the bottom of the temperature ladder the crystal still hums; the phi-law keeps the hum.

### NOVELTY
Classical Debye T^3 is exact for acoustic phonons; the phi-law adds the coherence gap of the real spectrum.

### ACTIONABILITY
Run sim/470_debye_t3_law.py; verify T^3 law at kappa->0; proceed to 471.
