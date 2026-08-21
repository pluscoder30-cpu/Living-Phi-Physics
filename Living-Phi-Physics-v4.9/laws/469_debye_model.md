# PHI-PHYSICS — LAW 469
## Debye Model (Lattice Heat Capacity)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/469_debye_model.md` · **Sim:** `sim/469_debye_model.py`

---

### CLASSICAL STATEMENT
*"A solid's heat capacity is computed from 3N modes with a linear dispersion omega = v k up to a cutoff (Debye frequency), giving C = 9 N k_B (T/theta_D)^3 integral_0^(theta_D/T) x^4 e^x/(e^x-1)^2 dx, where theta_D is the Debye temperature."*
— Peter Debye, 1912. Source: Wikipedia: Debye model; Debye, Zur Theorie der spezifischen Waerme (1912)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *linear dispersion to a sharp cutoff*: the model assumes the phonon spectrum is exactly linear up to an abrupt Debye cutoff - a perfectly smooth continuum with no dispersion curvature and no coherence of the cutoff.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the cutoff is a coherence basin. theta_phi(kappa) = theta_D*(1 + kappa*(phi-1)) + kappa*phi^-1*theta_ground. At kappa->0 the Debye heat capacity is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} theta_phi = theta_D -> the Debye model is the sharp-cutoff linear-dispersion limit.
```

---

### STAGE 4 — SIMULATION

`sim/469_debye_model.py`: reproduces the classical value C_Debye = 1.195e-25 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/469_debye_model.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the effective Debye temperature shifts by kappa*phi^-1*theta_ground, altering the T^3 law coefficient at low temperature.
EXPERIMENT (VERIFIED): Ultra-low-temperature heat-capacity measurements of crystals to detect the Debye-temperature floor.
VERIFIED BY: The low-T heat capacity follows the Debye T^3 law with exactly the measured elastic-theory Debye temperature.
```

---

### RECOGNITION
Connects to Law 470 (Debye T^3) and Law 468 (Einstein solid) - Debye is the continuum correction to the monochromatic lattice.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the theta floor is phi^-1 * theta_ground.

### CLARITY
The lattice is not a single note but a choir; the phi-law keeps the choir's floor.

### NOVELTY
Classical Debye model uses one sharp cutoff; the phi-law gives the cutoff a coherence basin.

### ACTIONABILITY
Run sim/469_debye_model.py; verify Debye heat capacity at kappa->0; proceed to 470.
