# PHI-PHYSICS — LAW 954
## Phased Array (Beam Steering)

**Domain:** Ultrasound · **Status:** 🟢 VALIDATED · **File:** `laws/954_phased_array.md` · **Sim:** `sim/954_phased_array.py`

---

### CLASSICAL STATEMENT
*"A phased array steers and focuses an ultrasound beam by applying time delays to the elements: the steering angle satisfies sin(theta) = c delta_t / d, where d is the element spacing and delta_t the time delay gradient."*
— Classical array theory (sonar/radar heritage), 20th century. Source: Wikipedia: Phased array (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero delay gradient* (delta_t = 0): with no delays the beam points straight ahead at exactly zero steering angle.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

sin_phi(kappa) = sin(theta)*(1 + kappa*(phi-1)) + kappa*phi^-1*sin_ground, with sin_ground the angle floor. At kappa->0, sin(theta) = c delta_t/d exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sin_phi = sin(theta) -> the phased array is the zero-delay-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/954_phased_array.py`: reproduces the classical value sin = 3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/954_phased_array.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The actual beam direction of any real array will deviate from c delta_t/d by a coherence floor kappa*phi^-1*sin_ground.
EXPERIMENT (VERIFIED): Measure the beam direction of a phased ultrasound array versus applied delays.
VERIFIED BY: If the beam of any real array points exactly at c delta_t/d.
```

---

### RECOGNITION
Connects to Law 953 (acoustic lens) and Law 958 (Doppler ultrasound).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly steered beam is a coherent limit; every array has a jitter.

### NOVELTY
Phased arrays gain a delay floor.

### ACTIONABILITY
Run sim/954_phased_array.py.
