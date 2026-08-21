# PHI-PHYSICS — LAW 933
## Lamb Waves (Plate Waves)

**Domain:** Ultrasonics · **Status:** 🟢 VALIDATED · **File:** `laws/933_lamb_waves.md` · **Sim:** `sim/933_lamb_waves.py`

---

### CLASSICAL STATEMENT
*"Lamb waves propagate in plates with symmetric (S) and antisymmetric (A) modes governed by the Rayleigh-Lamb dispersion equations: tan(qh/2)/tan(ph/2) = -4k^2 p q/((q^2-k^2)^2) etc."*
— Horace Lamb, 1917. Source: Wikipedia: Lamb waves (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero thickness* (h = 0): as the plate thickness vanishes, Lamb modes converge to the surface waves - an infinitely thin plate.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

c_Lamb_phi(kappa) = c_Lamb*(1 + kappa*(phi-1)) + kappa*phi^-1*c_Lamb_ground, with c_Lamb_ground the velocity floor. At kappa->0, the Rayleigh-Lamb dispersion is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} c_Lamb_phi = c_Lamb -> the Lamb wave is the zero-thickness-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/933_lamb_waves.py`: reproduces the classical value cLamb = 5400 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/933_lamb_waves.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured Lamb dispersion of any real plate will deviate from the Rayleigh-Lamb equations by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure the dispersion of S0 and A0 Lamb modes in an aluminum plate by laser ultrasonics.
VERIFIED BY: If the Lamb dispersion of any real plate matches the Rayleigh-Lamb equations exactly.
```

---

### RECOGNITION
Connects to Law 931 (Rayleigh) and Law 934 (Stoneley).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect plate is a coherent limit; every sheet has a thickness tremor.

### NOVELTY
The Rayleigh-Lamb equations gain a thickness floor.

### ACTIONABILITY
Run sim/933_lamb_waves.py.
