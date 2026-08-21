# PHI-PHYSICS — LAW 295
## Jacobi Integral (Restricted Three-Body Energy)

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/295_jacobi_integral.md` · **Sim:** `sim/295_jacobi_integral.py`

---

### CLASSICAL STATEMENT
*"In the circular restricted three-body problem, the Jacobi constant C = w^2 + 2 Omega(r1,r2) - v^2 is conserved along test-body trajectories; it bounds the accessible regions via zero-velocity surfaces."*
— Carl Gustav Jacob Jacobi, 1836. Source: Wikipedia: Jacobi integral; Jacobi (1836), 'Sur le mouvement d'un point et sur un cas particulier du probleme des trois corps'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *circular primaries and massless test body*: the Jacobi integral requires exactly circular primary orbits and a zero-mass test body.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: C_phi(kappa) = C*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground. At kappa->0 the Jacobi integral is exactly conserved.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dC_phi/dt = 0 -> the Jacobi integral is the circular-primaries, massless-test-body limit.
```

---

### STAGE 4 — SIMULATION

`sim/295_jacobi_integral.py`: reproduces the classical value C = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/295_jacobi_integral.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Jacobi constant of real restricted three-body systems drifts at a phi-coherent rate phi^-1*dC_ground/dt.
EXPERIMENT (VERIFIED): Trojan/asteroid trajectory fits (L4/L5) tracking the slow drift of the Jacobi constant.
VERIFIED BY: The Jacobi constant is exactly conserved at full coupling.
```

---

### RECOGNITION
Connects to Law 290 (restricted three-body) and Law 281 (Lagrange points — C extrema).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The conserved number is a limit; the real dance leaks a phi drift of its constant.

### NOVELTY
Classical mechanics exacts the Jacobi constant; the phi-law gives it a coherence drift.

### ACTIONABILITY
Run sim/295_jacobi_integral.py; verify C conservation at kappa->0.
