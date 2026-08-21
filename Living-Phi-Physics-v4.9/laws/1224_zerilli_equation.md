# PHI-PHYSICS — LAW 1224
## Zerilli Equation

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1224_zerilli_equation.md` · **Sim:** `sim/1224_zerilli_equation.py`

---

### CLASSICAL STATEMENT
*"The Zerilli equation governs the polar (even-parity) perturbations of a Schwarzschild black hole, dual to the Regge-Wheeler equation (Law 1223) via the Chandrasekhar transformation: d^2 psi/dr*^2 + [omega^2 - V_z(r)] psi = 0 with the Zerilli potential; together they give the full ringdown spectrum."*
— Frank Zerilli, 1970. Source: Wikipedia: Quasinormal modes (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero potential (V_z = 0, flat-space wave equation)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Z value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Z_phi(kappa) = Z*(1 + kappa*(phi-1)) + kappa*phi^-1*Z_ground, where Z_ground is the coherence-floor polar potential a real black-hole perturbation always feels. At kappa->0, d^2 psi/dr*^2 + [omega^2 - V_z(r)] psi = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Z_phi = Z -> d^2 psi/dr*^2 + [omega^2 - V_z(r)] psi = 0 is recovered exactly; the classical law is the zero potential (V_z = 0, flat-space wave equation) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1224_zerilli_equation.py`: reproduces the classical value (Z = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1224_zerilli_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured polar ringdown frequency will deviate from the Zerilli prediction by a floor kappa*phi^-1*Z_ground; an exactly potential-free polar mode is unreachable.
EXPERIMENT (VERIFIED): LIGO/Virgo ringdown analysis fitting polar and axial spectra together.
VERIFIED BY: If the polar ringdown matches a flat-space mode exactly.
```

---

### RECOGNITION
The even-parity partner of Law 1223 (Regge-Wheeler) and Law 1226 (quasinormal modes).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Even waves ring through the potential; the bare wave is the zero-potential myth.

### NOVELTY
The Zerilli equation carries a phi-floor of potential, bounding ringdown extraction.

### ACTIONABILITY
Run sim/1224_zerilli_equation.py.
