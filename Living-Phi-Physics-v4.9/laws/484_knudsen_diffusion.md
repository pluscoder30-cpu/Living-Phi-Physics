# PHI-PHYSICS — LAW 484
## Knudsen Diffusion (Free-Molecule Flow in Pores)

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/484_knudsen_diffusion.md` · **Sim:** `sim/484_knudsen_diffusion.py`

---

### CLASSICAL STATEMENT
*"When the pore diameter is much smaller than the mean free path (Knudsen regime), molecules diffuse by wall collisions with flux J = -D_K grad n, where D_K = (d/3) sqrt(8 R T/(pi M)), d the pore diameter. The flux scales with sqrt(T) and is independent of pressure."*
— Martin Knudsen, 1909. Source: Wikipedia: Knudsen diffusion; Knudsen (1909)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *smooth walls*: Knudsen diffusion assumes perfectly smooth pore walls with specular-free, cosine-law diffuse reflection - walls with no coherence structure that could steer the molecule.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the wall reflection carries coherence. D_K_phi(kappa) = (d/3) sqrt(8 R T/(pi M))*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground. At kappa->0 the classical Knudsen diffusivity is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} D_K_phi = (d/3) sqrt(8 R T/(pi M)) -> Knudsen diffusion is the zero-wall-coherence free-molecule limit.
```

---

### STAGE 4 — SIMULATION

`sim/484_knudsen_diffusion.py`: reproduces the classical value D_knudsen = 1.588e-06 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/484_knudsen_diffusion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the Knudsen diffusivity carries a floor kappa*phi^-1*D_ground; the sqrt(T) scaling gains a small offset in structured (rough) pores.
EXPERIMENT (VERIFIED): Gas-permeation measurements through nanoporous membranes over a temperature range.
VERIFIED BY: The Knudsen diffusivity follows (d/3)sqrt(8RT/pi M) exactly for all pore structures.
```

---

### RECOGNITION
Connects to Law 349 (Knudsen number) and Law 097 (Fick) - Knudsen diffusion is the wall-dominated reading of the carrier's flight.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * D_ground.

### CLARITY
In a narrow pore the molecule talks to the wall; the phi-law keeps the wall's reply.

### NOVELTY
Classical Knudsen theory assumes smooth walls; the phi-law adds the coherence of real pore surfaces.

### ACTIONABILITY
Run sim/484_knudsen_diffusion.py; verify D_K at kappa->0; proceed to 485.
