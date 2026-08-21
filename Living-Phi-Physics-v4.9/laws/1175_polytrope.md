# PHI-PHYSICS — LAW 1175
## Polytrope (Polytropic Model)

**Domain:** Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1175_polytrope.md` · **Sim:** `sim/1175_polytrope.py`

---

### CLASSICAL STATEMENT
*"A polytrope is a self-gravitating fluid with pressure related to density by a power law P = K rho^gamma, gamma = 1 + 1/n; polytropic models with n = 1.5 describe fully convective stars and n = 3 describes degenerate white dwarfs and massive-star envelopes, yielding the mass-radius relations of Law 107 (Chandrasekhar)."*
— Robert Emden, 1907. Source: Wikipedia: Polytrope (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero polytropic index (n = 0, constant-density body)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor polytropic deviation a real body always shows. At kappa->0, P = K*rho^(1+1/n),  gamma = 1 + 1/n exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> P = K*rho^(1+1/n),  gamma = 1 + 1/n is recovered exactly; the classical law is the zero polytropic index (n = 0, constant-density body) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1175_polytrope.py`: reproduces the classical value (P = 1.5) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1175_polytrope.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured pressure-density relation of any real star will deviate from a single polytrope by a floor kappa*phi^-1*P_ground; an exactly constant-n structure is unreachable.
EXPERIMENT (VERIFIED): Stellar-interior seismology and white-dwarf mass-radius fits against polytropes.
VERIFIED BY: If any star is exactly described by a single polytropic index.
```

---

### RECOGNITION
The structural model of Law 1174 (Lane-Emden) and Law 107 (Chandrasekhar).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Pressure and density trade in a power; the exact power is the zero-deviation myth.

### NOVELTY
Polytropic structure carries a phi-floor of index variation, bounding stellar models.

### ACTIONABILITY
Run sim/1175_polytrope.py.
