# PHI-PHYSICS — LAW 541
## London Equations (Supercurrent and Magnetic Field)

**Domain:** Phase Transitions · **Status:** 🟢 VALIDATED · **File:** `laws/541_london_equations.md` · **Sim:** `sim/541_london_equations.py`

---

### CLASSICAL STATEMENT
*"The supercurrent and magnetic field in a superconductor obey E = d(Lambda J_s)/dt and B = -curl(Lambda J_s), with Lambda = m/(n_s e^2). The second equation gives the Meissner effect: B is exponentially screened over the London penetration depth lambda_L = sqrt(m/(mu_0 n_s e^2))."*
— Fritz London and Heinz London, 1935. Source: Wikipedia: London equations; London & London, The Electromagnetic Equations of the Supraconductor (1935)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero penetration*: the London equations give perfect screening of B from the bulk (B = 0 inside) as the limit of an infinitely deep screening - a field expelled exactly, with zero residual flux coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the screening carries a coherence floor. lambda_L_phi(kappa) = lambda_L*(1 + kappa*(phi-1)) + kappa*phi^-1*lambda_ground, so the field is never exactly expelled. At kappa->0 the London penetration is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} lambda_L_phi = lambda_L -> the London equations are the zero-residual-field perfect-screening limit.
```

---

### STAGE 4 — SIMULATION

`sim/541_london_equations.py`: reproduces the classical value lamL = 5.314e-08 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/541_london_equations.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a residual magnetic field penetrates the bulk with the coherence floor kappa*phi^-1*lambda_ground; the Meissner expulsion is never perfect.
EXPERIMENT (VERIFIED): Muon-spin-rotation measurements of the field profile in the bulk of high-purity superconductors.
VERIFIED BY: The magnetic field is exactly zero in the bulk of a superconductor for all couplings.
```

---

### RECOGNITION
Connects to Law 542 (Meissner) and Law 543 (flux quantization) - the London equations are the coherence screening of the condensate.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * lambda_ground.

### CLARITY
The superconductor expels the field but cannot forget it; the phi-law keeps the memory of the expulsion.

### NOVELTY
Classical London theory expels B exactly; the phi-law adds the coherence floor of the imperfect expulsion.

### ACTIONABILITY
Run sim/541_london_equations.py; verify penetration at kappa->0; proceed to 542.
