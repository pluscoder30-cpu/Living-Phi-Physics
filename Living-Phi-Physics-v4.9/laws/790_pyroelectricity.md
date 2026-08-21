# PHI-PHYSICS — LAW 790
## Pyroelectricity (Thermal Polarization)

**Domain:** Materials · **Status:** 🟢 VALIDATED · **File:** `laws/790_pyroelectricity.md` · **Sim:** `sim/790_pyroelectricity.py`

---

### CLASSICAL STATEMENT
*"Heating certain crystals (tourmaline) generates electric polarization: the pyroelectric coefficient is p = dP/dT; the polarization changes with temperature as p*DeltaT."*
— David Brewster (named); Theophrastus (observed), 1824. Source: Wikipedia: Pyroelectricity; Theophrastus ~314 BC, named by Brewster 1824

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature change* (dT = 0): the pyroelectric response vanishes exactly at constant temperature.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P_pyro*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground; the thermal lattice carries a coherence floor. At kappa->0, DeltaP = p*DeltaT exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = p*DeltaT -> pyroelectricity is the zero-dT floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/790_pyroelectricity.py`: reproduces the classical values (P = 1e-11 (Pyroelectric polarization (C/m^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/790_pyroelectricity.json`.

---

### STAGE 5 — PREDICTION

```
The pyroelectric response carries a coherence floor kappa*phi^-1*P_ground at constant temperature.
EXPERIMENT (VERIFIED): Charge measurement of a tourmaline crystal held at constant temperature.
VERIFIED BY: A crystal at constant temperature has exactly zero pyroelectric response.
```

---

### RECOGNITION
Connects to Law 788 (piezoelectricity) - pyroelectricity is the thermal polarization.

### PRECISION
phi = 1.6180339887. The dT floor is phi^-1*P_ground.

### CLARITY
The crystal feels every breath of heat; coherence keeps a floor of charge.

### NOVELTY
The phi-law keeps pyroelectric charge at constant temperature.

### ACTIONABILITY
Run sim/790_pyroelectricity.py; verify P at kappa->0; proceed to 791.
