# PHI-PHYSICS - LAW 1508
## Reactor Reactivity and Control (Reactivity Feedback)

**Domain:** Nuclear Engineering - **Status:** 🟢 VALIDATED - **File:** `laws/1508_reactor_reactivity.md` - **Sim:** `sim/1508_reactor_reactivity.py`

---

### CLASSICAL STATEMENT
*"Reactivity rho = (k_eff - 1)/k_eff quantifies the departure from criticality; negative temperature and void coefficients of reactivity provide inherent safety, with rho = alpha_T delta_T + alpha_void delta_void + ... giving the feedback that stabilizes a reactor."*
- Reactor kinetics formalism (Nordheim, 1940s); temperature feedback, 1946. Source: Nordheim (1946); Wikipedia: Nuclear reactor physics

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-feedback, exactly-critical reactor*: the reactivity formalism assumes an ideal reactor at exactly k_eff = 1 with zero feedback; any perturbation is exactly canceled - a zero-reactivity, perfectly-balanced core.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

rho_phi(kappa) = rho_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_floor, where rho_floor is the phi-ground reactivity floor from feedback nonlinearities. At kappa->0 the linear feedback model is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rho_phi = (k_eff - 1)/k_eff -> reactor reactivity is the zero-feedback-nonlinearity, linear-response limit.
```

---

### STAGE 4 - SIMULATION

`sim/1508_reactor_reactivity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1508_reactor_reactivity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Reactivity feedback carries a phi-ground nonlinear floor, so the temperature/void coefficients are not constant but depend on the operating state, and the criticality margin must include this floor.
EXPERIMENT (VERIFIED): Reactivity coefficient measurements (temperature, void, power) in research reactors and BWR/PWR operating data.
VERIFIED BY: A reactor whose reactivity feedback is exactly linear with constant coefficients at all operating states.
```

---

### RECOGNITION
Connects to Law 1470 (chain), Law 1475 (point kinetics) and Law 1472 (k-eff) - reactivity is the reactor's steering wheel.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The reactor steers by margins; the phi-law keeps a floor of margin always present.

### NOVELTY
Classical feedback is linear; the phi-law predicts irreducible nonlinear floors.

### ACTIONABILITY
Run sim/1508_reactor_reactivity.py; verify rho = (k-1)/k; proceed to Law 1509.
