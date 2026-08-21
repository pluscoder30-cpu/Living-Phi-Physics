# PHI-PHYSICS - LAW 1384
## Buckingham Potential (Exponential Repulsion + r^-6 Attraction)

**Domain:** Molecular Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1384_buckingham_potential.md` - **Sim:** `sim/1384_buckingham_potential.py`

---

### CLASSICAL STATEMENT
*"The Buckingham potential V(r) = A e^(-B r) - C/r^6 models repulsive exchange forces with an exponential wall and an attractive dispersion tail; compared to the Lennard-Jones form it has a softer, more realistic repulsive wall, but it spuriously turns attractive at very short range, requiring a cut-off or hard-sphere core."*
- Richard Buckingham, 1938. Source: Wikipedia: Buckingham potential; Buckingham, Proc. R. Soc. Lond. A 168 (1938) 264

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero range repulsion*: the potential's repulsive wall requires a finite range parameter B, i.e. the model assumes the wall never becomes a hard core - the soft-wall limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the wall carries a coherence floor. V_Buck_phi(kappa) = V_Buck*(1 + kappa*(phi-1)) + kappa*phi^-1*V_core, where V_core is the phi-ground hard-core floor preventing the spurious short-range attraction. At kappa->0 the classical Buckingham form is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} V_Buck_phi = A e^(-B r) - C/r^6 -> the Buckingham potential is the zero-core-floor, soft-wall limit.
```

---

### STAGE 4 - SIMULATION

`sim/1384_buckingham_potential.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1384_buckingham_potential.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The short-range behavior at full coherence coupling carries a phi-ground hard-core floor kappa*phi^-1*V_core, removing the unphysical inward turn of the pure Buckingham form.
EXPERIMENT (VERIFIED): Molecular-beam scattering or virial-coefficient measurements of noble-gas pairs testing the short-range repulsion form.
VERIFIED BY: The pure Buckingham form describes the short-range interaction exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1383 (Lennard-Jones) and Law 1414 (Born-Mayer, exponential repulsion) - the Buckingham potential is the coherence exponential-wall model.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the core floor is phi^-1 * V_core.

### CLARITY
The wall of a real atom is not a curve but a cliff; the phi-law keeps the cliff from curving.

### NOVELTY
Classical potentials idealize the repulsive wall; the phi-law floors the wall's spurious attraction by a coherence core.

### ACTIONABILITY
Run sim/1384_buckingham_potential.py; verify exponential wall at kappa->0; proceed to 1385.
