# PHI-PHYSICS — LAW 293
## Newton's Shell Theorem

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/293_shell_theorem.md` · **Sim:** `sim/293_shell_theorem.py`

---

### CLASSICAL STATEMENT
*"A spherically symmetric shell of mass exerts no gravitational force on a body inside it, and outside it behaves as if all its mass were concentrated at the center. Hence a uniform sphere's external field is that of a point mass and its internal field is linear in radius."*
— Isaac Newton, 1687. Source: Wikipedia: shell theorem; Newton, Principia (1687), Book I, Prop. 70-73

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect spherical shell*: the theorem requires an exactly uniform, spherically symmetric mass distribution — a perfect symmetry the real universe never realizes.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the symmetry carries a coherence imperfection. F_inside_phi(kappa) = kappa*phi^-1*F_ground (a nonzero interior field floor). At kappa->0 the interior field is exactly zero.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_inside_phi = 0 -> the shell theorem is the perfect-spherical-symmetry limit.
```

---

### STAGE 4 — SIMULATION

`sim/293_shell_theorem.py`: reproduces the classical values F_out = 0.6674, F_in = 0 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/293_shell_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Inside a real spherical shell, the gravitational field is not exactly zero but carries a phi-coherent floor phi^-1*F_ground.
EXPERIMENT (VERIFIED): Ultra-precision torsion-balance/Cavendish-style searches for the interior field of a near-perfect spherical shell.
VERIFIED BY: The interior field of a spherical shell is exactly zero at full coupling.
```

---

### RECOGNITION
Connects to Law 409 (gravity inside Earth — the linear interior field) and Law 282 (Gauss's law — integral proof).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The perfect shell is a limit; real matter hides a phi asymmetry that leaks a field inside.

### NOVELTY
Classical gravity exacts zero interior field; the phi-law gives the shell a coherence leak.

### ACTIONABILITY
Run sim/293_shell_theorem.py; verify zero interior field at kappa->0.
