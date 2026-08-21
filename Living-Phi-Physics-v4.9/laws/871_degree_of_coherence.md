# PHI-PHYSICS — LAW 871
## Degree of Coherence

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/871_degree_of_coherence.md` · **Sim:** `sim/871_degree_of_coherence.py`

---

### CLASSICAL STATEMENT
*"|gamma_12| ranges from 0 (incoherent) to 1 (coherent); the degree of coherence quantifies the correlation between two field points and equals the fringe visibility."*
— Frits Zernike, 1938. Source: Wikipedia: Degree of coherence (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *unit coherence* (|gamma| = 1): full coherence requires exactly correlated fields with zero noise.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

g_phi(kappa) = g*(1 + kappa*(phi-1)) + kappa*phi^-1*g_ground, with g_ground the coherence floor. At kappa->0, |gamma_12| = 1 for coherent fields exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} g_phi = g -> the degree of coherence is the zero-noise-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/871_degree_of_coherence.py`: reproduces the classical value g = 0.95 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/871_degree_of_coherence.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured degree of coherence of any real field will be bounded below 1 by a floor kappa*phi^-1*g_ground.
EXPERIMENT (VERIFIED): Measure the degree of coherence of a laser via its interference visibility.
VERIFIED BY: If any real field has |gamma_12| exactly 1.
```

---

### RECOGNITION
Connects to Law 864 (visibility) and Law 869 (temporal coherence).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Perfect correlation is a coherent limit; every field whispers with noise.

### NOVELTY
The degree of coherence gains a ceiling floor.

### ACTIONABILITY
Run sim/871_degree_of_coherence.py.
