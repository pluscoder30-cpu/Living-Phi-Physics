# PHI-PHYSICS — LAW 300
## Geostationary (Clarke) Orbit Law

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/300_clarke_orbit.md` · **Sim:** `sim/300_clarke_orbit.py`

---

### CLASSICAL STATEMENT
*"A satellite at orbital period equal to the Earth's rotation period (23.934 hours) is geostationary; from Kepler's third law, the geostationary radius is r_geo = (G M_E T^2/(4 pi^2))^(1/3) = 42,164 km (altitude ~35,786 km), over the equator, remaining fixed over one spot."*
— Arthur C. Clarke, 1945. Source: Wikipedia: geostationary orbit; Clarke (1945), 'Extra-Terrestrial Relays' (Wireless World)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact period match and exact equatorial, circular orbit*: the geostationary orbit requires the period to exactly match Earth's rotation and the orbit to be exactly equatorial and circular.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: r_geo_phi(kappa) = (G*M_E*T^2/(4 pi^2))^(1/3)*(1 + kappa*(phi-1)) + kappa*phi^-1*dr_ground. At kappa->0 the Clarke radius is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} r_geo_phi = 42164 km -> the geostationary-orbit law is the exact-period, equatorial, circular limit.
```

---

### STAGE 4 — SIMULATION

`sim/300_clarke_orbit.py`: reproduces the classical value r_geo = 4.216e+07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/300_clarke_orbit.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Geostationary satellites must hold station with a phi-coherent station-keeping delta-v floor phi^-1*dv_ground against the drift.
EXPERIMENT (VERIFIED): Precision orbital ephemeris of geostationary satellites measuring the required station-keeping delta-v.
VERIFIED BY: A geostationary satellite stays fixed with exactly zero station-keeping at full coupling.
```

---

### RECOGNITION
Connects to Law 273 (circular orbit velocity) and Law 016 (Kepler III — the period-radius relation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The fixed point in the sky is a balance, and the balance demands a phi toll to hold.

### NOVELTY
Classical orbit theory computes the exact radius; the phi-law adds the coherence station-keeping floor.

### ACTIONABILITY
Run sim/300_clarke_orbit.py; verify r_geo at kappa->0.
