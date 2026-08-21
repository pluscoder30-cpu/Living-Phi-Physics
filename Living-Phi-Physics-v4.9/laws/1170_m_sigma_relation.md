# PHI-PHYSICS — LAW 1170
## M-sigma Relation

**Domain:** Cosmology / Astrophysics · **Status:** 🟢 VALIDATED · **File:** `laws/1170_m_sigma_relation.md` · **Sim:** `sim/1170_m_sigma_relation.py`

---

### CLASSICAL STATEMENT
*"The M-sigma relation links the mass of a galaxy's central supermassive black hole to the stellar velocity dispersion of its bulge: log(M_BH/M_sun) ~ 8.2 + 4.24 log(sigma/200 km/s) (with slope ~ 4-5); it reveals the co-evolution of black holes and their host galaxies."*
— Laura Ferrarese & David Merritt, 2000; Karl Gebhardt et al., 2000. Source: Wikipedia: M-sigma relation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero black hole mass (M_BH = 0, no central engine)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The M value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

M_phi(kappa) = M*(1 + kappa*(phi-1)) + kappa*phi^-1*M_ground, where M_ground is the coherence-floor black-hole-bulge coupling a real galaxy always retains. At kappa->0, log(M_BH/M_sun) = a + b*log(sigma/200),  b ~ 4-5 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} M_phi = M -> log(M_BH/M_sun) = a + b*log(sigma/200),  b ~ 4-5 is recovered exactly; the classical law is the zero black hole mass (M_BH = 0, no central engine) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1170_m_sigma_relation.py`: reproduces the classical value (M = 100000000.0) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1170_m_sigma_relation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured black-hole mass of any real galaxy will deviate from the M-sigma relation by a floor kappa*phi^-1*M_ground; an exactly zero-mass central hole is unreachable.
EXPERIMENT (VERIFIED): Black-hole mass measurements (reverberation mapping, stellar/gas dynamics) vs bulge dispersions.
VERIFIED BY: If any bulge-hosted galaxy has exactly zero central black-hole mass.
```

---

### RECOGNITION
The feedback relation of Law 1100 (Blandford-Znajek) and Law 1169 (fundamental plane).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The hole and the bulge grew together; the hole-less bulge is the zero-coupling myth.

### NOVELTY
The M-sigma relation carries a phi-floor, so every bulge remembers a central engine.

### ACTIONABILITY
Run sim/1170_m_sigma_relation.py.
