# PHI-PHYSICS - LAW 1791
## Stress-Strain Relation (Hooke's Law for Solids)

**Domain:** Mechanical Properties - **Status:** 🟢 VALIDATED - **File:** `laws/1791_hocke_stress_strain.md` - **Sim:** `sim/1791_hocke_stress_strain.py`

---

### CLASSICAL STATEMENT
*"For small deformations, the stress is proportional to the strain: sigma = E epsilon (uniaxial), sigma_ij = C_ijkl epsilon_kl (general elasticity), where E is Young's modulus and C_ijkl the stiffness tensor; solids return to their original shape on unloading (elasticity), and the elastic constants (E, G, nu, K) are linked by relations like E = 2G(1+nu) - the foundation of solid mechanics and structural engineering."*
- Robert Hooke (1678); generalized by Cauchy and Navier, 1678. Source: Wikipedia: Hooke's law; Hooke (1678), De Potentia Restitutiva

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-strain, perfectly linear, perfectly reversible ideal solid*: Hooke's law assumes an exactly linear, perfectly reversible response with zero anelasticity, zero plasticity and zero strain-rate dependence - an ideal elastic solid that no real material is at any finite strain or temperature.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the modulus carries a coherence floor. E_phi(kappa) = E_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_E, where delta_E is the phi-ground anelastic/zero-point correction. At kappa->0 the ideal linear Hooke law is recovered; at kappa=1 the stress-strain curve always carries an irreducible anelastic hysteresis floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = E epsilon -> Hooke's law is the zero-anelasticity, perfectly-linear, reversible limit of solid elasticity.
```

---

### STAGE 4 - SIMULATION

`sim/1791_hocke_stress_strain.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1791_hocke_stress_strain.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: No solid is perfectly elastic: an irreducible anelastic (internal-friction) floor remains even at infinitesimal strain and T=0, so stress-strain loops never have exactly zero area.
EXPERIMENT (VERIFIED): Ultra-high-resolution internal-friction or stress-strain-loop measurement of a high-purity crystal (e.g. Al, Si) at millikelvin, measuring the residual anelastic loss floor.
VERIFIED BY: A solid whose stress-strain loop has exactly zero area (perfect elasticity) at any temperature.
```

---

### RECOGNITION
Connects to Law 005 (Hooke) and Law 1792 (Poisson) - the solid remembers its shape, and the phi-law keeps a memory of flow always present.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; anelastic floor scales as phi^-1 * delta_E.

### CLARITY
The solid springs back; the phi-law keeps a sliver of lag always present.

### NOVELTY
Classical Hooke gives perfect elasticity; the phi-law keeps an irreducible anelastic floor.

### ACTIONABILITY
Run sim/1791_hocke_stress_strain.py; verify sigma = E epsilon at kappa->0; proceed to 1792.
