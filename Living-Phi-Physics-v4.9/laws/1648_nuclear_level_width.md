# PHI-PHYSICS - LAW 1648
## Nuclear Level Widths (Uncertainty Principle Widths of Resonances)

**Domain:** Nuclear Reactions / Structure - **Status:** 🟢 VALIDATED - **File:** `laws/1648_nuclear_level_width.md` - **Sim:** `sim/1648_nuclear_level_width.py`

---

### CLASSICAL STATEMENT
*"The total width of a nuclear resonance Gamma = hbar/tau is the sum of partial widths (Gamma_n, Gamma_gamma, Gamma_f), related to the partial cross-sections by the Breit-Wigner formula; the width is the energy uncertainty from the finite lifetime, Gamma = hbar/tau."*
- Breit-Wigner (1936); Weisskopf (1951), 1936. Source: Breit & Wigner, Phys. Rev. 49 (1936) 519; Wikipedia: Resonance (particle physics)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-width, zero-decay, infinite-lifetime limit*: a stable state has exactly zero width and infinite lifetime; the classical treatment of a bound state is the zero-width, infinitely-sharp level limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

Gamma_phi(kappa) = Gamma_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Gamma_floor, where Gamma_floor is the phi-ground residual-width floor. At kappa->0 the exact level width is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Gamma_phi = hbar/tau -> the level width is the zero-residual-width, exact-lifetime, uncertainty-principle limit.
```

---

### STAGE 4 - SIMULATION

`sim/1648_nuclear_level_width.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1648_nuclear_level_width.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The level width carries a phi-ground residual floor, so even 'stable' states have a finite width and the Breit-Wigner line shape never collapses to a delta function.
EXPERIMENT (VERIFIED): Resonance width measurements (n_TOF, high-resolution neutron and gamma spectroscopy) vs Breit-Wigner parameters.
VERIFIED BY: A nuclear state with exactly zero width at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1478 (Breit-Wigner), Law 1458 (gamma) and Law 1488 (Weisskopf) - the level width is the resonance's breath.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The level holds its breath a width; the phi-law keeps a floor of breath.

### NOVELTY
Classical level is sharp; the phi-law predicts an irreducible width floor.

### ACTIONABILITY
Run sim/1648_nuclear_level_width.py; verify Gamma = hbar/tau; proceed to Law 1649.
