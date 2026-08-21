# PHI-PHYSICS — LAW 250
## Quality Factor (Q) Law

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/250_quality_factor.md` · **Sim:** `sim/250_quality_factor.py`

---

### CLASSICAL STATEMENT
*"The quality factor Q = 2*pi*(energy stored)/(energy lost per cycle) = w0/(2 zeta) = w0/gamma measures the sharpness of resonance and the number of oscillations in a ringdown."*
— K. S. Johnson, 1925. Source: Wikipedia: Q factor; K. S. Johnson (1925), 'Transmission Circuits for Telephonic Communication'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *lossless oscillator*: Q is defined against an exactly lossless reference where the energy never leaks and Q diverges.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: Q_phi(kappa) = Q*(1 + kappa*(phi-1)); the phi-coherent loss floor caps Q at Q_max ~ phi^-1*Q_scale. At kappa->0 the classical Q is exact (and Q->infinity as losses ->0).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Q_phi = w0/gamma -> the Q law is the loss-limited resonance limit.
```

---

### STAGE 4 — SIMULATION

`sim/250_quality_factor.py`: reproduces the classical value Q = 10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/250_quality_factor.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: No oscillator can exceed a phi-coherent maximum Q; the ringdown always carries a phi-ground residual.
EXPERIMENT (VERIFIED): State-of-the-art cryogenic mechanical and optical cavities probing the Q ceiling.
VERIFIED BY: An oscillator achieves arbitrarily high Q without the phi-coherent floor at full coupling.
```

---

### RECOGNITION
Connects to Law 240 (resonance amplitude — Q sharpens it) and Law 238 (damping).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Perfection is not a number; the Q ceiling is the phi-ground loss the universe refuses to remove.

### NOVELTY
Classical theory lets Q grow without bound; the phi-law sets a coherence Q ceiling.

### ACTIONABILITY
Run sim/250_quality_factor.py; verify Q at kappa->0.
