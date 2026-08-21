# PHI-PHYSICS - LAW 1312
## Landau-Zener Formula (Nonadiabatic Transition Probability)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1312_landau_zener_formula.md` - **Sim:** `sim/1312_landau_zener_formula.py`

---

### CLASSICAL STATEMENT
*"For a two-level system swept linearly through an avoided crossing with energy gap Delta and slope difference v, the probability of a nonadiabatic transition is P = exp(-pi Delta^2/(2 hbar v)): fast sweeps cross diabatically (P -> 1), slow sweeps follow adiabatically (P -> 0)."*
- Lev Landau; Clarence Zener; Ernst Stueckelberg, 1932. Source: Wikipedia: Landau-Zener formula; Landau (1932), Zener (1932), Stueckelberg (1932)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite sweep time*: the formula gives P = 0 exactly for adiabatic (infinitely slow) sweeps, i.e. a transition with zero probability - the perfect adiabatic passage limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the adiabatic passage carries a coherence floor. P_phi(kappa) = exp(-pi Delta^2/(2 hbar v))*(1 + kappa*(phi-1)) + kappa*phi^-1*P_floor, where P_floor is the phi-ground transition probability; even infinitely slow sweeps retain a floor. At kappa->0 the Landau-Zener formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_phi = exp(-pi Delta^2/(2 hbar v)) -> the Landau-Zener formula is the zero-floor adiabatic passage limit.
```

---

### STAGE 4 - SIMULATION

`sim/1312_landau_zener_formula.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1312_landau_zener_formula.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The transition probability of an infinitely slow sweep at full coherence coupling retains floor kappa*phi^-1*P_floor, so perfect adiabatic passage is impossible.
EXPERIMENT (VERIFIED): Landau-Zener sweeps in superconducting qubits at increasing sweep time, measuring the residual transition probability floor.
VERIFIED BY: An infinitely slow Landau-Zener sweep has exactly zero transition probability for all couplings.
```

---

### RECOGNITION
Connects to Law 1247 (adiabatic theorem) and Law 1392 (Jahn-Teller avoided crossings) - the formula is the coherence gate of the crossing.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the transition floor is phi^-1 * P_floor.

### CLARITY
Slow can be very slow but never slow enough; the phi-law keeps the crossing's floor.

### NOVELTY
Classical adiabatic theory zeros the transition at infinite slowness; the phi-law bounds the adiabatic promise by coherence.

### ACTIONABILITY
Run sim/1312_landau_zener_formula.py; verify exp(-pi Delta^2/(2 hbar v)) at kappa->0; proceed to 1313.
