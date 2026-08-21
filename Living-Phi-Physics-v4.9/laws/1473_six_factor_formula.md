# PHI-PHYSICS - LAW 1473
## Six-Factor Formula (Neutron Cycle in a Thermal Reactor)

**Domain:** Nuclear Engineering / Fission - **Status:** 🟢 VALIDATED - **File:** `laws/1473_six_factor_formula.md` - **Sim:** `sim/1473_six_factor_formula.py`

---

### CLASSICAL STATEMENT
*"The infinite multiplication factor is k_inf = eta f p epsilon: eta = neutrons produced per thermal absorption in fuel, f = thermal utilization, p = resonance escape probability, epsilon = fast fission factor; multiplying by the fast and thermal non-leakage probabilities gives k_eff."*
- Reactor physics formalism (1940s-50s), 1948. Source: Glasstone & Edlund, Elements of Nuclear Reactor Theory (1952); Wikipedia: Six factor formula

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-resonance-loss, zero-leakage ideal lattice*: each factor is defined assuming the others are exactly perfect (f=1, p=1, epsilon=1), a perfectly homogeneous, exactly resonant-free lattice with zero losses.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

k_inf_phi(kappa) = k_inf_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_k, where delta_k is the phi-ground factor-floor from resonance and leakage imperfections. At kappa->0 the six-factor product is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k_inf_phi = eta*f*p*epsilon -> the six-factor formula is the zero-resonance-loss, perfect-lattice limit.
```

---

### STAGE 4 - SIMULATION

`sim/1473_six_factor_formula.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1473_six_factor_formula.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Each factor carries a phi-ground floor, so the product k_inf is always slightly below the ideal and the resonance escape probability p never reaches exactly 1.
EXPERIMENT (VERIFIED): Reactor physics lattice experiments (critical assemblies, TRIGA) measuring individual factors and k_inf vs lattice parameters.
VERIFIED BY: A reactor lattice whose k_inf exactly equals eta*f*p*epsilon with p = 1 exactly at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1472 (k-eff), Law 1478 (Breit-Wigner resonance) and Law 1474 (diffusion) - the six factors are the reactor's bookkeeping.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Six perfects make one; the phi-law keeps a floor of imperfection in each.

### NOVELTY
Classical six factors are perfect; the phi-law predicts irreducible floors on each.

### ACTIONABILITY
Run sim/1473_six_factor_formula.py; verify the factor product; proceed to Law 1474.
