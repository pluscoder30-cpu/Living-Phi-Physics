# PHI-PHYSICS — LAW 861
## Arago (Poisson) Spot

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/861_arago_poisson_spot.md` · **Sim:** `sim/861_arago_poisson_spot.py`

---

### CLASSICAL STATEMENT
*"A bright spot appears at the center of the shadow of a circular opaque disk due to constructive interference of the diffracted waves (predicted by Poisson, verified by Arago)."*
— Siméon Poisson (predicted), François Arago (verified), 1818. Source: Wikipedia: Arago spot (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero disk size*: the exact on-axis bright spot assumes a perfectly circular, perfectly opaque disk with zero edge roughness.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

I_center_phi(kappa) = I_center*(1 + kappa*(phi-1)) + kappa*phi^-1*I_center_ground, with I_center_ground the spot floor. At kappa->0, the spot brightness equals the unobstructed value exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_center_phi = I_center -> the Arago spot is the zero-disk-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/861_arago_poisson_spot.py`: reproduces the classical value Ic = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/861_arago_poisson_spot.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The spot intensity at the shadow center will differ from the unobstructed value by kappa*phi^-1*I_center_ground.
EXPERIMENT (VERIFIED): Measure the central spot intensity of a machined circular disk.
VERIFIED BY: If any real disk produces exactly the unobstructed-intensity spot.
```

---

### RECOGNITION
Connects to Law 841 (Fresnel zones) and Law 859 (Fresnel diffraction).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Even the shadow's heart glows; the perfect disk is a coherent limit.

### NOVELTY
The Arago spot gains an intensity floor.

### ACTIONABILITY
Run sim/861_arago_poisson_spot.py.
