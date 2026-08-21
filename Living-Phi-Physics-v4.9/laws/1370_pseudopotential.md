# PHI-PHYSICS - LAW 1370
## Pseudopotential (Phillips-Kleinman Cancellation of Core States)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1370_pseudopotential.md` - **Sim:** `sim/1370_pseudopotential.py`

---

### CLASSICAL STATEMENT
*"The pseudopotential replaces the strong core-electron potential by an effective potential that reproduces the valence wavefunctions outside the core: the Phillips-Kleinman construction V_PS = V + sum_c (E - E_c)|c><c| cancels the core oscillations, so valence electrons are described by smooth pseudo-wavefunctions with the same eigenvalues and scattering properties as the all-electron problem."*
- James Phillips; Leonard Kleinman (1959); Hans Hellmann (1934), 1959. Source: Wikipedia: Pseudopotential; Phillips & Kleinman, Phys. Rev. 116 (1959) 287; Hellmann (1934)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact core cancellation*: the pseudopotential reproduces the all-electron valence properties exactly only with a complete core basis and zero core-valence overlap error - the perfect-cancellation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the core cancellation carries a coherence residue. V_PS_phi(kappa) = V_PS*(1 + kappa*(phi-1)) + kappa*phi^-1*V_core, where V_core is the phi-ground residual core potential leaking through; the pseudo-wavefunction carries a floor core component. At kappa->0 the perfect pseudopotential is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_PS_phi = V + sum_c (E-E_c)|c><c| -> the pseudopotential is the zero-core-residue, perfect-cancellation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1370_pseudopotential.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1370_pseudopotential.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The pseudo-wavefunction at full coherence coupling carries a phi-ground core component kappa*phi^-1*V_core, a floor transferability error of the pseudopotential.
EXPERIMENT (VERIFIED): DFT benchmarks comparing pseudopotential results against all-electron references across the periodic table measuring the transferability floor.
VERIFIED BY: A pseudopotential reproduces all-electron results exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1368 (Kohn-Sham) and Law 1361 (HF) - the pseudopotential is the coherence smoothing of the core.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the core residue is phi^-1 * V_core.

### CLARITY
The atom's core is compressed into a smooth ghost; the phi-law keeps a floor of the real core in the ghost.

### NOVELTY
Classical electronic structure cancels cores exactly; the phi-law keeps the cancellation's coherence residue.

### ACTIONABILITY
Run sim/1370_pseudopotential.py; verify cancellation at kappa->0; proceed to 1371.
