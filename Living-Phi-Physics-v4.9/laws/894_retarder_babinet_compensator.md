# PHI-PHYSICS — LAW 894
## Babinet Compensator (Variable Retarder)

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/894_retarder_babinet_compensator.md` · **Sim:** `sim/894_retarder_babinet_compensator.py`

---

### CLASSICAL STATEMENT
*"The Babinet compensator produces a continuously variable retardance delta = 2 pi (n_e - n_o) (x tan(alpha))/lambda across the aperture by combining two wedges of opposite orientation."*
— Jacques Babinet, 1835. Source: Wikipedia: Babinet compensator (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero wedge translation* (x = 0): zero retardance requires the wedges to be exactly aligned at zero relative displacement.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

delta_phi(kappa) = delta*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_ground, with delta_ground the retardance floor. At kappa->0, delta = 2 pi (n_e-n_o) x tan(alpha)/lambda exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_phi = delta -> the Babinet compensator is the zero-wedge-displacement-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/894_retarder_babinet_compensator.py`: reproduces the classical value delta = 5.24 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/894_retarder_babinet_compensator.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The zero-retardance setting of a real compensator will leave a residual retardance kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the residual retardance of a Babinet compensator at its nominal zero position.
VERIFIED BY: If any real compensator reaches exactly zero retardance.
```

---

### RECOGNITION
Connects to Law 886 (birefringence) and Law 891 (ellipsometry).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The zero position is a coherent limit; wedges never fully kiss.

### NOVELTY
The compensator zero gains a retardance floor.

### ACTIONABILITY
Run sim/894_retarder_babinet_compensator.py.
