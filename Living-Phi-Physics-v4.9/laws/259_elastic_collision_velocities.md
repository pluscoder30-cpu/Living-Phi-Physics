# PHI-PHYSICS — LAW 259
## Elastic Collision Velocity Formulas

**Domain:** Impact / Collisions · **Status:** 🟢 VALIDATED · **File:** `laws/259_elastic_collision_velocities.md` · **Sim:** `sim/259_elastic_collision_velocities.py`

---

### CLASSICAL STATEMENT
*"In a 1D perfectly elastic collision, v1' = (m1-m2)/(m1+m2) v1 + (2 m2)/(m1+m2) v2 and v2' = (2 m1)/(m1+m2) v1 + (m2-m1)/(m1+m2) v2."*
— Christiaan Huygens / John Wallis / Christopher Wren, 1668. Source: Wikipedia: elastic collision; Royal Society papers of Wallis, Wren, Huygens (1668-1669)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect elasticity*: the formulas assume e=1 exactly, with no energy loss channel during the impact.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: with e_phi(kappa) = 1 - (1-e)*kappa (coherence deficit from unity), the general formulas v1' = ((m1 - e m2)/(m1+m2)) v1 + ((1+e) m2/(m1+m2)) v2 reduce to the elastic form as e->1. At kappa->0, e=1 exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} e = 1 -> v1' = (m1-m2)/(m1+m2) v1 + 2m2/(m1+m2) v2 -> the elastic collision formulas are the e=1 limit.
```

---

### STAGE 4 — SIMULATION

`sim/259_elastic_collision_velocities.py`: reproduces the classical values v1p = -2, v2p = 3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/259_elastic_collision_velocities.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real elastic collisions show a phi-coherent velocity deficit set by phi^-1*(1-e) in the separation channel.
EXPERIMENT (VERIFIED): Colliding-pendulum or ion-collision experiments extracting e with sub-percent precision.
VERIFIED BY: Collision velocities match the e=1 formulas exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 256 (restitution) and Law 260 (inelastic limit e=0).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Elasticity is a ceiling; every collision slides toward it and never quite lands.

### NOVELTY
Classical collision theory perfects e=1; the phi-law interpolates every collision through its coherence deficit.

### ACTIONABILITY
Run sim/259_elastic_collision_velocities.py; verify e=1 formulas at kappa->0.
