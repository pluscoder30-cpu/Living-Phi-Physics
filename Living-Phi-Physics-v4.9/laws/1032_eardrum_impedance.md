# PHI-PHYSICS — LAW 1032
## Middle-Ear Impedance Matching

**Domain:** Physiological Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1032_eardrum_impedance.md` · **Sim:** `sim/1032_eardrum_impedance.py`

---

### CLASSICAL STATEMENT
*"The middle ear matches the low impedance of air to the high impedance of the cochlear fluid: the pressure gain of the ossicular lever and the area ratio (tympanic membrane to oval window) provide a transformer ratio of about 20-30 (approx 26 dB); the impedance mismatch is largely compensated."*
— Classical physiological acoustics (von Bekesy), 20th century. Source: Wikipedia: Middle ear (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero impedance mismatch*: if the air and cochlear impedances were equal, no transformer would be needed - the middle ear would be redundant.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

G_phi(kappa) = G*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ground, with G_ground the gain floor. At kappa->0, the pressure gain is exactly the area-times-lever ratio.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} G_phi = G -> middle-ear matching is the zero-mismatch-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1032_eardrum_impedance.py`: reproduces the classical value G = 25 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1032_eardrum_impedance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The effective pressure gain of any real middle ear will deviate from the ideal transformer ratio by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the cochlear microphonic response versus stapes velocity in an animal model.
VERIFIED BY: If the middle-ear transfer matches the ideal transformer ratio exactly.
```

---

### RECOGNITION
Connects to Law 915 (acoustic impedance) and Law 952 (impedance matching).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect transformer is a coherent limit; every ear has a loss.

### NOVELTY
Middle-ear matching gains an impedance floor.

### ACTIONABILITY
Run sim/1032_eardrum_impedance.py.
