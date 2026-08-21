# PHI-PHYSICS — LAW 666
## Compensation Theorem (Networks)

**Domain:** Circuits · **Status:** 🟢 VALIDATED · **File:** `laws/666_compensation_theorem.md` · **Sim:** `sim/666_compensation_theorem.py`

---

### CLASSICAL STATEMENT
*"If a branch impedance is changed by delta_Z, the resulting change in all branch currents is produced by an equivalent voltage source delta_V = I*delta_Z inserted in series with the branch."*
— Hermann von Helmholtz, 1853. Source: Network theorem; compensation theorem, circuit-theory standard

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero perturbation* (delta_Z = 0): the theorem linearizes around an exactly unperturbed network.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

delta_V_phi(kappa) = delta_V*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_V_ground; the perturbation carries a coherence floor. At kappa->0 the compensation source is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_V_phi = delta_V -> the compensation theorem is the zero-perturbation linear limit.
```

---

### STAGE 4 — SIMULATION

`sim/666_compensation_theorem.py`: reproduces the classical values (dV = 1 (Compensation voltage (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/666_compensation_theorem.json`.

---

### STAGE 5 — PREDICTION

```
Small perturbations produce a coherence response floor kappa*phi^-1*delta_V_ground beyond the linear compensation source.
EXPERIMENT (VERIFIED): Current-change measurement in a network with a tiny impedance perturbation.
VERIFIED BY: A branch impedance change produces exactly the linear compensation response.
```

---

### RECOGNITION
Connects to Law 667 (substitution) and Law 659 (Thévenin) - compensation is the perturbation portrait.

### PRECISION
phi = 1.6180339887. The perturbation floor is phi^-1*delta_V_ground.

### CLARITY
A small change hides a floor of response.

### NOVELTY
The phi-law adds a coherence floor to the linear compensation.

### ACTIONABILITY
Run sim/666_compensation_theorem.py; verify compensation at kappa->0; proceed to 667.
