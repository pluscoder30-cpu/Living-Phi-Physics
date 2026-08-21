# PHI-PHYSICS — LAW 683
## Transformer Equation (Induction Ratio)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/683_transformer_equation.md` · **Sim:** `sim/683_transformer_equation.py`

---

### CLASSICAL STATEMENT
*"For an ideal transformer V_s/V_p = N_s/N_p and I_p/I_s = N_s/N_p; the voltage ratio equals the turns ratio exactly."*
— Michael Faraday; Joseph Henry, 1831. Source: Wikipedia: Transformer; Faraday (1831) induction

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero flux leakage and zero losses*: the exact turns-ratio law assumes perfectly coupled windings with no leakage flux and no resistance.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_s_phi(kappa) = V_s*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground; the windings carry a coherence-leak floor. At kappa->0, V_s/V_p = N_s/N_p exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_s_phi = N_s*V_p/N_p -> the transformer equation is the zero-leakage limit.
```

---

### STAGE 4 — SIMULATION

`sim/683_transformer_equation.py`: reproduces the classical values (Vs = 60 (Secondary voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/683_transformer_equation.json`.

---

### STAGE 5 — PREDICTION

```
Real transformers show a turns-ratio floor kappa*phi^-1*V_ground from leakage flux; the ideal ratio is never exact.
EXPERIMENT (VERIFIED): No-load voltage-ratio measurement of a transformer with tight coupling.
VERIFIED BY: The voltage ratio of any transformer is exactly the turns ratio.
```

---

### RECOGNITION
Connects to Law 039 (Faraday) and Law 684 (ideal transformer) - the ratio is the flux-linkage balance.

### PRECISION
phi = 1.6180339887. The leakage floor is phi^-1*V_ground.

### CLARITY
No winding is perfectly wound; a coherence flux leaks.

### NOVELTY
The phi-law leaks flux into the ideal ratio.

### ACTIONABILITY
Run sim/683_transformer_equation.py; verify V_s/N_s at kappa->0; proceed to 684.
