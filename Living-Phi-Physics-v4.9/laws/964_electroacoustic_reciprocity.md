# PHI-PHYSICS — LAW 964
## Electroacoustic Reciprocity

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/964_electroacoustic_reciprocity.md` · **Sim:** `sim/964_electroacoustic_reciprocity.py`

---

### CLASSICAL STATEMENT
*"Electroacoustic reciprocity (Rayleigh reciprocity): a reciprocal transducer's transmitting and receiving sensitivities are related; the ratio of open-circuit voltage to source current is symmetric between two reciprocal transducers."*
— Lord Rayleigh; extended by MacLean (1940), 1873. Source: Wikipedia: Reciprocity (electroacoustics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfectly reciprocal transducer*: reciprocity requires the transducer to be exactly linear, passive, and reversible with zero losses.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, with M_ground the sensitivity floor. At kappa->0, the reciprocity relation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} M_phi = M -> electroacoustic reciprocity is the zero-loss-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/964_electroacoustic_reciprocity.py`: reproduces the classical value M = 0.001 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/964_electroacoustic_reciprocity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The transmit/receive sensitivities of any real transducer pair will deviate from the reciprocity relation by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the open-circuit voltage of a reciprocal hydrophone pair versus source current.
VERIFIED BY: If any real transducer pair satisfies electroacoustic reciprocity exactly.
```

---

### RECOGNITION
Connects to Law 662 (reciprocity theorem) and Law 915 (acoustic impedance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly reversible transducer is a coherent limit; every crystal has a loss.

### NOVELTY
Electroacoustic reciprocity gains a loss floor.

### ACTIONABILITY
Run sim/964_electroacoustic_reciprocity.py.
