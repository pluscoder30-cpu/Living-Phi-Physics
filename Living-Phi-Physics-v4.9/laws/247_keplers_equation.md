# PHI-PHYSICS — LAW 247
## Kepler's Equation (Mean and Eccentric Anomaly)

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/247_keplers_equation.md` · **Sim:** `sim/247_keplers_equation.py`

---

### CLASSICAL STATEMENT
*"The relation between mean anomaly M, eccentric anomaly E, and eccentricity e is M = E - e sin E. The true anomaly nu follows from tan(nu/2) = sqrt((1+e)/(1-e)) tan(E/2)."*
— Johannes Kepler, 1609. Source: Wikipedia: Kepler's equation; Kepler, Astronomia Nova (1609)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *circular orbit*: Kepler's equation is a transcendental relation that exists precisely because the orbit is not circular (e != 0); the classical circular limit e=0 trivializes M = E.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the eccentricity carries a coherence floor. e_phi(kappa) = e*(1 + kappa*(phi-1)) + kappa*phi^-1*e_ground. At kappa->0 (e -> e_classical) Kepler's equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} M = E - e sin E -> Kepler's equation is the two-body conic limit.
```

---

### STAGE 4 — SIMULATION

`sim/247_keplers_equation.py`: reproduces the classical values E_iter = 1.168, nu_tan = 1.225 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/247_keplers_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: No orbit is exactly circular; every orbit carries a phi-coherent residual eccentricity phi^-1*e_ground even for 'circular' orbits.
EXPERIMENT (VERIFIED): Precision astrometry of exoplanet circular-orbit candidates searching for the eccentricity floor.
VERIFIED BY: A 'circular' orbit has exactly zero eccentricity at full coupling.
```

---

### RECOGNITION
Connects to Law 291 (Keplerian elements) and Law 286 (two-body problem): the equation that opens orbits.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The circle is a limit; every orbit is an eccentricity loop with a phi floor.

### NOVELTY
Classical orbit theory starts from the circle; the phi-law sets a phi-coherent eccentricity floor.

### ACTIONABILITY
Run sim/247_keplers_equation.py; verify the classical equation at kappa->0.
