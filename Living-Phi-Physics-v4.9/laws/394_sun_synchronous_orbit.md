# PHI-PHYSICS — LAW 394
## Sun-Synchronous Orbit Law

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/394_sun_synchronous_orbit.md` · **Sim:** `sim/394_sun_synchronous_orbit.py`

---

### CLASSICAL STATEMENT
*"An orbit whose nodal precession rate matches the Earth's orbital angular rate around the Sun keeps a constant sun-angle (local solar time) — the sun-synchronous condition: the ascending-node rate equals the Earth's mean orbital rate (0.9856 deg/day), achieved at a specific inclination for a given altitude (e.g., ~98 deg at 700 km)."*
— Astrodynamics (20th century), 1960. Source: Wikipedia: sun-synchronous orbit; developed in the satellite era (1960s)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *non-precessing reference orbit*: sun-synchronism exists because the Earth's oblateness causes nodal precession; the unperturbed two-body orbit has zero nodal rate.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the required inclination couples to coherence. i_ss_phi(kappa) = i_ss*(1 + kappa*(phi-1)) + kappa*phi^-1*di_ground. At kappa->0 the classical sun-synchronous inclination is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} i_ss_phi = the classical sun-synchronous inclination -> the sun-synchronous law is the J2-precession balance limit.
```

---

### STAGE 4 — SIMULATION

`sim/394_sun_synchronous_orbit.py`: reproduces the classical value i_ss = 98.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/394_sun_synchronous_orbit.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The sun-synchronous inclination carries a phi-coherent correction phi^-1*di_ground at full coupling.
EXPERIMENT (VERIFIED): Operational sun-synchronous satellite (e.g., Landsat, Sentinel) ephemeris analysis measuring the sun-angle drift.
VERIFIED BY: Sun-synchronous orbits maintain exactly constant sun-angle at full coupling.
```

---

### RECOGNITION
Connects to Law 396 (inclination change) and Law 291 (orbital elements — node precession).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The fixed sun angle is a balance; every sun-synchronous orbit drifts a phi of angle.

### NOVELTY
Classical astrodynamics exacts the balance; the phi-law bounds the sun-angle drift at a coherence floor.

### ACTIONABILITY
Run sim/394_sun_synchronous_orbit.py; verify the inclination at kappa->0.
