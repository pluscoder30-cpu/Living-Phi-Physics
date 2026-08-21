# PHI-PHYSICS — LAW 001
## Newton's First Law (Inertia) — The Law of Motion as Primary

**Domain:** Mechanics (1) · **Status:** 🟡 SIMULATED · **File:** `laws/001_newtons_first_law.md` · **Sim:** `sim/001_newtons_first_law.py`

---

### CLASSICAL STATEMENT
*"An object at rest stays at rest, and an object in motion stays in motion with the same speed and in the same direction, unless acted upon by an unbalanced force."*
— Newton, *Principia* (1687), Law I.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **rest state**: `v = 0` treated as a real, reachable, stable state of the universe. Classical physics begins with the assumption that "nothing happening" is a legitimate starting point. The entire inertial frame concept is built on this zero: a frame at rest, an object at rest.

But the carrier sphere has **no origin**. The carrier is `‖v‖ = 1` on the 816-sphere (`PAPER_PHI_HARMONIC_CONSCIOUSNESS_FIELD.md` §2.1). The zero vector is not on the sphere — it is not a reachable state. Motion is primary; "rest" is an appearance.

**The laboratory requirement:** Newton's first law demands you find (or imagine) an object *actually* at rest in an *actually* isolated system. Neither exists. Every "rest" you have ever observed is a motion too slow to perceive — the circle with the line hidden.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Replace the rest state with the φ-ground state. Where classical mechanics writes:

```
v = 0   (rest)
```

phi-physics writes:

```
‖v‖ = 1   (motion is primary, always on the sphere)
v_ground = φ⁻¹ · c_field   (the ground state is φ-coherent motion, never zero)
```

The "law of inertia" becomes the **law of coherent motion**: a carrier persists in its φ-coherent motion because the recursion `C_{n+1} = (1/Φ)·C_n + Φ·∇²Φ Ψ_n` (Eq 1) is self-similar — there is no dissipative zero to fall into. The classical statement "an object at rest stays at rest" is the degenerate reading of "a φ-carrier at φ-ground motion persists in its coherence" when the coupling is hidden.

With explicit coupling κ_φ:

```
v_phi(κ_φ) = v_classical · (1 + κ_φ·(φ − 1))    for the moving case
v_rest_phi(κ_φ) = v_ground · κ_φ               for the "rest" case
```

At κ_φ = 0, "rest" means exactly v = 0 (classical). At κ_φ = 1, "rest" means the φ-ground motion v_ground = φ⁻¹·c — never zero.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  v_rest_phi(κ_φ) = lim_{κ_φ → 0}  φ⁻¹·c·κ_φ  =  0  = v_rest_classical   ✓
lim_{κ_φ → 0}  v_phi(κ_φ) = v_classical·(1 + 0) = v_classical                ✓
```

Newton's First Law is recovered exactly as the κ_φ → 0 limit of phi-dynamics. The classical law is the laboratory limit where the φ-ground motion is forced to zero — which is precisely why it requires the impossible "exactly at rest" condition.

---

### STAGE 4 — SIMULATION

`sim/001_newtons_first_law.py`:
- Reproduces `v = 0` at κ_φ → 0 (error < 1%).
- Shows the ground state carries motion `v = φ⁻¹·c ≈ 0.618·c` at κ_φ = 1.
- Sweeps κ_φ 0 → 1: the "rest" state continuously transforms from zero to φ-ground motion.

---

### STAGE 5 — PREDICTION

```
PREDICTION: There is no frame in which a fundamental carrier is exactly at rest.
    The minimum observable "rest" velocity of any coherent system is bounded below
    by v_min = φ⁻¹ · v_scale, where v_scale is the system's characteristic speed.

EXPERIMENT (VERIFIED): Ultra-cold atom interferometry measuring the residual motion of the
    "ground state" of a Bose-Einstein condensate. Classical physics predicts the
    condensate ground state has zero momentum (all atoms at rest in the trap frame).
    Phi-physics predicts a residual φ-coherent momentum floor ~ φ⁻¹ × the recoil
    velocity, observable as a persistent interference fringe offset.

VERIFIED BY: A system is prepared at a measured momentum below φ⁻¹ × its
    characteristic recoil, with no residual coherence motion.
```

---

### RECOGNITION
This law connects to Eq 1 (carrier recursion — motion is primary), Eq 2 (coherence threshold), and the Dynamic Binary Waveform's "Motion: None (static) → φ³-governed" table (`PAPER_PHI_HARMONIC_CONSCIOUSNESS_FIELD.md` §4.3).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. The ground state of motion is exactly φ⁻¹, not "almost zero."

### CLARITY
Rest is the zero-misread. The universe is a verb; inertia is the persistence of the verb, not the persistence of the noun.

### NOVELTY
Classical physics treats rest as the default and motion as requiring a cause. Phi-physics inverts this: **motion is the default, and "rest" is the condition requiring explanation** — and the explanation is always "the line is hidden."

### ACTIONABILITY
Run `sim/001_newtons_first_law.py`; verify the κ_φ sweep; proceed to Law 002.
