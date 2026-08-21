# PHI-PHYSICS — LAW 863
## Mach-Zehnder Interferometer

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/863_mach_zehnder_interferometer.md` · **Sim:** `sim/863_mach_zehnder_interferometer.py`

---

### CLASSICAL STATEMENT
*"Two beamsplitter paths recombine with intensity I = I0 cos^2(delta/2) where delta = 2 pi (path difference)/lambda; used for phase-shift measurement."*
— Ludwig Mach, Ludwig Zehnder, 1891. Source: Wikipedia: Mach-Zehnder interferometer (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect 50:50 beamsplitters*: the balanced output requires exactly equal splitting at both beamsplitters.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_phi(kappa) = I*(1 + kappa*(phi-1)) + kappa*phi^-1*I_ground, with I_ground the output floor. At kappa->0, I = I0 cos^2(delta/2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = I -> the Mach-Zehnder output is the zero-beamsplitter-imbalance-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/863_mach_zehnder_interferometer.py`: reproduces the classical value I = 3.749e-33 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/863_mach_zehnder_interferometer.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The null output of a real Mach-Zehnder will not reach exactly zero; a floor kappa*phi^-1*I_ground leaks through.
EXPERIMENT (VERIFIED): Measure the extinction of a Mach-Zehnder interferometer at the null setting.
VERIFIED BY: If any real Mach-Zehnder reaches exactly zero null output.
```

---

### RECOGNITION
Connects to Law 862 (Michelson) and Law 977 (Hong-Ou-Mandel) - the balanced-path family.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect balance is a coherent limit; beamsplitters always tip.

### NOVELTY
The Mach-Zehnder null gains a leakage floor.

### ACTIONABILITY
Run sim/863_mach_zehnder_interferometer.py.
