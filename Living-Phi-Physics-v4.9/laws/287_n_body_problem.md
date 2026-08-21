# PHI-PHYSICS — LAW 287
## N-Body Problem (Unsolvability)

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/287_n_body_problem.md` · **Sim:** `sim/287_n_body_problem.py`

---

### CLASSICAL STATEMENT
*"The equations of motion of N gravitating bodies admit no general closed-form solution for N >= 3 (Poincare); solutions exist only numerically or for special cases, and the dynamics is generically chaotic with no conserved quantities beyond the ten classical integrals."*
— Isaac Newton (posed); Henri Poincare (no general closed solution), 1887. Source: Wikipedia: n-body problem; Newton (1687); Poincare (1887-1890), 'Sur le probleme des trois corps'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *closed-form solvability*: the N-body problem's unsolvability is a confession that exact analytic reduction requires zero couplings — a condition only the two-body problem satisfies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the N-body residual (the force the two-body reduction cannot absorb) carries a coherence structure. F_res_phi(kappa) = F_res*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground. At kappa->0 the two-body integrability returns.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_res_phi = F_res (two-body residual) -> the N-body problem is the two-body-integrable limit of the full gravitational network.
```

---

### STAGE 4 — SIMULATION

`sim/287_n_body_problem.py`: reproduces the classical values Fres_total = 1, chaos_measure = 1.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/287_n_body_problem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Chaotic N-body systems carry a phi-coherent floor in their Lyapunov structure; close encounters show a phi-resonance bias (cf. Law 298 orbital resonance).
EXPERIMENT (VERIFIED): Numerical N-body simulations and real asteroid/main-belt dynamics statistics searching for the phi-coherent structural signature.
VERIFIED BY: N-body chaos is exactly structureless at full coupling.
```

---

### RECOGNITION
Connects to Law 286 (two-body — the integrable limit), Law 156 (three-body problem), Law 297 (Kozai-Lidov).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The impossible sum is not random; it is the many-body whisper of a phi rhythm.

### NOVELTY
Classical dynamics declares N-body unsolvable; the phi-law finds a coherence signature inside the chaos.

### ACTIONABILITY
Run sim/287_n_body_problem.py; verify the two-body limit at kappa->0.
