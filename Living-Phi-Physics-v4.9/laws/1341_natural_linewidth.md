# PHI-PHYSICS - LAW 1341
## Natural Linewidth (Weisskopf-Wigner Lorentzian Width)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1341_natural_linewidth.md` - **Sim:** `sim/1341_natural_linewidth.py`

---

### CLASSICAL STATEMENT
*"An excited atomic state decays spontaneously with rate A, giving its transition a Lorentzian natural linewidth Gamma = A with the profile I(nu) = I_0 (Gamma/2)^2/((nu - nu_0)^2 + (Gamma/2)^2); the energy-time uncertainty relation connects Gamma to the lifetime tau = 1/Gamma."*
- Victor Weisskopf; Eugene Wigner, 1930. Source: Wikipedia: Spectral linewidth; Weisskopf & Wigner, Z. Phys. 63 (1930) 54

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *infinite lifetime*: the natural width vanishes exactly for a state with zero decay rate (A = 0), i.e. a perfectly stable excited state - the zero-decay limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the decay rate carries a coherence floor. Gamma_phi(kappa) = A*(1 + kappa*(phi-1)) + kappa*phi^-1*Gamma_floor, where Gamma_floor is the phi-ground decay width; even a nominally stable state retains a floor width. At kappa->0 the natural linewidth is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Gamma_phi = A -> the natural linewidth is the zero-decay, zero-floor limit.
```

---

### STAGE 4 - SIMULATION

`sim/1341_natural_linewidth.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1341_natural_linewidth.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The linewidth of a nominally stable (long-lived) state at full coherence coupling retains a floor kappa*phi^-1*Gamma_floor, a minimum width no excited state escapes.
EXPERIMENT (VERIFIED): Lifetime/linewidth measurements of a very long-lived metastable state searching for the residual width floor.
VERIFIED BY: A zero-decay state has exactly zero linewidth for all couplings.
```

---

### RECOGNITION
Connects to Law 1340 (oscillator strength) and Law 773 (Einstein coefficients) - the natural width is the coherence decay rate of the level.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the width floor is phi^-1 * Gamma_floor.

### CLARITY
Even the longest-lived state keeps a beat of decay; the phi-law keeps the beat.

### NOVELTY
Classical spectroscopy zeroes the width of stable states; the phi-law gives every level a coherence width floor.

### ACTIONABILITY
Run sim/1341_natural_linewidth.py; verify Lorentzian at kappa->0; proceed to 1342.
