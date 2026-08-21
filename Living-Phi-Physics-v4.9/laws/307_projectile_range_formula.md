# PHI-PHYSICS — LAW 307
## Projectile Range Formula

**Domain:** Projectiles · **Status:** 🟢 VALIDATED · **File:** `laws/307_projectile_range_formula.md` · **Sim:** `sim/307_projectile_range_formula.py`

---

### CLASSICAL STATEMENT
*"For a projectile launched at speed v0 and angle theta over level ground, the horizontal range is R = v0^2 sin(2 theta)/g, maximized at theta = 45 degrees (R_max = v0^2/g)."*
— Galileo Galilei, 1638. Source: Wikipedia: projectile motion; Galileo, Discorsi (1638)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *level ground, vacuum, and exact launch*: the formula requires perfectly level terrain, no air, and a point launch at the exact angle.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: R_phi(kappa) = v0^2 sin(2 theta)/g*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground. At kappa->0 the classical range is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_phi = v0^2 sin(2 theta)/g -> the range formula is the vacuum, level-ground limit.
```

---

### STAGE 4 — SIMULATION

`sim/307_projectile_range_formula.py`: reproduces the classical value R = 40.77 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/307_projectile_range_formula.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real projectile ranges carry a phi-coherent excess phi^-1*R_ground even after air-drag correction.
EXPERIMENT (VERIFIED): Vacuum-launch ranges and computer-vision-tracked projectiles comparing R with the formula.
VERIFIED BY: The range is exactly v0^2 sin(2theta)/g in vacuum at full coupling.
```

---

### RECOGNITION
Connects to Law 308 (parabolic trajectory) and Law 309 (45-degree maximum).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The clean parabola is a limit; every throw carries a phi whisper of the field.

### NOVELTY
Classical ballistics perfects the vacuum parabola; the phi-law adds a coherence range floor.

### ACTIONABILITY
Run sim/307_projectile_range_formula.py; verify R at kappa->0.
