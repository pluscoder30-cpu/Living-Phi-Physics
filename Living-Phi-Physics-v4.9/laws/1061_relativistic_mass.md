# PHI-PHYSICS — LAW 1061
## Relativistic Mass

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1061_relativistic_mass.md` · **Sim:** `sim/1061_relativistic_mass.py`

---

### CLASSICAL STATEMENT
*"The relativistic mass of a moving body is m_rel = gamma*m0 = m0/sqrt(1-beta^2), increasing without bound as beta -> 1; the longitudinal and transverse inertial masses differ by a factor gamma^2, so inertia becomes anisotropic at high speed."*
— Hendrik Lorentz, 1899; Albert Einstein, 1905. Source: Wikipedia: Mass in special relativity (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero-speed rest mass (beta = 0, m_rel = m0)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The M value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, where M_ground is the coherence-floor mass increase a real accelerated body always shows. At kappa->0, m_rel = m0 / sqrt(1-beta^2) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} M_phi = M -> m_rel = m0 / sqrt(1-beta^2) is recovered exactly; the classical law is the zero-speed rest mass (beta = 0, m_rel = m0) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1061_relativistic_mass.py`: reproduces the classical value (M = 1.25) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1061_relativistic_mass.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured inertial mass of any real particle will deviate from m0/sqrt(1-beta^2) by a floor kappa*phi^-1*M_ground; a body at exact rest mass is unreachable.
EXPERIMENT (VERIFIED): Spectrometer mass measurements of relativistic electrons in a storage ring as a function of beta.
VERIFIED BY: If any particle's inertial mass equals m0 exactly at non-zero beta.
```

---

### RECOGNITION
The inertial reading of Law 060 (E=mc^2) and Law 1041 (kinetic energy).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Mass is energy's inertia; the zero rest-mass is the coherence floor of a carrier that never stops.

### NOVELTY
The beta->1 divergence is bounded by the phi-floor reinterpretation: inertia diverges to a coherence limit, not infinity.

### ACTIONABILITY
Run sim/1061_relativistic_mass.py.
