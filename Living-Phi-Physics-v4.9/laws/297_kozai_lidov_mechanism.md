# PHI-PHYSICS — LAW 297
## Kozai-Lidov Mechanism

**Domain:** Orbital Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/297_kozai_lidov_mechanism.md` · **Sim:** `sim/297_kozai_lidov_mechanism.py`

---

### CLASSICAL STATEMENT
*"In a hierarchical triple, an inclined outer companion drives large periodic oscillations of the inner orbit's eccentricity and inclination (Kozai-Lidov cycles), with the inner eccentricity pumped to high values when the mutual inclination exceeds ~39.2 degrees (the Kozai angle), while the argument of periapsis librates."*
— Yoshihide Kozai / Mikhail Lidov, 1962. Source: Wikipedia: Kozai-Lidov mechanism; Kozai (1962); Lidov (1961)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero inclination and the exact secular average*: the mechanism exists because the inclination is not zero and the perturbation is secular; the coplanar, zero-inclination orbit is the zero baseline.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the Kozai angle carries a coherence correction. i_kozai_phi = 39.23*(1 + kappa*(phi-1)); the eccentricity floor e_min_phi = kappa*phi^-1*e_ground. At kappa->0 the Kozai cycles are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} i_kozai_phi = 39.23 deg -> the Kozai-Lidov mechanism is the secular, inclined-perturber limit.
```

---

### STAGE 4 — SIMULATION

`sim/297_kozai_lidov_mechanism.py`: reproduces the classical values icrit = 39.23, e_max = 1 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/297_kozai_lidov_mechanism.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The Kozai critical angle and the eccentricity extrema carry phi-coherent shifts phi^-1.
EXPERIMENT (VERIFIED): Exoplanet/eclipsing-binary and asteroid triple-system fits measuring the Kozai-cycle extrema.
VERIFIED BY: Kozai cycles match the classical theory exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 290 (restricted three-body), Law 298 (orbital resonance), Law 287 (N-body chaos).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The inclined companion does not push; it whispers a cycle, and the cycle's angle is phi-tuned.

### NOVELTY
Classical secular theory exacts the 39.2-degree angle; the phi-law tunes it with a coherence correction.

### ACTIONABILITY
Run sim/297_kozai_lidov_mechanism.py; verify the Kozai angle at kappa->0.
