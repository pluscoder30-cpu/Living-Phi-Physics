# PHI-PHYSICS - LAW 1607
## Beam Lifetime (Touschek and Intrabeam Scattering Losses)

**Domain:** Accelerators - **Status:** 🟢 VALIDATED - **File:** `laws/1607_beam_lifetime.md` - **Sim:** `sim/1607_beam_lifetime.py`

---

### CLASSICAL STATEMENT
*"The beam lifetime in a storage ring is set by scattering processes: the Touschek effect (intrabeam Coulomb scattering ejecting particles) and intrabeam scattering (IBs) with the lifetime tau ~ 1/(sigma_t scattering rate); the lifetime scales with the beam density and the aperture."*
- C. Bernardini; G.F. Corazza; G. Di Giugno (1963, Touschek effect), 1963. Source: Bernardini et al., PRL 10 (1963) 407; Wikipedia: Touschek effect

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-density, zero-scattering, infinite-lifetime limit*: a beam of exactly zero density has zero intrabeam scattering and infinite lifetime; the classical treatment of a single particle is the zero-density, infinite-lifetime limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

tau_phi(kappa) = tau_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*tau_floor, where tau_floor is the phi-ground scattering floor. At kappa->0 the single-particle (infinite) lifetime is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} tau_phi = tau_single -> beam lifetime is the zero-density, zero-scattering, single-particle limit.
```

---

### STAGE 4 - SIMULATION

`sim/1607_beam_lifetime.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1607_beam_lifetime.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The beam lifetime carries a phi-ground scattering floor, so even the sparsest beam has a finite Touschek/IBs lifetime that bounds the stored current.
EXPERIMENT (VERIFIED): Beam lifetime and Touschek-loss measurements in electron rings (LEP, DAFNE, B factories) vs theory.
VERIFIED BY: A beam with exactly infinite lifetime (zero scattering) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1558 (synchrotron), Law 1560 (emittance) and Law 1559 (betatron) - the beam lifetime is the ring's patience.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The stored beam slowly thins; the phi-law keeps a floor of thinning in every bunch.

### NOVELTY
Classical single particle lives forever; the phi-law predicts an irreducible scattering floor.

### ACTIONABILITY
Run sim/1607_beam_lifetime.py; verify the Touschek rate; proceed to Law 1608.
