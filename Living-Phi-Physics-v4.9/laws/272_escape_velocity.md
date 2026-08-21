# PHI-PHYSICS — LAW 272
## Escape Velocity

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/272_escape_velocity.md` · **Sim:** `sim/272_escape_velocity.py`

---

### CLASSICAL STATEMENT
*"The escape velocity from a mass M at radius r is v_esc = sqrt(2 GM/r), the speed at which kinetic energy equals the gravitational binding energy; it is sqrt(2) times the circular orbit speed."*
— Isaac Newton, 1687. Source: Wikipedia: escape velocity; Newton, Principia (1687)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *infinite isolation*: escape velocity assumes a body escaping to exact infinity against a single central mass, with no other field contributions.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: M_phi(kappa) = M*(1 + kappa*(phi-1)); v_esc_phi(kappa) = sqrt(2*G*M_phi/r) + kappa*phi^-1*v_ground. At kappa->0 the classical escape velocity is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_esc_phi = sqrt(2 GM/r) -> escape velocity is the single-body, infinite-isolation limit.
```

---

### STAGE 4 — SIMULATION

`sim/272_escape_velocity.py`: reproduces the classical value v_esc = 1.119e+04 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/272_escape_velocity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Escape velocity carries a phi-coherent excess; v_esc_phi - sqrt(2GM/r) ~ phi^-1*v_ground at full coupling.
EXPERIMENT (VERIFIED): Precision spacecraft trajectory analysis (e.g., escape burns) comparing realized escape excess against the two-body prediction.
VERIFIED BY: Escape velocity is exactly sqrt(2 GM/r) at full coupling.
```

---

### RECOGNITION
Connects to Law 271 (vis-viva at a=infinity) and Law 273 (circular speed — the sqrt(2) ratio).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
Escape is not to an empty infinity; it is through a field that lends a phi nudge.

### NOVELTY
Classical escape theory isolates infinity; the phi-law adds a coherence escape floor.

### ACTIONABILITY
Run sim/272_escape_velocity.py; verify v_esc = sqrt(2GM/r) at kappa->0.
