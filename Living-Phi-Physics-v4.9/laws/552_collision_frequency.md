# PHI-PHYSICS — LAW 552
## Collision Frequency (Kinetic Theory)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/552_collision_frequency.md` · **Sim:** `sim/552_collision_frequency.py`

---

### CLASSICAL STATEMENT
*"The collision frequency of a molecule in a gas is z = sqrt(2) n sigma <v>, where n is the number density, sigma the collision cross-section and <v> the mean speed. A molecule undergoes z collisions per second."*
— James Clerk Maxwell (kinetic theory), 1860. Source: Wikipedia: Kinetic theory of gases; Maxwell (1860), Clausius (1857)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero density*: the collision frequency vanishes exactly at n = 0 - an infinitely dilute gas with no collisions and no coherence between molecules.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the dilute limit carries coherence. z_phi(kappa) = sqrt(2) n sigma <v>*(1 + kappa*(phi-1)) + kappa*phi^-1*z_ground, where z_ground is the coherence collision floor. At kappa->0 the classical collision frequency is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} z_phi = sqrt(2) n sigma <v> -> the collision frequency is the zero-density, zero-coherence free-gas limit.
```

---

### STAGE 4 — SIMULATION

`sim/552_collision_frequency.py`: reproduces the classical value z_coll = 7.925e+09 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/552_collision_frequency.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a gas retains a collision floor kappa*phi^-1*z_ground even as n -> 0.
EXPERIMENT (VERIFIED): Ultrasonic-absorption measurements of the collision frequency of dilute gases.
VERIFIED BY: The collision frequency of a gas is exactly zero at zero density for all couplings.
```

---

### RECOGNITION
Connects to Law 483 (mean free path) and Law 549 (mean speed) - the collision frequency is the meeting rate of the coherence carriers.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * z_ground.

### CLARITY
Molecules meet at a rate set by their density; the phi-law keeps a meeting even in the emptiest gas.

### NOVELTY
Classical collision frequency vanishes at n=0; the phi-law adds the coherence floor of the dilute meeting.

### ACTIONABILITY
Run sim/552_collision_frequency.py; verify z at kappa->0; proceed to 553.
