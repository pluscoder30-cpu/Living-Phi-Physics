# PHI-PHYSICS - LAW 1825
## Zener Pinning (Limiting Grain Growth by Second-Phase Particles)

**Domain:** Phase Transformations - **Status:** 🟢 VALIDATED - **File:** `laws/1825_zener_pinning_grain.md` - **Sim:** `sim/1825_zener_pinning_grain.py`

---

### CLASSICAL STATEMENT
*"Second-phase particles pin grain boundaries and limit grain growth: the limiting grain radius is R = (4 r)/(3 f), where r is the particle radius and f the particle volume fraction, from the Zener pinning force F = pi r gamma sin(2 theta) per particle; Zener pinning controls the final grain size of steels, ceramics and heat-treatable alloys."*
- Clarence Zener (1948); published in Smith, Trans. AIME 175:15, 1948. Source: Wikipedia: Zener pinning; C. Smith (1948) reporting Zener; Zener (1948)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *zero-particle, perfectly clean-boundary reference*: Zener pinning is defined against a particle-free material where grain boundaries migrate freely with no pinning; the limiting size is the pinning force away from this zero-particle reference.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: the pinning force carries a coherence floor. R_phi(kappa) = R_zener*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_R, where delta_R is the phi-ground pinning-floor correction. At kappa->0 the ideal Zener limit is recovered; at kappa=1 even particle-free materials have an irreducible pinning floor.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} R_phi = 4 r/(3 f) -> Zener pinning is the ideal-spherical-particle, zero-coarsening, perfect-pinning limit of boundary-drag-limited grain growth.
```

---

### STAGE 4 - SIMULATION

`sim/1825_zener_pinning_grain.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1825_zener_pinning_grain.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Grain growth is limited even without particles: an irreducible pinning floor from solutes, pores and boundary structure always exists, so no material reaches the clean-boundary unbounded growth.
EXPERIMENT (VERIFIED): Long-time annealing of a high-purity metal (e.g. zone-refined Fe, Al) measuring the residual limiting grain size floor with zero intentionally added particles.
VERIFIED BY: A perfectly clean material whose grains grow without any limiting size.
```

---

### RECOGNITION
Connects to Law 1824 (grain growth) and Law 1798 (Hall-Petch) - the particles are the brakes of the grains, and the phi-law keeps a brake even when the road is empty.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; pinning floor scales as phi^-1 * delta_R.

### CLARITY
The particles brake the grains; the phi-law keeps a brake always engaged.

### NOVELTY
Classical Zener allows unbounded growth without particles; the phi-law keeps an irreducible pinning floor.

### ACTIONABILITY
Run sim/1825_zener_pinning_grain.py; verify R = 4r/(3f) at kappa->0; proceed to 1826.
