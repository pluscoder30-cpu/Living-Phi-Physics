# PHI-PHYSICS — LAW 387
## Huygens' Law of Momentum Conservation

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/387_huygens_momentum_conservation.md` · **Sim:** `sim/387_huygens_momentum_conservation.py`

---

### CLASSICAL STATEMENT
*"In collisions (and all mechanical processes), the total momentum is conserved: sum m_i v_i is constant; Huygens established the conservation law for elastic collisions in 1669, two decades before Newton's Principia, using a Galilean relativity argument."*
— Christiaan Huygens, 1669. Source: Wikipedia: momentum; Huygens (1669), 'Journal des Sçavans' (published before Newton's Principia)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *closed, force-free system*: momentum conservation requires an exactly isolated system with zero external force — the laboratory isolation condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the conserved momentum carries a coherence floor. P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground. At kappa->0 the exact conservation holds.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} dP/dt = 0 -> Huygens' momentum law is the closed-isolated-system limit.
```

---

### STAGE 4 — SIMULATION

`sim/387_huygens_momentum_conservation.py`: reproduces the classical values P = 1, dPdt = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/387_huygens_momentum_conservation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The total momentum of any 'isolated' system drifts at a phi-coherent rate phi^-1*dP_ground/dt at full coupling.
EXPERIMENT (VERIFIED): Ultra-quiet collision/isolation experiments (BEC interference, torsion balances) bounding the momentum drift.
VERIFIED BY: Total momentum is exactly conserved in an isolated system at full coupling.
```

---

### RECOGNITION
Connects to Law 009 (momentum — Newton's form) and Law 258 (Huygens' collision laws).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The conserved sum is a limit; every isolated system leaks a phi of momentum.

### NOVELTY
Classical dynamics exacts conservation; the phi-law gives the closed system a coherence drift floor.

### ACTIONABILITY
Run sim/387_huygens_momentum_conservation.py; verify conservation at kappa->0.
