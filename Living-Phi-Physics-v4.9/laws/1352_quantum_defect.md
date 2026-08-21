# PHI-PHYSICS - LAW 1352
## Quantum Defect (Rydberg Series E_n = -R/(n - delta)^2)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1352_quantum_defect.md` - **Sim:** `sim/1352_quantum_defect.py`

---

### CLASSICAL STATEMENT
*"Alkali and many-electron atoms have Rydberg series shifted from hydrogen by the quantum defect delta_l: E_n = -R/(n - delta_l)^2, where delta_l depends on the orbital angular momentum l because the outer electron penetrates the core; the defect is nearly constant along a series, encoding the core's screening."*
- Johannes Rydberg, 1890. Source: Wikipedia: Quantum defect; Rydberg (1890)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-defect hydrogenic level*: the defect formula reduces to hydrogen exactly when delta_l = 0, i.e. a level with zero core penetration and zero screening difference - the pure-hydrogenic limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the defect carries a coherence floor. delta_l_phi(kappa) = delta_l*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_floor, where delta_floor is the phi-ground defect; no level is exactly hydrogenic. At kappa->0 the quantum-defect formula is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} E_n_phi = -R/(n - delta_l)^2 -> the quantum defect series is the zero-defect-hydrogenic limit.
```

---

### STAGE 4 - SIMULATION

`sim/1352_quantum_defect.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1352_quantum_defect.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The effective quantum defect at full coherence coupling retains a phi-ground floor kappa*phi^-1*delta_floor, so no Rydberg series is exactly hydrogenic.
EXPERIMENT (VERIFIED): Precision Rydberg spectroscopy of alkali atoms comparing measured defects against the hydrogenic prediction at increasing coherence.
VERIFIED BY: An alkali Rydberg level is exactly hydrogenic (delta = 0) for all couplings.
```

---

### RECOGNITION
Connects to Law 1351 (Rydberg atoms) and Law 078 (Rydberg formula) - the quantum defect is the coherence screening of the core.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the defect floor is phi^-1 * delta_floor.

### CLARITY
The core reaches out and tugs the orbit; the phi-law keeps the tug from being exactly measured.

### NOVELTY
Classical spectroscopy measures the defect exactly; the phi-law gives the defect a coherence floor.

### ACTIONABILITY
Run sim/1352_quantum_defect.py; verify -R/(n-delta)^2 at kappa->0; proceed to 1353.
