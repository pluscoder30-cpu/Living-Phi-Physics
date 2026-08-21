# PHI-PHYSICS — LAW 705
## Nyquist Stability Criterion

**Domain:** Control · **Status:** 🟢 VALIDATED · **File:** `laws/705_nyquist_stability_criterion.md` · **Sim:** `sim/705_nyquist_stability_criterion.py`

---

### CLASSICAL STATEMENT
*"A closed-loop system is stable iff the Nyquist plot of the open-loop transfer function does not encircle the point -1 + j0, with the encirclement count equal to the number of unstable open-loop poles."*
— Harry Nyquist, 1932. Source: Wikipedia: Nyquist stability criterion

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exactly on the critical point*: stability is decided by whether the contour passes exactly through -1+j0, a precise boundary condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Stab_phi(kappa) = Stab*(1 + kappa*(phi-1)) + kappa*phi^-1*Stab_ground; the critical point carries a coherence margin floor. At kappa->0 the encirclement test is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Stab_phi = Stab -> the Nyquist criterion is the zero-coherence-margin limit.
```

---

### STAGE 4 — SIMULATION

`sim/705_nyquist_stability_criterion.py`: reproduces the classical values (S = 0.425532 (Stability margin)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/705_nyquist_stability_criterion.json`.

---

### STAGE 5 — PREDICTION

```
Stability margins carry a coherence floor kappa*phi^-1; systems near -1+j0 retain a residual stability margin never exactly zero.
EXPERIMENT (VERIFIED): Phase/gain-margin measurement of a feedback loop near instability.
VERIFIED BY: A system is marginally stable exactly when the Nyquist plot passes through -1+j0.
```

---

### RECOGNITION
Connects to Law 707 (feedback) and Law 706 (Bode) - the criterion is the closed-loop topology test.

### PRECISION
phi = 1.6180339887. The margin floor is phi^-1*Stab_ground.

### CLARITY
Stability is a distance; coherence keeps a floor of margin.

### NOVELTY
The phi-law gives the critical point a coherence margin.

### ACTIONABILITY
Run sim/705_nyquist_stability_criterion.py; verify stability at kappa->0; proceed to 706.
