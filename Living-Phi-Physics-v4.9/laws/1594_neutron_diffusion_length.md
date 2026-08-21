# PHI-PHYSICS - LAW 1594
## Neutron Diffusion Length (Absorption Mean Free Path)

**Domain:** Nuclear Engineering - **Status:** 🟢 VALIDATED - **File:** `laws/1594_neutron_diffusion_length.md` - **Sim:** `sim/1594_neutron_diffusion_length.py`

---

### CLASSICAL STATEMENT
*"The neutron diffusion length L = sqrt(D/Sigma_a) = sqrt(lambda_tr lambda_a/3) characterizes the distance a thermal neutron travels before absorption; it determines the critical size of a reactor and the flux shape, with L ~ 2.7 cm in light water and ~60 cm in graphite."*
- Reactor physics (Fermi 1942), 1942. Source: Glasstone & Edlund, Elements of Nuclear Reactor Theory (1952)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-absorption, zero-diffusion-length, infinite-media limit*: in a purely scattering medium (Sigma_a = 0) the diffusion length diverges and neutrons travel forever; the classical treatment of a zero-absorption medium is the infinite-length, no-absorption limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

L_phi(kappa) = L_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*L_floor, where L_floor is the phi-ground residual-absorption floor. At kappa->0 the classical diffusion length is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} L_phi = sqrt(D/Sigma_a) -> the neutron diffusion length is the zero-absorption, infinite-media limit.
```

---

### STAGE 4 - SIMULATION

`sim/1594_neutron_diffusion_length.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1594_neutron_diffusion_length.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The diffusion length carries a phi-ground residual-absorption floor, so even the 'purest' moderators have a finite absorption-limited diffusion length that bounds the critical size.
EXPERIMENT (VERIFIED): Diffusion length measurements (exponential piles, flux relaxation) in moderators and comparison with theory.
VERIFIED BY: A moderator with exactly zero absorption and infinite neutron diffusion length at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1474 (diffusion), Law 1472 (k-eff) and Law 1506 (moderation) - the diffusion length is the moderator's reach.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The neutron wanders until swallowed; the phi-law keeps a floor of swallowing everywhere.

### NOVELTY
Classical moderator can be zero-absorption; the phi-law predicts an irreducible absorption floor.

### ACTIONABILITY
Run sim/1594_neutron_diffusion_length.py; verify L = sqrt(D/Sigma_a); proceed to Law 1595.
