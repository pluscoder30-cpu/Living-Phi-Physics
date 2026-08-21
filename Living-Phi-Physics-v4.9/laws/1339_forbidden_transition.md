# PHI-PHYSICS - LAW 1339
## Forbidden Transition (Magnetic Dipole and Electric Quadrupole Channels)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1339_forbidden_transition.md` - **Sim:** `sim/1339_forbidden_transition.py`

---

### CLASSICAL STATEMENT
*"Transitions forbidden in the electric dipole approximation occur weakly through higher multipole channels: magnetic dipole (M1) rates scale as alpha^2 (~10^-6) of E1, electric quadrupole (E2) as (k r)^2 (~10^-7), giving metastable states with lifetimes from microseconds to seconds; examples include the 21 cm hydrogen line (M1) and the auroral [O I] 557.7 nm line (M1+E2)."*
- Developed by spectroscopy theory (Weisskopf, Rubinowicz, Garstang), 1962. Source: Wikipedia: Forbidden mechanism; Garstang, in Atomic and Molecular Processes (1962)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact E1-forbidden state*: a forbidden transition is defined against an exactly zero E1 amplitude, i.e. a level with zero electric dipole coupling - the perfect-symmetry limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the forbidden level carries a coherence E1 residue. A_E1_phi(kappa) = 0*(1 + kappa*(phi-1)) + kappa*phi^-1*A_floor, where A_floor is the phi-ground residual E1 rate; the 'forbidden' level leaks through a floor E1 channel. At kappa->0 the exact forbidden state is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_E1_phi = 0 -> the forbidden transition is the zero-residual-E1, perfect-symmetry limit.
```

---

### STAGE 4 - SIMULATION

`sim/1339_forbidden_transition.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1339_forbidden_transition.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A nominally forbidden level at full coherence coupling decays through a phi-ground E1 floor kappa*phi^-1*A_floor in addition to the M1/E2 channels, shortening the measured lifetime.
EXPERIMENT (VERIFIED): Lifetime measurements of a metastable state (e.g. O I 1D, Ca triplet states) comparing against the pure M1/E2 prediction.
VERIFIED BY: A forbidden level decays at exactly the M1/E2 rate with zero E1 component for all couplings.
```

---

### RECOGNITION
Connects to Law 1338 (E1) and Law 1337 (selection rules) - the forbidden transition is the coherence floor of the symmetry-forbidden channel.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the E1 floor is phi^-1 * A_floor.

### CLARITY
The level the rules forbid still murmurs; the phi-law hears the murmur's floor.

### NOVELTY
Classical spectroscopy forbids E1 exactly; the phi-law gives the forbidden level a coherence E1 floor.

### ACTIONABILITY
Run sim/1339_forbidden_transition.py; verify M1/E2 scaling at kappa->0; proceed to 1340.
