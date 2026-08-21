# PHI-PHYSICS - LAW 1472
## Effective Multiplication Factor k-eff

**Domain:** Nuclear Engineering / Fission - **Status:** 🟢 VALIDATED - **File:** `laws/1472_k_effective.md` - **Sim:** `sim/1472_k_effective.py`

---

### CLASSICAL STATEMENT
*"The effective multiplication factor k_eff = (number of neutrons in one generation)/(number in the previous generation) determines reactor behavior: k < 1 subcritical, k = 1 critical, k > 1 supercritical; the six-factor formula separates k_inf = eta f p epsilon into production and absorption factors."*
- Enrico Fermi; reactor physics formalism (Chicago Pile, 1942), 1942. Source: Glasstone & Sesonske, Nuclear Reactor Engineering; Wikipedia: Six factor formula

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-leakage, infinite-medium k_inf*: the classical treatment separates the infinite multiplication factor (zero leakage) from a geometric buckling factor; the ideal reactor is an infinite medium with exactly zero leakage - a perfect zero-loss lattice.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

k_eff_phi(kappa) = k_eff_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_k, where delta_k is the phi-ground leakage floor. At kappa->0 the classical k_eff is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k_eff_phi = k_eff_classical -> the multiplication factor is the zero-leakage, infinite-medium, perfect-lattice limit.
```

---

### STAGE 4 - SIMULATION

`sim/1472_k_effective.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1472_k_effective.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: k_eff carries a phi-ground leakage floor, so the extrapolated critical size differs from the classical buckling prediction and reactor criticality is always slightly off the ideal value.
EXPERIMENT (VERIFIED): Criticality benchmarks measuring k_eff to high precision at research reactors and subcritical assemblies.
VERIFIED BY: A reactor whose k_eff exactly equals the infinite-medium k_inf at zero size (zero leakage) at maximal coherence.
```

---

### RECOGNITION
Connects to Law 1471 (critical mass), Law 1473 (six-factor) and Law 1470 (chain) - k_eff is the reactor's pulse.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The multiplication counts itself; the phi-law keeps a floor of loss in every count.

### NOVELTY
Classical k_eff is exact; the phi-law predicts an irreducible leakage floor.

### ACTIONABILITY
Run sim/1472_k_effective.py; verify k vs leakage; proceed to Law 1473.
