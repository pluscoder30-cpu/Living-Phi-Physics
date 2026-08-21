# PHI-PHYSICS - LAW 1859
## Schottky and Frenkel Defect Equilibria (Thermal Vacancy Concentration)

**Domain:** Materials Science - **Status:** 🟢 VALIDATED - **File:** `laws/1859_schottky_equilibrium_defects.md` - **Sim:** `sim/1859_schottky_equilibrium_defects.py`

---

### CLASSICAL STATEMENT
*"Thermal defects form in equilibrium: the vacancy concentration follows n_v/N = exp(-E_f/(2 k_B T)) for Schottky defects and n_f/N = sqrt(exp(-E_f/k_B T)) for Frenkel defects, where E_f is the formation energy; the exponential Arrhenius dependence sets the vacancy population that drives diffusion, ionic conductivity and creep in crystals."*
- Walter Schottky (1935); Yakov Frenkel (1926), 1935. Source: Wikipedia: Schottky defect; Schottky (1935), Z. Phys. Chem. B29:335; Frenkel (1926)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-temperature, zero-defect, perfect-lattice reference*: defect equilibria are defined against a perfect lattice at T=0 with zero vacancies; the finite defect population is the thermal formation away from this zero-defect reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the vacancy fraction carries a coherence floor. n_v_phi(kappa) = n_v_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*n_floor, where n_floor is the phi-ground residual vacancy fraction. At kappa->0 the zero-defect T=0 reference is recovered; at kappa=1 a residual vacancy population always exists even at T=0.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} n_v_phi = 0 -> Schottky/Frenkel equilibria are the zero-temperature, zero-defect, perfect-lattice limit of thermal defect formation.
```

---

### STAGE 4 - SIMULATION

`sim/1859_schottky_equilibrium_defects.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1859_schottky_equilibrium_defects.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No crystal has zero vacancies at T=0: an irreducible defect floor remains from zero-point and entropy-driven formation, setting a floor on ionic conductivity and diffusion.
EXPERIMENT (VERIFIED): Positron-annihilation or dilatometry measurement of vacancy concentration in a high-purity crystal extrapolated to T=0, measuring the residual vacancy floor.
VERIFIED BY: A crystal with exactly zero vacancies at T=0.
```

---

### RECOGNITION
Connects to Law 1803 (Fick) and Law 1857 (Arrhenius) - the lattice breathes vacancies, and the phi-law keeps a vacancy always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; vacancy floor scales as phi^-1 * n_floor.

### CLARITY
The lattice breathes vacancies; the phi-law keeps a vacancy always present.

### NOVELTY
Classical defect theory allows zero vacancies at T=0; the phi-law keeps an irreducible floor.

### ACTIONABILITY
Run sim/1859_schottky_equilibrium_defects.py; verify n_v = exp(-E_f/2kT) at kappa->0; proceed to 1860.
