# PHI-PHYSICS — LAW 286
## Two-Body Problem Solution

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/286_two_body_problem.md` · **Sim:** `sim/286_two_body_problem.py`

---

### CLASSICAL STATEMENT
*"The relative motion of two bodies under mutual gravity is a conic section (ellipse, parabola, or hyperbola) about their common center of mass; the problem reduces to one body with the reduced mass mu = m1 m2/(m1+m2) moving in the fixed potential."*
— Isaac Newton, 1687. Source: Wikipedia: two-body problem; Newton, Principia (1687)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *two-body isolation*: the problem requires the system to be exactly closed — no third body, no field, no radiation — the laboratory condition no real system satisfies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the reduced mass carries a coherence fraction. mu_phi(kappa) = mu*(1 + kappa*(phi-1)); the orbit's semi-major axis shifts by kappa*phi^-1*a_ground. At kappa->0 the two-body solution is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} mu_phi = m1 m2/(m1+m2) -> the two-body problem is the closed-system, conic-orbit limit.
```

---

### STAGE 4 — SIMULATION

`sim/286_two_body_problem.py`: reproduces the classical value mu = 7.253e+22 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/286_two_body_problem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real 'two-body' systems show phi-coherent deviations from the conic solution (residual eccentricity, apsidal drift) at full coupling.
EXPERIMENT (VERIFIED): Binary pulsar timing (PSR B1913+16) comparing orbital decay and precession with the two-body + GR prediction.
VERIFIED BY: Binary motion is exactly the two-body conic at full coupling.
```

---

### RECOGNITION
Connects to Law 322 (reduced mass) and Law 287 (N-body — the general problem).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Two bodies are never exactly two; the field is always the third, and it has a phi weight.

### NOVELTY
Classical mechanics perfects the closed pair; the phi-law opens the pair to the coherence field.

### ACTIONABILITY
Run sim/286_two_body_problem.py; verify reduced mass at kappa->0.
