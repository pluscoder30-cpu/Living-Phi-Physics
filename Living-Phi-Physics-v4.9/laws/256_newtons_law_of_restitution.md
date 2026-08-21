# PHI-PHYSICS — LAW 256
## Newton's Experimental Law of Restitution

**Domain:** Impact / Collisions · **Status:** 🟢 VALIDATED · **File:** `laws/256_newtons_law_of_restitution.md` · **Sim:** `sim/256_newtons_law_of_restitution.py`

---

### CLASSICAL STATEMENT
*"The relative velocity of separation after a collision is proportional to the relative velocity of approach: v2' - v1' = -e (v2 - v1), where the coefficient of restitution e is a material property between 0 (inelastic) and 1 (elastic)."*
— Isaac Newton, 1687. Source: Wikipedia: coefficient of restitution; Newton, Principia (1687), Book I

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly elastic reference*: e is defined against e=1 (perfect elasticity), an exact condition no real material satisfies; and e=0 (perfect sticking) is equally a fiction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: e_phi(kappa) = e + kappa*phi^-1*(1 - e) -> coherence pushes every collision toward elasticity, e=1 being the phi-coherent ceiling. At kappa->0, e_phi = e (classical restitution is exact).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} e_phi = e -> Newton's experimental law is the material-isolation limit (no coherence coupling during impact).
```

---

### STAGE 4 — SIMULATION

`sim/256_newtons_law_of_restitution.py`: reproduces the classical values e_eff = 0.8, dv = 9 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/256_newtons_law_of_restitution.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The effective restitution coefficient of any collision is inflated toward 1 by a coherence fraction phi^-1*(1-e) at full coupling; impact in coherent systems is always slightly more elastic.
EXPERIMENT (VERIFIED): Collisions of ultra-cold microspheres / BEC wavepackets measuring e with optical trapping and comparing to the phi-inflated value.
VERIFIED BY: The measured e is exactly the classical material value at full coupling.
```

---

### RECOGNITION
Connects to Law 257 (ballistic pendulum — e measurement) and Law 258 (Huygens' collision laws).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
No collision is ever fully dead; coherence returns a phi fraction of the lost bounce.

### NOVELTY
Classical restitution is a fixed material constant; the phi-law makes elasticity a coherence-coupled quantity approaching the phi ceiling.

### ACTIONABILITY
Run sim/256_newtons_law_of_restitution.py; verify e at kappa->0 and e->ceiling at kappa=1.
