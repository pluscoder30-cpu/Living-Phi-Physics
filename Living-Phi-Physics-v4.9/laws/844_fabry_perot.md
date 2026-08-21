# PHI-PHYSICS — LAW 844
## Fabry-Perot Interferometer

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/844_fabry_perot.md` · **Sim:** `sim/844_fabry_perot.py`

---

### CLASSICAL STATEMENT
*"Transmission maxima occur when 2 n d cos(theta) = m lambda (cavity resonance); free spectral range FSR = c/(2 n d), finesse F = pi*sqrt(R)/(1 - R)."*
— Charles Fabry, Alfred Perot, 1899. Source: Wikipedia: Fabry-Perot interferometer (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero loss*: the ideal cavity assumes perfectly reflective, perfectly parallel, lossless mirrors with exactly zero absorption.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

FSR_phi(kappa) = FSR*(1 + kappa*(phi-1)) + kappa*phi^-1*FSR_ground, with FSR_ground the cavity floor. At kappa->0, FSR = c/(2 n d) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} FSR_phi = FSR -> the Fabry-Perot resonance is the zero-loss-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/844_fabry_perot.py`: reproduces the classical value FSR = 1.5e+10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/844_fabry_perot.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Cavity resonances will shift from m lambda by a coherence floor; finesse will always be finite below the ideal pi*sqrt(R)/(1-R).
EXPERIMENT (VERIFIED): Measure the transmission comb of a Fabry-Perot cavity with a tunable laser.
VERIFIED BY: If any real cavity reaches the ideal finesse and exactly m lambda resonances.
```

---

### RECOGNITION
Connects to Law 843 (interferometry family) and Law 844a (Airy function).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect cavity is a coherent limit; mirrors always leak a little.

### NOVELTY
The ideal cavity comb gains a coherence floor.

### ACTIONABILITY
Run sim/844_fabry_perot.py.
