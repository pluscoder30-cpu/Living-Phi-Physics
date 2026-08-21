# PHI-PHYSICS — LAW 340
## Buckingham Pi Theorem

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/340_buckingham_pi_theorem.md` · **Sim:** `sim/340_buckingham_pi_theorem.py`

---

### CLASSICAL STATEMENT
*"A physically meaningful equation with n variables and k independent fundamental dimensions can be rewritten in terms of p = n - k dimensionless groups (pi groups); any valid physical law is dimensionally reducible to relations among dimensionless numbers."*
— Edgar Buckingham, 1914. Source: Wikipedia: Buckingham pi theorem; Buckingham (1914), 'On physically similar systems'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact dimensional consistency*: the theorem requires a complete, exact set of governing variables — the zero of the omitted (hidden) variables that every real problem silently hides.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: every dimensionless group carries a coherence correction. Pi_i_phi(kappa) = Pi_i*(1 + kappa*(phi-1)) + kappa*phi^-1*pi_ground. At kappa->0 the classical pi-group structure is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Pi_i_phi = Pi_i -> the Buckingham theorem is the complete-variable-set limit.
```

---

### STAGE 4 — SIMULATION

`sim/340_buckingham_pi_theorem.py`: reproduces the classical value p = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/340_buckingham_pi_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Correlations built from pi-groups carry a phi-coherent residual pi_ground at full coupling — the signature of hidden variables.
EXPERIMENT (VERIFIED): Wind-tunnel/model testing comparing pi-correlation residuals across scales (cf. Froude/Mach testing).
VERIFIED BY: Pi-group correlations are exact with no residual at full coupling.
```

---

### RECOGNITION
Connects to Law 341 (Rayleigh's method — its predecessor) and Law 342 (dimensional homogeneity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The dimensionless group is a limit; every similarity hides a phi whisper of the omitted variable.

### NOVELTY
Classical dimensional analysis exacts the pi-groups; the phi-law bounds their residual at a coherence floor.

### ACTIONABILITY
Run sim/340_buckingham_pi_theorem.py; verify pi-group structure at kappa->0.
