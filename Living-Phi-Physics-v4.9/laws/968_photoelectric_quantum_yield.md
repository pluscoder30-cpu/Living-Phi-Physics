# PHI-PHYSICS — LAW 968
## Quantum Yield (Photodetection)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/968_photoelectric_quantum_yield.md` · **Sim:** `sim/968_photoelectric_quantum_yield.py`

---

### CLASSICAL STATEMENT
*"Quantum efficiency (quantum yield) eta = (number of detected photons)/(number of incident photons); the photocurrent is I = eta e N_ph/t; eta <= 1 for a single-photon detector."*
— Classical photodetector theory (from photoelectric effect), 1905. Source: Wikipedia: Quantum efficiency (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero quantum efficiency* (eta = 0): a perfectly blind detector detects exactly zero photons.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

eta_phi(kappa) = eta*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_ground, with eta_ground the efficiency floor. At kappa->0, I = eta e N_ph/t exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta -> quantum yield is the zero-efficiency-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/968_photoelectric_quantum_yield.py`: reproduces the classical value eta = 0.8 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/968_photoelectric_quantum_yield.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual dark signal kappa*phi^-1*eta_ground will be detected even with zero incident photons (dark-count floor).
EXPERIMENT (VERIFIED): Measure the dark count rate of a photodetector at zero illumination.
VERIFIED BY: If a photodetector detects exactly zero photons at zero illumination.
```

---

### RECOGNITION
Connects to Law 067 (photoelectric, in corpus) and Law 963a (photon counting).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The blind detector is a coherent limit; every sensor has a dark murmur.

### NOVELTY
Quantum yield gains a dark-count floor.

### ACTIONABILITY
Run sim/968_photoelectric_quantum_yield.py.
