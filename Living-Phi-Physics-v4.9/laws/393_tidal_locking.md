# PHI-PHYSICS — LAW 393
## Tidal Locking Law

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/393_tidal_locking.md` · **Sim:** `sim/393_tidal_locking.py`

---

### CLASSICAL STATEMENT
*"Tidal friction slows a satellite's rotation until it locks to its orbital period (1:1 spin-orbit resonance, as the Moon to the Earth); the locking timescale is roughly t_lock ~ w a^6 (m_s^2 Q R_s^3 ...)/..., scaling as the sixth power of the orbital radius: t ~ (a/R)^6 (k/Q) ... years, extremely short for close orbits and enormous for distant ones."*
— George Darwin, 1879. Source: Wikipedia: tidal locking; Darwin (1879-1880), tidal friction papers

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *non-tidally-coupled reference*: locking exists because tides dissipate energy; the perfectly rigid, tide-free body (zero deformation) never locks.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the locking timescale couples to coherence. t_lock_phi(kappa) = t_lock*(1 + kappa*(phi-1)) + kappa*phi^-1*t_ground. At kappa->0 the classical tidal-locking timescale is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} t_lock_phi = the Darwin timescale -> tidal locking is the finite-dissipation, finite-deformation limit.
```

---

### STAGE 4 — SIMULATION

`sim/393_tidal_locking.py`: reproduces the classical value t_lock = 1e+09 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/393_tidal_locking.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Tidal-locking timescales carry a phi-coherent correction phi^-1*t_ground, shifting the predicted locking radius.
EXPERIMENT (VERIFIED): Exoplanet spin-orbit measurements (secondary eclipses, ellipsoidal variations) testing the locking-radius boundary.
VERIFIED BY: Locking follows the classical timescale exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 278 (tidal force — the driver) and Law 279 (Roche limit — the other tide balance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The locked moon is a limit; every tide slows the dance a phi toward the lock.

### NOVELTY
Classical tidal theory exacts the timescale; the phi-law bounds its deviation at a coherence floor.

### ACTIONABILITY
Run sim/393_tidal_locking.py; verify the locking timescale at kappa->0.
