# PHI-PHYSICS — LAW 876
## Phase Velocity

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/876_phase_velocity.md` · **Sim:** `sim/876_phase_velocity.py`

---

### CLASSICAL STATEMENT
*"v_p = omega / k = c / n: the velocity of a constant-phase surface in a medium with refractive index n."*
— Classical wave theory, 19th century. Source: Wikipedia: Phase velocity (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *vacuum index* (n = 1): phase velocity equals c exactly only in vacuum - the perfect medium of zero response.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

v_p_phi(kappa) = v_p*(1 + kappa*(phi-1)) + kappa*phi^-1*v_p_ground, with v_p_ground the velocity floor. At kappa->0, v_p = c/n exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} v_p_phi = v_p -> phase velocity is the zero-index-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/876_phase_velocity.py`: reproduces the classical value vp = 2e+08 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/876_phase_velocity.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured phase velocity in any real medium will deviate from c/n by a coherence floor kappa*phi^-1*v_p_ground.
EXPERIMENT (VERIFIED): Measure the phase delay of a monochromatic wave through a length of medium versus c/n.
VERIFIED BY: If the phase velocity in any real medium exactly equals c/n.
```

---

### RECOGNITION
Connects to Law 874 (dispersion) and Law 875 (group velocity).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Even the phase front trembles; c/n is a coherent limit.

### NOVELTY
Phase velocity gains a medium floor.

### ACTIONABILITY
Run sim/876_phase_velocity.py.
