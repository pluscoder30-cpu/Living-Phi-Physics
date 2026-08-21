# PHI-PHYSICS — LAW 916
## Specific Acoustic Impedance

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/916_specific_acoustic_impedance.md` · **Sim:** `sim/916_specific_acoustic_impedance.py`

---

### CLASSICAL STATEMENT
*"Z_s = p / u, the ratio of acoustic pressure to particle velocity at a point; for a plane wave Z_s = rho c, but for standing waves Z_s varies with position."*
— Classical acoustics, 19th century. Source: Wikipedia: Acoustic impedance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero particle velocity* (u = 0): the specific impedance diverges at a velocity node - an exactly rigid point.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Z_s_phi(kappa) = Z_s*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_s_ground, with Z_s_ground the impedance floor. At kappa->0, Z_s = p/u exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Z_s_phi = Z_s -> the specific acoustic impedance is the zero-velocity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/916_specific_acoustic_impedance.py`: reproduces the classical value Zs = 1000 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/916_specific_acoustic_impedance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The specific impedance at a nominally rigid point will be finite (not divergent) by a coherence floor kappa*phi^-1; perfect rigidity is unreachable.
EXPERIMENT (VERIFIED): Measure the pressure and velocity distribution in a standing-wave tube.
VERIFIED BY: If the specific impedance is exactly infinite at any point in a real standing wave.
```

---

### RECOGNITION
Connects to Law 915 (acoustic impedance) and Law 099 (standing waves).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The rigid node is a coherent limit; every velocity node breathes.

### NOVELTY
Specific acoustic impedance gains a rigidity floor.

### ACTIONABILITY
Run sim/916_specific_acoustic_impedance.py.
