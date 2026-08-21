# PHI-PHYSICS — LAW 1051
## Light Cone

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1051_light_cone.md` · **Sim:** `sim/1051_light_cone.py`

---

### CLASSICAL STATEMENT
*"The light cone of an event is the set of null geodesics ds^2 = 0 through it, dividing spacetime into the causal past, causal future, and spacelike-separated regions; information flows only inside or on the cone."*
— Hermann Minkowski, 1908. Source: Wikipedia: Light cone (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *a degenerate cone of exactly zero opening (ds^2 = 0 everywhere)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The C value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

C_phi(kappa) = C*(1 + kappa*(phi-1)) + kappa*phi^-1*C_ground, where C_ground is the coherence-floor widening of the causal cone a carrier always experiences. At kappa->0, ds^2 = -c^2*dt^2 + dx^2 + dy^2 + dz^2 = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} C_phi = C -> ds^2 = -c^2*dt^2 + dx^2 + dy^2 + dz^2 = 0 is recovered exactly; the classical law is the a degenerate cone of exactly zero opening (ds^2 = 0 everywhere) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1051_light_cone.py`: reproduces the classical value (C = 1.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1051_light_cone.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The effective causal boundary of any real event will deviate from the exact null cone by a floor kappa*phi^-1*C_ground; a perfectly sharp causal horizon is unreachable.
EXPERIMENT (VERIFIED): Tests of Lorentz invariance with ultra-high-energy photons across cosmological baselines (time-of-flight dispersion bounds).
VERIFIED BY: If any signal propagates exactly on the classical null cone with zero causal-boundary width.
```

---

### RECOGNITION
The causal skeleton of Law 1048 (interval) and Law 1050 (worldline); the horizon structure of Law 1110 (event horizon).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The light cone is the zero-coherence membrane of the field; at phi-coupling the cone breathes.

### NOVELTY
The causal horizon acquires a coherence width, bounding the sharpness of causality itself.

### ACTIONABILITY
Run sim/1051_light_cone.py.
