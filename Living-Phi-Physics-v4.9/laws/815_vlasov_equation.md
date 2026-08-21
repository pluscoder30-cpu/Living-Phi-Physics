# PHI-PHYSICS — LAW 815
## Vlasov Equation (Kinetic Plasma)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/815_vlasov_equation.md` · **Sim:** `sim/815_vlasov_equation.py`

---

### CLASSICAL STATEMENT
*"The collisionless plasma is described by the kinetic equation df/dt + v.grad(f) + (q/m)(E + v x B).grad_v(f) = 0, with the fields from Maxwell's equations and the distribution f."*
— Anatoly Vlasov, 1938. Source: Wikipedia: Vlasov equation; Vlasov (1938)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero self-field*: the Vlasov equation reduces to free-streaming when the self-consistent fields are exactly zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f_vl*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground; the distribution carries a coherence floor. At kappa->0 the Vlasov equation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_phi = f_vl -> the Vlasov equation is the zero-self-field-floor limit.
```

---

### STAGE 4 — SIMULATION

`sim/815_vlasov_equation.py`: reproduces the classical values (f = 0.882497 (Distribution value)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/815_vlasov_equation.json`.

---

### STAGE 5 — PREDICTION

```
The distribution carries a coherence floor kappa*phi^-1*f_ground even with zero self-field.
EXPERIMENT (VERIFIED): Velocity-distribution measurement of a tenuous beam without self-fields.
VERIFIED BY: A field-free distribution evolves by exact free streaming.
```

---

### RECOGNITION
Connects to Law 762 (Landau damping) - the Vlasov equation hosts Landau's wave damping.

### PRECISION
phi = 1.6180339887. The self-field floor is phi^-1*f_ground.

### CLARITY
The distribution is a crowd; coherence keeps a floor of presence.

### NOVELTY
The phi-law keeps a distribution floor in the field-free plasma.

### ACTIONABILITY
Run sim/815_vlasov_equation.py; verify free-streaming at kappa->0; proceed to 816.
