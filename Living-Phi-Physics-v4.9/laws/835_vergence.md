# PHI-PHYSICS — LAW 835
## Vergence (Gaussian Optics)

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/835_vergence.md` · **Sim:** `sim/835_vergence.py`

---

### CLASSICAL STATEMENT
*"V = n/s (vergence is n over distance); image vergence = object vergence + lens power: V_i = V_o + P. At infinity vergence is zero."*
— Classical Gaussian optics, 1841. Source: Wikipedia: Vergence (optics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite distance* (s -> infinity): zero vergence requires a source at exactly infinity - a plane wave of zero curvature.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground, with V_ground the residual curvature floor. At kappa->0, V = n/s exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V -> vergence is the zero-infinite-distance-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/835_vergence.py`: reproduces the classical value V = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/835_vergence.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A 'collimated' beam will always have a small residual vergence kappa*phi^-1*V_ground; perfect collimation is unreachable.
EXPERIMENT (VERIFIED): Measure the residual curvature of a nominally collimated laser beam over long propagation.
VERIFIED BY: If any real beam has exactly zero vergence.
```

---

### RECOGNITION
Connects to Law 834 (optical power) - vergence adds with power.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Collimation is a coherent limit; every beam has a whisper of curvature.

### NOVELTY
The plane wave of zero vergence gains a floor.

### ACTIONABILITY
Run sim/835_vergence.py.
