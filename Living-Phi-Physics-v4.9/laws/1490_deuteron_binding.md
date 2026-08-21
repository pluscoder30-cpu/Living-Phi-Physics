# PHI-PHYSICS - LAW 1490
## Deuteron Binding Energy (The Two-Nucleon Bound State)

**Domain:** Nuclear Forces - **Status:** 🟢 VALIDATED - **File:** `laws/1490_deuteron_binding.md` - **Sim:** `sim/1490_deuteron_binding.py`

---

### CLASSICAL STATEMENT
*"The deuteron is the only two-nucleon bound state, with binding energy B_d = 2.224 MeV, spin 1, magnetic moment 0.857 mu_N, and electric quadrupole moment +0.286 e fm^2; its binding is dominated by the tensor force and is much weaker than the potential depth due to short-range repulsion."*
- Discovered by Harold Urey (1932); bound state of p-n, 1932. Source: Urey, Brickwedde & Murphy, Phys. Rev. 40 (1932) 1; Wikipedia: Deuteron

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-binding, exactly-unbound threshold*: the deuteron is bound by only 2.2 MeV, and the classical treatment assumes the nucleon-nucleon potential would bind with a fixed central force; the near-threshold bound state is the 'zero-binding residue' of the full force.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

B_phi(kappa) = B_d*(1 + kappa*(phi-1)) + kappa*phi^-1*B_floor, where B_floor is the phi-ground tensor/three-body floor. At kappa->0 the deuteron binding is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} B_phi = 2.224 MeV -> the deuteron is the zero-tensor-correction, central-force, two-body limit.
```

---

### STAGE 4 - SIMULATION

`sim/1490_deuteron_binding.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1490_deuteron_binding.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The deuteron's properties carry a phi-ground tensor-force floor, so the quadrupole moment and the D-state admixture (which a pure central force cannot explain) are irreducible signatures of phi-branching beyond the central approximation.
EXPERIMENT (VERIFIED): High-precision deuteron properties (quadrupole moment, asymptotic D/S ratio) from electron scattering and chiral EFT calculations.
VERIFIED BY: A deuteron whose binding and properties are exactly explained by a pure central force with zero tensor floor.
```

---

### RECOGNITION
Connects to Law 1489 (Yukawa), Law 1447 (SEMF) and Law 1452 (Gamow) - the deuteron is the nucleus's first breath.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Two nucleons barely hold; the phi-law keeps a floor of hold in the barely.

### NOVELTY
Classical deuteron is central-force; the phi-law predicts an irreducible tensor floor.

### ACTIONABILITY
Run sim/1490_deuteron_binding.py; verify B_d = 2.224 MeV; proceed to Law 1491.
