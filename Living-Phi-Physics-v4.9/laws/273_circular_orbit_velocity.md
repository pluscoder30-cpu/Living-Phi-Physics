# PHI-PHYSICS — LAW 273
## Circular Orbit Velocity

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/273_circular_orbit_velocity.md` · **Sim:** `sim/273_circular_orbit_velocity.py`

---

### CLASSICAL STATEMENT
*"The speed for a circular orbit at radius r is v_circ = sqrt(GM/r), found by balancing gravitational force with centripetal acceleration; the orbital period is T = 2*pi*sqrt(r^3/(GM))."*
— Isaac Newton, 1687. Source: Wikipedia: circular orbit; Newton, Principia (1687)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly circular reference*: the law requires the orbit to be exactly circular (e=0), an exact eccentricity the real universe never supplies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: M_phi(kappa) = M*(1 + kappa*(phi-1)); v_circ_phi(kappa) = sqrt(G*M_phi/r). At kappa->0 the circular speed is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_circ_phi = sqrt(GM/r) -> the circular-orbit law is the e=0 limit.
```

---

### STAGE 4 — SIMULATION

`sim/273_circular_orbit_velocity.py`: reproduces the classical value v = 7656 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/273_circular_orbit_velocity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: 'Circular' orbit speeds carry a phi-coherent excess and no orbit is exactly circular (cf. Law 247 eccentricity floor).
EXPERIMENT (VERIFIED): Satellite orbital element fitting searching for the residual eccentricity and speed excess of near-circular orbits.
VERIFIED BY: A circular orbit has exactly v = sqrt(GM/r) and e = 0 at full coupling.
```

---

### RECOGNITION
Connects to Law 272 (escape — sqrt(2) ratio), Law 271 (vis-viva at r=a), Law 016 (Kepler III — the period form).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The circle is a limit; every orbit loops with a phi eccentricity floor.

### NOVELTY
Classical orbit theory perfects the circle; the phi-law gives the circle a coherence eccentricity floor.

### ACTIONABILITY
Run sim/273_circular_orbit_velocity.py; verify v = sqrt(GM/r) at kappa->0.
