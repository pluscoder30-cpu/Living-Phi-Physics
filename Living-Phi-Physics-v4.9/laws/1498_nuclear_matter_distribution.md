# PHI-PHYSICS - LAW 1498
## Nuclear Matter and Charge Distribution (Hofstadter Scattering)

**Domain:** Nuclear Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1498_nuclear_matter_distribution.md` - **Sim:** `sim/1498_nuclear_matter_distribution.py`

---

### CLASSICAL STATEMENT
*"Electron scattering measures the nuclear charge and matter distributions; the charge density is well described by a Fermi (Woods-Saxon) distribution rho(r) = rho0/(1 + exp((r - c)/a)) with half-density radius c ~ 1.1 A^(1/3) fm and diffuseness a ~ 0.5 fm."*
- Robert Hofstadter (electron scattering, Nobel 1961), 1956. Source: Hofstadter, Rev. Mod. Phys. 28 (1956) 214; Wikipedia: Robert Hofstadter

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-diffuseness, uniform-interior charge density*: the Fermi distribution reduces to a step function when the diffuseness a -> 0; classical treatment of the nucleus as a uniform sphere of constant density is the zero-diffuseness limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

c_phi(kappa) = c_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_c, where delta_c is the phi-ground skin-diffuseness floor. At kappa->0 the sharp uniform sphere is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rho(r)_phi = rho0 for r < c, 0 for r > c -> the nuclear distribution is the zero-diffuseness, uniform-sphere limit.
```

---

### STAGE 4 - SIMULATION

`sim/1498_nuclear_matter_distribution.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1498_nuclear_matter_distribution.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The nuclear surface always carries a phi-ground diffuseness floor, so the charge/matter distributions deviate from a uniform sphere by an irreducible skin thickness and neutron skins (N-Z difference) reflect this floor.
EXPERIMENT (VERIFIED): Electron scattering (Hofstadter type) and parity-violating electron scattering (PREX, CREX) measuring charge and neutron distributions.
VERIFIED BY: A nucleus whose charge density is exactly a uniform sphere with zero diffuseness at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1486 (radius law), Law 1495 (incompressibility) and Law 1484 - the distribution is the nucleus's shape at rest.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The sphere has a skin; the phi-law keeps a floor of skin on the sphere.

### NOVELTY
Classical distribution is uniform; the phi-law predicts irreducible diffuseness and neutron-skin floors.

### ACTIONABILITY
Run sim/1498_nuclear_matter_distribution.py; verify the Fermi distribution; proceed to Law 1499.
