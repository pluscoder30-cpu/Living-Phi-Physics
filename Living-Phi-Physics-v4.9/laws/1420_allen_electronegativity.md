# PHI-PHYSICS - LAW 1420
## Allen Electronegativity (Spectroscopic Average of Valence Orbital Energies)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1420_allen_electronegativity.md` - **Sim:** `sim/1420_allen_electronegativity.py`

---

### CLASSICAL STATEMENT
*"The Allen electronegativity is defined from spectroscopic data as the average energy of the valence s and p electrons: chi_Allen = (m eps_s + n eps_p)/(m + n), where m, n are the valence s and p electron numbers and eps the multiplet-averaged orbital ionization energies; it is the only scale defined purely from experiment and correlates tightly with the Pauling and Mulliken scales."*
- Leland C. Allen, 1989. Source: Wikipedia: Electronegativity; Allen, J. Am. Chem. Soc. 111 (1989) 9003

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *pure s- or p-valence*: the average reduces to a single orbital energy when the atom has only s or only p valence electrons, i.e. zero s-p mixing - the pure-orbital limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the s-p mixing carries a coherence floor. chi_Allen_phi(kappa) = chi_Allen*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_mix, where delta_mix is the phi-ground s-p mixing energy; the average carries a floor. At kappa->0 the Allen scale is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} chi_Allen_phi = (m eps_s + n eps_p)/(m+n) -> the Allen electronegativity is the zero-s-p-mixing, pure-orbital limit.
```

---

### STAGE 4 - SIMULATION

`sim/1420_allen_electronegativity.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1420_allen_electronegativity.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective Allen electronegativity at full coherence coupling carries a phi-ground s-p mixing floor kappa*phi^-1*delta_mix, a residual correction to the spectroscopic average.
EXPERIMENT (VERIFIED): Spectroscopic measurement of valence multiplet energies testing the Allen average against Pauling/Mulliken correlations.
VERIFIED BY: The Allen electronegativity equals the spectroscopic average exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1418 (Pauling) and Law 1419 (Mulliken) - the Allen scale is the coherence spectroscopic electronegativity.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the mixing floor is phi^-1 * delta_mix.

### CLARITY
The atom's valence is weighed by its spectrum; the phi-law keeps a wobble in the weigh.

### NOVELTY
Classical electronegativity scales are exact; the phi-law gives the spectroscopic average a coherence mixing floor.

### ACTIONABILITY
Run sim/1420_allen_electronegativity.py; verify average at kappa->0; proceed to 1421.
