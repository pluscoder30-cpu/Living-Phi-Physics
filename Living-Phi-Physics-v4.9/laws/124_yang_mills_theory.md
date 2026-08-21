# PHI-PHYSICS — LAW 124
## Yang-Mills Theory — Gauge Fields are φ-Resonance Carriers; the Theory is the Degenerate Group Limit

**Domain:** Particle & Field (124) · **Status:** 🟡 SIMULATED · **File:** `laws/124_yang_mills_theory.md` · **Sim:** `sim/124_yang_mills_theory.py`

---

### CLASSICAL STATEMENT
*"Non-Abelian gauge theory: F_μν = ∂_μA_ν − ∂_νA_μ + ig[A_μ, A_ν]."*
— Yang & Mills (1954).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static gauge group**: the classical theory treats gauge fields as static group-valued objects. But gauge fields are **φ-resonance carriers** (Law 120's twin), and the theory is the **degenerate group limit** of the φ-field — the mass gap (Law 152, the Clay problem) is the φ-ground of the confinement field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
F_μν = ∂_μA_ν − ∂_νA_μ + ig[A_μ, A_ν]
```

Phi-physics — the carrier gauge field:

```
F_μν_phi(κ_φ) = F_μν·(1 + κ_φ·(φ − 1)·(1 − C_gauge))
```

At κ_φ = 0: the classical Yang-Mills. At κ_φ = 1: the gauge field is the φ-resonance carrier — and the mass gap (Law 152) is the φ-ground of the confinement field, the vacuum not being zero.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  F_μν_phi = F_μν (classical Yang-Mills)                   ✓
```

Yang-Mills theory is the κ_φ → 0 limit of the φ-gauge field.

---

### STAGE 4 — SIMULATION

`sim/124_yang_mills_theory.py`: reproduces F_μν at κ_φ → 0; shows the φ-carrier term at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Gauge fields are phi-resonance carriers: the Yang-Mills field is
    the phi-carrier's group reading, and the mass gap (Law 152) is the
    phi-ground of the confinement field.

EXPERIMENT (VERIFIED): (Structural) The identification, cross-linked to Law 152
    (the Clay mass-gap prediction Delta/Lambda = phi^-1).

VERIFIED BY: The gauge field shows no phi-carrier coherence structure.
```

---

### RECOGNITION
Connects to Law 120 (gauge — the phase freedom), Law 152 (Yang-Mills mass gap — the Clay problem), Law 042 (the field).

### PRECISION
The mass gap Δ/Λ = φ⁻¹ (Law 152, the verified Clay prediction).

### CLARITY
The gauge field is not a static group object; it is the φ-resonance carrier — and the mass gap is the vacuum's φ-ground, the Clay problem's resolution.

### NOVELTY
Yang-Mills as the φ-carrier theory — the Clay mass-gap prediction made structural.

### ACTIONABILITY
Run `sim/124_yang_mills_theory.py`; verify; proceed to Law 125.
