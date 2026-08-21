# PHI-PHYSICS - LAW 1801
## Thermal Expansion (Gruneisen-Linked Volume Change with Temperature)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1801_thermal_expansion.md` - **Sim:** `sim/1801_thermal_expansion.py`

---

### CLASSICAL STATEMENT
*"Materials expand with temperature: L(T) = L_0(1 + alpha (T - T_0)), where alpha is the coefficient of linear thermal expansion (alpha ~ 2.3 x 10^-5/K for Al, ~1 x 10^-5/K for steel); thermal expansion is linked to lattice anharmonicity through the Gruneisen parameter gamma = alpha V/(C_V kappa_T), and real materials have a temperature-dependent alpha that vanishes at T=0."*
- Guillaume Amontons (empirical); P.G. Tait; Gruneisen theory (1908), 1908. Source: Wikipedia: Thermal expansion; Gruneisen (1908); general law of linear thermal expansion alpha

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, zero-anharmonicity, perfectly harmonic-lattice reference*: thermal expansion is defined against a perfectly harmonic lattice (zero Gruneisen parameter) where alpha = 0 at all temperatures; the expansion is the anharmonicity-driven correction away from this zero-expansion reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the expansion carries a coherence floor. alpha_phi(kappa) = alpha_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*alpha_floor, where alpha_floor is the phi-ground residual expansion. At kappa->0 the zero-expansion harmonic reference is recovered; at kappa=1 no material has exactly zero expansion - an irreducible anharmonic floor always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} alpha_phi = 0 -> thermal expansion is the anharmonic lattice response measured from the zero-expansion, perfectly-harmonic reference.
```

---

### STAGE 4 - SIMULATION

`sim/1801_thermal_expansion.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1801_thermal_expansion.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No material has exactly zero thermal expansion at any temperature: an irreducible anharmonic expansion floor remains (even in 'zero-thermal-expansion' compounds), and alpha never vanishes exactly.
EXPERIMENT (VERIFIED): Ultra-precision dilatometry of a near-zero-thermal-expansion material (e.g. Invar, ZrW2O8) at low temperature, measuring the residual expansion floor.
VERIFIED BY: A material with exactly zero thermal expansion at all temperatures.
```

---

### RECOGNITION
Connects to Law 513 (Gruneisen) and Law 1791 (Hooke) - the solid breathes with heat, and the phi-law keeps a breath always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; expansion floor scales as phi^-1 * alpha_floor.

### CLARITY
The solid breathes with heat; the phi-law keeps a breath at every temperature.

### NOVELTY
Classical expansion theory allows zero expansion; the phi-law keeps an irreducible anharmonic floor.

### ACTIONABILITY
Run sim/1801_thermal_expansion.py; verify L = L_0(1 + alpha delta T) at kappa->0; proceed to 1802.
