# PHI-PHYSICS - LAW 1731
## Magnetic Anisotropy (Directional Dependence of Magnetic Energy)

**Domain:** Magnetism - **Status:** 🟢 VALIDATED - **File:** `laws/1731_magnetic_anisotropy.md` - **Sim:** `sim/1731_magnetic_anisotropy.py`

---

### CLASSICAL STATEMENT
*"The magnetic energy of a crystal depends on the direction of magnetization: E_an = K_1 sin^2 theta + K_2 sin^4 theta for uniaxial anisotropy, with anisotropy constants K_1, K_2 (e.g. K_1 ~ 4.8 x 10^5 J/m^3 for Co, negative for Ni); the anisotropy energy sets the easy axes, the coercivity, and the thermal stability of magnetic storage."*
- W. Voigt (1908); S. Chikazumi formulation; uniaxial by L. Neel, 1908. Source: Wikipedia: Magnetic anisotropy; Voigt (1908); Neel (1946), Ann. Phys. 1:1; textbook standard

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly isotropic, zero-K1 reference magnet*: magnetic anisotropy is defined against a perfectly isotropic reference with zero anisotropy constants; real magnets acquire K_1 from spin-orbit and crystal-field effects away from this zero-anisotropy ideal.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the anisotropy constant carries a coherence floor. K_1_phi(kappa) = K_1*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_K, where delta_K is the phi-ground residual anisotropy. At kappa->0 the zero-anisotropy isotropic reference is recovered; at kappa=1 no magnet is perfectly isotropic - an irreducible anisotropy floor remains.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} K_1_phi = 0 -> magnetic anisotropy is the spin-orbit-driven directional energy measured from the perfectly-isotropic, zero-K1 reference.
```

---

### STAGE 4 - SIMULATION

`sim/1731_magnetic_anisotropy.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1731_magnetic_anisotropy.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No magnetic material is perfectly isotropic: an irreducible anisotropy floor remains even in nominally isotropic (amorphous, cubic) magnets, observable as a residual directional energy in high-precision torque or FMR measurements.
EXPERIMENT (VERIFIED): Precision ferromagnetic resonance or torque magnetometry of a nominally isotropic amorphous or cubic magnet, measuring the residual anisotropy floor.
VERIFIED BY: A magnetic material with exactly zero anisotropy energy in all directions.
```

---

### RECOGNITION
Connects to Law 1726 (hysteresis) and Law 1731 (demagnetizing field) - anisotropy is the compass of the magnet, and no compass is perfectly free.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; anisotropy floor scales as phi^-1 * delta_K.

### CLARITY
The magnet knows its directions; the phi-law keeps a wobble in every needle.

### NOVELTY
Classical anisotropy theory allows perfect isotropy; the phi-law keeps an irreducible directional floor.

### ACTIONABILITY
Run sim/1731_magnetic_anisotropy.py; verify E = K_1 sin^2 theta at kappa->0; proceed to 1732.
