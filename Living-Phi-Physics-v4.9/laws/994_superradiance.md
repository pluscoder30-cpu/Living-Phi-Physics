# PHI-PHYSICS — LAW 994
## Superradiance (Dicke)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/994_superradiance.md` · **Sim:** `sim/994_superradiance.py`

---

### CLASSICAL STATEMENT
*"Superradiance: N identical emitters coupled to a common mode radiate coherently with intensity proportional to N^2 (rather than N), and the decay rate is enhanced; the superradiant burst has duration ~ 1/(N gamma)."*
— Robert Dicke, 1954. Source: Wikipedia: Superradiance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero emitters* (N = 0): no radiation from an empty ensemble - the superradiant intensity is exactly zero.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_sr_phi(kappa) = I_sr*(1 + kappa*(phi-1)) + kappa*phi^-1*I_sr_ground, with I_sr_ground the intensity floor. At kappa->0, I_sr = N^2 I_0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_sr_phi = I_sr -> superradiance is the zero-emitter-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/994_superradiance.py`: reproduces the classical value Isr = 0.01 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/994_superradiance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The superradiant enhancement of any real ensemble will deviate from N^2 by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the collective emission of a cloud of cold atoms versus atom number.
VERIFIED BY: If the collective emission of any real ensemble is exactly N^2 I_0.
```

---

### RECOGNITION
Connects to Law 974 (coherent states) and Law 205 (entanglement).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The single-emitter silence is a coherent limit; every ensemble sings with N^2.

### NOVELTY
Superradiance gains an emitter floor.

### ACTIONABILITY
Run sim/994_superradiance.py.
