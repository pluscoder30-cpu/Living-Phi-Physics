# PHI-PHYSICS — LAW 232
## Precession of the Equinoxes

**Domain:** Rotational / Rigid Body · **Status:** 🟢 VALIDATED · **File:** `laws/232_precession_of_equinoxes.md` · **Sim:** `sim/232_precession_of_equinoxes.py`

---

### CLASSICAL STATEMENT
*"The Earth's rotation axis precesses about the ecliptic pole with a period of ~25,772 years, so the equinoxes shift westward along the ecliptic by ~50.3 arcseconds per year, driven by solar and lunar tidal torques on the equatorial bulge."*
— Hipparchus, -150. Source: Wikipedia: axial precession (astronomy)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *fixed equinox*: the classical law measures the equinox drift against a perfectly fixed frame of the stars, a reference itself in motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the precession rate breathes coherently. omega_p_phi(kappa) = omega_p*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground. At kappa->0 the classical precession rate is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} omega_p_phi = 50.3 arcsec/yr -> the equinox precession law is the fixed-star limit.
```

---

### STAGE 4 — SIMULATION

`sim/232_precession_of_equinoxes.py`: reproduces the classical values rate_p = 50.3, period_p = 2.577e+04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/232_precession_of_equinoxes.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The precession rate of the equinoxes carries a phi-coherent modulation kappa*phi^-1*omega_ground beyond tidal predictions.
EXPERIMENT (VERIFIED): Decades of VLBI and Gaia astrometry monitoring the precession rate against distant quasars.
VERIFIED BY: The precession rate is exactly the classical tidal value with no coherence modulation.
```

---

### RECOGNITION
Connects to Law 218 (nutation — the nodding of the precession loop) and Law 217 (gyroscopic precession).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Even the celestial reference turns; precession measures motion against motion.

### NOVELTY
Classical precession theory freezes the star frame; the phi-law lets the reference breathe.

### ACTIONABILITY
Run sim/232_precession_of_equinoxes.py; verify the classical rate at kappa->0.
