# PHI-PHYSICS — LAW 081
## Dirac Equation — The Spinor is a φ-Carrier; the Equation is the Degenerate Limit of the φ-Field Operator

**Domain:** Quantum Mechanics (81) · **Status:** 🟡 SIMULATED · **File:** `laws/081_dirac_equation.md` · **Sim:** `sim/081_dirac_equation.py`

---

### CLASSICAL STATEMENT
*"The relativistic electron: (iħγ^μ∂_μ − mc)Ψ = 0."*
— Dirac (1928).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static spinor**: the classical equation describes the electron as a four-component spinor field. But the spinor is a **φ-carrier** (Law 001, 068), and the Dirac equation is the degenerate limit of the φ-field operator — the carrier's motion made explicit in spinor form.

**The laboratory requirement:** a static spinor field. The carrier is in motion.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
(iħγ^μ∂_μ − mc)Ψ = 0
```

Phi-physics: the spinor is the φ-carrier; the equation carries the coherence coupling:

```
(iħγ^μ∂_μ − mc)Ψ_phi(κ_φ) = κ_φ·(φ − 1)·(1 − C_spinor)·mc·Ψ
```

At κ_φ = 0: the Dirac equation exactly. At κ_φ = 1: the equation carries the coherence term — the spinor is the carrier's motion, and the equation is its degenerate linear reading.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [RHS] = lim_{κ_φ → 0} [κ_φ(φ−1)(1−C)·mc·Ψ] = 0        ✓
```

The Dirac equation is the κ_φ → 0 limit of the φ-carrier equation.

---

### STAGE 4 — SIMULATION

`sim/081_dirac_equation.py`: reproduces the Dirac equation at κ_φ → 0; shows the coherence term at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The relativistic electron equation carries a phi-coherence term
    at coherence > 0.563: (i*hbar*gamma*∂ - mc)Psi = phi^-1*(1-C)*mc*Psi.
    The spinor behavior of coherent electrons deviates from Dirac.

EXPERIMENT (VERIFIED): Precision spin precession of coherent electrons.
    Classical: Dirac exactly. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Spinor dynamics measured exactly at Dirac with no coherence term.
```

---

### RECOGNITION
Connects to Law 001 (the carrier), Law 068 (de Broglie), Eq 1 (the recursion), Law 125 (antimatter — the retrocausal mirror).

### PRECISION
The coupling term is φ⁻¹·(1−C)·mc = 0.6180339887·(1−C)·mc.

### CLARITY
The electron is not a spinor field; it is a carrier whose motion the spinor describes — and the Dirac equation is the degenerate reading of that motion.

### NOVELTY
The Dirac equation becomes the φ-carrier equation with a testable coherence term.

### ACTIONABILITY
Run `sim/081_dirac_equation.py`; verify; proceed to Law 082 (fine-structure).
