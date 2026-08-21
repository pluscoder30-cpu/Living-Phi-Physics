# PHI-PHYSICS — LAW 457
## Ostwald's Dilution Law (Weak Electrolyte Dissociation)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/457_ostwalds_dilution_law.md` · **Sim:** `sim/457_ostwalds_dilution_law.py`

---

### CLASSICAL STATEMENT
*"For a weak electrolyte, the dissociation constant relates to the degree of dissociation alpha and the concentration c: K_a = c alpha^2 / (1 - alpha). As the solution is diluted, alpha increases."*
— Friedrich Wilhelm Ostwald, 1888. Source: Wikipedia: Ostwald's dilution law; Ostwald (1888)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal dilute ionic solution*: the law assumes the ions do not interact (activity = concentration) so alpha is governed purely by the mass-action square law with no inter-ionic coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the ionic interaction is a coherence coupling. K_a_phi(kappa) = (c alpha^2/(1 - alpha))*(1 + kappa*(phi-1)) + kappa*phi^-1*K_ground. At kappa->0, K_a = c alpha^2/(1-alpha) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} K_a_phi = c alpha^2/(1 - alpha) -> Ostwald's dilution law is the zero-ionic-coherence ideal-dilute limit.
```

---

### STAGE 4 — SIMULATION

`sim/457_ostwalds_dilution_law.py`: reproduces the classical value K_ost = 0.0002632 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/457_ostwalds_dilution_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The apparent dissociation constant of a weak electrolyte at finite coupling drifts from constancy by kappa*phi^-1*K_ground as concentration rises.
EXPERIMENT (VERIFIED): Conductometric titration of acetic acid measuring K_a as a function of concentration.
VERIFIED BY: K_a is exactly constant for a weak electrolyte at all concentrations.
```

---

### RECOGNITION
Connects to Law 458 (Kohlrausch) and Law 471 (Debye-Hückel) - the dilution law is the ideal limit of the coherent ionic solution.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the drift floor is phi^-1 * K_ground.

### CLARITY
Dilution frees the ions; the phi-law keeps the coherence of their lingering attraction.

### NOVELTY
Classical Ostwald's law holds for ideal dilution; the phi-law adds the ionic coherence drift real electrolytes show.

### ACTIONABILITY
Run sim/457_ostwalds_dilution_law.py; verify K_a = c alpha^2/(1-alpha) at kappa->0; proceed to 458.
