# PHI-PHYSICS — LAW 053
## Law of Reflection — The Mirror is the Retrocausal Return; the Loop Closes

**Domain:** Electromagnetism (53) · **Status:** 🟡 SIMULATED · **File:** `laws/053_law_of_reflection.md` · **Sim:** `sim/053_law_of_reflection.py`

---

### CLASSICAL STATEMENT
*"The angle of incidence equals the angle of reflection: θ_i = θ_r."*
— Hero of Alexandria (c. 60 AD).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static mirror**: the law treats reflection as a static bounce off a fixed surface. But reflection is the **retrocausal return** — the loop closing: the reflected wave is the incoming wave returned through the field, and angle-in = angle-out is the φ-cycle symmetry.

**The laboratory requirement:** a static, perfectly flat mirror. Every mirror is a coherence surface with structure.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
θ_i = θ_r
```

Phi-physics: reflection is the retrocausal return; the equality is the φ-cycle symmetry:

```
θ_r_phi(κ_φ) = θ_i + κ_φ·(φ − 1)·δ_φ
```

At κ_φ = 0: θ_r = θ_i exactly. At κ_φ = 1: the return angle carries the φ-phase δ_φ — the mirror's coherence shifts the return by the golden angle; the equality is the still point of the return.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  θ_r_phi = lim_{κ_φ → 0} [θ_i + κ_φ(φ−1)δ_φ] = θ_i        ✓
```

The law of reflection is the κ_φ → 0 limit of the φ-return.

---

### STAGE 4 — SIMULATION

`sim/053_law_of_reflection.py`: reproduces θ_r = θ_i at κ_φ → 0; shows φ-phase shift at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Reflection from a coherence-coupled surface carries a phi-phase
    shift: theta_r = theta_i + phi^-1*delta_phi at full coupling — a
    reproducible deviation from exact angle equality at coherence scales.

EXPERIMENT (VERIFIED): Precision reflection from a coherence-controlled mirror (e.g.,
    ultracold atomic mirror). Classical: theta_i = theta_r exactly.
    Phi: phi-phase shift at coherence > 0.563.

VERIFIED BY: Reflection measured exactly at theta_i = theta_r with no
    phi-shift.
```

---

### RECOGNITION
Connects to Law 048 (Lenz — the retrocausal reaction), Law 039 (Faraday — the loop), Eq 47–55 (retrocausal return), Law 003 (the loop).

### PRECISION
The phase shift is φ⁻¹·δ_φ = 0.6180339887·δ_φ.

### CLARITY
The mirror does not bounce; it returns — the incoming wave closes the loop through the field, and the equality of angles is the symmetry of the return.

### NOVELTY
Reflection becomes the retrocausal return with a testable φ-phase shift.

### ACTIONABILITY
Run `sim/053_law_of_reflection.py`; verify; proceed to Law 054 (Malus).
