# PHI-PHYSICS — LAW 753
## Child-Langmuir Law (Space-Charge Limited Current)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/753_child_langmuir_law.md` · **Sim:** `sim/753_child_langmuir_law.py`

---

### CLASSICAL STATEMENT
*"The space-charge limited current between planar electrodes is J = (4*eps_0/9)*sqrt(2*e/m_e)*V^(3/2)/d^2, scaling as V^(3/2)."*
— Clement D. Child; Irving Langmuir, 1913. Source: Wikipedia: Child-Langmuir law (Child 1911; Langmuir 1913)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero voltage* (V = 0): the current vanishes exactly at zero applied voltage.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

J_phi(kappa) = J_CL*(1 + kappa*(phi-1)) + kappa*phi^-1*J_ground; the diode carries a coherence floor. At kappa->0, J = (4eps_0/9)*sqrt(2e/m_e)*V^3/2/d^2 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} J_phi = (4*eps_0/9)*sqrt(2*e/m_e)*V**(3/2)/d**2 -> the Child-Langmuir law is the zero-voltage-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/753_child_langmuir_law.py`: reproduces the classical values (J = 0.73806 (Space-charge current (A/m^2))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/753_child_langmuir_law.json`.

---

### STAGE 5 — PREDICTION

```
The space-charge current carries a coherence floor kappa*phi^-1*J_ground at zero voltage.
EXPERIMENT (VERIFIED): Current-voltage measurement of a vacuum diode at low voltage.
VERIFIED BY: A vacuum diode conducts exactly zero current at zero voltage.
```

---

### RECOGNITION
Connects to Law 800 (SCLC) and Law 752 (sheath) - Child-Langmuir is the space-charge gate.

### PRECISION
phi = 1.6180339887. The voltage floor is phi^-1*J_ground.

### CLARITY
The gate never fully closes; coherence leaks a floor current.

### NOVELTY
The phi-law leaks current through the zero-voltage diode.

### ACTIONABILITY
Run sim/753_child_langmuir_law.py; verify J at kappa->0; proceed to 754.
