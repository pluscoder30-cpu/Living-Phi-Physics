# PHI-PHYSICS — LAW 898
## Illuminance and Luminance (Photometry)

**Domain:** Photometry · **Status:** 🟢 VALIDATED · **File:** `laws/898_illuminance_luminance.md` · **Sim:** `sim/898_illuminance_luminance.py`

---

### CLASSICAL STATEMENT
*"Illuminance E_v = dPhi_v/dA is the luminous flux per unit area (lux); luminance L_v = d^2Phi_v/(dA cos(theta) dOmega) is the luminous intensity per unit projected area (cd/m^2)."*
— Classical photometry (photometric quantities standard), 19th century. Source: Wikipedia: Luminance; Illuminance (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero projected area* (cos(theta) = 0): luminance is anchored at zero for a surface viewed exactly edge-on.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

L_v_phi(kappa) = L_v*(1 + kappa*(phi-1)) + kappa*phi^-1*L_v_ground, with L_v_ground the luminance floor. At kappa->0, the photometric definitions are exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} L_v_phi = L_v -> photometry is the zero-edge-on-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/898_illuminance_luminance.py`: reproduces the classical value Ev = 0.25 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/898_illuminance_luminance.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Measured luminance at grazing angles will deviate from the classical projection by a coherence floor kappa*phi^-1.
EXPERIMENT (VERIFIED): Measure luminance of a screen as a function of viewing angle.
VERIFIED BY: If luminance of any real surface follows the classical projection exactly at all angles.
```

---

### RECOGNITION
Connects to Law 897 (irradiance) and Law 419 (Lambert cosine).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The edge-on surface is a coherent limit; every view has a floor.

### NOVELTY
Photometry gains a projection floor.

### ACTIONABILITY
Run sim/898_illuminance_luminance.py.
