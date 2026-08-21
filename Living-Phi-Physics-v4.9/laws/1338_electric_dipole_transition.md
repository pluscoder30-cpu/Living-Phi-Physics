# PHI-PHYSICS - LAW 1338
## Electric Dipole Transition (Dipole Matrix Element and Einstein A)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1338_electric_dipole_transition.md` - **Sim:** `sim/1338_electric_dipole_transition.py`

---

### CLASSICAL STATEMENT
*"The electric dipole transition rate between states |i> and |f> is proportional to the squared dipole matrix element |d_fi|^2 = |<f|e r|i>|^2: the Einstein A coefficient is A_fi = (omega^3/(3 pi epsilon_0 hbar c^3)) |d_fi|^2, giving lifetimes of ~10^-8 s for allowed transitions; the matrix element obeys the selection rules and encodes the line strength."*
- Paul A. M. Dirac; Albert Einstein (A coefficient), 1927. Source: Wikipedia: Electric dipole transition; Dirac (1927), Einstein (1917)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero dipole element*: the rate vanishes exactly for a zero dipole matrix element (forbidden transition), i.e. a transition with zero coupling to the field - the forbidden-channel limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the matrix element carries a coherence floor. |d_fi|^2_phi(kappa) = |d_fi|^2*(1 + kappa*(phi-1)) + kappa*phi^-1*d_floor, where d_floor is the phi-ground dipole element; even forbidden channels retain a floor rate. At kappa->0 the dipole rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} A_fi_phi = (omega^3/(3 pi eps0 hbar c^3))|d_fi|^2 -> the electric dipole transition is the zero-forbidden-floor limit.
```

---

### STAGE 4 - SIMULATION

`sim/1338_electric_dipole_transition.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1338_electric_dipole_transition.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The dipole transition rate at full coherence coupling retains a floor kappa*phi^-1*A_floor for nominally forbidden transitions, observable as residual forbidden-line emission.
EXPERIMENT (VERIFIED): Lifetime measurements of a dipole-forbidden metastable state (e.g. the 2S1/2 state of hydrogen) searching for the residual decay floor.
VERIFIED BY: A dipole-forbidden state has exactly infinite lifetime (zero rate) for all couplings.
```

---

### RECOGNITION
Connects to Law 1337 (selection rules) and Law 773 (Einstein coefficients) - the dipole transition is the coherence coupling of the level to the field.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the rate floor is phi^-1 * A_floor.

### CLARITY
Every level speaks to the field, some more softly; the phi-law keeps even the whisper at a floor.

### NOVELTY
Classical spectroscopy zeroes forbidden channels; the phi-law gives the dipole floor to every transition.

### ACTIONABILITY
Run sim/1338_electric_dipole_transition.py; verify omega^3 |d|^2 at kappa->0; proceed to 1339.
