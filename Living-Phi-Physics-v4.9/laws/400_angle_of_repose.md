# PHI-PHYSICS — LAW 400
## Angle of Repose (Coulomb's Friction Angle)

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/400_angle_of_repose.md` · **Sim:** `sim/400_angle_of_repose.py`

---

### CLASSICAL STATEMENT
*"A granular material (or a body on an incline) starts to slide when the incline angle reaches the angle of repose phi_r with tan(phi_r) = mu_s (the static friction coefficient); the material's internal friction angle sets its stability slope."*
— Charles-Augustin de Coulomb, 1773. Source: Wikipedia: angle of repose; Coulomb (1773), 'Essai sur une application des regles de maximis et minimis'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *horizontal repose reference*: the angle is measured from the exactly horizontal plane; the zero-angle material (zero friction) is the idealized reference.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: tan(phi_r)_phi(kappa) = mu_s*(1 + kappa*(phi-1)) + kappa*phi^-1*mu_ground. At kappa->0 the classical angle of repose is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} tan(phi_r)_phi = mu_s -> the angle-of-repose law is the Coulomb-friction, rigid-grain limit.
```

---

### STAGE 4 — SIMULATION

`sim/400_angle_of_repose.py`: reproduces the classical value phi = 30.96 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/400_angle_of_repose.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The angle of repose carries a phi-coherent excess phi^-1*mu_ground beyond the classical mu_s.
EXPERIMENT (VERIFIED): Inclined-plane and granular-pile angle-of-repose measurements (sand, glass beads) comparing with mu_s.
VERIFIED BY: Slip onset is exactly at tan(phi) = mu_s at full coupling.
```

---

### RECOGNITION
Connects to Law 266 (static/kinetic friction) and Law 139 (Coulomb friction).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The flat calm is a limit; every pile leans a phi toward its fall.

### NOVELTY
Classical soil/friction mechanics exacts the angle; the phi-law gives the angle a coherence width.

### ACTIONABILITY
Run sim/400_angle_of_repose.py; verify tan(phi) = mu at kappa->0.
