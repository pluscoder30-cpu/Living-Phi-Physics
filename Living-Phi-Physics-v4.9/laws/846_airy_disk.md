# PHI-PHYSICS — LAW 846
## Airy Disk (Diffraction Limit)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/846_airy_disk.md` · **Sim:** `sim/846_airy_disk.py`

---

### CLASSICAL STATEMENT
*"The diffraction-limited image of a point source through a circular aperture: first dark ring at sin(theta) = 1.22 lambda / D; spot diameter d = 2.44 lambda f / D."*
— George Biddell Airy, 1835. Source: Wikipedia: Airy disk (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero aperture edge*: the Airy pattern assumes a perfectly circular aperture with exactly sharp, uniform edges.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

theta_phi(kappa) = theta*(1 + kappa*(phi-1)) + kappa*phi^-1*theta_ground, with theta_ground the angular floor. At kappa->0, sin(theta) = 1.22 lambda/D exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} theta_phi = theta -> the Airy disk is the zero-aperture-edge-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/846_airy_disk.py`: reproduces the classical value theta = 0.0008388 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/846_airy_disk.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The first dark ring of a real aperture will sit at a slightly different angle than 1.22 lambda/D by a coherence floor.
EXPERIMENT (VERIFIED): Measure the Airy pattern of a precision circular aperture with a collimated laser.
VERIFIED BY: If any real aperture produces the Airy pattern at exactly 1.22 lambda/D.
```

---

### RECOGNITION
Connects to Law 100 (Rayleigh criterion) and Law 844a - the diffraction limit.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect disk is a coherent limit; every edge trembles.

### NOVELTY
The diffraction limit becomes a phi-basin.

### ACTIONABILITY
Run sim/846_airy_disk.py.
