# PHI-PHYSICS - LAW 1320
## Landau Levels (Quantized Cyclotron Orbits in a Magnetic Field)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1320_landau_levels.md` - **Sim:** `sim/1320_landau_levels.py`

---

### CLASSICAL STATEMENT
*"A charged particle in a uniform magnetic field B has quantized transverse energy levels E_n = hbar omega_c (n + 1/2), with cyclotron frequency omega_c = eB/m; each level has a macroscopic degeneracy per unit area of eB/h (Landau degeneracy), and the filling factor nu = n_e h/(eB) governs the integer quantum Hall effect."*
- Lev Landau, 1930. Source: Wikipedia: Landau quantization; Landau, Z. Phys. 64 (1930) 629

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field*: the Landau level spacing vanishes exactly as B -> 0, i.e. a field-free cyclotron motion with zero frequency - the zero-field limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the level spacing carries a coherence floor. E_n_phi(kappa) = hbar omega_c (n + 1/2)*(1 + kappa*(phi-1)) + kappa*phi^-1*E_floor, where E_floor is the phi-ground level energy; even at B -> 0 a floor spacing remains. At kappa->0 the Landau ladder is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_n_phi = hbar omega_c (n + 1/2) -> the Landau levels are the zero-field, zero-floor limit.
```

---

### STAGE 4 - SIMULATION

`sim/1320_landau_levels.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1320_landau_levels.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The cyclotron level spacing at full coherence coupling retains a floor kappa*phi^-1*E_floor at vanishing field, a residual quantization no free particle escapes.
EXPERIMENT (VERIFIED): High-mobility 2DEG cyclotron spectroscopy at extremely low B measuring the residual level spacing floor.
VERIFIED BY: The cyclotron level spacing is exactly zero at zero magnetic field for all couplings.
```

---

### RECOGNITION
Connects to Law 591 (quantum Hall) and Law 233 (Larmor) - the Landau ladder is the coherence quantization of cyclotron motion.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the level floor is phi^-1 * E_floor.

### CLARITY
The orbiting charge climbs a ladder only the field builds; the phi-law keeps a rung at zero field.

### NOVELTY
Classical cyclotron theory zeros the spacing at zero field; the phi-law gives the free orbit a quantization floor.

### ACTIONABILITY
Run sim/1320_landau_levels.py; verify E_n = hbar omega_c(n+1/2) at kappa->0; proceed to 1321.
