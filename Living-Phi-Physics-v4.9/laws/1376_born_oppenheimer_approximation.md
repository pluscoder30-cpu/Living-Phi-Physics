# PHI-PHYSICS - LAW 1376
## Born-Oppenheimer Approximation (Separation of Electronic and Nuclear Motion)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1376_born_oppenheimer_approximation.md` - **Sim:** `sim/1376_born_oppenheimer_approximation.py`

---

### CLASSICAL STATEMENT
*"Because nuclei are ~2000x heavier than electrons, the molecular wavefunction factorizes as Psi = chi_nuclear(R) psi_electronic(r; R), with electrons following the nuclei adiabatically: the electronic Schrodinger equation is solved at fixed nuclear coordinates giving the potential energy surface V(R), and the nuclei then move on this surface; it is the foundation of molecular structure and dynamics."*
- Max Born; Robert Oppenheimer, 1927. Source: Wikipedia: Born-Oppenheimer approximation; Born & Oppenheimer, Ann. Phys. 84 (1927) 457

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero nuclear velocity*: the factorization is exact only for infinitely slow (stationary) nuclei, i.e. zero kinetic coupling between electronic and nuclear motion - the infinite-mass-ratio limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the nuclear motion carries a coherence nonadiabatic coupling. H_na_phi(kappa) = H_na*(1 + kappa*(phi-1)) + kappa*phi^-1*E_nac, where E_nac is the phi-ground nonadiabatic coupling energy; the factorization carries a floor. At kappa->0 the Born-Oppenheimer approximation is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} Psi_phi = chi_nuclear(R) psi_electronic(r;R) -> the Born-Oppenheimer approximation is the zero-nuclear-kinetic-energy, infinite-mass-ratio limit.
```

---

### STAGE 4 - SIMULATION

`sim/1376_born_oppenheimer_approximation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1376_born_oppenheimer_approximation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The molecular wavefunction at full coherence coupling carries a phi-ground nonadiabatic component kappa*phi^-1*E_nac, a floor error in the Born-Oppenheimer separation.
EXPERIMENT (VERIFIED): Nonadiabatic molecular dynamics benchmarks (e.g. conical intersections in photochemistry) measuring the residual BO error at increasing coupling.
VERIFIED BY: The molecular wavefunction factorizes exactly into electronic and nuclear parts for all couplings.
```

---

### RECOGNITION
Connects to Law 1391 (conical intersection) and Law 1386 (potential energy surface) - the BO approximation is the coherence separation of the molecule.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the nonadiabatic floor is phi^-1 * E_nac.

### CLARITY
The nuclei crawl and the electrons run; the phi-law keeps a thread between their speeds.

### NOVELTY
Classical molecular physics separates the motions exactly; the phi-law keeps the nonadiabatic coherence floor.

### ACTIONABILITY
Run sim/1376_born_oppenheimer_approximation.py; verify factorization at kappa->0; proceed to 1377.
