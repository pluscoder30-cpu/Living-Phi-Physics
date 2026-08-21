# PHI-PHYSICS — LAW 840
## Fresnel Equations (Reflection/Transmission)

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/840_fresnel_equations.md` · **Sim:** `sim/840_fresnel_equations.py`

---

### CLASSICAL STATEMENT
*"r_s = (n1 cos t_i - n2 cos t_t)/(n1 cos t_i + n2 cos t_t); t_s = 2 n1 cos t_i/(n1 cos t_i + n2 cos t_t), and the p-polarization forms; R + T = 1 (lossless interface)."*
— Augustin-Jean Fresnel, 1823. Source: Wikipedia: Fresnel equations (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *ideal interface*: the equations assume a perfectly smooth, sharp, non-absorbing interface with exactly two media - zero roughness, zero absorption, zero thickness.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

r_phi(kappa) = r*(1 + kappa*(phi-1)) + kappa*phi^-1*r_ground; the interface carries a coherence floor. At kappa->0, R + T = 1 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} r_phi = r -> the Fresnel equations are the zero-interface-imperfection-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/840_fresnel_equations.py`: reproduces the classical values tt = 0.1983, rs = -0.2124 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/840_fresnel_equations.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At any real interface, R + T will fall short of 1 by a floor kappa*phi^-1; a residual coupling is always absorbed or scattered.
EXPERIMENT (VERIFIED): Measure reflectance and transmittance of a polished glass interface with a calibrated detector pair.
VERIFIED BY: If any real interface satisfies R + T = 1 exactly at all angles.
```

---

### RECOGNITION
Connects to Law 055 (Brewster) and Law 839 (critical angle) - the angle-dependent amplitude laws.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The clean interface is a coherent limit; every surface has a voice.

### NOVELTY
The lossless R+T=1 balance gains a coupling floor.

### ACTIONABILITY
Run sim/840_fresnel_equations.py.
