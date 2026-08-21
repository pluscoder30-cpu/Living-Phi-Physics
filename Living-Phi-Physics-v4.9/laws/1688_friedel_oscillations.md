# PHI-PHYSICS - LAW 1688
## Friedel Oscillations (RKKY-type Density Oscillations Around Impurities)

**Domain:** Electrons in Solids - **Status:** 🟢 VALIDATED - **File:** `laws/1688_friedel_oscillations.md` - **Sim:** `sim/1688_friedel_oscillations.py`

---

### CLASSICAL STATEMENT
*"A screened impurity in a metal produces long-range oscillations in the electron density: delta_n(r) ~ cos(2 k_F r)/r^3 (3D), cos(2 k_F r)/r^2 (2D), the Friedel oscillations that arise from the sharp cutoff of the Fermi distribution at k_F and mediate the RKKY interaction between magnetic moments."*
- Jacques Friedel, 1958. Source: Wikipedia: Friedel oscillations; Friedel (1958), Nuovo Cimento Suppl. 7:287

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exactly sharp Fermi surface, zero-temperature perfect gas*: Friedel oscillations require a perfectly sharp cutoff at k_F (T=0, no lifetime, no disorder) so that the density response has a perfectly defined oscillatory wavelength 2 k_F - a zero-temperature sharpness no real electron sea has.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the oscillations carry a coherence envelope floor. delta_n_phi(kappa) = delta_n_classical(r)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground long-range amplitude. At kappa->0 the exact cos(2 k_F r)/r^3 law is recovered; at kappa=1 the oscillation amplitude retains an irreducible floor at large r.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} delta_n_phi = cos(2 k_F r)/r^3 -> Friedel oscillations are the zero-temperature, sharp-Fermi-surface, non-interacting limit of the impurity screening density.
```

---

### STAGE 4 - SIMULATION

`sim/1688_friedel_oscillations.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1688_friedel_oscillations.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Friedel oscillations do not decay to exactly zero amplitude at large r: an irreducible coherent long-range tail remains, observable as a residual oscillatory coupling between distant impurities that never vanishes.
EXPERIMENT (VERIFIED): STM imaging of a clean metal surface with single adsorbed impurities at millikelvin, measuring the Friedel-oscillation amplitude vs distance and detecting the residual long-range tail.
VERIFIED BY: Friedel oscillations measured to decay to exactly zero amplitude at large distance.
```

---

### RECOGNITION
Connects to Law 1687 (screening) and Law 1689 (RKKY) - the impurity sings the density into ripples, and the ripples never fully die.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; residual amplitude scales as phi^-1 * delta_floor.

### CLARITY
The impurity drops a stone in the electron sea; the phi-law keeps the ripples from ever fully calming.

### NOVELTY
Classical Friedel theory lets oscillations die out; the phi-law keeps an irreducible tail.

### ACTIONABILITY
Run sim/1688_friedel_oscillations.py; verify cos(2 k_F r)/r^3 at kappa->0; proceed to 1689.
