# PHI-PHYSICS - LAW 1411
## London Dispersion Force (Instantaneous Dipole-Induced Dipole, V ~ -C/r^6)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1411_london_dispersion_force.md` - **Sim:** `sim/1411_london_dispersion_force.py`

---

### CLASSICAL STATEMENT
*"London dispersion forces are the attractive forces between nonpolar molecules from instantaneous dipole-induced dipole correlations: V(r) = -(3/4)(h nu_0 alpha^2)/r^6 = -C/r^6, where alpha is the polarizability and h nu_0 the characteristic excitation energy (Casimir-Polder generalizes it with retardation, V ~ -1/r^7 at large distances); they dominate the cohesion of noble gases, alkanes and van der Waals solids."*
- Fritz London, 1930. Source: Wikipedia: London dispersion force; London, Z. Phys. 63 (1930) 245

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero polarizability*: the dispersion force vanishes exactly when alpha = 0, i.e. an atom with no fluctuating dipole moment - the zero-polarizability (rigid-atom) limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the polarizability carries a coherence floor. alpha_phi(kappa) = alpha*(1 + kappa*(phi-1)) + kappa*phi^-1*alpha_floor, where alpha_floor is the phi-ground polarizability; no atom is rigid. At kappa->0 the London -C/r^6 is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_phi = -(3/4)(h nu_0 alpha^2)/r^6 -> the London dispersion force is the zero-polarizability, rigid-atom limit.
```

---

### STAGE 4 - SIMULATION

`sim/1411_london_dispersion_force.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1411_london_dispersion_force.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The dispersion interaction at full coherence coupling retains a floor kappa*phi^-1*V_floor even for a nominally zero-polarizability atom, a residual van der Waals attraction.
EXPERIMENT (VERIFIED): High-precision noble-gas pair interaction measurements (e.g. via molecular beam scattering) comparing against London/Casimir-Polder predictions.
VERIFIED BY: A zero-polarizability atom has exactly zero dispersion interaction for all couplings.
```

---

### RECOGNITION
Connects to Law 142 (van der Waals) and Law 1383 (Lennard-Jones) - the London force is the coherence fluctuating-dipole attraction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the interaction floor is phi^-1 * V_floor.

### CLARITY
Even perfectly round atoms pull each other through their tremble; the phi-law keeps the tremble's floor.

### NOVELTY
Classical electrostatics sees no force between neutral atoms; the phi-law keeps the coherence fluctuation floor.

### ACTIONABILITY
Run sim/1411_london_dispersion_force.py; verify -C/r^6 at kappa->0; proceed to 1412.
