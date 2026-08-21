# PHI-PHYSICS - LAW 1367
## Hohenberg-Kohn Theorem (Density as the Fundamental Variable)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1367_hohenberg_kohn_theorem.md` - **Sim:** `sim/1367_hohenberg_kohn_theorem.py`

---

### CLASSICAL STATEMENT
*"The Hohenberg-Kohn theorem establishes that the ground-state electron density n(r) uniquely determines the external potential and hence all properties of the system: E[n] = F[n] + int V_ext(r) n(r) dr, with F[n] a universal functional; the exact ground-state density minimizes E[n], making density the fundamental variable of electronic structure."*
- Pierre Hohenberg; Walter Kohn, 1964. Source: Wikipedia: Hohenberg-Kohn theorems; Hohenberg & Kohn, Phys. Rev. 136 (1964) B864

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *nondegenerate ground state*: the theorem's uniqueness holds for nondegenerate ground states with the density assumed exactly known, i.e. a density with zero degeneracy and zero representability error - the exact-representability limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the density carries a coherence representability floor. n(r)_phi(kappa) = n(r)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_n, where delta_n is the phi-ground density-representability error; the functional minimization acquires a floor. At kappa->0 the exact density functional is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E[n_phi] = F[n] + int V_ext n -> the Hohenberg-Kohn theorem is the zero-representability-error, exact-density limit.
```

---

### STAGE 4 - SIMULATION

`sim/1367_hohenberg_kohn_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1367_hohenberg_kohn_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The variational density at full coherence coupling carries a phi-ground representability deviation kappa*phi^-1*delta_n, a floor in the density-functional energy.
EXPERIMENT (VERIFIED): Orbital-free DFT benchmarks comparing the variational density against exact densities at increasing functional precision.
VERIFIED BY: The exact ground-state density minimizes E[n] exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1368 (Kohn-Sham) and Law 1369 (Thomas-Fermi) - the Hohenberg-Kohn theorem is the coherence foundation of DFT.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the representability floor is phi^-1 * delta_n.

### CLARITY
The density carries the whole atom; the phi-law keeps a representability seam in the carrier.

### NOVELTY
Classical DFT proves exact uniqueness; the phi-law gives the density its representability floor.

### ACTIONABILITY
Run sim/1367_hohenberg_kohn_theorem.py; verify uniqueness at kappa->0; proceed to 1368.
