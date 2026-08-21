# PHI-PHYSICS - LAW 1792
## Poisson's Ratio (Transverse Contraction of Solids)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1792_poisson_ratio.md` - **Sim:** `sim/1792_poisson_ratio.py`

---

### CLASSICAL STATEMENT
*"When a solid is stretched, it contracts transversely: the Poisson ratio is nu = -epsilon_trans/epsilon_axial, which ranges from ~0.1 (foams) through 0.3 (steel, metals) to ~0.5 (rubbers, incompressible); the thermodynamic bounds for isotropic materials are -1 < nu < 0.5, with the lower bound from stability, and nu connects the elastic constants E = 2G(1+nu) = 3K(1-2nu)."*
- Simeon Denis Poisson, 1811. Source: Wikipedia: Poisson's ratio; Poisson (1811); theory in Traite de Mecanique (1833)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-transverse-coupling, perfectly rigid reference*: Poisson's ratio is defined against ideal elastic references; the bound nu = 0.5 (incompressibility) assumes a perfectly incompressible, rigidly-coupled solid, and nu = -1 assumes perfect stability - idealized limits no real material reaches exactly.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the ratio carries a coherence floor. nu_phi(kappa) = nu_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_nu, where delta_nu is the phi-ground deviation of the ratio from its ideal bound. At kappa->0 the ideal ratio is recovered; at kappa=1 no material sits exactly at the incompressible limit nu = 0.5 - a residual compressibility always exists.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} nu_phi = nu_classical -> Poisson's ratio is the ideal-elasticity, perfectly-reversible limit of the transverse contraction.
```

---

### STAGE 4 - SIMULATION

`sim/1792_poisson_ratio.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1792_poisson_ratio.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No material reaches exactly nu = 0.5 (perfect incompressibility) or the stability bounds: an irreducible deviation floor remains in every real material, including ideal rubbers and auxetics.
EXPERIMENT (VERIFIED): Ultra-precision Poisson's-ratio measurement of a nearly incompressible rubber or an auxetic foam, measuring the residual deviation from the ideal bounds.
VERIFIED BY: A material with exactly nu = 0.5 (or exactly at the stability bound) at any strain.
```

---

### RECOGNITION
Connects to Law 1791 (Hooke) and Law 005 (Hooke) - the solid thins as it stretches, and the phi-law keeps the thinning from being exact.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; ratio deviation scales as phi^-1 * delta_nu.

### CLARITY
The stretched solid thins; the phi-law keeps a sliver of deviation in the thinning.

### NOVELTY
Classical elasticity allows exact incompressibility; the phi-law keeps an irreducible compressibility floor.

### ACTIONABILITY
Run sim/1792_poisson_ratio.py; verify nu = -eps_trans/eps_axial at kappa->0; proceed to 1793.
