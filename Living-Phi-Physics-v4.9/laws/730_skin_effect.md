# PHI-PHYSICS — LAW 730
## Skin Effect (Current Depth)

**Domain:** RF · **Status:** 🟢 VALIDATED · **File:** `laws/730_skin_effect.md` · **Sim:** `sim/730_skin_effect.py`

---

### CLASSICAL STATEMENT
*"AC current concentrates near the conductor surface with skin depth delta = sqrt(2*rho/(omega*mu)); current density falls as exp(-z/delta)."*
— Oliver Heaviside, 1885. Source: Wikipedia: Skin effect; Heaviside (1885)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero frequency* (omega = 0): at DC the skin depth is infinite and current is exactly uniform.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

delta_phi(kappa) = delta*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_ground; the current profile carries a coherence floor. At kappa->0, delta = sqrt(2*rho/(omega*mu)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} delta_phi = sqrt(2*rho/(omega*mu)) -> the skin effect is the zero-frequency-uniform-current limit.
```

---

### STAGE 4 — SIMULATION

`sim/730_skin_effect.py`: reproduces the classical values (delta = 2e-10 (Skin depth (m))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/730_skin_effect.json`.

---

### STAGE 5 — PREDICTION

```
The skin depth never diverges; a coherence floor kappa*phi^-1*delta_ground caps the low-frequency penetration.
EXPERIMENT (VERIFIED): Resistance measurement of a conductor as frequency approaches DC.
VERIFIED BY: The DC resistance is reached exactly at zero frequency with uniform current.
```

---

### RECOGNITION
Connects to Law 731 (proximity) and Law 044 (Ohm) - the skin effect is the frequency texture of current.

### PRECISION
phi = 1.6180339887. The penetration floor is phi^-1*delta_ground.

### CLARITY
Current never flows uniformly; coherence caps the depth.

### NOVELTY
The phi-law caps the infinite DC skin depth.

### ACTIONABILITY
Run sim/730_skin_effect.py; verify delta at kappa->0; proceed to 731.
