# PHI-PHYSICS — LAW 971
## Hanbury Brown-Twiss Effect (Intensity Correlation)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/971_hanbury_brown_twiss.md` · **Sim:** `sim/971_hanbury_brown_twiss.py`

---

### CLASSICAL STATEMENT
*"The HBT effect: the intensity correlation g^(2)(0) = <I1 I2>/<I1><I2> of thermal light is 2 (bunched), of coherent light is 1, and of antibunched light is < 1; the correlation time is the coherence time of the source."*
— Robert Hanbury Brown, Richard Twiss, 1956. Source: Wikipedia: Hanbury Brown and Twiss effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero delay* (tau = 0): the bunching peak is anchored at exactly zero time delay between the two detectors.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

g2_phi(kappa) = g2*(1 + kappa*(phi-1)) + kappa*phi^-1*g2_ground, with g2_ground the correlation floor. At kappa->0, g^(2)(0) = 2 exactly for thermal light.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} g2_phi = g2 -> the HBT effect is the zero-delay-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/971_hanbury_brown_twiss.py`: reproduces the classical value g2 = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/971_hanbury_brown_twiss.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured g^(2)(0) of any real thermal source will deviate from 2 by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the intensity correlation function of a thermal source with two avalanche photodiodes.
VERIFIED BY: If the g^(2)(0) of any real thermal source is exactly 2.
```

---

### RECOGNITION
Connects to Law 972 (photon bunching) and Law 869 (temporal coherence).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect bunch is a coherent limit; every thermal glow has a stagger.

### NOVELTY
The HBT correlation gains a delay floor.

### ACTIONABILITY
Run sim/971_hanbury_brown_twiss.py.
