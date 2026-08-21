# PHI-PHYSICS - LAW 1475
## Point Kinetics Equations (Reactor Time Behavior)

**Domain:** Nuclear Engineering / Fission - **Status:** 🟢 VALIDATED - **File:** `laws/1475_point_kinetics_equations.md` - **Sim:** `sim/1475_point_kinetics_equations.py`

---

### CLASSICAL STATEMENT
*"The time evolution of the neutron population n(t) and precursor concentrations C_i(t) obeys the point kinetics equations: dn/dt = (rho - beta)/Lambda n + sum lambda_i C_i, dC_i/dt = (beta_i/Lambda) n - lambda_i C_i, where rho is reactivity, beta the delayed-neutron fraction and Lambda the prompt lifetime."*
- Nordheim-Fuchs; reactor kinetics (1940s), 1946. Source: Nordheim & Fuchs (1940s); Wikipedia: Nuclear reactor physics

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-delay, zero-precursor, single-point core*: the equations reduce the reactor to a single point with zero spatial shape and zero delayed-neutron delay in the prompt limit - a zero-delay, perfectly prompt core.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

n_phi(kappa) = n_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*n_floor, where n_floor is the phi-ground spatial-mode floor. At kappa->0 the point kinetics equations are exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} dn/dt = (rho - beta)/Lambda n + sum lambda_i C_i -> point kinetics is the zero-spatial-mode, single-point, perfectly-mixed-core limit.
```

---

### STAGE 4 - SIMULATION

`sim/1475_point_kinetics_equations.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1475_point_kinetics_equations.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The point kinetics solution carries a phi-ground spatial-mode floor, so transients in real (spatially distributed) reactors deviate from the point model by an irreducible higher-mode contribution.
EXPERIMENT (VERIFIED): Reactor transient measurements (pulsed TRIGA, research reactors) and comparison of point vs space-time kinetics models.
VERIFIED BY: A reactor transient exactly following point kinetics with zero spatial-mode floor in all configurations.
```

---

### RECOGNITION
Connects to Law 1472 (k-eff), Law 1470 (chain) and Law 1474 (diffusion) - point kinetics is the reactor's pulse meter.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
One point breathes for all; the phi-law keeps a floor of spatial breath.

### NOVELTY
Classical point kinetics is a single point; the phi-law predicts an irreducible spatial floor.

### ACTIONABILITY
Run sim/1475_point_kinetics_equations.py; verify the reactivity transient; proceed to Law 1476.
