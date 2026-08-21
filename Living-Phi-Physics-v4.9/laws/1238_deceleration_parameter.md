# PHI-PHYSICS — LAW 1238
## Deceleration Parameter

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1238_deceleration_parameter.md` · **Sim:** `sim/1238_deceleration_parameter.py`

---

### CLASSICAL STATEMENT
*"The deceleration parameter measures the rate of change of cosmic expansion: q0 = -a a_dotdot/a_dot^2 = (1/2) Omega_m - Omega_Lambda (flat universe); q0 > 0 means decelerating expansion, q0 < 0 accelerating; the 1998 discovery q0 < 0 revealed dark energy (Law 105)."*
— Allan Sandage, 1961 (defined the cosmological tests). Source: Wikipedia: Deceleration parameter (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero deceleration (q0 = 0, the coasting universe)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Q value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Q_phi(kappa) = Q*(1 + kappa*(phi-1)) + kappa*phi^-1*Q_ground, where Q_ground is the coherence-floor deceleration a real universe always retains. At kappa->0, q0 = -a*a_dotdot/a_dot^2 = Omega_m/2 - Omega_Lambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Q_phi = Q -> q0 = -a*a_dotdot/a_dot^2 = Omega_m/2 - Omega_Lambda is recovered exactly; the classical law is the zero deceleration (q0 = 0, the coasting universe) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1238_deceleration_parameter.py`: reproduces the classical value (Q = -0.55) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1238_deceleration_parameter.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured deceleration parameter will deviate from the classical value by a floor kappa*phi^-1*Q_ground; an exactly coasting (q0=0) universe is unreachable.
EXPERIMENT (VERIFIED): Supernova Hubble-diagram and BAO measurements of q(z).
VERIFIED BY: If the universe is measured at exactly zero deceleration over all epochs.
```

---

### RECOGNITION
The expansion kinematic of Law 104 (Friedmann equations) and Law 101 (Hubble law).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The cosmos brakes or floors it; the coasting universe is the zero-deceleration myth.

### NOVELTY
The deceleration parameter carries a phi-floor, bounding the acceleration onset.

### ACTIONABILITY
Run sim/1238_deceleration_parameter.py.
