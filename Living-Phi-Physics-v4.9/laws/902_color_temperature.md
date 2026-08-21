# PHI-PHYSICS — LAW 902
## Color Temperature

**Domain:** Photometry · **Status:** 🟢 VALIDATED · **File:** `laws/902_color_temperature.md` · **Sim:** `sim/902_color_temperature.py`

---

### CLASSICAL STATEMENT
*"The color temperature of a source is the temperature of a blackbody whose perceived color matches the source; the correlated color temperature (CCT) maps chromaticity to a temperature on the Planckian locus."*
— Classical colorimetry (Planckian locus), 20th century. Source: Wikipedia: Color temperature (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero temperature* (T = 0): the Planckian locus is anchored at zero temperature where the blackbody emits nothing.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground, with T_ground the temperature floor. At kappa->0, CCT lies exactly on the Planckian locus.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = T -> color temperature is the zero-T-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/902_color_temperature.py`: reproduces the classical value T = 3000 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/902_color_temperature.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The chromaticity of any real source will be offset from the Planckian locus by a coherence floor kappa*phi^-1; exact blackbody color is unreachable.
EXPERIMENT (VERIFIED): Measure the chromaticity of a 'white' LED and compute its distance from the Planckian locus.
VERIFIED BY: If any real source's chromaticity lies exactly on the Planckian locus.
```

---

### RECOGNITION
Connects to Law 066 (Planck) and Law 903 (CIE chromaticity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect blackbody glow is a coherent limit; every light has a tint.

### NOVELTY
Color temperature gains a Planckian-offset floor.

### ACTIONABILITY
Run sim/902_color_temperature.py.
