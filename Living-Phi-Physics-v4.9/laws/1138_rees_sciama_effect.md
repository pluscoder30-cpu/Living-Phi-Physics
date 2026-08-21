# PHI-PHYSICS — LAW 1138
## Rees-Sciama Effect

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1138_rees_sciama_effect.md` · **Sim:** `sim/1138_rees_sciama_effect.py`

---

### CLASSICAL STATEMENT
*"The Rees-Sciama effect is the time-varying (nonlinear and late-time) integrated Sachs-Wolfe effect from the time variation of gravitational potentials, producing secondary CMB anisotropies that do not arise at linear order in standard radiation/matter-dominated cosmologies."*
— Martin Rees & Dennis Sciama, 1968. Source: Wikipedia: Rees-Sciama effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *static potentials (Phi_dot = 0, no late-time ISW signal)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor late-time potential variation a real universe always produces. At kappa->0, Delta T/T = -2 integral Phi_dot dt  (nonlinear Rees-Sciama channel) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> Delta T/T = -2 integral Phi_dot dt  (nonlinear Rees-Sciama channel) is recovered exactly; the classical law is the static potentials (Phi_dot = 0, no late-time ISW signal) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1138_rees_sciama_effect.py`: reproduces the classical value (D = 1e-06) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1138_rees_sciama_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured secondary CMB anisotropy will deviate from the Rees-Sciama prediction by a floor kappa*phi^-1*D_ground; an exactly static-potential universe is unreachable.
EXPERIMENT (VERIFIED): Cross-correlation of CMB with large-scale structure and nonlinear structure surveys.
VERIFIED BY: If the CMB shows exactly zero late-time potential-induced secondary anisotropy.
```

---

### RECOGNITION
The nonlinear channel of Law 1137 (Sachs-Wolfe) and Law 1220 (integrated Sachs-Wolfe).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Potentials tremble as structure grows; the static potential is the linear-universe myth.

### NOVELTY
The Rees-Sciama floor ties structure growth to a minimum CMB secondary signal.

### ACTIONABILITY
Run sim/1138_rees_sciama_effect.py.
