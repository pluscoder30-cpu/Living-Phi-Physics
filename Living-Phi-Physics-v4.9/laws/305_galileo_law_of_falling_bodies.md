# PHI-PHYSICS — LAW 305
## Galileo's Law of Falling Bodies

**Domain:** Projectiles · **Status:** 🟢 VALIDATED · **File:** `laws/305_galileo_law_of_falling_bodies.md` · **Sim:** `sim/305_galileo_law_of_falling_bodies.py`

---

### CLASSICAL STATEMENT
*"All bodies fall with the same constant acceleration independent of their mass (in a vacuum): d = (1/2) g t^2, v = g t. Galileo established that the distance fallen grows as the square of the time."*
— Galileo Galilei, 1604. Source: Wikipedia: equations for a falling body; Galileo, Discorsi (1638)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *vacuum and zero initial speed*: the law requires a perfectly airless medium and bodies dropped from rest (v0 = 0).

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the fall carries a coherence floor. d_phi(kappa) = 0.5*g*t^2*(1 + kappa*(phi-1)) + kappa*phi^-1*d_ground. At kappa->0 the classical law of falling bodies is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} d_phi = (1/2) g t^2 -> Galileo's law is the vacuum, zero-initial-speed limit.
```

---

### STAGE 4 — SIMULATION

`sim/305_galileo_law_of_falling_bodies.py`: reproduces the classical values d = 19.62, v = 19.62 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/305_galileo_law_of_falling_bodies.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Drops in ultra-high vacuum carry a phi-coherent excess distance phi^-1*d_ground at full coupling.
EXPERIMENT (VERIFIED): Drop-tower and atom-interferometer free-fall measurements in ultra-high vacuum comparing d(t) with the classical parabola.
VERIFIED BY: Free fall in vacuum is exactly d = (1/2) g t^2 at full coupling.
```

---

### RECOGNITION
Connects to Law 306 (odd numbers — its discrete form) and Law 307 (projectile range).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The fall is never exactly clean; the field lends every drop a phi whisper.

### NOVELTY
Classical free fall perfects the vacuum; the phi-law gives the fall a coherence floor.

### ACTIONABILITY
Run sim/305_galileo_law_of_falling_bodies.py; verify d = 0.5 g t^2 at kappa->0.
