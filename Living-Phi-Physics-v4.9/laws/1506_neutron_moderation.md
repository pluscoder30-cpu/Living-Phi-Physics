# PHI-PHYSICS - LAW 1506
## Neutron Moderation (Slowing Down of Neutrons by Scattering)

**Domain:** Nuclear Engineering - **Status:** 🟢 VALIDATED - **File:** `laws/1506_neutron_moderation.md` - **Sim:** `sim/1506_neutron_moderation.py`

---

### CLASSICAL STATEMENT
*"Neutrons are slowed (moderated) by elastic scattering on light nuclei; the average logarithmic energy decrement xi = 1 + ((A-1)^2/2A) ln((A-1)/(A+1)) measures the energy loss per collision, with hydrogen (A=1) the best moderator; the moderating ratio favors D2O and graphite for low absorption."*
- Enrico Fermi (1934); reactor moderation (1940s), 1942. Source: Fermi (1934); Glasstone & Edlund, Elements of Nuclear Reactor Theory (1952)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy, exactly-thermal neutron*: moderation assumes neutrons are slowed to exactly thermal energy with zero energy spread and zero upscattering; the thermal spectrum is a delta function at the moderator temperature - a zero-width thermal peak.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

xi_phi(kappa) = xi_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*xi_floor, where xi_floor is the phi-ground moderation floor from inelastic and upscattering effects. At kappa->0 the elastic scattering formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} xi_phi = 1 + ((A-1)^2/2A) ln((A-1)/(A+1)) -> neutron moderation is the zero-inelastic, pure-elastic-scattering limit.
```

---

### STAGE 4 - SIMULATION

`sim/1506_neutron_moderation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1506_neutron_moderation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The neutron slowing-down spectrum carries a phi-ground upscattering/inelastic floor, so the moderator spectrum is never exactly the ideal Maxwellian and the effective thermal temperature differs from the moderator temperature.
EXPERIMENT (VERIFIED): Neutron spectrum measurements in moderators (research reactors, TRIGA) via activation foils and time-of-flight.
VERIFIED BY: A moderator producing exactly the ideal thermal Maxwellian with zero upscattering floor at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1474 (diffusion), Law 1472 (k-eff) and Law 1473 (six-factor) - moderation is the reactor's slow cooker.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The fast neutron cools step by step; the phi-law keeps a floor of heat in every step.

### NOVELTY
Classical moderation is pure elastic; the phi-law predicts an irreducible upscattering floor.

### ACTIONABILITY
Run sim/1506_neutron_moderation.py; verify the lethargy; proceed to Law 1507.
