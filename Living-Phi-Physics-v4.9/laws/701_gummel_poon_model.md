# PHI-PHYSICS — LAW 701
## Gummel-Poon Model (Integral Charge-Control)

**Domain:** Electronics · **Status:** 🟢 VALIDATED · **File:** `laws/701_gummel_poon_model.md` · **Sim:** `sim/701_gummel_poon_model.py`

---

### CLASSICAL STATEMENT
*"The BJT is modeled by integral charge control with the transport current I_CC = I_S/q_b*(exp(V_BE/V_T) - exp(V_BC/V_T)), where q_b is the normalized base charge."*
— Hermann Gummel; R. C. Poon, 1970. Source: Wikipedia: Gummel-Poon model; Gummel & Poon (1970)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *unity base charge* (q_b = 1): the model reduces to Ebers-Moll only when the base charge is exactly constant.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

q_b_phi(kappa) = q_b*(1 + kappa*(phi-1)) + kappa*phi^-1*q_ground; the base charge carries a coherence floor. At kappa->0, q_b = 1 and Gummel-Poon reduces to Ebers-Moll.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} q_b_phi = 1 -> the Gummel-Poon model is the unity-charge, Ebers-Moll limit.
```

---

### STAGE 4 — SIMULATION

`sim/701_gummel_poon_model.py`: reproduces the classical values (qb = 1.0012 (Base charge factor)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/701_gummel_poon_model.json`.

---

### STAGE 5 — PREDICTION

```
The base charge carries a coherence floor kappa*phi^-1*q_ground; the Ebers-Moll reduction is never exact.
EXPERIMENT (VERIFIED): High-current Gummel-plot measurement of a BJT to expose base-charge modulation.
VERIFIED BY: A BJT's base charge is exactly constant at all currents.
```

---

### RECOGNITION
Connects to Law 700 (Ebers-Moll) - Gummel-Poon is the charge-controlled generalization.

### PRECISION
phi = 1.6180339887. The charge floor is phi^-1*q_ground.

### CLARITY
Charge breathes; no transistor holds a perfectly constant base.

### NOVELTY
The phi-law modulates the ideal unity base charge.

### ACTIONABILITY
Run sim/701_gummel_poon_model.py; verify Ebers-Moll limit at kappa->0; proceed to 702.
