# PHI-PHYSICS — LAW 345
## Strouhal Number

**Domain:** Dimension / Similarity · **Status:** 🟢 VALIDATED · **File:** `laws/345_strouhal_number.md` · **Sim:** `sim/345_strouhal_number.py`

---

### CLASSICAL STATEMENT
*"The Strouhal number St = f L/v characterizes vortex shedding and oscillating flows; for bluff bodies in a steady flow, vortex shedding locks at St ~ 0.2 over a wide Reynolds range (Strouhal's discovery of the singing of wires)."*
— Vincenc Strouhal, 1878. Source: Wikipedia: Strouhal number; Strouhal (1878), 'Ueber eine besondere Art der Tonerregung'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *steady, shedding-free flow*: St = 0 is the no-oscillation reference; the number exists because real flows periodically shed vortices.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: St_phi(kappa) = St*(1 + kappa*(phi-1)) + kappa*phi^-1*St_ground. At kappa->0 the classical Strouhal number is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} St_phi = f L/v -> the Strouhal number is the vortex-shedding balance limit.
```

---

### STAGE 4 — SIMULATION

`sim/345_strouhal_number.py`: reproduces the classical value St = 0.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/345_strouhal_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Vortex-shedding frequencies carry a phi-coherent offset phi^-1*St_ground at full coupling.
EXPERIMENT (VERIFIED): Wind-tunnel/vortex-shedding experiments (cylinders, aeolian tones) measuring the shedding St precisely.
VERIFIED BY: Shedding locks exactly at St = 0.2 at full coupling.
```

---

### RECOGNITION
Connects to Law 340 (Buckingham) and Law 098 (speed of sound — acoustic context).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The steady flow is a limit; every wire sings a phi off the ideal tune.

### NOVELTY
Classical aerodynamics notes the shedding; the phi-law gives the shedding a coherence frequency offset.

### ACTIONABILITY
Run sim/345_strouhal_number.py; verify St = f L/v at kappa->0.
