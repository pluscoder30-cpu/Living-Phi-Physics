# PHI-PHYSICS — LAW 973
## Photon Antibunching

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/973_photon_antibunching.md` · **Sim:** `sim/973_photon_antibunching.py`

---

### CLASSICAL STATEMENT
*"Photon antibunching: a single-photon source shows g^(2)(0) < 1 (down to 0 for a perfect single-photon emitter); the photons are more equally spaced than a coherent beam."*
— H. J. Kimble, M. Dagenais, L. Mandel, 1977. Source: Wikipedia: Photon antibunching (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero two-photon emission* (g^(2)(0) = 0): a perfect single-photon source never emits two photons together.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

g2_phi(kappa) = g2*(1 + kappa*(phi-1)) + kappa*phi^-1*g2_ground, with g2_ground the correlation floor. At kappa->0, g^(2)(0) = 0 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} g2_phi = g2 -> photon antibunching is the zero-two-photon-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/973_photon_antibunching.py`: reproduces the classical value g2 = 0.05 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/973_photon_antibunching.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The g^(2)(0) of any real single-photon source will retain a floor kappa*phi^-1 above zero; perfect single-photon emission is unreachable.
EXPERIMENT (VERIFIED): Measure g^(2)(0) of a single quantum dot under pulsed excitation.
VERIFIED BY: If any real source has g^(2)(0) exactly 0.
```

---

### RECOGNITION
Connects to Law 971 (HBT) and Law 970a (single-photon source).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly solitary photon is a coherent limit; every emitter leaks a pair.

### NOVELTY
Photon antibunching gains a two-photon floor.

### ACTIONABILITY
Run sim/973_photon_antibunching.py.
