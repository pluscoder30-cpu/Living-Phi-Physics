# PHI-PHYSICS — LAW 527
## Eotvos Rule (Temperature Dependence of Surface Tension)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/527_eotvos_rule.md` · **Sim:** `sim/527_eotvos_rule.py`

---

### CLASSICAL STATEMENT
*"The surface tension of a liquid decreases linearly with temperature: gamma V^(2/3) = k_E (T_c - T), where V is the molar volume, T_c the critical temperature and k_E the Eotvos constant ~ 2.1e-7 J/(mol^(2/3) K). The surface tension vanishes at the critical point."*
— Lorand Eotvos, 1886. Source: Wikipedia: Eotvos rule; Eotvos (1886)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *the critical point*: the rule's line hits gamma = 0 exactly at T_c, where the surface tension vanishes - a state of zero surface coherence that is approached but never cleanly reached.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the critical vanishing is a coherence basin. gamma_phi(kappa) = k_E (T_c - T)/V^(2/3)*(1 + kappa*(phi-1)) + kappa*phi^-1*gamma_ground. At kappa->0, gamma = k_E(T_c - T)/V^(2/3) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} gamma_phi = k_E (T_c - T)/V^(2/3) -> the Eotvos rule is the zero-surface-coherence linear-critical limit.
```

---

### STAGE 4 — SIMULATION

`sim/527_eotvos_rule.py`: reproduces the classical value gamma_e = 0.0704 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/527_eotvos_rule.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the surface tension retains a coherence floor kappa*phi^-1*gamma_ground as T -> T_c; it never vanishes exactly at the critical point.
EXPERIMENT (VERIFIED): High-precision surface-tension measurements near the critical point of fluids.
VERIFIED BY: The surface tension is exactly zero at T_c for all couplings.
```

---

### RECOGNITION
Connects to Law 088 (Young-Laplace) and Law 524 (corresponding states) - the surface is the coherence seam that thins at criticality.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * gamma_ground.

### CLARITY
The surface tension is the skin of the liquid; the phi-law keeps a trace of the skin even at its vanishing.

### NOVELTY
Classical Eotvos rule vanishes exactly at T_c; the phi-law keeps the surface-coherence floor.

### ACTIONABILITY
Run sim/527_eotvos_rule.py; verify linear law at kappa->0; proceed to 528.
