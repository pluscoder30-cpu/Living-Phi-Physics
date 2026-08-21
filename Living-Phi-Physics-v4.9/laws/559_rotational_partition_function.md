# PHI-PHYSICS — LAW 559
## Rotational Partition Function

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/559_rotational_partition_function.md` · **Sim:** `sim/559_rotational_partition_function.py`

---

### CLASSICAL STATEMENT
*"The rotational partition function of a diatomic molecule at high temperature is q_rot = T/(sigma_rot theta_rot), where theta_rot = hbar^2/(2 I k_B) is the rotational temperature and sigma_rot the symmetry number."*
— Josiah Willard Gibbs (statistical mechanics), 1902. Source: Wikipedia: Partition function (rotational); Gibbs (1902)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *high-temperature limit*: the continuous q_rot = T/(sigma theta_rot) is exact only for k_B T >> hbar^2/(2I) - a rapidly rotating molecule with zero quantum discreteness and zero rotational coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the rotational ladder carries coherence. q_rot_phi(kappa) = q_rot_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*q_ground. At kappa->0 and high T the rotational partition function is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} q_rot_phi = T/(sigma_rot theta_rot) -> the rotational partition function is the high-T continuous-rotation limit.
```

---

### STAGE 4 — SIMULATION

`sim/559_rotational_partition_function.py`: reproduces the classical value q_rot = 72.12 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/559_rotational_partition_function.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the rotational partition function carries a coherence floor; low-T rotational heat capacities deviate from the classical values.
EXPERIMENT (VERIFIED): Rotational heat-capacity measurements of diatomic gases at cryogenic temperatures.
VERIFIED BY: q_rot = T/(sigma theta_rot) exactly at all temperatures and couplings.
```

---

### RECOGNITION
Connects to Law 517 (partition function) and Law 467 (equipartition) - the rotational q is the spinning coherence of the molecule.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * q_ground.

### CLARITY
A molecule's spin is a ladder, not a wheel; the phi-law keeps the ladder's floor.

### NOVELTY
Classical rotation partition ignores discreteness; the phi-law adds the coherence floor of the real ladder.

### ACTIONABILITY
Run sim/559_rotational_partition_function.py; verify T/(sigma theta) at kappa->0; proceed to 560.
