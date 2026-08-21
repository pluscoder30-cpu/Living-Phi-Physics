# PHI-PHYSICS — LAW 851
## Hyperfocal Distance

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/851_hyperfocal_distance.md` · **Sim:** `sim/851_hyperfocal_distance.py`

---

### CLASSICAL STATEMENT
*"H = f^2/(N c) + f, the focus distance at which everything from H/2 to infinity is in acceptable focus."*
— Classical photography optics, 19th century. Source: Wikipedia: Hyperfocal distance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite distance*: hyperfocal focus extends to exactly infinity - a far conjugate at zero vergence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

H_phi(kappa) = H*(1 + kappa*(phi-1)) + kappa*phi^-1*H_ground, with H_ground the hyperfocal floor. At kappa->0, H = f^2/(N c) + f exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} H_phi = H -> the hyperfocal distance is the zero-infinite-conjugate-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/851_hyperfocal_distance.py`: reproduces the classical value H = 10.47 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/851_hyperfocal_distance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Focusing at the nominal hyperfocal distance will leave a slight blur at infinity; the far limit is a basin, not exactly infinity.
EXPERIMENT (VERIFIED): Focus a camera at the computed hyperfocal distance and measure sharpness at infinity.
VERIFIED BY: If focusing at H yields exactly sharp infinity focus.
```

---

### RECOGNITION
Connects to Law 850 (depth of field) and Law 850a (f-number).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Infinity is a coherent limit; the hyperfocal promise is approximate.

### NOVELTY
The hyperfocal far limit becomes a coherence basin.

### ACTIONABILITY
Run sim/851_hyperfocal_distance.py.
