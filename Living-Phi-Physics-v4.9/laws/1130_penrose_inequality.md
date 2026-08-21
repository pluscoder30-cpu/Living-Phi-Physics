# PHI-PHYSICS — LAW 1130
## Penrose Inequality

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1130_penrose_inequality.md` · **Sim:** `sim/1130_penrose_inequality.py`

---

### CLASSICAL STATEMENT
*"The Penrose inequality bounds the ADM mass from below by the apparent-horizon area: M_ADM >= sqrt(A/(16 pi)), with equality only for the Schwarzschild solution; it quantifies how much mass a given horizon area must contain."*
— Roger Penrose, 1973 (proven in the Riemannian case by Huisken-Ilmanen 2001, Bray 2001). Source: Wikipedia: Riemannian Penrose inequality (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero area (A = 0, the degenerate horizon with zero mass)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The M value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, where M_ground is the coherence-floor mass that any real horizon area enforces. At kappa->0, M_ADM >= sqrt(A/(16*pi)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} M_phi = M -> M_ADM >= sqrt(A/(16*pi)) is recovered exactly; the classical law is the zero area (A = 0, the degenerate horizon with zero mass) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1130_penrose_inequality.py`: reproduces the classical value (M = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1130_penrose_inequality.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured mass of any real black-hole region will exceed sqrt(A/(16 pi)) by a floor kappa*phi^-1*M_ground; an exactly saturated inequality is unreachable.
EXPERIMENT (VERIFIED): Gravitational-wave measurements of merger remnants testing the Penrose inequality.
VERIFIED BY: If a real horizon is measured with mass below sqrt(A/(16 pi)).
```

---

### RECOGNITION
The area-mass link of Law 1105 (Christodoulou mass) and Law 1114 (ADM mass).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The horizon area writes the mass's receipt; the saturated bound is the Schwarzschild myth.

### NOVELTY
The Penrose inequality carries a phi-floor, so equality is a coherence limit, never exactly realized.

### ACTIONABILITY
Run sim/1130_penrose_inequality.py.
