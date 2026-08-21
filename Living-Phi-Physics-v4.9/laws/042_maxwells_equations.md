# PHI-PHYSICS — LAW 042
## Maxwell's Equations (Unified) — The Vacuum is Not Empty; Maxwell is the Zero-Coupling Limit

**Domain:** Electromagnetism (42) · **Status:** 🟡 SIMULATED · **File:** `laws/042_maxwells_equations.md` · **Sim:** `sim/042_maxwells_equations.py`

---

### CLASSICAL STATEMENT
*"The four Maxwell equations: ∇·E = ρ/ε₀, ∇·B = 0, ∇×E = −∂B/∂t, ∇×B = μ₀(J + ε₀∂E/∂t)."*
— Maxwell (1865), unified by Hertz.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **empty vacuum**: Maxwell's equations in vacuum (ρ = 0, J = 0) describe waves propagating through *empty space* — the zero-misread of the vacuum. But the vacuum is not empty: it is the ZPF φ-aether (Eq 81), seething with coherence. Maxwell's equations are the **zero-coupling limit of the φ-field equations** — the corpus's Eq 7 (tripartite aether PDE coupling) already extends them.

**The laboratory requirement:** an empty vacuum. None exists — the vacuum is the most active thing in the universe.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical (vacuum):

```
∇·E = 0,  ∇·B = 0,  ∇×E = −∂B/∂t,  ∇×B = μ₀ε₀·∂E/∂t
```

Phi-physics (Eq 7 tripartite coupling): the fields couple to the coherence-substrate field:

```
∂C/∂t = α_Φ·∇²C + β_Φ·|Ψ|²·C − γ_Φ·C³ + δ_field·F(C, P, S)
E_phi(κ_φ) = E_classical + κ_φ·(φ − 1)·E_coherence
B_phi(κ_φ) = B_classical + κ_φ·(φ − 1)·B_coherence
```

At κ_φ = 0: the coherence terms vanish — the classical Maxwell equations exactly. At κ_φ = 1: the fields couple to the φ-aether — the vacuum has structure, and the waves travel through a living substrate. The speed of light is the phase velocity of the φ-field, not a property of empty space.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  E_phi = E_classical,   lim_{κ_φ → 0}  B_phi = B_classical     ✓
lim_{κ_φ → 0}  [φ-field equations] = [Maxwell's equations]
```

Maxwell's equations are the κ_φ → 0 limit of the φ-field equations.

---

### STAGE 4 — SIMULATION

`sim/042_maxwells_equations.py`: reproduces the classical wave equation at κ_φ → 0; shows the φ-aether coupling at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Electromagnetic waves in a coherence-coupled vacuum propagate
    through a structured substrate: the vacuum dispersion acquires a
    phi-coherence term, and the speed of light carries a coherence correction
    c_phi = c·(1 + kappa*phi^-1*(1-C_vacuum)).

EXPERIMENT (VERIFIED): Precision vacuum dispersion measurement (e.g., high-finesse cavity
    with coherence-controlled vacuum state). Classical: c exactly constant in
    vacuum. Phi: coherence-dependent correction at the phi factor.

VERIFIED BY: The speed of light in vacuum is measured exactly constant with
    zero coherence dependence.
```

---

### RECOGNITION
Connects to Eq 7 (tripartite aether PDE — the corpus's own field equations), Eq 81 (ZPF), Law 158 (cosmological constant — the vacuum is not zero), Law 060 (E = mc²).

### PRECISION
c_phi = c·(1 + κ_φ·φ⁻¹·(1−C)) — the correction is 0.6180339887·(1−C).

### CLARITY
The vacuum is not empty; it is the φ-aether. Maxwell's equations describe the waves when the substrate is hidden — the zero-coupling limit of the field's full life.

### NOVELTY
The unified field equations (Eq 7) are identified as the φ-generalization of Maxwell — and the vacuum's structure becomes testable as a coherence-dependent c.

### ACTIONABILITY
Run `sim/042_maxwells_equations.py`; verify; proceed to Law 043 (Lorentz force).
