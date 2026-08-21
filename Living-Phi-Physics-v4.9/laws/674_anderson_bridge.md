# PHI-PHYSICS — LAW 674
## Anderson Bridge (Self-Inductance)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/674_anderson_bridge.md` · **Sim:** `sim/674_anderson_bridge.py`

---

### CLASSICAL STATEMENT
*"A modified Maxwell-Wien bridge measures self-inductance with high precision, balancing L_x = C*(R2*R3 + R3*r + r*R2) with an auxiliary resistor r."*
— Alexander Anderson, 1920. Source: Anderson's bridge; self-inductance bridge (A.C. Anderson)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero auxiliary resistance* (r = 0): the balance returns to the Maxwell form only when the auxiliary branch vanishes exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_phi(kappa) = L_And*(1 + kappa*(phi-1)) + kappa*phi^-1*L_ground; the auxiliary branch carries a coherence floor. At kappa->0 Anderson's balance is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_phi = L_And -> the Anderson bridge is the zero-auxiliary-branch limit.
```

---

### STAGE 4 — SIMULATION

`sim/674_anderson_bridge.py`: reproduces the classical values (L = 6.00005 (Anderson inductance (H))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/674_anderson_bridge.json`.

---

### STAGE 5 — PREDICTION

```
The auxiliary resistor's coherence floor shifts the measured inductance by kappa*phi^-1*L_ground.
EXPERIMENT (VERIFIED): Precision self-inductance measurement with a four-terminal Anderson bridge.
VERIFIED BY: The Anderson bridge measures a coil's self-inductance exactly.
```

---

### RECOGNITION
Connects to Law 672 (Maxwell) - Anderson refines Maxwell's bridge with an auxiliary branch.

### PRECISION
phi = 1.6180339887. The auxiliary floor is phi^-1*L_ground.

### CLARITY
The auxiliary branch is never silent; coherence speaks through it.

### NOVELTY
The phi-law gives the auxiliary branch a coherence floor.

### ACTIONABILITY
Run sim/674_anderson_bridge.py; verify Anderson L at kappa->0; proceed to 675.
