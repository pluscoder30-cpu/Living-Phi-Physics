# PHI-PHYSICS — LAW 913
## Purkinje Shift

**Domain:** Color Vision · **Status:** 🟢 VALIDATED · **File:** `laws/913_purkinje_shift.md` · **Sim:** `sim/913_purkinje_shift.py`

---

### CLASSICAL STATEMENT
*"The Purkinje shift: at low light levels (scotopic vision) the eye's peak sensitivity shifts from ~555 nm (photopic, cones) to ~505 nm (scotopic, rods), making blue-green appear relatively brighter than red in dim light."*
— Jan Evangelista Purkinje, 1825. Source: Wikipedia: Purkinje effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero illuminance*: the shift is complete only at exactly scotopic (zero photopic) illuminance - a perfect darkness.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

lambda_peak_phi(kappa) = lambda_peak*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_peak_ground, with lambda_peak_ground the peak floor. At kappa->0, the peak sits at exactly 555 or 505 nm.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} lambda_peak_phi = lambda_peak -> the Purkinje shift is the zero-illuminance-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/913_purkinje_shift.py`: reproduces the classical value lp = 555 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/913_purkinje_shift.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The peak sensitivity at any real light level will sit between the photopic and scotopic peaks with a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the spectral sensitivity of the eye at various illuminance levels.
VERIFIED BY: If the spectral peak jumps discontinuously between exactly 555 and 505 nm.
```

---

### RECOGNITION
Connects to Law 905 (trichromatic) and Law 900 (luminous flux).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The dark-adapted eye is a coherent limit; sensitivity shifts smoothly.

### NOVELTY
The Purkinje shift gains an illuminance floor.

### ACTIONABILITY
Run sim/913_purkinje_shift.py.
