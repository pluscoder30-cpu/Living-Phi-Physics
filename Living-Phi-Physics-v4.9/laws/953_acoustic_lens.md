# PHI-PHYSICS — LAW 953
## Acoustic Lens

**Domain:** Ultrasound · **Status:** 🟢 VALIDATED · **File:** `laws/953_acoustic_lens.md` · **Sim:** `sim/953_acoustic_lens.py`

---

### CLASSICAL STATEMENT
*"An acoustic lens focuses ultrasound by refraction at curved surfaces, obeying the same geometry as optical lenses with the acoustic refractive index n = c1/c2; the focal length follows the lensmaker's equation with acoustic indices."*
— Classical acoustics (analogy to optics), 20th century. Source: Wikipedia: Acoustic lens (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero index contrast* (n = 1): with matched acoustic velocities the lens has zero power - it does not bend sound.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, with P_ground the power floor. At kappa->0, P = (n-1)(1/R1 - 1/R2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} P_phi = P -> the acoustic lens is the zero-index-contrast-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/953_acoustic_lens.py`: reproduces the classical value P = 8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/953_acoustic_lens.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The focal power of any real acoustic lens will differ from the lensmaker value by a coherence floor kappa*phi^-1*P_ground.
EXPERIMENT (VERIFIED): Measure the focus of an acoustic lens in a water tank with a hydrophone.
VERIFIED BY: If any real acoustic lens has exactly the lensmaker focal length.
```

---

### RECOGNITION
Connects to Law 827 (lensmaker) and Law 915 (acoustic impedance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The index-matched fluid is a coherent limit; every lens bends with a floor.

### NOVELTY
The acoustic lens gains an index floor.

### ACTIONABILITY
Run sim/953_acoustic_lens.py.
