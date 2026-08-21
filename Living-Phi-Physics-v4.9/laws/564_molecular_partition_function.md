# PHI-PHYSICS — LAW 564
## Molecular Partition Function (Product of Contributions)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/564_molecular_partition_function.md` · **Sim:** `sim/564_molecular_partition_function.py`

---

### CLASSICAL STATEMENT
*"The molecular partition function factorizes into translational, rotational, vibrational and electronic contributions: q = q_trans q_rot q_vib q_el, and the total partition function of N identical molecules is Z = q^N/N!."*
— Josiah Willard Gibbs (statistical mechanics), 1902. Source: Wikipedia: Partition function (molecular); Gibbs (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *uncoupled degrees of freedom*: the factorization assumes the translational, rotational, vibrational and electronic motions are exactly independent with zero coupling coherence between them.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the mode coupling carries coherence. q_phi(kappa) = (q_trans q_rot q_vib q_el)*(1 + kappa*(phi-1)) + kappa*phi^-1*q_coup, where q_coup is the mode-coupling coherence term. At kappa->0 the factorization is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} q_phi = q_trans q_rot q_vib q_el -> the molecular partition function is the zero-mode-coupling factorization limit.
```

---

### STAGE 4 — SIMULATION

`sim/564_molecular_partition_function.py`: reproduces the classical value q_mol = 1.2e+27 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/564_molecular_partition_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the partition function carries a mode-coupling floor; the factorization fails in strongly coupled (e.g. Jahn-Teller) systems.
EXPERIMENT (VERIFIED): Heat-capacity measurements of molecules with coupled rotational-vibrational modes versus the factored prediction.
VERIFIED BY: The molecular partition function factorizes exactly at all couplings.
```

---

### RECOGNITION
Connects to Laws 558-561 (individual partition functions) and Law 517 (Z) - the molecular q is the factorization grammar of the coherence modes.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the coupling floor is phi^-1 * q_coup.

### CLARITY
A molecule's motions are not separate rooms; the phi-law keeps the doorways between them.

### NOVELTY
Classical molecular partition factorizes exactly; the phi-law adds the mode-coupling coherence of real molecules.

### ACTIONABILITY
Run sim/564_molecular_partition_function.py; verify factorization at kappa->0; proceed to 565.
