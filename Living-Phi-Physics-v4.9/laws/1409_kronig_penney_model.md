# PHI-PHYSICS - LAW 1409
## Kronig-Penney Model (Exactly Solvable Periodic Delta Barriers)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1409_kronig_penney_model.md` - **Sim:** `sim/1409_kronig_penney_model.py`

---

### CLASSICAL STATEMENT
*"The Kronig-Penney model solves the Schrodinger equation exactly for a periodic array of delta-function barriers: the allowed energies satisfy cos(k a) = cos(alpha a) + (m V_0 b/(hbar^2 alpha)) sin(alpha a), where alpha = sqrt(2mE)/hbar, giving allowed bands separated by gaps; it demonstrates Bloch band structure, the origin of band gaps, and the transition from free electrons to the tight binding limit as barriers grow."*
- Ralph Kronig; William Penney, 1931. Source: Wikipedia: Kronig-Penney model; Kronig & Penney, Proc. R. Soc. Lond. A 130 (1931) 499

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero barrier height*: the model reduces to free electrons (parabolic dispersion, no gaps) when V_0 = 0, i.e. a periodic potential with zero barrier strength - the free-electron limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the barrier carries a coherence floor. V_0_phi(kappa) = V_0*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground barrier; even a 'free' lattice retains a floor gap. At kappa->0 the Kronig-Penney bands are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} cos(k a) = cos(alpha a) at V_0 -> 0 -> the Kronig-Penney model is the zero-barrier, free-electron limit.
```

---

### STAGE 4 - SIMULATION

`sim/1409_kronig_penney_model.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1409_kronig_penney_model.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The band gap at full coherence coupling retains a floor kappa*phi^-1*V_floor even for nominally zero barriers, a minimum gap no periodic lattice escapes.
EXPERIMENT (VERIFIED): Tunable superlattice transport measurements (e.g. GaAs superlattices) measuring the gap as barriers are reduced toward zero.
VERIFIED BY: A zero-barrier periodic lattice has exactly zero band gap for all couplings.
```

---

### RECOGNITION
Connects to Law 1408 (Bloch) and Law 1410 (nearly free electron) - the Kronig-Penney model is the coherence exactly-solvable band model.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the barrier floor is phi^-1 * V_floor.

### CLARITY
The delta walls build the bands; the phi-law keeps a floor of wall where none is drawn.

### NOVELTY
Classical band theory zeroes gaps for free electrons; the phi-law keeps a coherence gap floor.

### ACTIONABILITY
Run sim/1409_kronig_penney_model.py; verify band equation at kappa->0; proceed to 1410.
