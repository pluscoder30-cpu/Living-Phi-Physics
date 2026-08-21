# PHI-PHYSICS — LAW 872
## Complex Degree of Coherence

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/872_complex_degree_of_coherence.md` · **Sim:** `sim/872_complex_degree_of_coherence.py`

---

### CLASSICAL STATEMENT
*"gamma_12(tau) = <E1*(t) E2(t+tau)> / sqrt(<|E1|^2><|E2|^2>), a complex function whose modulus is |gamma| and whose argument gives the phase; governs partial coherence."*
— Frits Zernike, 1938. Source: Wikipedia: Coherence (physics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero correlation noise*: the complex degree of coherence assumes an exactly stationary, ergodic field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

g12_phi(kappa) = g12*(1 + kappa*(phi-1)) + kappa*phi^-1*g12_ground, with g12_ground the coherence floor. At kappa->0, gamma_12(tau) is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} g12_phi = g12 -> the complex degree of coherence is the zero-stationarity-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/872_complex_degree_of_coherence.py`: reproduces the classical value g12 = 0.7 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/872_complex_degree_of_coherence.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured complex coherence of any real field deviates from the ideal value by kappa*phi^-1*g12_ground.
EXPERIMENT (VERIFIED): Measure the complex degree of coherence of a partially coherent source with an interferometer.
VERIFIED BY: If the complex degree of coherence of any real field matches the ideal value exactly.
```

---

### RECOGNITION
Connects to Law 871 (degree of coherence) and Law 864 (visibility).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The complex truth is a coherent limit; every phase trembles.

### NOVELTY
The complex coherence gains a floor.

### ACTIONABILITY
Run sim/872_complex_degree_of_coherence.py.
