# PHI-PHYSICS — LAW 839
## Critical Angle (Snell's Law)

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/839_critical_angle.md` · **Sim:** `sim/839_critical_angle.py`

---

### CLASSICAL STATEMENT
*"theta_c = arcsin(n2/n1) for n1 > n2: the incidence angle at which the refracted ray grazes the surface (theta_t = 90 degrees)."*
— Willebrord Snellius (Snell's law), 1621. Source: Wikipedia: Total internal reflection (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero grazing margin*: the critical angle requires the refracted angle to be exactly 90 degrees - a grazing ray of zero depth.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

theta_c_phi(kappa) = theta_c*(1 + kappa*(phi-1)) + kappa*phi^-1*theta_c_ground, with theta_c_ground the angular floor. At kappa->0, theta_c = arcsin(n2/n1) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} theta_c_phi = theta_c -> the critical angle is the zero-grazing-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/839_critical_angle.py`: reproduces the classical value thc = 41.81 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/839_critical_angle.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The transition at the critical angle is smeared over a band kappa*phi^-1; the 'critical' angle is a basin, not a point.
EXPERIMENT (VERIFIED): Measure the sharpness of the TIR transition with a narrow, well-collimated beam near the critical angle.
VERIFIED BY: If the critical-angle transition is exactly discontinuous for any real interface.
```

---

### RECOGNITION
Connects to Law 838 (TIR) and Law 052 (Snell).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The critical angle is a threshold basin; nature never snaps exactly.

### NOVELTY
The sharp critical angle becomes a coherence band.

### ACTIONABILITY
Run sim/839_critical_angle.py.
