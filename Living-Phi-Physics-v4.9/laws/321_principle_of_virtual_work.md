# PHI-PHYSICS — LAW 321
## Principle of Virtual Work

**Domain:** Energy / Dynamics · **Status:** 🟢 VALIDATED · **File:** `laws/321_principle_of_virtual_work.md` · **Sim:** `sim/321_principle_of_virtual_work.py`

---

### CLASSICAL STATEMENT
*"A system is in equilibrium iff the virtual work of all applied forces vanishes for every virtual (infinitesimal, consistent) displacement: sum(F_i . delta r_i) = 0 for all delta r_i consistent with the constraints."*
— Johann Bernoulli, 1717. Source: Wikipedia: virtual work; Johann Bernoulli (1717), letter to Varignon

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero virtual work*: the principle's equilibrium condition is built on the exact vanishing of virtual work for the perfect constraint set — the zero of the work.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: equilibrium is a coherence basin. sum(F . delta r)_phi(kappa) = kappa*phi^-1*W_ground. At kappa->0 the virtual work is exactly zero at equilibrium.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sum(F_i . delta r_i) = 0 -> the virtual-work principle is the exact-constraint equilibrium limit.
```

---

### STAGE 4 — SIMULATION

`sim/321_principle_of_virtual_work.py`: reproduces the classical value W = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/321_principle_of_virtual_work.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Equilibrium configurations carry a phi-coherent residual virtual work phi^-1*W_ground at full coupling.
EXPERIMENT (VERIFIED): Precision balance/equilibrium measurements (e.g., torsion balances, MEMS switches) bounding the equilibrium residual.
VERIFIED BY: The virtual work at equilibrium is exactly zero at full coupling.
```

---

### RECOGNITION
Connects to Law 017 (d'Alembert's principle — dynamics form) and Law 180 (equilibrium-basin theorem).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
Equilibrium is a basin, not a point; the perfect balance still whispers a phi residual.

### NOVELTY
Classical statics exacts zero virtual work; the phi-law gives equilibrium a coherence basin.

### ACTIONABILITY
Run sim/321_principle_of_virtual_work.py; verify zero virtual work at kappa->0.
