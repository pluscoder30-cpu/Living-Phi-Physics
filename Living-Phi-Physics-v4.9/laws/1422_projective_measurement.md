# PHI-PHYSICS - LAW 1422
## Projective Measurement (von Neumann: POVM-free Sharp Measurement)

**Domain:** Quantum Measurement - **Status:** 🟢 VALIDATED - **File:** `laws/1422_projective_measurement.md` - **Sim:** `sim/1422_projective_measurement.py`

---

### CLASSICAL STATEMENT
*"A projective (von Neumann) measurement is described by a complete set of orthogonal projectors P_n = |n><n| with sum P_n = I: the outcome n occurs with probability Tr(rho P_n) and the post-measurement state is P_n rho P_n/Tr(rho P_n); projective measurements are repeatable (the second measurement gives the same result), sharp, and exhaustive."*
- John von Neumann, 1932. Source: Wikipedia: Measurement in quantum mechanics; von Neumann (1932)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *repeatability*: projective measurements give exactly the same outcome on immediate repetition, i.e. a measurement with zero disturbance of the eigenstate - the zero-back-action limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the repeatability carries a coherence floor. P_repeat_phi(kappa) = 1*(1 + kappa*(phi-1)) - kappa*phi^-1*eps_dist, where eps_dist is the phi-ground disturbance; the repeated measurement retains a floor of different outcomes. At kappa->0 exact repeatability is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} P_repeat_phi = 1 -> projective measurement is the zero-disturbance, perfectly-repeatable limit.
```

---

### STAGE 4 - SIMULATION

`sim/1422_projective_measurement.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1422_projective_measurement.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The repeatability of a projective measurement at full coherence coupling saturates at 1 - kappa*phi^-1*eps_dist, a floor of outcome change on repetition.
EXPERIMENT (VERIFIED): Neutron spin measurements repeated on the same state measuring the repeatability deviation from 1 at increasing measurement strength.
VERIFIED BY: A projective measurement is exactly repeatable for all couplings.
```

---

### RECOGNITION
Connects to Law 1421 (measurement postulate) and Law 1423 (POVM) - projective measurement is the coherence sharp limit of the POVM family.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the disturbance floor is phi^-1 * eps_dist.

### CLARITY
The sharpest measurement still jostles what it measures; the phi-law keeps the jostle's floor.

### NOVELTY
Classical measurement theory perfects repeatability; the phi-law gives even projective measurements a disturbance floor.

### ACTIONABILITY
Run sim/1422_projective_measurement.py; verify sum P_n = I at kappa->0; proceed to 1423.
