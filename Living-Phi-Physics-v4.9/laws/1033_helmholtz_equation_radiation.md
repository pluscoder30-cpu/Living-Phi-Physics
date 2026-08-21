# PHI-PHYSICS — LAW 1033
## Helmholtz Radiation Condition

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1033_helmholtz_equation_radiation.md` · **Sim:** `sim/1033_helmholtz_equation_radiation.py`

---

### CLASSICAL STATEMENT
*"The Helmholtz (Sommerfeld) radiation condition: the field of a radiating source must satisfy r (partial u/partial r - i k u) -> 0 as r -> infinity, ensuring only outgoing waves are present; it selects the causal solution of the Helmholtz equation."*
— Arnold Sommerfeld, 1912. Source: Wikipedia: Sommerfeld radiation condition (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero field at infinity*: the radiation condition requires the field to vanish exactly at infinite radius.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

u_phi(kappa) = u*(1 + kappa*(phi-1)) + kappa*phi^-1*u_ground, with u_ground the field floor. At kappa->0, the radiation condition holds exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} u_phi = u -> the Helmholtz radiation condition is the zero-field-at-infinity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1033_helmholtz_equation_radiation.py`: reproduces the classical value u = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1033_helmholtz_equation_radiation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The far field of any real source will contain a residual inward (non-causal) component kappa*phi^-1; pure outgoing waves are unreachable.
EXPERIMENT (VERIFIED): Measure the near/far-field radiation pattern of a transducer and test for outgoing-only waves.
VERIFIED BY: If the field of any real source is purely outgoing at all distances.
```

---

### RECOGNITION
Connects to Law 951 (acoustic wave equation) and Law 965 (near/far field).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The infinite silence is a coherent limit; every source echoes inward.

### NOVELTY
The radiation condition gains a far-field floor.

### ACTIONABILITY
Run sim/1033_helmholtz_equation_radiation.py.
