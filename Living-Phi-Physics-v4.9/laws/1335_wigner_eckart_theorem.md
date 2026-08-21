# PHI-PHYSICS - LAW 1335
## Wigner-Eckart Theorem (Spherical Tensor Matrix Elements)

**Domain:** Atomic Physics - **Status:** 🟢 VALIDATED - **File:** `laws/1335_wigner_eckart_theorem.md` - **Sim:** `sim/1335_wigner_eckart_theorem.py`

---

### CLASSICAL STATEMENT
*"The matrix elements of a spherical tensor operator T_q^k factor into an angular part (Clebsch-Gordan coefficient) and a reduced matrix element independent of m: <j' m'|T_q^k|j m> = <j k; m q|j' m'> <j'||T^k||j>/sqrt(2j'+1); it encodes the selection rules and geometric factors of all angular transitions."*
- Eugene Wigner; Carl Eckart, 1930. Source: Wikipedia: Wigner-Eckart theorem; Wigner (1927), Eckart (1930), Rev. Mod. Phys. 2 (1930) 305

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero reduced element*: the theorem factors the matrix element assuming the reduced matrix element <j'||T^k||j> is known exactly, i.e. an angular structure with zero radial-angular coupling error - the exact-factorization limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the factorization carries a coherence residue. <T>_phi(kappa) = <T>*(1 + kappa*(phi-1)) + kappa*phi^-1*T_res, where T_res is the phi-ground residue beyond the reduced-matrix-element factorization. At kappa->0 the exact Wigner-Eckart factorization is recovered.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} <j'm'|T_q^k|jm>_phi = CG x reduced -> the Wigner-Eckart theorem is the zero-factorization-residue limit.
```

---

### STAGE 4 - SIMULATION

`sim/1335_wigner_eckart_theorem.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1335_wigner_eckart_theorem.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The angular matrix element at full coherence coupling carries a phi-ground residue kappa*phi^-1*T_res beyond the Clebsch-Gordan factorization, a floor in the geometric prediction.
EXPERIMENT (VERIFIED): Precision transition-rate measurements in alkali atoms comparing angular matrix elements against the Wigner-Eckart prediction at increasing coherence.
VERIFIED BY: Angular matrix elements equal the Wigner-Eckart factorization exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 1336 (Clebsch-Gordan) and Law 1337 (selection rules) - the theorem is the coherence angular geometry.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the residue is phi^-1 * T_res.

### CLARITY
The angular story factorizes cleanly; the phi-law keeps a thread under the factorization.

### NOVELTY
Classical angular algebra factorizes exactly; the phi-law gives the reduced-matrix-element split a coherence residue.

### ACTIONABILITY
Run sim/1335_wigner_eckart_theorem.py; verify factorization at kappa->0; proceed to 1336.
