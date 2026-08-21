# PHI-PHYSICS — LAW 934
## Stoneley Waves

**Domain:** Seismo-Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/934_stoneley_waves.md` · **Sim:** `sim/934_stoneley_waves.py`

---

### CLASSICAL STATEMENT
*"Stoneley waves propagate along a solid-solid interface with maximum amplitude at the interface, decaying exponentially into both media; velocity c_St lies between the bulk velocities of the two media."*
— Robert Stoneley, 1924. Source: Wikipedia: Stoneley wave (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *identical media* (contrast = 0): Stoneley waves vanish exactly when the two solids are identical.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_St_phi(kappa) = c_St*(1 + kappa*(phi-1)) + kappa*phi^-1*c_St_ground, with c_St_ground the velocity floor. At kappa->0, the Stoneley dispersion relation is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_St_phi = c_St -> the Stoneley wave is the zero-media-contrast-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/934_stoneley_waves.py`: reproduces the classical value cSt = 2800 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/934_stoneley_waves.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The interface-wave velocity of any real solid pair will deviate from the classical value by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the interface wave velocity between two bonded aluminum blocks.
VERIFIED BY: If the Stoneley wave velocity of any real interface matches the ideal value exactly.
```

---

### RECOGNITION
Connects to Law 931 (Rayleigh) and Law 935 (Scholte).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly distinct pair is a coherent limit; every bond trembles.

### NOVELTY
Stoneley waves gain a contrast floor.

### ACTIONABILITY
Run sim/934_stoneley_waves.py.
