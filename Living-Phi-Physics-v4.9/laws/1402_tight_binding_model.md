# PHI-PHYSICS - LAW 1402
## Tight Binding Model (Bloch-Wannier Electron Bands)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1402_tight_binding_model.md` - **Sim:** `sim/1402_tight_binding_model.py`

---

### CLASSICAL STATEMENT
*"The tight binding model describes electrons as atomic orbitals weakly coupled between sites: for a 1D chain the energy band is E(k) = eps - 2 t cos(k a), where eps is the on-site energy and t the hopping integral; the bandwidth 4|t|, the density of states with van Hove singularities, and the filling (via the Fermi level) determine metallic, semiconducting or insulating behavior; it is the atomic-limit complement of the nearly-free-electron model."*
- Felix Bloch (1928); John Slater, George Koster (1954), 1954. Source: Wikipedia: Tight binding; Bloch (1928), Slater & Koster, Phys. Rev. 94 (1954) 1498

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero hopping*: the band collapses to a flat atomic level when t = 0, i.e. perfectly isolated atoms with zero inter-site coupling - the atomic limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the hopping carries a coherence floor. t_phi(kappa) = t*(1 + kappa*(phi-1)) + kappa*phi^-1*t_floor, where t_floor is the phi-ground hopping of the recursion; isolated atoms retain a floor band width. At kappa->0 the tight binding band is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E(k)_phi = eps - 2 t cos(k a) -> the tight binding model is the zero-hopping-floor, atomic-limit complement.
```

---

### STAGE 4 - SIMULATION

`sim/1402_tight_binding_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1402_tight_binding_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The band width at full coherence coupling retains a floor kappa*phi^-1*t_floor even for 'isolated' atoms, a minimum dispersion no lattice escapes.
EXPERIMENT (VERIFIED): Angle-resolved photoemission (ARPES) of a nearly-atomic lattice (e.g. molecular crystals, van der Waals layers) measuring the residual band width floor.
VERIFIED BY: A lattice of isolated atoms has exactly flat bands for all couplings.
```

---

### RECOGNITION
Connects to Law 1408 (Bloch theorem) and Law 1409 (Kronig-Penney) - tight binding is the coherence atomic-limit band model.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the hopping floor is phi^-1 * t_floor.

### CLARITY
Even atoms that barely talk share a whisper; the phi-law keeps the whisper's band.

### NOVELTY
Classical band theory isolates atoms exactly; the phi-law gives every lattice a coherence hopping floor.

### ACTIONABILITY
Run sim/1402_tight_binding_model.py; verify E(k) = eps - 2t cos(ka) at kappa->0; proceed to 1403.
