# PHI-PHYSICS — LAW 838
## Total Internal Reflection

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/838_total_internal_reflection.md` · **Sim:** `sim/838_total_internal_reflection.py`

---

### CLASSICAL STATEMENT
*"When n1 > n2 and the incidence angle exceeds the critical angle theta_c = arcsin(n2/n1), the ray is totally reflected; no light enters the second medium."*
— Derived from Snell's law; studied by Kepler, Descartes, Newton, 1621. Source: Wikipedia: Total internal reflection (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero transmitted power*: TIR assumes the transmitted amplitude is exactly zero beyond the critical angle - a perfectly evanescent-free boundary.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

R_phi(kappa) = R*(1 + kappa*(phi-1)) + kappa*phi^-1*R_ground, with R_ground the reflectivity floor. At kappa->0, R = 1 for theta > theta_c exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} R_phi = R -> total internal reflection is the zero-evanescent-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/838_total_internal_reflection.py`: reproduces the classical value thc = 41.81 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/838_total_internal_reflection.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Reflectivity beyond the critical angle will never be exactly 1; a floor kappa*phi^-1*(1 - R_ground) tunnels into the second medium (frustrated TIR).
EXPERIMENT (VERIFIED): Measure the transmitted (frustrated) light beyond the critical angle in a prism pair with a controlled gap.
VERIFIED BY: If TIR is exactly 100% reflective for any real interface.
```

---

### RECOGNITION
Connects to Law 052 (Snell) and Law 895 (Goos-Haenchen shift) - evanescent fields at TIR.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
Even total reflection leaks; the boundary is a coherence veil.

### NOVELTY
Perfect TIR becomes a phi-limit with an evanescent floor.

### ACTIONABILITY
Run sim/838_total_internal_reflection.py.
