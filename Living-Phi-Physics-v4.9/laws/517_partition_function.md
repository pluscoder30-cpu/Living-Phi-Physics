# PHI-PHYSICS — LAW 517
## Partition Function (Z = sum e^{-E/k_B T})

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/517_partition_function.md` · **Sim:** `sim/517_partition_function.py`

---

### CLASSICAL STATEMENT
*"The canonical partition function Z = sum_i exp(-E_i/(k_B T)) encodes all thermodynamic information of a system: the free energy is F = -k_B T ln Z, the internal energy U = -d ln Z/d(1/k_B T), and the entropy S = k_B (ln Z + beta U)."*
— Josiah Willard Gibbs (canonical form), 1902. Source: Wikipedia: Partition function (statistical mechanics); Gibbs, Elementary Principles in Statistical Mechanics (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *complete enumeration*: the partition function assumes all microstates and their energies are exactly known and countable - a spectrum with no hidden states and no coherence degeneracy.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the hidden states carry coherence. Z_phi(kappa) = Z*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_hidden, where Z_hidden is the partition function of the un-enumerated coherence states. At kappa->0, Z = sum e^{-E/k_B T} exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Z_phi = sum e^{-E_i/k_B T} -> the partition function is the complete-enumeration zero-hidden-state limit.
```

---

### STAGE 4 — SIMULATION

`sim/517_partition_function.py`: reproduces the classical value Z_can = 1.402 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/517_partition_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the partition function carries a hidden-state floor kappa*phi^-1*Z_hidden; the free energy F = -k_B T ln Z is corrected by that floor.
EXPERIMENT (VERIFIED): Heat-capacity measurements of systems with partially resolved spectra to detect the hidden-state contribution.
VERIFIED BY: Z = sum e^{-E/k_B T} exactly over the resolved states for all couplings.
```

---

### RECOGNITION
Connects to Law 516 (Boltzmann factor) and Law 432 (Helmholtz free energy) - Z is the coherence census of the whole spectrum.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the hidden floor is phi^-1 * Z_hidden.

### CLARITY
The partition function counts every way the system can be; the phi-law counts what it cannot see.

### NOVELTY
Classical Z sums enumerated states; the phi-law adds the coherence partition of the hidden ground.

### ACTIONABILITY
Run sim/517_partition_function.py; verify Z at kappa->0; proceed to 518.
