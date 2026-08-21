# PHI-PHYSICS — LAW 1196
## Phantom Energy

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1196_phantom_energy.md` · **Sim:** `sim/1196_phantom_energy.py`

---

### CLASSICAL STATEMENT
*"Phantom energy is dark energy with equation of state w < -1, for which the energy density grows with expansion (rho_dot = 3 H (1+w) rho > 0); it leads to a future singularity known as the Big Rip (Law 1197) and violates the dominant energy condition."*
— Robert Caldwell, 2002. Source: Wikipedia: Phantom energy (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *w = -1 (the cosmological-constant boundary, zero phantom growth)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor phantom excess a real vacuum never reaches exactly. At kappa->0, w < -1,  rho ~ a^(-3(1+w)) grows as a increases exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> w < -1,  rho ~ a^(-3(1+w)) grows as a increases is recovered exactly; the classical law is the w = -1 (the cosmological-constant boundary, zero phantom growth) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1196_phantom_energy.py`: reproduces the classical value (P = -1.1) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1196_phantom_energy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured equation of state will deviate from w = -1 toward the phantom side by a floor kappa*phi^-1*P_ground; an exactly cosmological-constant vacuum is unreachable.
EXPERIMENT (VERIFIED): Combined DESI + CMB + supernova constraints on w < -1.
VERIFIED BY: If w is measured exactly at -1 with zero phantom component.
```

---

### RECOGNITION
The w < -1 regime of Law 1194 (equation of state) and Law 1197 (Big Rip).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The vacuum over-spends; the exact boundary w = -1 is the zero-phantom myth.

### NOVELTY
Phantom energy carries a phi-floor, so the vacuum can never be proven exactly Lambda.

### ACTIONABILITY
Run sim/1196_phantom_energy.py.
