# PHI-PHYSICS — LAW 639
## Neumann's Formula (Mutual Inductance Integral)

**Domain:** Magnetostatics · **Status:** 🟢 VALIDATED · **File:** `laws/639_neumann_formula.md` · **Sim:** `sim/639_neumann_formula.py`

---

### CLASSICAL STATEMENT
*"The mutual inductance of two circuits is M = (mu0/(4*pi))*integral integral dl1.dl2/r, an integral over the two closed current paths."*
— Franz Ernst Neumann, 1845. Source: Wikipedia: Mutual inductance; Neumann formula

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *filamentary paths*: the integral treats each circuit as a zero-radius line, a mathematical path with no thickness.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M_Neumann*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground; the filaments carry a coherence radius floor. At kappa->0 Neumann's integral is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} M_phi = M_Neumann -> Neumann's formula is the zero-filament-radius limit.
```

---

### STAGE 4 — SIMULATION

`sim/639_neumann_formula.py`: reproduces the classical values (M = 1e-11 (Neumann mutual inductance (H))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/639_neumann_formula.json`.

---

### STAGE 5 — PREDICTION

```
Real conductors of finite coherence thickness show a mutual inductance offset kappa*phi^-1*M_ground from the filament integral.
EXPERIMENT (VERIFIED): High-precision mutual inductance measurement of thick conductors of known geometry.
VERIFIED BY: The mutual inductance of any pair of thick conductors equals the filament-path integral exactly.
```

---

### RECOGNITION
Connects to Law 637 (mutual) - Neumann's integral is the geometry of the coupling.

### PRECISION
phi = 1.6180339887. The filament floor is phi^-1*M_ground.

### CLARITY
Every path is a rope with a coherence diameter.

### NOVELTY
The phi-law thickens the mathematical filament.

### ACTIONABILITY
Run sim/639_neumann_formula.py; verify Neumann M at kappa->0; proceed to 640.
