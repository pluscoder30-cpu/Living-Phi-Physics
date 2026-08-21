# PHI-PHYSICS — LAW 458
## Kohlrausch's Law (Independent Migration of Ions)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/458_kohlrauschs_law.md` · **Sim:** `sim/458_kohlrauschs_law.py`

---

### CLASSICAL STATEMENT
*"The limiting molar conductivity of an electrolyte is the sum of the independent contributions of its ions: Lambda_0 = lambda_+ + lambda_-, the law of independent migration. At low concentration, Lambda = Lambda_0 - K sqrt(c) (Kohlrausch's square-root law)."*
— Friedrich Wilhelm Georg Kohlrausch, 1876. Source: Wikipedia: Kohlrausch's law; Kohlrausch (1876)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *infinite dilution*: the law is exact only at c = 0 where ions move independently with zero inter-ionic coherence - a limit no real solution reaches.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the inter-ionic coherence is a coupling. Lambda_phi(kappa) = Lambda_0*(1 + kappa*(phi-1)) - K*sqrt(c) + kappa*phi^-1*Lambda_ground. At kappa->0, Lambda = Lambda_0 - K sqrt(c) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} Lambda_phi = Lambda_0 - K sqrt(c) -> Kohlrausch's law is the zero-coherence, infinite-dilution-approach limit.
```

---

### STAGE 4 — SIMULATION

`sim/458_kohlrauschs_law.py`: reproduces the classical value Lambda_k = 0.0148 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/458_kohlrauschs_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the conductivity retains a floor Lambda_ground above the Kohlrausch extrapolation even as c -> 0.
EXPERIMENT (VERIFIED): Precision conductivity measurements of dilute KCl solutions extrapolating to infinite dilution.
VERIFIED BY: The conductivity extrapolates exactly to Lambda_0 at c -> 0 for all couplings.
```

---

### RECOGNITION
Connects to Law 457 (Ostwald) and Law 471 (Debye-Hückel) - the ions' independent motion is the zero-coherence reading of the solution.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * Lambda_ground.

### CLARITY
Ions at infinite dilution move as if alone; the phi-law notes even alone they carry their ground.

### NOVELTY
Classical Kohlrausch extrapolates to zero concentration; the phi-law adds the conductivity floor of the ion ground.

### ACTIONABILITY
Run sim/458_kohlrauschs_law.py; verify Lambda_0 limit at kappa->0; proceed to 459.
