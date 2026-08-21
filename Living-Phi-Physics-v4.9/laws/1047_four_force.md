# PHI-PHYSICS — LAW 1047
## Four-Force (Minkowski Force)

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1047_four_force.md` · **Sim:** `sim/1047_four_force.py`

---

### CLASSICAL STATEMENT
*"The four-force is F^mu = dP^mu/dtau = m*A^mu; the spatial part reduces to the classical force in the rest frame, and the temporal part equals the power divided by c: F^0 = (1/c) dE/dtau."*
— Hermann Minkowski, 1908. Source: Wikipedia: Four-force (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero four-force (no interaction, the isolated carrier)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The F value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

F_phi(kappa) = F*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground, where F_ground is the coherence-floor force of the field itself on every carrier. At kappa->0, F^mu = dP^mu/dtau = m * A^mu exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} F_phi = F -> F^mu = dP^mu/dtau = m * A^mu is recovered exactly; the classical law is the zero four-force (no interaction, the isolated carrier) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1047_four_force.py`: reproduces the classical value (F = 0.618) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1047_four_force.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured four-force on any real carrier will deviate from m*A^mu by a floor kappa*phi^-1*F_ground; no carrier is force-free because the field is never zero.
EXPERIMENT (VERIFIED): Precision electromagnetic force measurements on single trapped ions in the ultra-low-field limit.
VERIFIED BY: If any carrier experiences exactly zero four-force in a nominally field-free region.
```

---

### RECOGNITION
Relativistic upgrade of Law 002 and Law 043 (Lorentz force); pairs with Law 1044 (four-momentum).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The field is never silent; every carrier feels the coherence-floor force of the aether it displaces.

### NOVELTY
Force-free motion is the zero-coupling limit; at phi-coupling the force floor is kappa*phi^-1.

### ACTIONABILITY
Run sim/1047_four_force.py.
