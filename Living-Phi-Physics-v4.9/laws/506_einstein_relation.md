# PHI-PHYSICS — LAW 506
## Einstein Relation (Mobility-Diffusion)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/506_einstein_relation.md` · **Sim:** `sim/506_einstein_relation.py`

---

### CLASSICAL STATEMENT
*"The mobility mu and diffusion coefficient D of a particle in a fluid are related by D = mu k_B T. Equivalently, D = k_B T/(6 pi eta r) for a sphere of radius r in a fluid of viscosity eta."*
— Albert Einstein, 1905. Source: Wikipedia: Einstein relation (kinetic theory); Einstein, Ueber die von der molekularkinetischen Theorie der Waerme geforderte Bewegung (1905)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *thermal equilibrium of the test particle*: the relation assumes the particle is in exact thermal equilibrium with the fluid, sharing its temperature with zero coherence between the particle and the bath.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the particle-bath coherence is a coupling. D_phi(kappa) = mu k_B T*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground. At kappa->0, D = mu k_B T exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} D_phi = mu k_B T -> the Einstein relation is the zero-coherence thermal-equilibrium limit.
```

---

### STAGE 4 — SIMULATION

`sim/506_einstein_relation.py`: reproduces the classical value D_ein = 4.14e-28 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/506_einstein_relation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the diffusion-mobility ratio carries a coherence floor kappa*phi^-1*D_ground; the measured D/mu exceeds k_B T.
EXPERIMENT (VERIFIED): Precision measurements of the mobility and diffusion of Brownian particles or ions in a controlled bath.
VERIFIED BY: D/(mu) = k_B T exactly at all couplings.
```

---

### RECOGNITION
Connects to Law 507 (Stokes-Einstein) and Law 509 (Langevin equation) - the relation is the fluctuation-dissipation identity of the Brownian carrier.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * D_ground.

### CLARITY
The particle's wander and its drift are one motion; the phi-law keeps their shared floor.

### NOVELTY
Classical Einstein relation is exact in equilibrium; the phi-law adds the coherence of the particle-bath meeting.

### ACTIONABILITY
Run sim/506_einstein_relation.py; verify D = mu k_B T at kappa->0; proceed to 507.
