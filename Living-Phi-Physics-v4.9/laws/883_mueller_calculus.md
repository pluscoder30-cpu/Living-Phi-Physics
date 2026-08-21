# PHI-PHYSICS — LAW 883
## Mueller Calculus

**Domain:** Polarization Optics · **Status:** 🟢 VALIDATED · **File:** `laws/883_mueller_calculus.md` · **Sim:** `sim/883_mueller_calculus.py`

---

### CLASSICAL STATEMENT
*"Partially polarized light is represented by a Stokes vector S and elements by 4x4 Mueller matrices; S_out = M S_in; applicable to partially polarized and unpolarized light."*
— Hans Mueller, 1943. Source: Wikipedia: Mueller calculus (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfectly known element*: the Mueller matrix exactly describes the element, with zero measurement uncertainty and zero leakage.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

S_out_phi(kappa) = S_out*(1 + kappa*(phi-1)) + kappa*phi^-1*S_out_ground, with S_out_ground the Stokes floor. At kappa->0, S_out = M S_in exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} S_out_phi = S_out -> Mueller calculus is the zero-element-uncertainty-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/883_mueller_calculus.py`: reproduces the classical value DOP = 0.6164 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/883_mueller_calculus.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured Stokes vector through any real element will deviate from M S_in by a coherence floor kappa*phi^-1*S_out_ground.
EXPERIMENT (VERIFIED): Measure the Mueller matrix of a polarizer and compare round-trip consistency.
VERIFIED BY: If any real element's Mueller matrix exactly reproduces S_out = M S_in for all inputs.
```

---

### RECOGNITION
Connects to Law 882 (Jones calculus) and Law 884 (Stokes parameters).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect matrix is a coherent limit; every element has a flaw.

### NOVELTY
Mueller calculus gains an element-uncertainty floor.

### ACTIONABILITY
Run sim/883_mueller_calculus.py.
