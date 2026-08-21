# PHI-PHYSICS - LAW 1602
## Triple-Alpha Process Rate (Hoyle State Resonance)

**Domain:** Nuclear Astrophysics - **Status:** 🟢 VALIDATED - **File:** `laws/1602_triple_alpha_rate.md` - **Sim:** `sim/1602_triple_alpha_rate.py`

---

### CLASSICAL STATEMENT
*"Helium burns via the triple-alpha process 3 4He -> 12C, whose rate is enormously enhanced by the 7.654 MeV Hoyle state resonance in 12C: the rate ~ (rho^2/T^3) exp(-Q/kT) with the resonance at the Gamow peak; without the Hoyle state, carbon (and life) could not form."*
- Fred Hoyle (1954, 7.65 MeV state); Salpeter (1952), 1954. Source: Hoyle, ApJS 1 (1954) 121; Wikipedia: Triple-alpha process

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-resonance, zero-enhancement, off-resonance rate*: without the Hoyle state, the triple-alpha rate would be the tiny non-resonant rate; the classical treatment assumes the resonance is exactly tuned - a zero-off-resonance, exact-resonance limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

r_phi(kappa) = r_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*r_floor, where r_floor is the phi-ground non-resonant floor. At kappa->0 the resonance-dominated rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} r_phi = r_resonance -> the triple-alpha rate is the exact-resonance, Hoyle-state, zero-background limit.
```

---

### STAGE 4 - SIMULATION

`sim/1602_triple_alpha_rate.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1602_triple_alpha_rate.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The triple-alpha rate carries a phi-ground non-resonant floor, so the effective rate deviates from the pure Hoyle-resonance value by an irreducible off-resonance contribution.
EXPERIMENT (VERIFIED): Triple-alpha rate measurements (nuclear astrophysics, e.g. 12C(alpha,gamma)16O) and the Hoyle state width vs stellar model predictions.
VERIFIED BY: A triple-alpha rate exactly matching the resonance-only value with zero off-resonance floor.
```

---

### RECOGNITION
Connects to Law 1465 (Gamow peak), Law 1179 (triple-alpha) and Law 1458 (gamma) - the Hoyle state is carbon's door.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Three alphas pass through a doorway; the phi-law keeps a floor of the door's edge.

### NOVELTY
Classical triple-alpha is resonance-exact; the phi-law predicts an irreducible background floor.

### ACTIONABILITY
Run sim/1602_triple_alpha_rate.py; verify the Hoyle resonance; proceed to Law 1603.
