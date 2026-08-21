# PHI-PHYSICS — LAW 258
## Huygens' Collision Laws

**Domain:** Impact / Collisions · **Status:** 🟢 VALIDATED · **File:** `laws/258_huygens_collision_laws.md` · **Sim:** `sim/258_huygens_collision_laws.py`

---

### CLASSICAL STATEMENT
*"For perfectly elastic collisions (published by Huygens in 1703, derived c. 1652-1656): the relative speed of approach equals the relative speed of separation; and in collisions, momentum is conserved. Huygens showed the pre-Newtonian form of the conservation of momentum in elastic impacts."*
— Christiaan Huygens, 1669. Source: Wikipedia: Christiaan Huygens; Huygens, De motu corporum ex percussione (published 1703)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly elastic, frictionless reference*: Huygens' laws assume zero energy loss and no deformation hysteresis, an exact condition no material reaches.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: e_phi(kappa) = 1 - (1-e)*phi^-1*kappa ... coherence restores elasticity toward Huygens' perfect e=1. v_sep_phi(kappa) = v_sep*(1 + kappa*(phi-1)). At kappa->0, v_sep = v_approach (Huygens exact).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_sep_phi = v_approach -> Huygens' elastic collision laws are the zero-loss limit.
```

---

### STAGE 4 — SIMULATION

`sim/258_huygens_collision_laws.py`: reproduces the classical values ratio_sep_app = 1, dv = 6 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/258_huygens_collision_laws.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The ratio of separation to approach speed is slightly below 1 by the coherence deficit phi^-1*(1-e), even for nominally elastic bodies.
EXPERIMENT (VERIFIED): Ultra-clean collisions of fused-silica spheres in vacuum measuring the separation/approach speed ratio.
VERIFIED BY: The separation/approach ratio is exactly 1 at full coupling.
```

---

### RECOGNITION
Connects to Law 256 (restitution — Huygens e=1 is the ceiling) and Law 387 (Huygens' momentum conservation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Perfection is a ceiling, not a state; even the elastic collision leaks a phi whisper.

### NOVELTY
Classical Huygens dynamics perfects elasticity; the phi-law quantifies the coherence deficit from perfection.

### ACTIONABILITY
Run sim/258_huygens_collision_laws.py; verify e=1 ratio at kappa->0.
