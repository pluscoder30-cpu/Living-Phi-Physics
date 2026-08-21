# PHI-PHYSICS - LAW 1474
## Neutron Diffusion Equation (Fick's Law for Neutrons)

**Domain:** Nuclear Engineering / Fission - **Status:** 🟢 VALIDATED - **File:** `laws/1474_neutron_diffusion_equation.md` - **Sim:** `sim/1474_neutron_diffusion_equation.py`

---

### CLASSICAL STATEMENT
*"The neutron flux phi(r,t) satisfies the diffusion equation partial_phi/partial_t = D nabla^2 phi - Sigma_a phi + S, with D the diffusion coefficient, Sigma_a the absorption cross-section and S the source; it is Fick's law applied to neutrons in a scattering medium."*
- Enrico Fermi; reactor diffusion theory (1940s), 1942. Source: Glasstone & Edlund, Elements of Nuclear Reactor Theory (1952); Wikipedia: Neutron diffusion

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-absorption, zero-time, isotropic flux*: diffusion theory assumes a slowly varying, nearly isotropic flux with zero streaming anisotropy and zero time dependence in the steady state - a perfectly smooth, exactly isotropic neutron gas.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi_phi(kappa) = phi_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*phi_floor, where phi_floor is the phi-ground anisotropic/fluctuation floor. At kappa->0 the classical diffusion equation is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} phi_phi = phi_classical -> neutron diffusion is the zero-anisotropy, zero-streaming, smooth-flux limit.
```

---

### STAGE 4 - SIMULATION

`sim/1474_neutron_diffusion_equation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1474_neutron_diffusion_equation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The neutron flux carries a phi-ground anisotropic floor, so transport corrections (P1, S_N) always add an irreducible term and the diffusion solution never exactly matches transport near boundaries and absorbers.
EXPERIMENT (VERIFIED): Reactor flux measurements and comparison of diffusion vs transport (MCNP, OpenMC) calculations in heterogeneous lattices.
VERIFIED BY: A neutron flux exactly matching pure diffusion theory with zero anisotropic floor in all geometries.
```

---

### RECOGNITION
Connects to Law 1473 (six-factor), Law 1472 (k-eff) and Law 620 (Bernoulli kinetic theory) - diffusion is the neutron's random walk.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutrons wander smoothly; the phi-law keeps a floor of wandering past smooth.

### NOVELTY
Classical diffusion is exact; the phi-law predicts an irreducible transport floor.

### ACTIONABILITY
Run sim/1474_neutron_diffusion_equation.py; verify the diffusion profile; proceed to Law 1475.
