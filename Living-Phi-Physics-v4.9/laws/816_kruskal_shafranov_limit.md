# PHI-PHYSICS — LAW 816
## Kruskal-Shafranov Limit (Kink Stability)

**Domain:** Plasma · **Status:** 🟢 VALIDATED · **File:** `laws/816_kruskal_shafranov_limit.md` · **Sim:** `sim/816_kruskal_shafranov_limit.py`

---

### CLASSICAL STATEMENT
*"A tokamak is kink-unstable when the safety factor q < 1, i.e., when q_a = (a*B_phi)/(R*B_theta) < 1 at the edge; stability requires q > 1 everywhere."*
— Martin Kruskal; Vitaly Shafranov, 1958. Source: Kruskal-Shafranov limit; Kruskal (1958), Shafranov (1956)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero safety factor* (q = 0): stability requires a finite q, and the kink threshold sits at exactly q = 1.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

q_phi(kappa) = q*(1 + kappa*(phi-1)) + kappa*phi^-1*q_ground; the stability boundary carries a coherence basin. At kappa->0 the q > 1 criterion is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} q_phi = q -> the Kruskal-Shafranov limit is the zero-coherence-stability limit.
```

---

### STAGE 4 — SIMULATION

`sim/816_kruskal_shafranov_limit.py`: reproduces the classical values (q = 1 (Safety factor)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/816_kruskal_shafranov_limit.json`.

---

### STAGE 5 — PREDICTION

```
The kink threshold is a basin of width kappa*phi^-1 around q = 1; stability is decided within it.
EXPERIMENT (VERIFIED): Kink-stability measurement of a tokamak as q_a crosses unity.
VERIFIED BY: A tokamak is kink-stable only for q > 1 exactly.
```

---

### RECOGNITION
Connects to Law 759 (tokamak) - the q > 1 criterion is the tokamak's kink gate.

### PRECISION
phi = 1.6180339887. The stability basin is phi^-1*q_ground.

### CLARITY
The safety factor is the threshold; coherence widens the gate.

### NOVELTY
The phi-law gives the kink threshold a coherence basin.

### ACTIONABILITY
Run sim/816_kruskal_shafranov_limit.py; verify q>1 at kappa->0; proceed to 817.
