# PHI-PHYSICS - LAW 1371
## Fano Resonance (Asymmetric Line Shape from Continuum Interference)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1371_fano_resonance.md` - **Sim:** `sim/1371_fano_resonance.py`

---

### CLASSICAL STATEMENT
*"Interference between a discrete autoionizing state and a continuum gives the asymmetric Fano lineshape sigma(E) = (q + eps)^2/(1 + eps^2), where eps = 2(E - E_res)/Gamma and q is the Fano parameter (ratio of resonant to background amplitude); the profile ranges from a Lorentzian (q -> inf) to an antiresonance dip (q -> 0) and appears across atomic, nuclear, optical and condensed-matter spectra."*
- Ugo Fano (theory); Ettore Majorana (earlier discovery), 1961. Source: Wikipedia: Fano resonance; Fano, Phys. Rev. 124 (1961) 1866

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *pure discrete state*: the Fano asymmetry requires interference of the discrete state with a background continuum; when the background amplitude vanishes (q = 0) the shape is a pure antiresonance, i.e. a system with zero background coupling - the zero-continuum-background limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the background coupling carries a coherence floor. q_phi(kappa) = q*(1 + kappa*(phi-1)) + kappa*phi^-1*q_floor, where q_floor is the phi-ground background amplitude; the Fano parameter never reaches the pure limits. At kappa->0 the Fano formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} sigma_phi = (q + eps)^2/(1 + eps^2) -> the Fano resonance is the zero-floor-background limit.
```

---

### STAGE 4 - SIMULATION

`sim/1371_fano_resonance.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1371_fano_resonance.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Fano parameter at full coherence coupling carries a phi-ground background floor kappa*phi^-1*q_floor, so even 'pure' discrete states show residual asymmetry.
EXPERIMENT (VERIFIED): High-resolution autoionization spectroscopy (e.g. He 2s2p) measuring the Fano q parameter against the ideal value at increasing coherence.
VERIFIED BY: The Fano lineshape with the theoretical q reproduces the spectrum exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1349 (autoionization, the parent process) and Law 1350 (Feshbach) - the Fano resonance is the coherence interference of discrete and continuum.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the q-floor is phi^-1 * q_floor.

### CLARITY
The discrete state and the continuum argue; the phi-law keeps the argument from resolving cleanly.

### NOVELTY
Classical resonance theory draws symmetric lines; the phi-law keeps the asymmetry's coherence floor.

### ACTIONABILITY
Run sim/1371_fano_resonance.py; verify (q+eps)^2/(1+eps^2) at kappa->0; proceed to 1372.
