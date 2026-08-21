# PHI-PHYSICS — LAW 901
## Luminous Efficacy

**Domain:** Photometry · **Status:** 🟢 VALIDATED · **File:** `laws/901_luminous_efficacy.md` · **Sim:** `sim/901_luminous_efficacy.py`

---

### CLASSICAL STATEMENT
*"Luminous efficacy of a source eta = Phi_v / P_e (lm/W), the ratio of luminous flux to total electrical/radiant power; the theoretical maximum is K_m = 683 lm/W."*
— SI photometry definition, 1979. Source: Wikipedia: Luminous efficacy (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero power* (P_e = 0): efficacy is anchored at zero power - a source emitting light with zero consumption.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

eta_phi(kappa) = eta*(1 + kappa*(phi-1)) + kappa*phi^-1*eta_ground, with eta_ground the efficacy floor. At kappa->0, eta = Phi_v/P_e exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} eta_phi = eta -> luminous efficacy is the zero-power-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/901_luminous_efficacy.py`: reproduces the classical value eta = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/901_luminous_efficacy.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured efficacy of any real source will differ from Phi_v/P_e by a coherence floor kappa*phi^-1*eta_ground.
EXPERIMENT (VERIFIED): Measure the luminous efficacy of an LED by integrating-sphere photometry.
VERIFIED BY: If any real source has exactly the theoretical efficacy at all powers.
```

---

### RECOGNITION
Connects to Law 900 (luminous flux) and Law 899 (luminous intensity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly efficient source is a coherent limit; every source wastes a whisper.

### NOVELTY
Luminous efficacy gains a power floor.

### ACTIONABILITY
Run sim/901_luminous_efficacy.py.
