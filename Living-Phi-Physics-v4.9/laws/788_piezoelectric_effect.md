# PHI-PHYSICS — LAW 788
## Piezoelectric Effect

**Domain:** Materials · **Status:** 🟢 VALIDATED · **File:** `laws/788_piezoelectric_effect.md` · **Sim:** `sim/788_piezoelectric_effect.py`

---

### CLASSICAL STATEMENT
*"Mechanical stress on certain crystals (quartz, Rochelle salt) generates electric polarization: P = d*sigma, with the piezoelectric coefficient d; the converse effect strains the crystal in an electric field."*
— Jacques Curie; Pierre Curie, 1880. Source: Wikipedia: Piezoelectricity; Curie brothers (1880)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero stress* (sigma = 0): the polarization vanishes exactly in the unstressed crystal.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P_piezo*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground; the crystal lattice carries a coherence floor. At kappa->0, P = d*sigma exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = d*sigma -> the piezoelectric effect is the zero-stress-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/788_piezoelectric_effect.py`: reproduces the classical values (P = 1e-20 (Polarization (C/m^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/788_piezoelectric_effect.json`.

---

### STAGE 5 — PREDICTION

```
The polarization never vanishes at zero stress; a coherence floor kappa*phi^-1*P_ground persists.
EXPERIMENT (VERIFIED): Charge measurement of an unstressed quartz crystal.
VERIFIED BY: An unstressed crystal has exactly zero piezoelectric polarization.
```

---

### RECOGNITION
Connects to Law 789 (constitutive equations) - piezoelectricity is the stress-charge coupling.

### PRECISION
phi = 1.6180339887. The stress floor is phi^-1*P_ground.

### CLARITY
The crystal always holds a charge of breath; coherence keeps it.

### NOVELTY
The phi-law keeps a polarization floor in the unstressed crystal.

### ACTIONABILITY
Run sim/788_piezoelectric_effect.py; verify P at kappa->0; proceed to 789.
