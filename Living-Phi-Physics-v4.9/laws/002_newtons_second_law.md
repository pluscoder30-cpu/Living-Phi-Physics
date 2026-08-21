# PHI-PHYSICS — LAW 002
## Newton's Second Law (F = ma) — Force as Coherence Gradient

**Domain:** Mechanics (2) · **Status:** 🟡 SIMULATED · **File:** `laws/002_newtons_second_law.md` · **Sim:** `sim/002_newtons_second_law.py`

---

### CLASSICAL STATEMENT
*"The alteration of motion is ever proportional to the motive force impressed; and is made in the direction of the right line in which that force is impressed."*
— Newton, *Principia* (1687), Law II. Modern form: **F = ma**.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **equilibrium condition**: `F = 0 → a = 0` — motion stops. Classical dynamics is written around the rest solution; force is defined as *that which causes acceleration*, implying acceleration is a departure from a natural zero-acceleration state. The whole framework assumes a background of inertial rest.

But the carrier recursion (Eq 1) has no zero-acceleration baseline: `C_{n+1} = (1/Φ)·C_n + Φ·∇²Φ Ψ_n` — the state is *always* changing. The second derivative `∇²Φ` is a permanent feature, not a perturbation. Acceleration is not an interruption of rest; it is the texture of the field.

**The laboratory requirement:** F = ma demands an inertial frame — a frame with exactly zero acceleration. None exists. Every frame is itself accelerating in some φ-coherent sense; the "inertial frame" is the det = 0 fiction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Replace the static equilibrium with the φ-ground acceleration. Classical:

```
F = m·a,    with equilibrium: F = 0 ⇒ a = 0
```

Phi-physics: acceleration is coherence-gradients; force is the coupling of the carrier to the field's curvature. With explicit coupling:

```
a_phi(κ_φ) = (F/m) · (1 + κ_φ·(φ − 1)) + κ_φ · a_ground
a_ground   = φ⁻¹ · a_scale     (the φ-ground acceleration, never zero)
```

At κ_φ = 0: `a = F/m` exactly (classical). At κ_φ = 1: the natural state carries φ-ground acceleration even with F = 0 — matching Law 001's insight that rest is motion.

Equivalently, in operator form (recognizing the corpus's Eq 1):

```
a_{n+1} = (1/Φ)·a_n + Φ·∇²Φ(Ψ)      — the recursion is the law
F = m·a  is the degenerate linearization at κ_φ → 0
```

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  a_phi = lim_{κ_φ → 0} [ (F/m)(1 + κ_φ(φ−1)) + κ_φ·a_ground ]
                    = F/m + 0
                    = a_classical                                    ✓
```

Also the equilibrium limit:
```
lim_{κ_φ → 0, F → 0}  a_phi = 0  = a_classical_equilibrium          ✓
```

Newton's Second Law is the κ_φ → 0 limit of phi-dynamics. The classical "F = 0 ⇒ a = 0" is the degenerate case where the φ-ground motion is forced to zero.

---

### STAGE 4 — SIMULATION

`sim/002_newtons_second_law.py`:
- Reproduces `a = F/m` at κ_φ → 0 (error < 1%).
- Shows the natural state carries φ-ground acceleration at κ_φ = 1.
- Sweeps κ_φ 0 → 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: In any system with coherence C > C_emergence (0.563), a residual
    acceleration a_ground ≈ φ⁻¹ · a_scale persists even when the net classical
    force is zero.

EXPERIMENT (VERIFIED): Precision torsion balance / equivalence-principle test in a
    vibration-isolated chamber, measuring the residual acceleration of the
    apparatus in the "force-free" configuration. Classical: exactly 0.
    Phi-physics: a residual ~ φ⁻¹ × (thermal/coherence scale).

VERIFIED BY: The residual acceleration is measured below φ⁻¹ × the apparatus's
    characteristic acceleration scale in a coherence > 0.563 system.
```

---

### RECOGNITION
Connects to Eq 1 (the recursion — acceleration is the permanent ∇²Φ term), Eq 6 (coherence transport — force as coherence gradient), and `EQUATIONS_SET_08` (weight dynamics — the corpus already rewrites gradient descent as field dynamics).

### PRECISION
φ⁻¹ = 0.6180339887. The ground acceleration is exactly φ⁻¹ of the characteristic scale.

### CLARITY
F = ma describes how force *changes* motion. It silently assumes the zero-acceleration background. Phi-physics says: there is no background of rest — there is a background of φ-coherent motion, and force is what re-tunes it.

### NOVELTY
The classical second law defines force as the *cause of deviation from rest*. The phi second law defines force as *the coupling that re-tunes coherence*. Same mathematics at the limit; radically different ontology at the core.

### ACTIONABILITY
Run `sim/002_newtons_second_law.py`; verify; proceed to Law 003 (action = reaction as the loop).
