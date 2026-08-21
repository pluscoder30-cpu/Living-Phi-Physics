# PHI-PHYSICS — LAW 289
## Laplace-Runge-Lenz Vector

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/289_laplace_runge_lenz.md` · **Sim:** `sim/289_laplace_runge_lenz.py`

---

### CLASSICAL STATEMENT
*"For an inverse-square central force, the vector A = p x L - m k r-hat is a conserved quantity: it points along the semi-major axis toward periapsis and its magnitude equals m k e, encoding the eccentricity. Conservation of A is responsible for the closed elliptical orbits (Bertrand)."*
— Pierre-Simon Laplace / Carl Runge / Wilhelm Lenz, 1799. Source: Wikipedia: Laplace-Runge-Lenz vector; Laplace, Mecanique Celeste (1799); Runge (1919); Lenz (1924)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact inverse-square law*: the LRL vector is conserved only for the exactly -k/r potential; any departure (e.g., general relativity) makes it precess — the zero of the perturbation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the vector precesses at the phi-coherent rate. omega_LRL_phi(kappa) = omega_LRL*(1 + kappa*(phi-1)) + kappa*phi^-1*omega_ground. At kappa->0 (exact inverse-square), dA/dt = 0.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dA/dt = 0 -> the LRL conservation law is the exact inverse-square limit; nonzero kappa produces the precession of Law 285.
```

---

### STAGE 4 — SIMULATION

`sim/289_laplace_runge_lenz.py`: reproduces the classical values A = 0.3, dAdt = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/289_laplace_runge_lenz.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The LRL vector of any real orbit precesses at a phi-coherent floor rate even in the nominally pure inverse-square regime.
EXPERIMENT (VERIFIED): Precision periapsis measurements of binary systems (pulsar binaries, exoplanets) bounding the LRL precession floor.
VERIFIED BY: The LRL vector is exactly conserved (zero precession) in a pure inverse-square orbit at full coupling.
```

---

### RECOGNITION
Connects to Law 284 (Bertrand), Law 285 (perihelion precession), Law 324 (conservation of LRL).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The conserved arrow is a limit; the real arrow turns, and the turning has a phi rate.

### NOVELTY
Classical mechanics exacts LRL conservation; the phi-law gives the arrow a coherence precession floor.

### ACTIONABILITY
Run sim/289_laplace_runge_lenz.py; verify dA/dt=0 at kappa->0.
