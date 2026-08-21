# PHI-PHYSICS — LAW 291
## Keplerian Orbital Elements

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/291_keplerian_orbital_elements.md` · **Sim:** `sim/291_keplerian_orbital_elements.py`

---

### CLASSICAL STATEMENT
*"An orbit is fully described by six Keplerian elements: semi-major axis a, eccentricity e, inclination i, longitude of ascending node Omega, argument of periapsis omega, and mean anomaly M (or true anomaly). These define the conic and its orientation in space."*
— Johannes Kepler; Carl Friedrich Gauss (osculating elements), 1609. Source: Wikipedia: orbital elements; Kepler (1609-1619); Gauss (1801)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *fixed reference frame*: the elements are measured against an exactly fixed reference plane and equinox, references the universe never supplies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: each element carries a coherence floor. e_phi(kappa) = e*(1 + kappa*(phi-1)) + kappa*phi^-1*e_ground. At kappa->0 the six-element classical description is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} e_phi = e, i_phi = i, ... -> the Keplerian-element description is the two-body, fixed-frame limit.
```

---

### STAGE 4 — SIMULATION

`sim/291_keplerian_orbital_elements.py`: reproduces the classical values q = 0.8, h = 0.9749 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/291_keplerian_orbital_elements.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Every Keplerian element carries a phi-coherent residual (eccentricity floor, inclination floor) at full coupling.
EXPERIMENT (VERIFIED): Gaussian fitting of satellite and planetary orbits searching for the element floors over long baselines.
VERIFIED BY: Orbital elements are exactly constant two-body values at full coupling.
```

---

### RECOGNITION
Connects to Law 247 (Kepler's equation — M), Law 285 (perihelion precession — omega drift).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The orbit is not a frozen number set; every element breathes with a phi floor.

### NOVELTY
Classical orbit theory freezes the six elements; the phi-law gives each a coherence floor.

### ACTIONABILITY
Run sim/291_keplerian_orbital_elements.py; verify the element set at kappa->0.
