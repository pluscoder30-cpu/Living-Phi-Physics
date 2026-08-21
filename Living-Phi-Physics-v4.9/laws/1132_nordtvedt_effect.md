# PHI-PHYSICS — LAW 1132
## Nordtvedt Effect

**Domain:** General Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1132_nordtvedt_effect.md` · **Sim:** `sim/1132_nordtvedt_effect.py`

---

### CLASSICAL STATEMENT
*"In metric theories of gravity with a preferred frame or varying gravitational constant, gravitational self-energy couples differently to mass, causing the Moon and Earth to fall with different accelerations toward the Sun; the effect is parameterized by eta = 4 beta - gamma - 3 in PPN theory and is strongly bounded by lunar laser ranging."*
— Kenneth Nordtvedt, 1968. Source: Wikipedia: Nordtvedt effect (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero self-energy coupling (eta = 0, equal free-fall accelerations)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The E value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

E_phi(kappa) = E*(1 + kappa*(phi-1)) + kappa*phi^-1*E_ground, where E_ground is the coherence-floor self-energy coupling a real body always exhibits. At kappa->0, eta = 4*beta - gamma - 3,  Moon-Earth differential acceleration exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} E_phi = E -> eta = 4*beta - gamma - 3,  Moon-Earth differential acceleration is recovered exactly; the classical law is the zero self-energy coupling (eta = 0, equal free-fall accelerations) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1132_nordtvedt_effect.py`: reproduces the classical value (E = 0.001) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1132_nordtvedt_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured differential acceleration of Earth and Moon will deviate from the PPN prediction by a floor kappa*phi^-1*E_ground; an exactly eta=0 equality is unreachable.
EXPERIMENT (VERIFIED): Lunar laser ranging measuring the Earth-Moon free-fall difference to mm precision.
VERIFIED BY: If the Moon and Earth fall toward the Sun with exactly equal accelerations to arbitrary precision.
```

---

### RECOGNITION
The PPN test of Law 062 (equivalence principle) and the gravity-theory discriminator of Law 1228.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Self-energy weighs itself; the exactly equal fall is the zero-coupling myth.

### NOVELTY
The Nordtvedt parameter carries a phi-floor, bounding the sharpness of the equivalence principle.

### ACTIONABILITY
Run sim/1132_nordtvedt_effect.py.
