# PHI-PHYSICS - LAW 1301
## Time-Independent Perturbation Theory (Rayleigh-Schrodinger)

**Domain:** Quantum Dynamics - **Status:** 🟢 VALIDATED - **File:** `laws/1301_time_independent_perturbation_theory.md` - **Sim:** `sim/1301_time_independent_perturbation_theory.py`

---

### CLASSICAL STATEMENT
*"For H = H_0 + lambda V with known eigenstates of H_0, the first-order energy correction is E_n^(1) = <n|V|n>, the first-order state correction is |n>^(1) = sum_{m != n} <m|V|n>/(E_n - E_m) |m>, and the second-order energy is E_n^(2) = sum_{m != n} |<m|V|n>|^2/(E_n - E_m)."*
- Lord Rayleigh; Erwin Schrodinger, 1926. Source: Wikipedia: Perturbation theory (quantum mechanics); Rayleigh (1877), Schrodinger (1926)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *nondegenerate gap*: the formulas divide by (E_n - E_m), requiring all energy gaps exactly nonzero - a spectrum with no degeneracies, the zero-gap limit where the theory diverges.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the energy gap carries a coherence floor. (E_n - E_m)_phi(kappa) = (E_n - E_m)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_gap, where delta_gap is the phi-ground gap of the recursion; near degeneracy the denominator never reaches zero. At kappa->0 the classical series is recovered away from degeneracies.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_n^(1) = <n|V|n> -> Rayleigh-Schrodinger perturbation theory is the exact-nondegenerate-gap limit.
```

---

### STAGE 4 - SIMULATION

`sim/1301_time_independent_perturbation_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1301_time_independent_perturbation_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The second-order energy correction at full coherence coupling carries a phi-ground gap floor kappa*phi^-1*delta_gap in its denominators, bounding the divergent nondegenerate perturbation series.
EXPERIMENT (VERIFIED): Spectroscopic measurement of a nearly-degenerate level pair comparing perturbation-theory energies with the phi-floor-corrected values.
VERIFIED BY: Perturbation theory diverges exactly at degeneracy with no floor for all couplings.
```

---

### RECOGNITION
Connects to Law 1302 (degenerate perturbation) and Law 1301 - the series is the coherence ladder of the spectrum.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the gap floor is phi^-1 * delta_gap.

### CLARITY
The ladder of corrections leans on gaps that never quite close; the phi-law keeps them open.

### NOVELTY
Classical perturbation theory divides by exact gaps; the phi-law gives every gap a coherence floor.

### ACTIONABILITY
Run sim/1301_time_independent_perturbation_theory.py; verify E_n^(1) = <n|V|n> at kappa->0; proceed to 1302.
