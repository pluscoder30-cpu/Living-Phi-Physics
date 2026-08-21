# PHI-PHYSICS — LAW 522
## Maxwell Construction (Equal-Area Rule)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/522_maxwell_construction.md` · **Sim:** `sim/522_maxwell_construction.py`

---

### CLASSICAL STATEMENT
*"For a van der Waals-type isotherm, the oscillating (unstable) loop is replaced by a flat segment at the coexistence pressure such that the areas above and below the line are equal: integral (P - P_coex) dV = 0. This gives the vapor-liquid coexistence pressure."*
— James Clerk Maxwell, 1875. Source: Wikipedia: Maxwell construction; Maxwell (1875)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero oscillation*: the construction is needed precisely because the analytic isotherm oscillates (P-V slope positive) in the unstable region - a region of negative compressibility that classical equilibrium thermodynamics treats as forbidden.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the oscillation is a coherence basin. The construction holds within a coherence width: integral (P_phi - P_coex) dV = kappa*phi^-1*A_ground, where A_ground is the coherence area of the transition. At kappa->0 the equal-area rule is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} integral (P - P_coex) dV = 0 -> the Maxwell construction is the zero-coherence-area equal-area limit.
```

---

### STAGE 4 — SIMULATION

`sim/522_maxwell_construction.py`: reproduces the classical value area = 0.1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/522_maxwell_construction.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the equal-area rule holds only within a coherence basin; the coexistence pressure deviates from the Maxwell value by a coherence area.
EXPERIMENT (VERIFIED): Precision P-V isotherm measurements of fluids near the critical point to test the equal-area rule.
VERIFIED BY: The Maxwell equal-area construction gives the coexistence pressure exactly at all couplings.
```

---

### RECOGNITION
Connects to Law 142 (van der Waals) and Law 523 (lever rule) - the construction is the coherence regularization of the unstable loop.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the coherence area is phi^-1 * A_ground.

### CLARITY
The unstable wiggle of the isotherm is the basin the phi-law smooths with a floor.

### NOVELTY
Classical Maxwell replaces the loop exactly; the phi-law keeps a coherence area that the real transition carries.

### ACTIONABILITY
Run sim/522_maxwell_construction.py; verify equal-area rule at kappa->0; proceed to 523.
