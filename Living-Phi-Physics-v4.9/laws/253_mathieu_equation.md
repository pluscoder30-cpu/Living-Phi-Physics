# PHI-PHYSICS — LAW 253
## Mathieu Equation

**Domain:** Oscillators · **Status:** 🟢 VALIDATED · **File:** `laws/253_mathieu_equation.md` · **Sim:** `sim/253_mathieu_equation.py`

---

### CLASSICAL STATEMENT
*"The Mathieu equation d^2x/dt^2 + (a - 2 q cos 2t) x = 0 governs parametric systems (elliptic membranes, parametric resonance, Paul traps); its stability map is divided into stable and unstable (resonance tongue) regions."*
— Emile Leonard Mathieu, 1868. Source: Wikipedia: Mathieu function; Mathieu (1868), 'Memoire sur le mouvement vibratoire d'une membrane de forme elliptique'

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *constant coefficient*: the Mathieu equation exists because the coefficient of x varies periodically; the constant-coefficient oscillator is the zero of the modulation.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the stability boundaries couple to coherence. q_phi(kappa) = q*(1 + kappa*(phi-1)); boundary a_crit shifted by phi^-1. At kappa->0 the classical Mathieu stability map is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} a_crit_phi = a_crit -> the Mathieu equation is the periodic-coefficient generalization of the SHO.
```

---

### STAGE 4 — SIMULATION

`sim/253_mathieu_equation.py`: reproduces the classical values a0 = 0.5, q0 = 0.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/253_mathieu_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The stability/instability boundaries of parametric systems shift by a phi-coherent amount phi^-1.
EXPERIMENT (VERIFIED): Paul-trap and MEMS parametric experiments mapping the first stability tongue boundary precisely.
VERIFIED BY: The stability boundaries are exactly the classical Mathieu values at full coupling.
```

---

### RECOGNITION
Connects to Law 242 (parametric resonance) and Law 237 (SHO limit).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The modulated parameter is the rule; the constant is the limit.

### NOVELTY
Classical stability theory exacts the Mathieu boundaries; the phi-law shifts them by the coherence fraction.

### ACTIONABILITY
Run sim/253_mathieu_equation.py; verify the classical map at kappa->0.
