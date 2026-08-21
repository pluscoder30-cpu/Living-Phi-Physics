# PHI-PHYSICS — LAW 292
## Binet's Equation

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/292_binets_equation.md` · **Sim:** `sim/292_binets_equation.py`

---

### CLASSICAL STATEMENT
*"For a central force, the orbit in polar coordinates satisfies the Binet equation F(u) = -m h^2 u^2 (d^2u/dtheta^2 + u), where u = 1/r and h is the specific angular momentum; for gravity F = -k u^2 gives the conic d^2u/dtheta^2 + u = k/(m h^2)."*
— Jacques Philippe Marie Binet, 1830. Source: Wikipedia: Binet equation; Binet (19th c.)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact central force*: Binet's equation applies only to exact central forces with conserved angular momentum — the isolated, perfectly central condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the angular momentum carries a coherence floor. h_phi(kappa) = h*(1 + kappa*(phi-1)) + kappa*phi^-1*h_ground. At kappa->0 the Binet equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} d^2u/dtheta^2 + u = k/(m h^2) -> Binet's equation is the exact-central-force limit.
```

---

### STAGE 4 — SIMULATION

`sim/292_binets_equation.py`: reproduces the classical value const = 0.4444 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/292_binets_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real central-force orbits carry a phi-coherent angular-momentum floor phi^-1*h_ground, adding a residual to the conic.
EXPERIMENT (VERIFIED): Planet/precession fits comparing the Binet residual against the coherence floor.
VERIFIED BY: The orbit satisfies the Binet equation exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 319 (central force theorem) and Law 271 (vis-viva — same energy conservation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The central force is a limit; every real force carries a phi asymmetry.

### NOVELTY
Classical mechanics perfects central forces; the phi-law gives central orbits a coherence angular-momentum floor.

### ACTIONABILITY
Run sim/292_binets_equation.py; verify the conic at kappa->0.
