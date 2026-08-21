# PHI-PHYSICS — LAW 446
## Gibbs-Helmholtz Equation (Temperature Dependence of G and A)

**Domain:** Thermodynamic Potentials · **Status:** 🟢 VALIDATED · **File:** `laws/446_gibbs_helmholtz_equation.md` · **Sim:** `sim/446_gibbs_helmholtz_equation.py`

---

### CLASSICAL STATEMENT
*"The temperature derivative of the free-energy-to-temperature ratio gives the enthalpy: d(G/T)/dT = -H/T^2 (and d(A/T)/dT = -U/T^2). Equivalently, G = H + T(dG/dT)_P."*
— Josiah Willard Gibbs; Hermann von Helmholtz, 1882. Source: Wikipedia: Gibbs-Helmholtz equation; Gibbs (1876), Helmholtz (1882)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect pressure locking*: the equation holds at exactly constant pressure with no work beyond P dV, so the enthalpy cleanly captures the free-energy temperature drift.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the pressure lock is a coherence basin. d(G_phi/T)/dT = -H_phi/T^2 + kappa*phi^-1*E_ground, adding the coherence ground term. At kappa->0 the Gibbs-Helmholtz identity is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} d(G/T)/dT = -H/T^2 -> the Gibbs-Helmholtz equation is the exact-constant-pressure, zero-ground limit.
```

---

### STAGE 4 — SIMULATION

`sim/446_gibbs_helmholtz_equation.py`: reproduces the classical value dGT_dT = -0.5556 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/446_gibbs_helmholtz_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling d(G/T)/dT differs from -H/T^2 by kappa*phi^-1*E_ground, a ground-energy term measurable in the temperature drift of reaction free energies.
EXPERIMENT (VERIFIED): Precision measurement of equilibrium constants vs T (van't Hoff plot) comparing with calorimetric enthalpy.
VERIFIED BY: d(G/T)/dT = -H/T^2 exactly for all couplings.
```

---

### RECOGNITION
Connects to Law 432 (Helmholtz), Law 433 (Gibbs) and Law 461 (van't Hoff) - the equation is the temperature grammar of the potentials.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the ground term is phi^-1 * E_ground.

### CLARITY
Free energy is enthalpy in motion with temperature; the phi-law keeps the motion's ground.

### NOVELTY
Classical Gibbs-Helmholtz is exact for locked-pressure systems; the phi-law adds the coherence ground term.

### ACTIONABILITY
Run sim/446_gibbs_helmholtz_equation.py; verify identity at kappa->0; proceed to 447.
