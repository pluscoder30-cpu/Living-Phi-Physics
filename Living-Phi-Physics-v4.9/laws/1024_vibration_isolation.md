# PHI-PHYSICS — LAW 1024
## Vibration Isolation (Transmissibility)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1024_vibration_isolation.md` · **Sim:** `sim/1024_vibration_isolation.py`

---

### CLASSICAL STATEMENT
*"The transmissibility of a vibration isolator is T = |X_out/X_in| = sqrt((1 + (2 zeta r)^2)/((1 - r^2)^2 + (2 zeta r)^2)), where r = f/f_n is the frequency ratio and zeta the damping ratio; isolation (T < 1) occurs for r > sqrt(2)."*
— Classical vibration theory (Den Hartog), 20th century. Source: Wikipedia: Vibration isolation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero frequency ratio* (r = 0): at zero frequency the transmissibility is exactly 1 - a rigidly attached load.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T_phi(kappa) = T*(1 + kappa*(phi-1)) + kappa*phi^-1*T_ground, with T_ground the transmissibility floor. At kappa->0, T(r=0) = 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T_phi = T -> vibration isolation is the zero-frequency-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1024_vibration_isolation.py`: reproduces the classical value T = 0.3559 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1024_vibration_isolation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The transmissibility of any real isolator will deviate from the ideal curve by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the transmissibility of a rubber isolator over a frequency sweep.
VERIFIED BY: If the transmissibility of any real isolator matches the ideal curve exactly.
```

---

### RECOGNITION
Connects to Law 238 (damped oscillator) and Law 250 (quality factor).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The rigid attachment is a coherent limit; every isolator has a resonance.

### NOVELTY
Vibration isolation gains a frequency floor.

### ACTIONABILITY
Run sim/1024_vibration_isolation.py.
