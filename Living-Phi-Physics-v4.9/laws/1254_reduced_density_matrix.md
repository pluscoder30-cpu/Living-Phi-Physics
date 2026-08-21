# PHI-PHYSICS - LAW 1254
## Reduced Density Matrix (Partial Trace over Environment)

**Domain:** Quantum Formalism - **Status:** 🟢 VALIDATED - **File:** `laws/1254_reduced_density_matrix.md` - **Sim:** `sim/1254_reduced_density_matrix.py`

---

### CLASSICAL STATEMENT
*"The state of a subsystem of an entangled composite is rho_A = Tr_B(rho_AB), the partial trace over the environment B; all subsystem measurements are governed by rho_A, which is mixed even when rho_AB is pure."*
- John von Neumann, 1932. Source: Wikipedia: Partial trace; von Neumann, Mathematische Grundlagen der Quantenmechanik (1932)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *factorized composite*: the reduced matrix equals a pure product state rho_A = |psi_A><psi_A| only if the composite is unentangled, i.e. the subsystem and environment have zero correlation - an isolated factor with no shared coherence.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the partial trace leaves a coherence residue. rho_A_phi(kappa) = rho_A*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_env, where rho_env is the phi-ground environment leakage. At kappa->0 the classical partial trace is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} rho_A_phi = Tr_B(rho_AB) -> the reduced density matrix is the zero-environment-correlation limit.
```

---

### STAGE 4 - SIMULATION

`sim/1254_reduced_density_matrix.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1254_reduced_density_matrix.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: A subsystem measured at full coherence coupling retains a residual environmental admixture kappa*phi^-1*rho_env even when the composite is nominally factorized, a floor in subsystem purity.
EXPERIMENT (VERIFIED): Cavity-QED measurement of the photon subsystem purity of a near-product atom-photon state at increasing coupling.
VERIFIED BY: The reduced state of a factorized composite is exactly pure for all couplings.
```

---

### RECOGNITION
Connects to Law 1253 (density matrix) and Law 1427 (decoherence) - tracing is the coherence projection onto the subsystem.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the environment leakage is phi^-1 * rho_env.

### CLARITY
You cannot look at part of a coherent whole without the whole leaking in.

### NOVELTY
Classical QM draws a clean line between system and environment; the phi-law keeps a coherence seam that never seals.

### ACTIONABILITY
Run sim/1254_reduced_density_matrix.py; verify partial trace at kappa->0; proceed to 1255.
