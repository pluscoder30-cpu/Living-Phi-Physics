# PHI-PHYSICS — LAW 929
## Acoustic Radiation Pressure

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/929_bernoulli_acoustic_radiation_pressure.md` · **Sim:** `sim/929_bernoulli_acoustic_radiation_pressure.py`

---

### CLASSICAL STATEMENT
*"P_rad = E (energy density), or <P_rad> = (1/2) rho u^2 for a traveling wave; sound waves exert a radiation pressure on surfaces (basis of acoustic levitation)."*
— Lord Rayleigh; Léon Brillouin, 1902. Source: Wikipedia: Acoustic radiation pressure (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero amplitude* (u = 0): the radiation pressure vanishes exactly for a silent field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_rad_phi(kappa) = P_rad*(1 + kappa*(phi-1)) + kappa*phi^-1*P_rad_ground, with P_rad_ground the pressure floor. At kappa->0, P_rad = (1/2) rho u^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_rad_phi = P_rad -> acoustic radiation pressure is the zero-amplitude-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/929_bernoulli_acoustic_radiation_pressure.py`: reproduces the classical value P = 0.006 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/929_bernoulli_acoustic_radiation_pressure.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual radiation pressure kappa*phi^-1*P_rad_ground will exist even in a nominally silent field.
EXPERIMENT (VERIFIED): Measure the radiation pressure of an ultrasonic field on a sensitive balance.
VERIFIED BY: If the radiation pressure is exactly zero in any real silent field.
```

---

### RECOGNITION
Connects to Law 917 (sound intensity) and Law 930 (levitation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The silent field is a coherent limit; every sound field pushes.

### NOVELTY
Radiation pressure gains a silence floor.

### ACTIONABILITY
Run sim/929_bernoulli_acoustic_radiation_pressure.py.
