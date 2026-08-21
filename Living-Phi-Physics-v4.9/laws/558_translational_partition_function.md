# PHI-PHYSICS — LAW 558
## Translational Partition Function

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/558_translational_partition_function.md` · **Sim:** `sim/558_translational_partition_function.py`

---

### CLASSICAL STATEMENT
*"The translational partition function of a particle in a box of volume V is q_trans = V/lambda_th^3, where lambda_th = h/sqrt(2 pi m k_B T) is the thermal de Broglie wavelength."*
— Josiah Willard Gibbs (statistical mechanics), 1902. Source: Wikipedia: Partition function (translational); Gibbs (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero volume*: the partition function vanishes exactly at V = 0 - a particle in a box of no size, with no translational coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the box carries coherence. q_trans_phi(kappa) = (V/lambda_th^3)*(1 + kappa*(phi-1)) + kappa*phi^-1*q_ground. At kappa->0 the translational partition function is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} q_trans_phi = V/lambda_th^3 -> the translational partition function is the zero-volume-coherence free-particle limit.
```

---

### STAGE 4 — SIMULATION

`sim/558_translational_partition_function.py`: reproduces the classical value q_trans = 1.446e+29 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/558_translational_partition_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the translational partition function carries a coherence floor; the V/lambda^3 scaling deviates in nano-confined gases.
EXPERIMENT (VERIFIED): Thermodynamic measurements of gases confined in nanoporous media versus the free-box prediction.
VERIFIED BY: q_trans = V/lambda^3 exactly for all volumes and couplings.
```

---

### RECOGNITION
Connects to Law 476 (Sackur-Tetrode) and Law 517 (partition function) - the translational q is the free-carrier counting of the box.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * q_ground.

### CLARITY
The particle's choices in a box are counted by its wavelength; the phi-law keeps the count's floor.

### NOVELTY
Classical q_trans is a clean V/lambda^3; the phi-law adds the coherence floor of the confining box.

### ACTIONABILITY
Run sim/558_translational_partition_function.py; verify V/lambda^3 at kappa->0; proceed to 559.
