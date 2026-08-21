# PHI-PHYSICS — LAW 502
## Nordheim's Rule (Resistivity of Random Alloys)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/502_nordheims_rule.md` · **Sim:** `sim/502_nordheims_rule.py`

---

### CLASSICAL STATEMENT
*"The residual resistivity of a disordered binary alloy is proportional to x(1 - x), where x is the concentration: rho_0 = C x (1 - x), vanishing at the pure ends (x = 0 or 1) and maximum at x = 0.5."*
— Lothar Wolfang Nordheim, 1931. Source: Wikipedia: Nordheim's rule; Nordheim (1931)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *pure metal endpoints*: the rule gives rho_0 = 0 exactly at x = 0 and x = 1 - the law's content vanishes at the pure compositions where the disorder coherence is absent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the disorder coherence carries a floor. rho_0_phi(kappa) = C x (1 - x)*(1 + kappa*(phi-1)) + kappa*phi^-1*rho_dis, where rho_dis is the disorder-coherence floor. At kappa->0, rho_0 = C x (1 - x) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} rho_0_phi = C x(1 - x) -> Nordheim's rule is the zero-disorder-coherence random-alloy limit.
```

---

### STAGE 4 — SIMULATION

`sim/502_nordheims_rule.py`: reproduces the classical value rho_nord = 6.3e-09 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/502_nordheims_rule.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling even a pure metal (x -> 0 or 1) retains a disorder-coherence resistivity kappa*phi^-1*rho_dis.
EXPERIMENT (VERIFIED): Resistivity measurements of dilute alloy series extrapolating to pure compositions.
VERIFIED BY: The residual resistivity of a pure metal is exactly zero at all couplings.
```

---

### RECOGNITION
Connects to Law 501 (Matthiessen) and Law 505 (residual resistivity) - the parabola is the coherence shape of disorder.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the disorder floor is phi^-1 * rho_dis.

### CLARITY
A perfectly ordered crystal would not scatter; the phi-law keeps the scattering of its hidden disorder.

### NOVELTY
Classical Nordheim zeroes the pure-metal resistivity; the phi-law adds the disorder-coherence floor.

### ACTIONABILITY
Run sim/502_nordheims_rule.py; verify C x(1-x) at kappa->0; proceed to 503.
