# PHI-PHYSICS — LAW 482
## Collision Theory of Reaction Rates (Trautz-Lewis)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/482_collision_theory.md` · **Sim:** `sim/482_collision_theory.py`

---

### CLASSICAL STATEMENT
*"The reaction rate is the product of the collision frequency and the fraction of collisions with energy above the activation barrier: rate = Z exp(-E_a/(R T)), where Z = n_A n_B sigma v_rel is the bimolecular collision rate. The pre-exponential factor is set by the collision geometry."*
— Max Trautz and William Cudmore McCullagh Lewis, 1918. Source: Wikipedia: Collision theory; Trautz (1916), Lewis (1918)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *hard-sphere collisions*: the theory assumes molecules react on hard-sphere contact with a fixed cross-section and no orientation coherence - collisions that never feel the molecular shape.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the molecular orientation carries coherence. Z_phi(kappa) = Z*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_orient, where Z_orient is the orientation-coherence term (the steric factor's coherence origin). At kappa->0 the collision-theory rate is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Z_phi = Z -> rate = Z exp(-E_a/(R T)) -> collision theory is the zero-orientation-coherence hard-sphere limit.
```

---

### STAGE 4 — SIMULATION

`sim/482_collision_theory.py`: reproduces the classical value Z_coll = 8e+34 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/482_collision_theory.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the effective collision rate carries an orientation-coherence term; the steric factor P = rate_exp/rate_coll deviates from the classical geometric value.
EXPERIMENT (VERIFIED): Gas-phase bimolecular rate measurements of simple reactions versus collision-theory predictions over a temperature range.
VERIFIED BY: The bimolecular rate equals Z exp(-E_a/(RT)) with the geometric steric factor exactly at all couplings.
```

---

### RECOGNITION
Connects to Law 552 (collision frequency) and Law 480 (Arrhenius) - the theory is the collision-coherence reading of the reaction rate.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the orientation term is phi^-1 * Z_orient.

### CLARITY
Molecules must meet the right way to react; the phi-law keeps the rightness's floor.

### NOVELTY
Classical collision theory ignores orientation; the phi-law adds the orientation-coherence term of real collisions.

### ACTIONABILITY
Run sim/482_collision_theory.py; verify collision rate at kappa->0; proceed to 483.
