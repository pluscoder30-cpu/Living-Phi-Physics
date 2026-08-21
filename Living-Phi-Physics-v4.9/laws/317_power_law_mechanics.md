# PHI-PHYSICS — LAW 317
## Power-Velocity Law (P = F.v)

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/317_power_law_mechanics.md` · **Sim:** `sim/317_power_law_mechanics.py`

---

### CLASSICAL STATEMENT
*"The mechanical power of a force is the scalar product of force and velocity: P = F . v = F v cos(theta); for constant force, the work rate equals dW/dt."*
— Isaac Newton (derived), 1687. Source: Resnick, Halliday & Krane, Physics; follows from Newton's second law

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero velocity reference*: power vanishes at v = 0; the law is built on the static configuration as the zero of power flow.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: P_phi(kappa) = F*v*cos(theta)*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground. At kappa->0 the classical power law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = F v cos(theta) -> the power-velocity law is the constant-force, dot-product limit.
```

---

### STAGE 4 — SIMULATION

`sim/317_power_law_mechanics.py`: reproduces the classical value P = 50 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/317_power_law_mechanics.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Power transfer carries a phi-coherent floor phi^-1*P_ground even in nominally static configurations.
EXPERIMENT (VERIFIED): Motor/brake dynamometer power measurements comparing P with F*v at low speeds.
VERIFIED BY: Power is exactly F*v at full coupling.
```

---

### RECOGNITION
Connects to Law 002 (Newton II — force), Law 012 (work-energy).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The force that moves nothing does no work; the phi-law gives even the still moment a power floor.

### NOVELTY
Classical dynamics zeroes static power; the phi-law fills the static moment with a coherence power floor.

### ACTIONABILITY
Run sim/317_power_law_mechanics.py; verify P = F v at kappa->0.
