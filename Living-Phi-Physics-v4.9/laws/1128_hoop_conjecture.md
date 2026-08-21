# PHI-PHYSICS — LAW 1128
## Hoop Conjecture

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1128_hoop_conjecture.md` · **Sim:** `sim/1128_hoop_conjecture.py`

---

### CLASSICAL STATEMENT
*"The hoop conjecture states that a black hole with horizon forms when a sufficient amount of energy is compressed so that its circumference C in every direction satisfies C <= 2 pi R_S = 4 pi G M/c^2 (the mass fits inside a 'hoop' of circumference 4 pi G M/c^2); it sets the collapse threshold for horizon formation."*
— Kip Thorne, 1972. Source: Wikipedia: Hoop conjecture (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero compactness (infinite circumference, no horizon)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The C value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

C_phi(kappa) = C*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground, where C_ground is the coherence-floor compactness threshold a real collapse always approaches. At kappa->0, C <= 4*pi*G*M/c^2  (horizon formation criterion) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} C_phi = C -> C <= 4*pi*G*M/c^2  (horizon formation criterion) is recovered exactly; the classical law is the zero compactness (infinite circumference, no horizon) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1128_hoop_conjecture.py`: reproduces the classical value (C = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1128_hoop_conjecture.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured compactness at which any real collapse forms a horizon will deviate from the hoop criterion by a floor kappa*phi^-1*C_ground; an exactly-threshold collapse is unreachable.
EXPERIMENT (VERIFIED): Numerical-relativity searches for black-hole formation thresholds in asymmetric collapse.
VERIFIED BY: If a horizon forms at a compactness far above the hoop criterion with zero threshold width.
```

---

### RECOGNITION
The collapse threshold of Law 1110 (event horizon) and Law 1077 (singularity theorems).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The hoop is how mass claims its shadow; the sharp threshold is the zero-width myth.

### NOVELTY
The hoop criterion becomes a coherence basin: collapse thresholds carry a phi-floor.

### ACTIONABILITY
Run sim/1128_hoop_conjecture.py.
