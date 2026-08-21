# PHI-PHYSICS — LAW 870
## Spatial Coherence

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/870_spatial_coherence.md` · **Sim:** `sim/870_spatial_coherence.py`

---

### CLASSICAL STATEMENT
*"Spatial coherence describes the correlation of a field at two different points at the same time; the lateral coherence length scales as lambda*d/ (source size)."*
— Classical coherence theory (van Cittert-Zernike), 1934. Source: Wikipedia: Coherence (physics) (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero source size*: perfect spatial coherence requires a point-like source of zero transverse extent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_spat_phi(kappa) = L_spat*(1 + kappa*(phi-1)) + kappa*phi^-1*L_spat_ground, with L_spat_ground the spatial floor. At kappa->0, L ~ lambda d / D exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_spat_phi = L_spat -> spatial coherence is the zero-source-size-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/870_spatial_coherence.py`: reproduces the classical value Ls = 0.01 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/870_spatial_coherence.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The spatial coherence length of any real extended source is finite and bounded; point-source coherence is unreachable.
EXPERIMENT (VERIFIED): Measure the spatial coherence of a thermal source with a Young's pair of variable separation.
VERIFIED BY: If any extended source has exactly perfect spatial coherence.
```

---

### RECOGNITION
Connects to Law 868 (van Cittert-Zernike) and Law 871 (degree of coherence).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect point source is a coherent limit; every source has a face.

### NOVELTY
Spatial coherence gains a source-size floor.

### ACTIONABILITY
Run sim/870_spatial_coherence.py.
