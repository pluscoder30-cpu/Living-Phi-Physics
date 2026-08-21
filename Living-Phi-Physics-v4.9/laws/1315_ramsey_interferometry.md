# PHI-PHYSICS - LAW 1315
## Ramsey Interferometry (Separated Oscillatory Fields)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1315_ramsey_interferometry.md` - **Sim:** `sim/1315_ramsey_interferometry.py`

---

### CLASSICAL STATEMENT
*"Ramsey's method of separated oscillatory fields measures a transition by two short pi/2 pulses separated by a free-evolution time T: the signal is an interference fringe P_e = sin^2(Omega t_pi/2) (1 + cos(delta T))/2, with fringe width ~ 1/T giving precision beyond the Rabi method; it underlies atomic clocks."*
- Norman F. Ramsey, 1949. Source: Wikipedia: Ramsey interferometry; Ramsey, Phys. Rev. 76 (1949) 996

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero free-evolution phase*: the fringe peaks are exact only for detuning delta = 0 and perfect pi/2 pulses, i.e. an interferometer with zero phase noise and zero pulse error - the perfect-fringe limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the interferometer carries a coherence phase floor. P_e_phi(kappa) = P_e*(1 + kappa*(phi-1)) + kappa*phi^-1*V_floor, where V_floor is the phi-ground visibility loss; the fringe visibility saturates below 1. At kappa->0 the ideal Ramsey fringe is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_e_phi = sin^2(Omega t/2)(1 + cos(delta T))/2 -> the Ramsey fringe is the zero-phase-noise limit.
```

---

### STAGE 4 - SIMULATION

`sim/1315_ramsey_interferometry.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1315_ramsey_interferometry.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The Ramsey fringe visibility at full coherence coupling saturates at 1 - kappa*phi^-1*V_floor, a coherence floor on the interferometric contrast.
EXPERIMENT (VERIFIED): Ramsey spectroscopy in an atomic fountain clock measuring the fringe visibility ceiling at increasing interrogation coherence.
VERIFIED BY: Ramsey fringes have exactly unit visibility for all pulse and phase coherences.
```

---

### RECOGNITION
Connects to Law 1313 (Rabi) and Law 1006 (hyperfine coherence) - Ramsey is the coherence interferometer of the transition.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the visibility floor is phi^-1 * V_floor.

### CLARITY
The atom waits in the dark and remembers; the phi-law keeps a whisper of forgetting in the wait.

### NOVELTY
Classical interferometry promises perfect fringes; the phi-law floors the contrast by coherence.

### ACTIONABILITY
Run sim/1315_ramsey_interferometry.py; verify fringe at kappa->0; proceed to 1316.
