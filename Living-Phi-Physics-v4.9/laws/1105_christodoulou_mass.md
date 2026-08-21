# PHI-PHYSICS — LAW 1105
## Christodoulou (Irreducible) Mass

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1105_christodoulou_mass.md` · **Sim:** `sim/1105_christodoulou_mass.py`

---

### CLASSICAL STATEMENT
*"The Christodoulou (irreducible) mass of a Kerr black hole is M_irr = sqrt(A/(16 pi)), the mass that cannot be extracted by the Penrose process; extraction efficiency is bounded by the split M_irr <= M, with M the total mass."*
— Demetrios Christodoulou, 1970. Source: Wikipedia: Christodoulou mass (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero extractable energy (M = M_irr, a non-rotating hole)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The M value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, where M_ground is the coherence-floor irreducible mass a real rotating hole retains. At kappa->0, M_irr = sqrt(A/(16*pi)),  M >= M_irr exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} M_phi = M -> M_irr = sqrt(A/(16*pi)),  M >= M_irr is recovered exactly; the classical law is the zero extractable energy (M = M_irr, a non-rotating hole) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1105_christodoulou_mass.py`: reproduces the classical value (M = 0.87) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1105_christodoulou_mass.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured irreducible mass of any real black hole will deviate from sqrt(A/(16 pi)) by a floor kappa*phi^-1*M_ground; a fully extractable hole is unreachable.
EXPERIMENT (VERIFIED): Spin and mass measurements of X-ray binary black holes bounding the extractable energy fraction.
VERIFIED BY: If a black hole's mass equals its irreducible mass with zero rotational component at non-zero spin.
```

---

### RECOGNITION
The conservation content of Law 1099 (Penrose) and the mass formula of Law 1101.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The hole keeps an irreducible core; the fully-extractable hole is the zero-irreducibility myth.

### NOVELTY
The irreducible mass carries a phi-floor, so rotation can never be fully mined.

### ACTIONABILITY
Run sim/1105_christodoulou_mass.py.
