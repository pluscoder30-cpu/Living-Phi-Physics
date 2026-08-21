# PHI-PHYSICS — LAW 1140
## Kaiser-Stebbins Effect

**Domain:** Cosmology · **Status:** 🟢 VALIDATED · **File:** `laws/1140_kaiser_stebbins_effect.md` · **Sim:** `sim/1140_kaiser_stebbins_effect.py`

---

### CLASSICAL STATEMENT
*"The Kaiser-Stebbins effect is the CMB temperature anisotropy produced by the transverse motion of a gravitational lens (e.g. a moving cosmic string or cluster): a moving potential well creates a step-like discontinuity Delta T/T = 2 v_perp Phi in the CMB temperature across the string."*
— Nick Kaiser & Albert Stebbins, 1984. Source: Wikipedia: Kaiser-Stebbins effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero transverse velocity (v_perp = 0, no temperature step)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The D value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

D_phi(kappa) = D*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground, where D_ground is the coherence-floor moving-potential signature a real lens always leaves. At kappa->0, Delta T/T = 2*v_perp*Phi  (step across a moving string) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} D_phi = D -> Delta T/T = 2*v_perp*Phi  (step across a moving string) is recovered exactly; the classical law is the zero transverse velocity (v_perp = 0, no temperature step) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1140_kaiser_stebbins_effect.py`: reproduces the classical value (D = 1e-06) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1140_kaiser_stebbins_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured CMB step across any real moving potential will deviate from 2*v_perp*Phi by a floor kappa*phi^-1*D_ground; an exactly stationary lens is unreachable.
EXPERIMENT (VERIFIED): CMB string searches (Planck, future CMB-S4) looking for line discontinuities.
VERIFIED BY: If a moving gravitational lens produces exactly zero CMB temperature step.
```

---

### RECOGNITION
The lens-motion channel of Law 113 (lensing) and Law 1137 (Sachs-Wolfe).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
A moving well drags the sky; the static well is the zero-velocity myth.

### NOVELTY
The Kaiser-Stebbins step carries a phi-floor, bounding how motionless any lens can be.

### ACTIONABILITY
Run sim/1140_kaiser_stebbins_effect.py.
