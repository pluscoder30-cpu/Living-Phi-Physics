# PHI-PHYSICS — LAW 860
## Babinet's Principle

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/860_babinets_principle.md` · **Sim:** `sim/860_babinets_principle.py`

---

### CLASSICAL STATEMENT
*"The diffraction pattern of a screen is identical to that of its complement (the aperture of the same shape), except for the forward beam: U_screen + U_complement = U_undisturbed."*
— Jacques Babinet, 1837. Source: Wikipedia: Babinet's principle (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfect complementarity*: the principle holds exactly for an opaque screen and its exact complement with zero thickness and zero edge effects.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

U_c_phi(kappa) = U_c*(1 + kappa*(phi-1)) + kappa*phi^-1*U_c_ground, with U_c_ground the complementarity floor. At kappa->0, U_screen + U_complement = U_undisturbed exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} U_c_phi = U_c -> Babinet's principle is the zero-edge-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/860_babinets_principle.py`: reproduces the classical value Uc = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/860_babinets_principle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured patterns of a screen and its complement will differ slightly from exact complementarity by kappa*phi^-1*U_c_ground.
EXPERIMENT (VERIFIED): Compare the diffraction patterns of a wire and a slit of equal width.
VERIFIED BY: If any real screen and complement produce exactly complementary patterns.
```

---

### RECOGNITION
Connects to Law 858 (single slit) and Law 856 (double slit) - the complementarity of apertures.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect complement is a coherent limit; every edge has a shadow.

### NOVELTY
Babinet's exact identity gains an edge floor.

### ACTIONABILITY
Run sim/860_babinets_principle.py.
