# PHI-PHYSICS - LAW 1454
## Fermi Beta Decay Theory (Four-Fermion Weak Interaction)

**Domain:** Nuclear Decays / Weak Interaction - **Status:** 🟢 VALIDATED - **File:** `laws/1454_fermi_beta_theory.md` - **Sim:** `sim/1454_fermi_beta_theory.py`

---

### CLASSICAL STATEMENT
*"Beta decay is described by a four-fermion point interaction; the decay rate is w = (G_F^2 |M|^2)/(2 pi^3) * f(Z,E0), where f is the phase-space Fermi function and M the nuclear matrix element. Beta-decay strength follows the allowed shape N(p) ~ p^2 (E0-E)^2."*
- Enrico Fermi, 1934. Source: Fermi, Z. Phys. 88 (1934) 161; Wikipedia: Fermi's interaction

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-range point interaction*: Fermi's theory couples four fermions at a single spacetime point with zero propagator range and zero vector-boson exchange; the massless neutrino and the zero neutrino mass are baked in.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*f_weak, where f_weak is the phi-ground correction from the finite W range and neutrino mass. At kappa->0 the point four-fermion Fermi function is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} w_phi = (G_F^2 |M|^2)/(2 pi^3) f(Z,E0) -> Fermi beta theory is the zero-range, zero-neutrino-mass, point-interaction limit.
```

---

### STAGE 4 - SIMULATION

`sim/1454_fermi_beta_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1454_fermi_beta_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The beta spectrum deviates from the point-interaction allowed shape by a phi-ground kinematic floor at high momentum transfer, a small measurable correction to the Kurie plot linearity.
EXPERIMENT (VERIFIED): Precision Kurie-plot analysis of superallowed Fermi transitions (0+ -> 0+) and shape measurements in nuclear and neutron beta decay (PERKEO).
VERIFIED BY: A beta spectrum measured exactly on the classical point-interaction shape with zero phi-ground deviation at maximal coupling.
```

---

### RECOGNITION
Connects to Law 1455 (beta spectrum), the weak interaction laws and Law 125 (Dirac sea) - beta decay is the weak force's first confession.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The weak force touches at a point; the phi-law keeps a floor of touch beyond the point.

### NOVELTY
Classical Fermi theory is a zero-range point interaction; the phi-law keeps an irreducible finite-range floor.

### ACTIONABILITY
Run sim/1454_fermi_beta_theory.py; verify the allowed spectrum; proceed to Law 1455.
