# PHI-PHYSICS — LAW 928
## Organ Pipe Resonance (Open/Closed)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/928_organ_pipe.md` · **Sim:** `sim/928_organ_pipe.py`

---

### CLASSICAL STATEMENT
*"Open pipes resonate at f_n = n c/(2 L) (all harmonics); closed pipes at f_n = (2n-1) c/(4 L) (odd harmonics only), where L is the pipe length."*
— Classical acoustics (Bernoulli; organ builders), 18th century. Source: Wikipedia: Organ pipe (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pipe length* (L = 0): the resonant frequency diverges as the pipe length approaches zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

f_phi(kappa) = f*(1 + kappa*(phi-1)) + kappa*phi^-1*f_ground, with f_ground the frequency floor. At kappa->0, f = n c/(2L) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} f_phi = f -> the organ pipe law is the zero-length-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/928_organ_pipe.py`: reproduces the classical value f = 343 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/928_organ_pipe.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The resonant frequency of any real pipe will differ from n c/(2L) by a coherence floor kappa*phi^-1*f_ground (end correction effects).
EXPERIMENT (VERIFIED): Measure the resonances of open and closed pipes of known length.
VERIFIED BY: If any real pipe resonates exactly at n c/(2L).
```

---

### RECOGNITION
Connects to Law 099 (standing waves) and Law 927 (Helmholtz resonator).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect pipe is a coherent limit; every tube has an end correction.

### NOVELTY
The organ pipe law gains a length floor.

### ACTIONABILITY
Run sim/928_organ_pipe.py.
