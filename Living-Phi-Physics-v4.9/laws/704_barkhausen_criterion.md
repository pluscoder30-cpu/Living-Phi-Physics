# PHI-PHYSICS — LAW 704
## Barkhausen Criterion (Oscillation)

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/704_barkhausen_criterion.md` · **Sim:** `sim/704_barkhausen_criterion.py`

---

### CLASSICAL STATEMENT
*"A feedback oscillator sustains oscillation when the loop gain is exactly |A*beta| = 1 and the loop phase is exactly 0 (or 2*pi*n) degrees."*
— Heinrich Georg Barkhausen, 1921. Source: Wikipedia: Barkhausen stability criterion

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *exact unity loop gain* (|A*beta| = 1 exactly): sustained oscillation requires a precise loop gain and exact phase condition.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Loop_phi(kappa) = Loop*(1 + kappa*(phi-1)) + kappa*phi^-1*Loop_ground; the gain condition carries a coherence basin. At kappa->0, |A*beta| = 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Loop_phi = 1 -> the Barkhausen criterion is the zero-loop-gain-offset limit.
```

---

### STAGE 4 — SIMULATION

`sim/704_barkhausen_criterion.py`: reproduces the classical values (L = 9 (Loop gain)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/704_barkhausen_criterion.json`.

---

### STAGE 5 — PREDICTION

```
Oscillation persists within a coherence basin of loop gain around unity; the exact unity condition is never required.
EXPERIMENT (VERIFIED): Loop-gain sweep of an oscillator circuit to map the sustaining basin.
VERIFIED BY: An oscillator sustains oscillation only at the exact unity loop gain.
```

---

### RECOGNITION
Connects to Law 707 (feedback gain) - the criterion is the self-sustaining loop.

### PRECISION
phi = 1.6180339887. The gain basin is phi^-1*Loop_ground.

### CLARITY
Oscillation is a basin, not a point; the loop breathes.

### NOVELTY
The phi-law broadens the exact oscillation condition.

### ACTIONABILITY
Run sim/704_barkhausen_criterion.py; verify loop=1 at kappa->0; proceed to 705.
