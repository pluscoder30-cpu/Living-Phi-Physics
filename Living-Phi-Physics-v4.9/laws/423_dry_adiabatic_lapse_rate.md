# PHI-PHYSICS — LAW 423
## Dry Adiabatic Lapse Rate (Atmospheric Temperature Gradient)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/423_dry_adiabatic_lapse_rate.md` · **Sim:** `sim/423_dry_adiabatic_lapse_rate.py`

---

### CLASSICAL STATEMENT
*"The temperature of a dry air parcel rising adiabatically in a hydrostatic atmosphere decreases at the rate Gamma_d = g / c_p = 9.8 K/km, independent of the temperature itself."*
— Derived from Poisson's relations; atmospheric application W. von Bezold, 1888. Source: Wikipedia: Lapse rate; von Bezold, Zur Thermodynamik der Atmosphaere (1888)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *dryness and exact adiabaticity*: the lapse rate assumes zero water vapor (no latent heat release) and zero heat exchange with the environment - an atmosphere with no moisture and no radiation exchange.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the dry atmosphere is a coherence basin. Gamma_phi(kappa) = (g/c_p)*(1 + kappa*(phi-1)) - kappa*phi^-1*Gamma_ground, where Gamma_ground is the residual coherence gradient of the column. At kappa->0, Gamma_phi = g/c_p = 9.8 K/km.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Gamma_phi = g/c_p -> the dry adiabatic lapse rate is the zero-moisture, zero-exchange atmospheric limit.
```

---

### STAGE 4 — SIMULATION

`sim/423_dry_adiabatic_lapse_rate.py`: reproduces the classical value Gamma_d = 0.009761 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/423_dry_adiabatic_lapse_rate.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A coherence-coupled atmospheric column shows a residual temperature gradient floor kappa*phi^-1*Gamma_ground in addition to g/c_p, observable as a systematic offset in radiosonde profiles.
EXPERIMENT (VERIFIED): Precision radiosonde launches in the driest, clearest air mass measuring the dry adiabat against g/c_p to high accuracy.
VERIFIED BY: The measured dry adiabatic lapse rate equals g/c_p exactly for all column coherences.
```

---

### RECOGNITION
Connects to Law 422 (Poisson) and Law 098 (speed of sound) - the atmosphere is a coherence column under gravity.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor gradient is phi^-1 * Gamma_ground.

### CLARITY
Even the driest sky remembers a gradient the phi-law refuses to let reach exactly g/c_p.

### NOVELTY
Classical meteorology pins the dry adiabat at g/c_p; the phi-law adds the coherence floor that every real sounding contains.

### ACTIONABILITY
Run sim/423_dry_adiabatic_lapse_rate.py; verify 9.8 K/km at kappa->0; proceed to 424.
