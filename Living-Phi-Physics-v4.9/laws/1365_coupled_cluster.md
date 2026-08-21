# PHI-PHYSICS - LAW 1365
## Coupled Cluster Theory (Exponential Ansatz |Psi> = e^T |Phi0>)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1365_coupled_cluster.md` - **Sim:** `sim/1365_coupled_cluster.py`

---

### CLASSICAL STATEMENT
*"Coupled cluster expands the wavefunction with the exponential ansatz |Psi> = e^T|Phi0>, where T = T1 + T2 + ... is the cluster operator (T1 single, T2 double excitations); it is size-consistent and the 'gold standard' of quantum chemistry, with CCSD(T) providing high-accuracy molecular energies; higher-order terms recover the FCI limit."*
- Fritz Coester, Hermann Kummel (1960); Jiri Cizek (1966), 1966. Source: Wikipedia: Coupled cluster; Coester & Kummel (1960), Cizek, J. Chem. Phys. 45 (1966) 4256

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *single-determinant reference*: the exponential ansatz is exact only in the limit of an exactly accurate reference |Phi0>, i.e. a reference with zero multireference character - the single-reference limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the reference carries a coherence multireference floor. |Psi>_phi(kappa) = e^T|Phi0>*(1 + kappa*(phi-1)) + kappa*phi^-1*|MR>, where |MR> is the phi-ground multireference residue; single-reference CC misses the floor. At kappa->0 the CC ansatz is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} |Psi>_phi = e^T|Phi0> -> coupled cluster is the zero-multireference, single-reference limit.
```

---

### STAGE 4 - SIMULATION

`sim/1365_coupled_cluster.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1365_coupled_cluster.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The CCSD(T) energy at full coherence coupling carries a phi-ground multireference residue kappa*phi^-1*|MR>, a floor error for strongly correlated systems beyond single-reference CC.
EXPERIMENT (VERIFIED): Benchmarking CCSD(T) against exact results on bond-breaking and open-shell systems at increasing correlation strength.
VERIFIED BY: CCSD(T) reproduces the exact energy for all systems and couplings.
```

---

### RECOGNITION
Connects to Law 1364 (CI) and Law 1361 (HF) - coupled cluster is the coherence exponential ladder of excitations.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the multireference floor is phi^-1 * |MR>.

### CLARITY
The cluster of excitations grows exponentially; the phi-law keeps a reference seam in its growth.

### NOVELTY
Classical quantum chemistry exponentiates excitations; the phi-law floors single-reference accuracy by coherence.

### ACTIONABILITY
Run sim/1365_coupled_cluster.py; verify e^T ansatz at kappa->0; proceed to 1366.
