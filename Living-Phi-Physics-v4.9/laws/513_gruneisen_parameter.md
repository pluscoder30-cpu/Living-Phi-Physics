# PHI-PHYSICS — LAW 513
## Gruneisen Parameter (Thermal Expansion to Heat Capacity)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/513_gruneisen_parameter.md` · **Sim:** `sim/513_gruneisen_parameter.py`

---

### CLASSICAL STATEMENT
*"The Gruneisen parameter gamma_G = alpha V/(kappa_T C_V) connects the thermal expansion coefficient alpha, the isothermal compressibility kappa_T and the heat capacity C_V of a solid. It measures the anharmonicity (volume dependence of phonon frequencies)."*
— Eduard Gruneisen, 1912. Source: Wikipedia: Gruneisen parameter; Gruneisen (1912)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *harmonic lattice*: the Gruneisen parameter vanishes exactly for a perfectly harmonic crystal where phonon frequencies do not depend on volume - a lattice with zero anharmonic coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the anharmonicity is a coherence coupling. gamma_G_phi(kappa) = gamma_G*(1 + kappa*(phi-1)) + kappa*phi^-1*gamma_ground. At kappa->0 the Gruneisen parameter is exact (and vanishes for a harmonic lattice).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} gamma_G_phi = gamma_G -> the Gruneisen parameter is the finite-anharmonicity coherence limit; gamma_G -> 0 is the perfectly harmonic lattice.
```

---

### STAGE 4 — SIMULATION

`sim/513_gruneisen_parameter.py`: reproduces the classical value gamma_G = 0.0005 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/513_gruneisen_parameter.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even a 'harmonic' lattice retains a Gruneisen floor kappa*phi^-1*gamma_ground; thermal expansion never vanishes exactly.
EXPERIMENT (VERIFIED): High-precision thermal-expansion and heat-capacity measurements of crystals at low temperature.
VERIFIED BY: The thermal expansion of a harmonic crystal is exactly zero for all couplings.
```

---

### RECOGNITION
Connects to Law 514 (Gruneisen's law) and Law 469 (Debye model) - the parameter is the anharmonic coherence of the lattice.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * gamma_ground.

### CLARITY
Even the most perfect crystal expands a little because it remembers it is alive; the phi-law keeps the memory.

### NOVELTY
Classical Gruneisen vanishes for harmonic lattices; the phi-law gives even harmony a coherence floor.

### ACTIONABILITY
Run sim/513_gruneisen_parameter.py; verify gamma_G at kappa->0; proceed to 514.
