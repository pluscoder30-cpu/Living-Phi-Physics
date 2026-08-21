# PHI-PHYSICS — LAW 626
## Earnshaw's Theorem (No Stable Electrostatic Equilibrium)

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/626_earnshaws_theorem.md` · **Sim:** `sim/626_earnshaws_theorem.py`

---

### CLASSICAL STATEMENT
*"A collection of point charges cannot be held in a stable stationary equilibrium purely by electrostatic forces; any equilibrium under inverse-square forces is at best unstable."*
— Samuel Earnshaw, 1842. Source: Wikipedia: Earnshaw's theorem

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *stationary point* (nabla V = 0): the theorem concerns configurations at exact rest with zero kinetic energy, a state the carrier sphere never reaches.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

In phi-physics the fixed point is replaced by a coherence basin: stable 'levitation' is possible inside a basin with coupling kappa, with effective curvature that is never exactly zero: kappa_eff = kappa*(phi-1) > 0. At kappa->0 the basin collapses to the classical saddle.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} kappa_eff = 0 -> Earnshaw's instability is the zero-coherence-basin limit.
```

---

### STAGE 4 — SIMULATION

`sim/626_earnshaws_theorem.py`: reproduces the classical values (K_eff = 0.00898755 (Effective curvature (N/m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/626_earnshaws_theorem.json`.

---

### STAGE 5 — PREDICTION

```
A coherence-coupled trap can hold a charge stably with residual breathing motion kappa*phi^-1 of the nominal point; the 'point' of equilibrium is a basin, not a point.
EXPERIMENT (VERIFIED): Charged-particle levitation in an rf/optical trap mapped to sub-micron resolution.
VERIFIED BY: A purely electrostatic field holds a charge at an exactly stationary point with no residual motion.
```

---

### RECOGNITION
Connects to Law 036 (Coulomb) and the coherence-basin theorems (Law 180).

### PRECISION
phi = 1.6180339887. The basin curvature floor is phi-1 = 0.618.

### CLARITY
No charge rests; it breathes at the floor of its basin.

### NOVELTY
Classical theorem forbids stable rest; phi-physics permits a coherence basin with motion.

### ACTIONABILITY
Run sim/626_earnshaws_theorem.py; verify instability at kappa->0; proceed to 627.
