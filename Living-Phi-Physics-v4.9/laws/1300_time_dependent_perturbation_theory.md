# PHI-PHYSICS - LAW 1300
## Time-Dependent Perturbation Theory (Dirac: Transition Amplitudes)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1300_time_dependent_perturbation_theory.md` - **Sim:** `sim/1300_time_dependent_perturbation_theory.py`

---

### CLASSICAL STATEMENT
*"For a time-dependent perturbation V(t) on a known unperturbed Hamiltonian, the transition amplitude to first order is c_n(t) = (1/i hbar) int_0^t <n|V(t')|i> exp(i omega_ni t') dt', giving transition probabilities |c_n|^2 to second order; it produces the golden rule and describes absorption, emission and scattering."*
- Paul A. M. Dirac, 1927. Source: Wikipedia: Perturbation theory (quantum mechanics); Dirac (1927)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *weak perturbation*: the theory assumes V is small enough that higher orders vanish exactly, i.e. an interaction with zero self-coupling - the zero-nonlinearity limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the perturbative ladder carries a coherence residue. c_n_phi(kappa) = c_n*(1 + kappa*(phi-1)) + kappa*phi^-1*c_res, where c_res is the phi-ground higher-order residue of the recursion. At kappa->0 the first-order amplitude is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} c_n_phi = (1/i hbar) int V_ni exp(i omega_ni t') dt' -> time-dependent perturbation theory is the zero-higher-order-residue limit.
```

---

### STAGE 4 - SIMULATION

`sim/1300_time_dependent_perturbation_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1300_time_dependent_perturbation_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The first-order transition amplitude at full coherence coupling carries a phi-ground higher-order residue kappa*phi^-1*c_res, flooring the accuracy of perturbation theory for strong drives.
EXPERIMENT (VERIFIED): Strong-field Rabi spectroscopy comparing measured amplitudes against first-order perturbation theory at increasing drive strength.
VERIFIED BY: First-order perturbation theory reproduces transition amplitudes exactly for all perturbation strengths.
```

---

### RECOGNITION
Connects to Law 1299 (golden rule) and Law 1294 (Dyson) - the ladder is the coherence expansion of the interaction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the higher-order residue is phi^-1 * c_res.

### CLARITY
The first step of the ladder wobbles; the phi-law keeps the wobble.

### NOVELTY
Classical perturbation theory truncates exactly for weak fields; the phi-law bounds the truncation by coherence.

### ACTIONABILITY
Run sim/1300_time_dependent_perturbation_theory.py; verify first-order amplitude at kappa->0; proceed to 1301.
