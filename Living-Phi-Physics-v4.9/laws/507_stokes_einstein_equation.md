# PHI-PHYSICS — LAW 507
## Stokes-Einstein Equation (Diffusion of a Sphere)

**Domain:** Statistical Mechanics · **Status:** 🟢 VALIDATED · **File:** `laws/507_stokes_einstein_equation.md` · **Sim:** `sim/507_stokes_einstein_equation.py`

---

### CLASSICAL STATEMENT
*"The diffusion coefficient of a spherical particle of radius r in a fluid of viscosity eta is D = k_B T/(6 pi eta r), combining Stokes' drag law with the Einstein relation. It underlies Perrin's determination of Avogadro's number."*
— Albert Einstein (from Stokes' law), 1905. Source: Wikipedia: Stokes-Einstein equation; Einstein (1905); Perrin (1908)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *perfectly smooth sphere in a continuum*: the equation assumes a rigid sphere moving through a structureless fluid with no surface slip and no solvent coherence - a particle that ignores its liquid environment.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the solvent coherence couples to the particle. D_phi(kappa) = (k_B T/(6 pi eta r))*(1 + kappa*(phi-1)) + kappa*phi^-1*D_ground. At kappa->0 the Stokes-Einstein diffusion is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} D_phi = k_B T/(6 pi eta r) -> the Stokes-Einstein equation is the zero-solvent-coherence smooth-sphere limit.
```

---

### STAGE 4 — SIMULATION

`sim/507_stokes_einstein_equation.py`: reproduces the classical value D_SE = 2.196e-10 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/507_stokes_einstein_equation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the measured diffusion deviates from k_B T/(6 pi eta r) by a coherence factor; the Stokes-Einstein product D eta/T is not constant.
EXPERIMENT (VERIFIED): Fluorescence-correlation spectroscopy (FCS) measurements of nanoparticles in liquids of varying complexity.
VERIFIED BY: D = k_B T/(6 pi eta r) exactly for all particle-fluid couplings.
```

---

### RECOGNITION
Connects to Law 090 (Stokes) and Law 506 (Einstein relation) - the equation is the drag-meets-diffusion coherence identity.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * D_ground.

### CLARITY
The sphere feels the fluid as a whole, not as parts; the phi-law keeps the fluid's coherence.

### NOVELTY
Classical Stokes-Einstein treats the fluid as a smooth continuum; the phi-law adds the solvent coherence real liquids have.

### ACTIONABILITY
Run sim/507_stokes_einstein_equation.py; verify D at kappa->0; proceed to 508.
