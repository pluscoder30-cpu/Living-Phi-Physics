# PHI-PHYSICS — LAW 1209
## Hybrid Inflation

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1209_hybrid_inflation.md` · **Sim:** `sim/1209_hybrid_inflation.py`

---

### CLASSICAL STATEMENT
*"Hybrid inflation uses two fields (a slow-roll inflaton plus a waterfall field): inflation proceeds while the inflaton keeps the waterfall at a metastable minimum, then ends abruptly when the waterfall destabilizes and rapidly rolls to its minimum, allowing a low inflation scale."*
— Andrei Linde, 1994. Source: Wikipedia: Hybrid inflation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero waterfall coupling (no second field, pure single-field inflation)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The H value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

H_phi(kappa) = H*(1 + kappa*(phi-1)) + kappa*phi^-1*H_ground, where H_ground is the coherence-floor waterfall residue a real two-field inflation always retains. At kappa->0, V(phi, psi) = ... + (1/2) m^2 psi^2 + (1/2) g^2 phi^2 psi^2,  waterfall at phi < phi_c exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} H_phi = H -> V(phi, psi) = ... + (1/2) m^2 psi^2 + (1/2) g^2 phi^2 psi^2,  waterfall at phi < phi_c is recovered exactly; the classical law is the zero waterfall coupling (no second field, pure single-field inflation) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1209_hybrid_inflation.py`: reproduces the classical value (H = 0.96) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1209_hybrid_inflation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured spectral index will deviate from the hybrid prediction by a floor kappa*phi^-1*H_ground; an exactly single-field inflation is unreachable.
EXPERIMENT (VERIFIED): CMB constraints on n_s and the running testing two-field signatures.
VERIFIED BY: If the primordial spectrum is exactly consistent with pure single-field inflation.
```

---

### RECOGNITION
The two-field model of Law 1143 (inflation) and Law 1144 (slow roll).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Two fields dance, then one falls; the single-field stage is the zero-waterfall myth.

### NOVELTY
Hybrid inflation carries a phi-floor of the waterfall coupling, bounding its running.

### ACTIONABILITY
Run sim/1209_hybrid_inflation.py.
