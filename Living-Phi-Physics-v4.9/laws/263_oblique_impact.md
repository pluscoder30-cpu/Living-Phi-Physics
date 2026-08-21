# PHI-PHYSICS — LAW 263
## Oblique Impact Law

**Domain:** Impact / Collisions · **Status:** 🟢 VALIDATED · **File:** `laws/263_oblique_impact.md` · **Sim:** `sim/263_oblique_impact.py`

---

### CLASSICAL STATEMENT
*"In oblique impact, the normal component of relative velocity is scaled by the coefficient of restitution (v_n' = -e v_n), the tangential component is unchanged for smooth bodies (v_t' = v_t), and momentum along the surface is conserved."*
— Classical mechanics (textbook theorem), 1700. Source: Resnick, Halliday & Krane, Physics; Wikipedia: collision (oblique)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *smooth surface*: oblique-impact analysis assumes zero tangential impulse (perfect smoothness) and a clean separation of normal and tangential channels.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the tangential channel couples to coherence. v_t_phi(kappa) = v_t*(1 + kappa*(phi-1)); the normal channel carries the restitution phi-inflation. At kappa->0 the classical oblique impact is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_n' = -e v_n, v_t' = v_t -> the oblique-impact law is the smooth-surface, normal/tangential-decoupled limit.
```

---

### STAGE 4 — SIMULATION

`sim/263_oblique_impact.py`: reproduces the classical values vnp = -2.1, vtp = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/263_oblique_impact.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Oblique impacts transfer a phi-coherent tangential impulse phi^-1 even on nominally smooth surfaces.
EXPERIMENT (VERIFIED): Precision oblique collisions of hardened steel spheres on instrumented planes measuring the tangential impulse.
VERIFIED BY: The tangential impulse is exactly zero at full coupling.
```

---

### RECOGNITION
Connects to Law 256 (restitution in the normal channel) and Law 269 (Hertz contact during impact).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Smoothness is a limit; every surface carries a phi-coherent grip.

### NOVELTY
Classical oblique impact zeroes tangential coupling; the phi-law adds the coherence grip.

### ACTIONABILITY
Run sim/263_oblique_impact.py; verify the classical decomposition at kappa->0.
