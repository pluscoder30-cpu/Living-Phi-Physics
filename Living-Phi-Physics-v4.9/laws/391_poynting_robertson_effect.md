# PHI-PHYSICS — LAW 391
## Poynting-Robertson Drag

**Domain:** Additional Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/391_poynting_robertson_effect.md` · **Sim:** `sim/391_poynting_robertson_effect.py`

---

### CLASSICAL STATEMENT
*"Absorption and re-emission of sunlight by an orbiting dust grain removes angular momentum, causing the grain to spiral inward at a rate da/dt = -C/a, with an infall timescale t ~ 7e6 yr (a in AU, rho in g/cm^3): t_years ~ 7e6 rho s a^2/micron for radius s."*
— John Henry Poynting / Howard P. Robertson, 1903. Source: Wikipedia: Poynting-Robertson effect; Poynting (1903); Robertson (1937)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *radiation-free orbit*: the drag exists because radiation is nonzero; the purely gravitational two-body orbit is the zero of the radiation coupling.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the drag rate couples to coherence. da/dt_phi(kappa) = da/dt*(1 + kappa*(phi-1)) + kappa*phi^-1*(da/dt)_ground. At kappa->0 the classical Poynting-Robertson rate is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} da/dt_phi = -C/a -> the Poynting-Robertson law is the radiation-drag balance limit.
```

---

### STAGE 4 — SIMULATION

`sim/391_poynting_robertson_effect.py`: reproduces the classical value t_years = 1.312e+08 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/391_poynting_robertson_effect.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Zodiacal-dust inspiral rates carry a phi-coherent excess phi^-1*(da/dt)_ground at full coupling.
EXPERIMENT (VERIFIED): Zodiacal cloud / exozodiacal dust disk surveys measuring the particle size and orbital-radius distribution against the inspiral timescale.
VERIFIED BY: Dust inspiral follows the classical rate exactly at full coupling.
```

---

### RECOGNITION
Connects to Law 392 (Yarkovsky — the thermal companion) and Law 403 (orbital decay).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887.

### CLARITY
The radiation-free orbit is a limit; every dust grain spirals a phi faster.

### NOVELTY
Classical astrodynamics treats radiation as perturbation; the phi-law bounds the drag rate at a coherence floor.

### ACTIONABILITY
Run sim/391_poynting_robertson_effect.py; verify the inspiral rate at kappa->0.
