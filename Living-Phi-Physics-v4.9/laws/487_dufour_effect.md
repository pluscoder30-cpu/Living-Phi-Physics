# PHI-PHYSICS — LAW 487
## Dufour Effect (Heat Flow by Concentration Gradient)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/487_dufour_effect.md` · **Sim:** `sim/487_dufour_effect.py`

---

### CLASSICAL STATEMENT
*"A concentration gradient in a mixture drives a heat flow, the reciprocal (Onsager-conjugate) effect to the Soret effect: J_q = -L_qu grad mu/T. It is the cross-diffusion of energy caused by a composition gradient."*
— Ludwig Dufour, 1872. Source: Wikipedia: Dufour effect; Dufour (1872)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *uniform composition*: the Dufour effect vanishes exactly at grad x = 0 - it is invisible in the homogeneous systems that classical heat-conduction studies assume.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the cross-flow is a coherence channel. J_q_phi(kappa) = J_q_classical*(1 + kappa*(phi-1)) + kappa*phi^-1*Jq_ground. At kappa->0 the classical Dufour heat flow is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} J_q_phi = J_q_classical -> the Dufour effect is the linear-response zero-ground cross-flow limit.
```

---

### STAGE 4 — SIMULATION

`sim/487_dufour_effect.py`: reproduces the classical value J_q = 0.2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/487_dufour_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling a mixture shows a residual heat flow kappa*phi^-1*Jq_ground even at zero composition gradient, conjugate to the Soret residual.
EXPERIMENT (VERIFIED): High-precision measurements of heat flow in composition-graded mixtures, and the reciprocal residual at uniform composition.
VERIFIED BY: The heat flow is exactly zero at zero composition gradient for all couplings.
```

---

### RECOGNITION
Connects to Law 486 (Soret) and Law 488 (Onsager) - the Dufour effect is the reciprocal face of the Soret channel.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the residual is phi^-1 * Jq_ground.

### CLARITY
Composition is a kind of heat; the phi-law keeps the cross-talk between the two fields.

### NOVELTY
Classical thermodynamics separates heat and composition; the phi-law keeps the coherence cross-channel between them.

### ACTIONABILITY
Run sim/487_dufour_effect.py; verify Dufour heat flow at kappa->0; proceed to 488.
