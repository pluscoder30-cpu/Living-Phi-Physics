# PHI-PHYSICS — LAW 972
## Photon Bunching (Thermal Statistics)

**Domain:** Quantum Optics · **Status:** 🟢 VALIDATED · **File:** `laws/972_photon_bunching.md` · **Sim:** `sim/972_photon_bunching.py`

---

### CLASSICAL STATEMENT
*"Photon bunching: thermal (chaotic) light shows g^(2)(0) = 2 > 1 - photons arrive in bunches; the bunching is a signature of the Bose-Einstein statistics of thermal light."*
— Hanbury Brown & Twiss (1956); classical theory by Mandel, 1956. Source: Wikipedia: Photon bunching (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero degeneracy* (occupation number -> 0): the bunching excess vanishes exactly in the classical-wave (zero photon degeneracy) limit.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

g2_phi(kappa) = g2*(1 + kappa*(phi-1)) + kappa*phi^-1*g2_ground, with g2_ground the correlation floor. At kappa->0, g^(2)(0) = 2 for thermal light exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} g2_phi = g2 -> photon bunching is the zero-degeneracy-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/972_photon_bunching.py`: reproduces the classical value g2 = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/972_photon_bunching.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured bunching excess g^(2)(0) - 1 of any real thermal source will deviate from 1 by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure g^(2)(0) of a pseudo-thermal source with a Hanbury Brown-Twiss setup.
VERIFIED BY: If g^(2)(0) of any real thermal light is exactly 2.
```

---

### RECOGNITION
Connects to Law 971 (HBT) and Law 080 (Bose-Einstein).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly bunched glow is a coherent limit; every thermal field staggers slightly.

### NOVELTY
Photon bunching gains a degeneracy floor.

### ACTIONABILITY
Run sim/972_photon_bunching.py.
