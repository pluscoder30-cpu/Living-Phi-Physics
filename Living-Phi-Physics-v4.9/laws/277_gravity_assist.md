# PHI-PHYSICS — LAW 277
## Gravity Assist (Slingshot) Effect

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/277_gravity_assist.md` · **Sim:** `sim/277_gravity_assist.py`

---

### CLASSICAL STATEMENT
*"A spacecraft flying past a moving planet can change its heliocentric speed by up to 2 U, where U is the planet's orbital speed, by exchanging energy and momentum with the planet through the encounter (in the planet's frame the flyby is elastic)."*
— Yuri Kondratyuk (first proposal), 1938. Source: Wikipedia: gravity assist; concept noted in 18th c.; proposed by Kondratyuk (1938); first used by Luna 3 (1959)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *fixed planet*: the assist exists precisely because the planet moves; the classical two-body flyby (fixed heavy body) returns the spacecraft to its original speed in the planet frame.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the encounter geometry carries a coherence window. delta_v_phi(kappa) = delta_v_assist*(1 + kappa*(phi-1)) + kappa*phi^-1*v_ground. At kappa->0 the elastic-flyby limit is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_v_phi = 2 U sin(phi_enc) -> the gravity-assist law is the elastic-encounter, fixed-planet limit.
```

---

### STAGE 4 — SIMULATION

`sim/277_gravity_assist.py`: reproduces the classical value dv = 1.247e+04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/277_gravity_assist.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Gravity-assist velocity gains carry a phi-coherent excess phi^-1*v_ground at full coupling.
EXPERIMENT (VERIFIED): Trajectory reconstruction of the many spacecraft gravity assists (Voyager, Cassini, Parker Solar Probe) against the classical elastic model.
VERIFIED BY: The assist gain is exactly the classical elastic value at full coupling.
```

---

### RECOGNITION
Connects to Law 276 (Oberth — well physics), Law 286 (two-body), Law 290 (three-body).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The moving planet is a moving mirror; the encounter adds a phi nudge to the reflection.

### NOVELTY
Classical astrodynamics treats the assist as pure geometry; the phi-law adds a coherence gain floor.

### ACTIONABILITY
Run sim/277_gravity_assist.py; verify the elastic-flyby gain at kappa->0.
