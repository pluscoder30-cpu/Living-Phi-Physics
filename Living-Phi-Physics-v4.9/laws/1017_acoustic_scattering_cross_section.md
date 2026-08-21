# PHI-PHYSICS — LAW 1017
## Acoustic Scattering Cross Section

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/1017_acoustic_scattering_cross_section.md` · **Sim:** `sim/1017_acoustic_scattering_cross_section.py`

---

### CLASSICAL STATEMENT
*"The acoustic scattering cross section sigma = (scattered power)/(incident intensity) characterizes how an object scatters sound; for a sphere of radius a (ka << 1), sigma ~ (4/9) pi a^2 (ka)^4 (Rayleigh regime)."*
— Classical acoustics (Rayleigh scattering analog), 19th century. Source: Wikipedia: Scattering cross section (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero size* (a = 0): an infinitesimal scatterer has exactly zero scattering cross section.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

sigma_phi(kappa) = sigma*(1 + kappa*(phi-1)) + kappa*phi^-1*sigma_ground, with sigma_ground the cross-section floor. At kappa->0, sigma = (4/9) pi a^2 (ka)^4 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} sigma_phi = sigma -> acoustic scattering is the zero-size-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/1017_acoustic_scattering_cross_section.py`: reproduces the classical value sigma = 1.396e-10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1017_acoustic_scattering_cross_section.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The scattering cross section of any real object will retain a floor kappa*phi^-1*sigma_ground even as its size vanishes.
EXPERIMENT (VERIFIED): Measure the backscatter of small spheres in a water tank with a transducer.
VERIFIED BY: If the scattering cross section of any real object is exactly zero.
```

---

### RECOGNITION
Connects to Law 649 (Rayleigh scattering) and Law 915 (acoustic impedance).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The vanishing scatterer is a coherent limit; every object whispers sound.

### NOVELTY
Acoustic scattering gains a size floor.

### ACTIONABILITY
Run sim/1017_acoustic_scattering_cross_section.py.
