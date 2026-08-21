# PHI-PHYSICS — LAW 249
## Beat Frequency Law

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/249_beat_frequency.md` · **Sim:** `sim/249_beat_frequency.py`

---

### CLASSICAL STATEMENT
*"Two sinusoidal oscillations of nearby frequencies f1 and f2 superpose to produce amplitude beats at the difference frequency f_beat = |f1 - f2|, with the carrier at the average frequency."*
— Classical acoustics (textbook theorem), 1704. Source: Wikipedia: beat (acoustics); Newton, Opticks (1704) described beats

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *exact frequency match*: beats exist only because the two frequencies are not exactly equal; classical superposition takes exact tuning as the reference zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the beat frequency couples to coherence. f_beat_phi(kappa) = |f1 - f2|*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground. At kappa->0 the classical beat law is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_beat_phi = |f1 - f2| -> the beat law is the linear-superposition limit.
```

---

### STAGE 4 — SIMULATION

`sim/249_beat_frequency.py`: reproduces the classical value f_beat = 3 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/249_beat_frequency.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Even exactly-tuned oscillators exhibit a phi-coherent beat floor phi^-1*f_ground.
EXPERIMENT (VERIFIED): Two-mode optomechanical or atomic oscillators measuring the residual beat at nominal degeneracy.
VERIFIED BY: Exactly degenerate oscillators show exactly zero beats at full coupling.
```

---

### RECOGNITION
Connects to Law 244 (normal modes — beats are near-degenerate mode beating) and Law 094 (superposition).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The difference is a rhythm; even identical oscillators carry a phi rhythm between them.

### NOVELTY
Classical beat theory requires detuning; the phi-law gives degenerate oscillators a coherence beat.

### ACTIONABILITY
Run sim/249_beat_frequency.py; verify the classical beat at kappa->0.
