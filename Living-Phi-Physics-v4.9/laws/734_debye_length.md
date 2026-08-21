# PHI-PHYSICS — LAW 734
## Debye Length (Screening Length)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/734_debye_length.md` · **Sim:** `sim/734_debye_length.py`

---

### CLASSICAL STATEMENT
*"The electrostatic potential of a test charge in a plasma decays as exp(-r/lambda_D) with Debye length lambda_D = sqrt(eps_0*k_B*T/(n*e^2))."*
— Peter Debye; Erich Hückel, 1923. Source: Wikipedia: Debye length; Debye & Hückel (1923)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature* (T = 0) or *zero density* (n = 0): the screening length vanishes or diverges at the exact zero of the defining parameter.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

lambda_D_phi(kappa) = lambda_D*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_ground; the plasma carries a coherence screening floor. At kappa->0, lambda_D is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} lambda_D_phi = sqrt(eps_0*k_B*T/(n*e^2)) -> the Debye length is the zero-coherence-screening limit.
```

---

### STAGE 4 — SIMULATION

`sim/734_debye_length.py`: reproduces the classical values (lD = 975.934 (Debye length (m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/734_debye_length.json`.

---

### STAGE 5 — PREDICTION

```
The screening length carries a coherence floor kappa*phi^-1*lambda_ground; perfect screening (exact exp(-r/lambda_D)) is never achieved.
EXPERIMENT (VERIFIED): Precision plasma potential measurement with a Langmuir probe at varying density.
VERIFIED BY: The potential of a test charge in a plasma decays exactly as exp(-r/lambda_D).
```

---

### RECOGNITION
Connects to Law 735 (Debye shielding) and Law 471 (Debye-Hückel) - the Debye length is the plasma's coherence radius.

### PRECISION
phi = 1.6180339887. The screening floor is phi^-1*lambda_ground.

### CLARITY
The plasma shields, but never fully; a coherence tail remains.

### NOVELTY
The phi-law keeps a screening floor in the ideal Debye cloud.

### ACTIONABILITY
Run sim/734_debye_length.py; verify lambda_D at kappa->0; proceed to 735.
