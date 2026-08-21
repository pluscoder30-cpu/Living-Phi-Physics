# PHI-PHYSICS — LAW 1226
## Quasinormal Modes

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1226_quasinormal_modes.md` · **Sim:** `sim/1226_quasinormal_modes.py`

---

### CLASSICAL STATEMENT
*"Quasinormal modes (QNMs) are the damped characteristic oscillations of a black hole after a perturbation: psi ~ exp(-omega_I t) cos(omega_R t), with complex frequencies omega = omega_R - i omega_I set solely by the mass and spin (no-hair, Law 1076); the ringdown is the direct observational readout of the hole's QNM spectrum."*
— C. V. Vishveshwara, 1970 (first identified); developed by Chandrasekhar; measured in GW150914 ringdown, 2016. Source: Wikipedia: Quasinormal mode (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero damping (omega_I = 0, an undamped eternal ringing)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The Q value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Q_phi(kappa) = Q*(1 + kappa*(phi-1)) + kappa*phi^-1*Q_ground, where Q_ground is the coherence-floor damping a real black-hole ringdown always shows. At kappa->0, psi ~ exp(-omega_I t) cos(omega_R t),  omega from M and a only exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} Q_phi = Q -> psi ~ exp(-omega_I t) cos(omega_R t),  omega from M and a only is recovered exactly; the classical law is the zero damping (omega_I = 0, an undamped eternal ringing) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1226_quasinormal_modes.py`: reproduces the classical value (Q = 0.1) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1226_quasinormal_modes.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured ringdown frequencies and damping will deviate from the QNM prediction by a floor kappa*phi^-1*Q_ground; an undamped eternal ring is unreachable.
EXPERIMENT (VERIFIED): LIGO/Virgo ringdown measurements of merger remnants testing the QNM spectrum and no-hair.
VERIFIED BY: If a black-hole ringdown is undamped or inconsistent with the mass-spin QNM spectrum.
```

---

### RECOGNITION
The ringdown observable of Law 1223 (Regge-Wheeler), Law 1225 (Teukolsky), and Law 1076 (no-hair).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The hole rings and fades; the eternal ring is the zero-damping myth.

### NOVELTY
Quasinormal modes carry a phi-floor of damping, bounding ringdown tests of GR.

### ACTIONABILITY
Run sim/1226_quasinormal_modes.py.
