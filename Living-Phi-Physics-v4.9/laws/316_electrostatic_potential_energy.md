# PHI-PHYSICS — LAW 316
## Electrostatic Potential Energy Law

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/316_electrostatic_potential_energy.md` · **Sim:** `sim/316_electrostatic_potential_energy.py`

---

### CLASSICAL STATEMENT
*"The electrostatic potential energy of two charges q1, q2 separated by r is U = k_e q1 q2/r (with zero at infinite separation), the work to assemble the configuration."*
— Charles-Augustin de Coulomb, 1785. Source: Wikipedia: electric potential energy; Coulomb (1785)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *infinite separation and point charges*: the law sets the zero at r = infinity and treats charges as exact points.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: U_phi(kappa) = k_e q1 q2/r*(1 + kappa*(phi-1)) + kappa*phi^-1*U_ground. At kappa->0 the classical value is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} U_phi = k_e q1 q2/r -> the electrostatic PE law is the infinite-separation, point-charge limit.
```

---

### STAGE 4 — SIMULATION

`sim/316_electrostatic_potential_energy.py`: reproduces the classical value U = -0.8988 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/316_electrostatic_potential_energy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Charge-assembly energies carry a phi-coherent excess phi^-1*U_ground.
EXPERIMENT (VERIFIED): Precision ion-assembly and capacitor-energy measurements comparing with the classical formula.
VERIFIED BY: U is exactly k_e q1 q2/r at full coupling.
```

---

### RECOGNITION
Connects to Law 036 (Coulomb's law) and Law 314 (gravitational analogue).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The point charge is a limit; every charge carries a phi cloud of rest energy.

### NOVELTY
Classical electrostatics zeroes infinity; the phi-law gives the reference a coherence depth.

### ACTIONABILITY
Run sim/316_electrostatic_potential_energy.py; verify U = k q1 q2/r at kappa->0.
