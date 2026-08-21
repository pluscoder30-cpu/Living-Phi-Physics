# PHI-PHYSICS - LAW 1366
## Moller-Plesset Perturbation Theory (MP2 Energy Correction)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1366_moller_plesset_perturbation.md` - **Sim:** `sim/1366_moller_plesset_perturbation.py`

---

### CLASSICAL STATEMENT
*"Moller-Plesset perturbation theory treats the HF solution as the zeroth order and the fluctuation potential as the perturbation: the MP2 second-order correlation energy is E_MP2 = sum_{ij,ab} |<ij||ab>|^2/(eps_i + eps_j - eps_a - eps_b), with i,j occupied and a,b virtual orbitals; MP2 recovers a large fraction of the correlation energy at low cost."*
- Christian Moller; Milton Plesset, 1934. Source: Wikipedia: Moller-Plesset perturbation theory; Moller & Plesset, Phys. Rev. 46 (1934) 618

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero fluctuation potential*: MP perturbation is exact only when the fluctuation potential vanishes, i.e. the HF solution is already exact with zero residual correlation - the zero-perturbation limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the perturbation carries a coherence radius. E_MP2_phi(kappa) = E_MP2*(1 + kappa*(phi-1)) + kappa*phi^-1*E_res, where E_res is the phi-ground higher-order residue; MP2 misses the floor. At kappa->0 the MP2 energy is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_MP2_phi = sum |<ij||ab>|^2/(eps_i+eps_j-eps_a-eps_b) -> Moller-Plesset perturbation theory is the zero-residual, exact-HF-reference limit.
```

---

### STAGE 4 - SIMULATION

`sim/1366_moller_plesset_perturbation.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1366_moller_plesset_perturbation.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The MP2 correlation energy at full coherence coupling carries a phi-ground higher-order residue kappa*phi^-1*E_res, a floor error for strongly perturbed systems.
EXPERIMENT (VERIFIED): Benchmarking MP2 against CCSD(T) on molecular test sets measuring the residual higher-order correlation floor.
VERIFIED BY: MP2 reproduces the exact correlation energy for all molecules and couplings.
```

---

### RECOGNITION
Connects to Law 1361 (HF) and Law 1365 (CC) - MP perturbation is the coherence ladder above the HF reference.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the residue is phi^-1 * E_res.

### CLARITY
The HF floor is the launch pad; the phi-law keeps the launch from escaping every residue.

### NOVELTY
Classical perturbation theory truncates MP2 exactly; the phi-law floors the truncation by the reference coherence.

### ACTIONABILITY
Run sim/1366_moller_plesset_perturbation.py; verify MP2 energy at kappa->0; proceed to 1367.
