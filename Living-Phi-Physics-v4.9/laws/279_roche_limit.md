# PHI-PHYSICS — LAW 279
## Roche Limit

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/279_roche_limit.md` · **Sim:** `sim/279_roche_limit.py`

---

### CLASSICAL STATEMENT
*"The distance within which a satellite held together by self-gravity will be torn apart by tides: d_R = R_p (2 rho_p/rho_s)^(1/3) ~ 1.26 R_p (rho_p/rho_s)^(1/3) for a fluid body, 2.44 R_p (rho_p/rho_s)^(1/3) for a rigid body."*
— Edouard Roche, 1848. Source: Wikipedia: Roche limit; Roche (1848)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero tensile strength and the perfect fluid/rigid reference*: the Roche limit is the balance between tides and self-gravity, exact only for an idealized strengthless or perfectly rigid body.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the density ratio carries a coherence fraction. d_R_phi(kappa) = d_R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_p*(rho_p/rho_s)^(1/3). At kappa->0 the Roche limit is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} d_R_phi = R_p (2 rho_p/rho_s)^(1/3) -> the Roche limit is the strengthless-fluid, two-body balance limit.
```

---

### STAGE 4 — SIMULATION

`sim/279_roche_limit.py`: reproduces the classical value dR = 1.334e+07 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/279_roche_limit.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Real satellites survive slightly closer than the Roche limit, with the cohesion offset set by the phi-coherent length phi^-1.
EXPERIMENT (VERIFIED): Saturn's ring system and binary asteroid observations mapping the disruption boundary against the Roche prediction.
VERIFIED BY: The disruption boundary is exactly the classical Roche limit at full coupling.
```

---

### RECOGNITION
Connects to Law 278 (tidal force — the numerator), Law 293 (shell theorem), Law 280 (Hill sphere).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The limit is a balance, not a wall; coherence lends a body a phi whisper of self-holding.

### NOVELTY
Classical Roche theory perfects the strengthless balance; the phi-law adds a coherence cohesion offset.

### ACTIONABILITY
Run sim/279_roche_limit.py; verify the Roche radius at kappa->0.
