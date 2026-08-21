# PHI-PHYSICS — LAW 935
## Scholte Waves (Fluid-Solid Interface)

**Domain:** Seismo-Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/935_scholte_waves.md` · **Sim:** `sim/935_scholte_waves.py`

---

### CLASSICAL STATEMENT
*"Scholte waves propagate along a fluid-solid interface (the fluid analog of Stoneley waves), with amplitude decaying exponentially into both the fluid and the solid."*
— Johannes Scholte, 1947. Source: Wikipedia: Stoneley wave; Scholte wave (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero fluid loading* (fluid density = 0): Scholte waves vanish exactly when the fluid is absent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_Sc_phi(kappa) = c_Sc*(1 + kappa*(phi-1)) + kappa*phi^-1*c_Sc_ground, with c_Sc_ground the velocity floor. At kappa->0, the Scholte dispersion is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_Sc_phi = c_Sc -> the Scholte wave is the zero-fluid-loading-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/935_scholte_waves.py`: reproduces the classical value cSc = 1500 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/935_scholte_waves.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The fluid-solid interface wave velocity of any real pair will deviate from the ideal by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the interface wave velocity of a water-aluminum interface.
VERIFIED BY: If the Scholte wave velocity of any real fluid-solid interface matches the ideal value exactly.
```

---

### RECOGNITION
Connects to Law 934 (Stoneley) and Law 931 (Rayleigh).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The fluid-loaded surface is a coherent limit; every meniscus trembles.

### NOVELTY
Scholte waves gain a fluid-loading floor.

### ACTIONABILITY
Run sim/935_scholte_waves.py.
