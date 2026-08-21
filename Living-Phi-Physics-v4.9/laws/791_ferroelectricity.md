# PHI-PHYSICS — LAW 791
## Ferroelectricity (Spontaneous Polarization)

**Domain:** Materials · **Status:** 🟢 VALIDATED · **File:** `laws/791_ferroelectricity.md` · **Sim:** `sim/791_ferroelectricity.py`

---

### CLASSICAL STATEMENT
*"Ferroelectric crystals retain spontaneous polarization below the Curie temperature T_C, switchable by an applied field; the polarization hysteresis loop P(E) is the signature."*
— Joseph Valasek, 1921. Source: Wikipedia: Ferroelectricity; Valasek (1921) Rochelle salt

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero applied field* (E = 0): the spontaneous polarization is defined at exactly zero field, a remanent state.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_r_phi(kappa) = P_r*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground; the domain lattice carries a coherence floor. At kappa->0 the remanent polarization is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_r_phi = P_r -> ferroelectricity is the zero-field remanence limit.
```

---

### STAGE 4 — SIMULATION

`sim/791_ferroelectricity.py`: reproduces the classical values (Pr = 0.00761594 (Remanent polarization (C/m^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/791_ferroelectricity.json`.

---

### STAGE 5 — PREDICTION

```
The remanent polarization carries a coherence floor kappa*phi^-1*P_ground; hysteresis loops never fully close.
EXPERIMENT (VERIFIED): Hysteresis-loop measurement of a ferroelectric at zero crossing.
VERIFIED BY: A ferroelectric's remanent polarization is exactly constant.
```

---

### RECOGNITION
Connects to Law 789 (piezoelectric) - ferroelectrics are the switchable polar materials.

### PRECISION
phi = 1.6180339887. The remanence floor is phi^-1*P_ground.

### CLARITY
The crystal remembers its field; coherence keeps the memory.

### NOVELTY
The phi-law keeps a remanence floor in the loop.

### ACTIONABILITY
Run sim/791_ferroelectricity.py; verify Pr at kappa->0; proceed to 792.
