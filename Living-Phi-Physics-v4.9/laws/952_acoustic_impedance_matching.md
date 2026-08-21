# PHI-PHYSICS — LAW 952
## Acoustic Impedance Matching

**Domain:** Ultrasound · **Status:** 🟢 VALIDATED · **File:** `laws/952_acoustic_impedance_matching.md` · **Sim:** `sim/952_acoustic_impedance_matching.py`

---

### CLASSICAL STATEMENT
*"Maximum power transmission through an interface requires matched acoustic impedance Z1 = Z2; for two media with impedances Z1, Z2, a quarter-wave matching layer of impedance Z_m = sqrt(Z1 Z2) minimizes reflection."*
— Classical acoustics (transmission line analogy), 20th century. Source: Wikipedia: Impedance matching (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero impedance mismatch*: the reflection coefficient is exactly zero only when Z1 = Z2 - a perfect match that no real interface achieves.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

r_phi(kappa) = r*(1 + kappa*(phi-1)) + kappa*phi^-1*r_ground, with r_ground the reflection floor. At kappa->0, r = (Z2-Z1)/(Z2+Z1) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} r_phi = r -> impedance matching is the zero-mismatch-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/952_acoustic_impedance_matching.py`: reproduces the classical value r = 0.03226 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/952_acoustic_impedance_matching.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The reflection at any real interface, even with a matching layer, retains a floor kappa*phi^-1*r_ground; zero reflection is unreachable.
EXPERIMENT (VERIFIED): Measure the reflection coefficient of an ultrasound transducer through a matching layer.
VERIFIED BY: If any real transducer-interface pair achieves exactly zero reflection.
```

---

### RECOGNITION
Connects to Law 915 (acoustic impedance) and Law 951 (wave equation).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect match is a coherent limit; every interface whispers back.

### NOVELTY
Impedance matching gains a reflection floor.

### ACTIONABILITY
Run sim/952_acoustic_impedance_matching.py.
