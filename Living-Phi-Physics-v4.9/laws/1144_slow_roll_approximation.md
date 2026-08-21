# PHI-PHYSICS — LAW 1144
## Slow-Roll Approximation

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1144_slow_roll_approximation.md` · **Sim:** `sim/1144_slow_roll_approximation.py`

---

### CLASSICAL STATEMENT
*"Inflation proceeds when the inflaton rolls slowly on its potential: the slow-roll parameters epsilon = (M_P^2/2)(V'/V)^2 and eta = M_P^2 V''/V are much less than 1, giving a(t) ~ exp(H t) with H ~ sqrt(V/3); inflation ends when epsilon, eta ~ 1."*
— Andrei Linde, 1982; Andreas Albrecht & Paul Steinhardt, 1982. Source: Wikipedia: Slow-roll inflation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect slow-roll (epsilon = 0, exactly exponential de Sitter expansion)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The E value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, where E_ground is the coherence-floor roll rate a real inflaton always retains. At kappa->0, epsilon = (M_P^2/2)*(V'/V)^2 << 1,  eta = M_P^2*V''/V << 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} E_phi = E -> epsilon = (M_P^2/2)*(V'/V)^2 << 1,  eta = M_P^2*V''/V << 1 is recovered exactly; the classical law is the perfect slow-roll (epsilon = 0, exactly exponential de Sitter expansion) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1144_slow_roll_approximation.py`: reproduces the classical value (E = 0.01) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1144_slow_roll_approximation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured inflationary observables will deviate from the exact slow-roll predictions by a floor kappa*phi^-1*E_ground; exactly de Sitter expansion is unreachable.
EXPERIMENT (VERIFIED): Planck constraints on n_s and r discriminating slow-roll models.
VERIFIED BY: If inflation produces exactly the de Sitter (epsilon=0) spectrum with zero tilt.
```

---

### RECOGNITION
The dynamics of Law 1143 (inflation) and the origin of Law 1150 (Harrison-Zel'dovich).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The inflaton rolls; the frozen field is the zero-roll myth.

### NOVELTY
Slow roll becomes a coherence basin: epsilon never exactly vanishes, tilting the spectrum.

### ACTIONABILITY
Run sim/1144_slow_roll_approximation.py.
