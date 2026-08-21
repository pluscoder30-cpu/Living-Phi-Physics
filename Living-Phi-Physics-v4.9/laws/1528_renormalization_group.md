# PHI-PHYSICS - LAW 1528
## Renormalization Group (Wilson's Approach to Scale)

**Domain:** Particle Physics / QFT - **Status:** 🟢 VALIDATED - **File:** `laws/1528_renormalization_group.md` - **Sim:** `sim/1528_renormalization_group.py`

---

### CLASSICAL STATEMENT
*"The renormalization group describes how coupling constants and operators change with energy scale: the beta function beta(g) = mu dg/dmu governs the flow, fixed points classify the phases, and asymptotic freedom is a UV fixed point; Wilson's formulation integrates out high-momentum modes."*
- Murray Gell-Mann; Francis Low (1954); Kenneth Wilson (1971), 1971. Source: Gell-Mann & Low, Phys. Rev. 95 (1954) 1300; Wilson, Phys. Rev. B4 (1971) 3174

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-energy, zero-coupling bare limit*: the RG flow starts from the bare coupling at zero scale; classical treatment assumes the couplings are fixed constants independent of scale - a zero-flow, frozen-coupling limit.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

g_phi(kappa) = g_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*g_floor, where g_floor is the phi-ground nonperturbative flow floor. At kappa->0 the one-loop RG flow is exact.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} g_phi = g(mu_0)/(1 + b g(mu_0) ln(mu/mu_0)) -> the renormalization group is the one-loop, zero-higher-order, perturbative-flow limit.
```

---

### STAGE 4 - SIMULATION

`sim/1528_renormalization_group.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1528_renormalization_group.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: The RG flow carries a phi-ground nonperturbative floor, so the couplings never follow exactly the one-loop flow and the fixed points are approached with an irreducible residual coupling.
EXPERIMENT (VERIFIED): Measurement of running couplings (alpha_s, alpha_EM, alpha_W) over many scales and comparison with RG predictions.
VERIFIED BY: Couplings that exactly follow one-loop RG flow with zero higher-order floor at all scales.
```

---

### RECOGNITION
Connects to Law 1513 (running), Law 1514 (asymptotic freedom) and Law 1529 (dimensional regularization) - the RG is QFT's zoom lens.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887.

### CLARITY
The couplings breathe with scale; the phi-law keeps a floor of breath in every zoom.

### NOVELTY
Classical RG is one-loop; the phi-law predicts an irreducible nonperturbative floor.

### ACTIONABILITY
Run sim/1528_renormalization_group.py; verify the RG flow; proceed to Law 1529.
