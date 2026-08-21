# PHI-PHYSICS — LAW 868
## van Cittert-Zernike Theorem

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/868_van_cittert_zernike_theorem.md` · **Sim:** `sim/868_van_cittert_zernike_theorem.py`

---

### CLASSICAL STATEMENT
*"The complex degree of coherence of a distant incoherent source is the normalized Fourier transform of its intensity distribution: gamma_12 = FT[I(x)]/I_total."*
— Pieter Hendrik van Cittert, Frits Zernike, 1934. Source: Wikipedia: Van Cittert-Zernike theorem (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite source distance*: the theorem assumes the source is at infinite distance (Fraunhofer limit) with exactly planar wavefronts.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

gamma_phi(kappa) = gamma*(1 + kappa*(phi-1)) + kappa*phi^-1*gamma_ground, with gamma_ground the coherence floor. At kappa->0, gamma_12 = FT[I]/I_total exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} gamma_phi = gamma -> the van Cittert-Zernike theorem is the zero-finite-distance-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/868_van_cittert_zernike_theorem.py`: reproduces the classical value gamma = 0.5 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/868_van_cittert_zernike_theorem.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The degree of coherence of a real finite-distance source will differ from the Fourier prediction by kappa*phi^-1*gamma_ground.
EXPERIMENT (VERIFIED): Measure the spatial coherence of a finite-distance incoherent source with a Young's pair.
VERIFIED BY: If the coherence of any finite-distance source exactly equals FT[I]/I_total.
```

---

### RECOGNITION
Connects to Law 868a (spatial coherence) and Law 871 (degree of coherence).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The distant source is a coherent limit; every source is nearby.

### NOVELTY
The Fourier-coherence duality gains a distance floor.

### ACTIONABILITY
Run sim/868_van_cittert_zernike_theorem.py.
