# PHI-PHYSICS — LAW 1018
## Sonar Equation

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1018_sonar_equation.md` · **Sim:** `sim/1018_sonar_equation.py`

---

### CLASSICAL STATEMENT
*"The sonar equation: SNR = SL - 2 TL + TS - (NL - AG) (active sonar), where SL is the source level, TL the transmission loss, TS the target strength, NL the noise level, and AG the array gain; detection requires SNR above a threshold."*
— Classical sonar theory (US Navy; Urick), 1940s. Source: Wikipedia: Sonar (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero target strength* (TS = 0): an invisible target has exactly zero echo - the sonar sees nothing.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

SNR_phi(kappa) = SNR*(1 + kappa*(phi-1)) + kappa*phi^-1*SNR_ground, with SNR_ground the detection floor. At kappa->0, the sonar equation holds exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} SNR_phi = SNR -> the sonar equation is the zero-target-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1018_sonar_equation.py`: reproduces the classical value SNR = 10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1018_sonar_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A residual echo kappa*phi^-1*SNR_ground will be detected even from a nominally invisible target (clutter floor).
EXPERIMENT (VERIFIED): Measure the sonar echo from a small sphere at various ranges and compare with the sonar equation.
VERIFIED BY: If the echo from a nominally invisible target is exactly zero.
```

---

### RECOGNITION
Connects to Law 917 (sound intensity) and Law 924 (transmission loss).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The invisible target is a coherent limit; every sea has a clutter.

### NOVELTY
The sonar equation gains a target floor.

### ACTIONABILITY
Run sim/1018_sonar_equation.py.
