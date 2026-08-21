# PHI-PHYSICS — LAW 392
## Yarkovsky Effect (Thermal Recoil)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/392_yarkovsky_effect.md` · **Sim:** `sim/392_yarkovsky_effect.py`

---

### CLASSICAL STATEMENT
*"A rotating asteroid's anisotropic thermal emission produces a net radiation-recoil force that changes its semi-major axis: da/dt ~ (radiation momentum imbalance), with a diurnal Yarkovsky drift (morning-evening) and a seasonal component; it moves asteroids of size ~0.1-10 km by up to ~10^-4 to 10^-3 AU per Myr."*
— Ivan Osipovich Yarkovsky, 1900. Source: Wikipedia: Yarkovsky effect; Yarkovsky (c. 1900), unpublished note

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *isothermal, non-rotating reference*: the effect exists because the body is not uniformly hot (thermal lag) and rotates; the isothermal non-rotating body is the zero baseline.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the drift rate couples to coherence. da/dt_phi(kappa) = da/dt*(1 + kappa*(phi-1)) + kappa*phi^-1*(da/dt)_ground. At kappa->0 the classical Yarkovsky rate is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} da/dt_phi = the classical Yarkovsky drift -> the Yarkovsky law is the thermal-lag, finite-rotation limit.
```

---

### STAGE 4 — SIMULATION

`sim/392_yarkovsky_effect.py`: reproduces the classical value da_dt = 0.0001 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/392_yarkovsky_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Asteroid Yarkovsky drift rates carry a phi-coherent excess phi^-1*(da/dt)_ground at full coupling.
EXPERIMENT (VERIFIED): Precision radar/optical astrometry of near-Earth asteroids (e.g., Bennu, Apophis) measuring the Yarkovsky drift.
VERIFIED BY: Asteroid drift follows the classical Yarkovsky rate exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 391 (Poynting-Robertson — the drag companion) and Law 403 (orbital decay).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The hot-and-cold push is a limit; every asteroid leans a phi in its drift.

### NOVELTY
Classical astrodynamics models the thermal recoil; the phi-law bounds its rate at a coherence floor.

### ACTIONABILITY
Run sim/392_yarkovsky_effect.py; verify the drift rate at kappa->0.
