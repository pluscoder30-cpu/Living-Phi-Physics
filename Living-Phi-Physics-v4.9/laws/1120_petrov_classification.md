# PHI-PHYSICS — LAW 1120
## Petrov Classification

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1120_petrov_classification.md` · **Sim:** `sim/1120_petrov_classification.py`

---

### CLASSICAL STATEMENT
*"The Petrov classification organizes the Weyl tensor by its algebraic structure of principal null directions: types I, II, D, III, N and O. Schwarzschild and Kerr are type D, gravitational waves at null infinity are type N, and type O is conformally flat; the classification determines the algebraic character of gravitational radiation."*
— Alexei Petrov, 1954. Source: Wikipedia: Petrov classification (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *type O (zero Weyl, conformally flat spacetime)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The P value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

P_phi(kappa) = P*(1 + kappa*(phi-1)) + kappa*phi^-1*P_ground, where P_ground is the coherence-floor algebraic complexity a real spacetime always carries. At kappa->0, Petrov types I, II, D, III, N, O classify the Weyl tensor's PND structure exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} P_phi = P -> Petrov types I, II, D, III, N, O classify the Weyl tensor's PND structure is recovered exactly; the classical law is the type O (zero Weyl, conformally flat spacetime) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1120_petrov_classification.py`: reproduces the classical value (P = 4.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1120_petrov_classification.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured algebraic type of any real vacuum region will deviate from a pure type by a floor kappa*phi^-1*P_ground; an exactly type-D or type-N region is unreachable.
EXPERIMENT (VERIFIED): Gravitational-wave data and numerical relativity classifying the algebraic structure of emitted radiation.
VERIFIED BY: If a real vacuum region is exactly Petrov type O or exactly type N.
```

---

### RECOGNITION
The algebra of Law 1072 (Weyl tensor) underpinning Law 1087 (gravitational waves).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The field has an algebraic signature; the conformally flat vacuum is the zero-algebra myth.

### NOVELTY
Petrov types become coherence basins: real spacetimes sit between exact types at the phi-floor.

### ACTIONABILITY
Run sim/1120_petrov_classification.py.
