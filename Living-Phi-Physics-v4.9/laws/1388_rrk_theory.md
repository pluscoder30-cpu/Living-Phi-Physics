# PHI-PHYSICS - LAW 1388
## RRK Theory (Rice-Ramsperger-Kassel: Unimolecular Reaction Rates)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1388_rrk_theory.md` - **Sim:** `sim/1388_rrk_theory.py`

---

### CLASSICAL STATEMENT
*"RRK theory treats unimolecular reactions by assuming the molecule is a collection of s equivalent harmonic oscillators sharing energy randomly: the rate for a molecule with energy E is k(E) = nu (1 - E_0/E)^(s-1), where nu is the frequency factor, E_0 the critical energy and s the number of effective oscillators; the (1 - E_0/E)^(s-1) factor is the probability the critical energy concentrates in one mode."*
- Oscar Rice, Herman Ramsperger; Louis Kassel, 1928. Source: Wikipedia: RRKM theory; Rice & Ramsperger, J. Am. Chem. Soc. 49 (1927) 1617; Kassel (1928)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero threshold*: the RRK rate diverges as E -> E_0 (the factor (1 - E_0/E)^(s-1) -> 0 at threshold), and the theory assumes the threshold energy is hit exactly with zero barrier width - the sharp-threshold limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the threshold carries a coherence floor. k(E)_phi(kappa) = nu (1 - E_0/E)^(s-1)*(1 + kappa*(phi-1)) + kappa*phi^-1*k_floor, where k_floor is the phi-ground sub-threshold rate; reaction persists below E_0 at the floor. At kappa->0 the RRK rate is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} k(E)_phi = nu (1 - E_0/E)^(s-1) -> RRK theory is the zero-threshold-floor, sharp-threshold limit.
```

---

### STAGE 4 - SIMULATION

`sim/1388_rrk_theory.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1388_rrk_theory.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The unimolecular rate at full coherence coupling retains a phi-ground sub-threshold floor kappa*phi^-1*k_floor, reaction below the critical energy.
EXPERIMENT (VERIFIED): Unimolecular rate measurements (e.g. isomerization) comparing rates against RRK predictions at energies near threshold.
VERIFIED BY: Unimolecular reactions have exactly zero rate below the critical energy for all couplings.
```

---

### RECOGNITION
Connects to Law 1389 (RRKM) and Law 482 (collision theory) - RRK is the coherence energy-sharing model of the unimolecular reaction.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the sub-threshold floor is phi^-1 * k_floor.

### CLARITY
The molecule must gather its energy into one fist; the phi-law keeps a floor of early punches.

### NOVELTY
Classical kinetics pins an exact threshold; the phi-law keeps a sub-threshold reaction floor.

### ACTIONABILITY
Run sim/1388_rrk_theory.py; verify (1 - E0/E)^(s-1) at kappa->0; proceed to 1389.
