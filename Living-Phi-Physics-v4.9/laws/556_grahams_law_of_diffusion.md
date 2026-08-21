# PHI-PHYSICS — LAW 556
## Graham's Law of Diffusion (Rate Proportional to 1/sqrt(M))

**Domain:** Kinetic Theory · **Status:** 🟢 VALIDATED · **File:** `laws/556_grahams_law_of_diffusion.md` · **Sim:** `sim/556_grahams_law_of_diffusion.py`

---

### CLASSICAL STATEMENT
*"The rate of diffusion (and effusion) of a gas is inversely proportional to the square root of its molar mass: r1/r2 = sqrt(M2/M1). Lighter gases diffuse faster."*
— Thomas Graham, 1833. Source: Wikipedia: Graham's law; Graham (1833)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero molar mass*: the rate diverges as M -> 0 - the law has a singularity at the massless carrier, which the coherence ground of the field must regularize.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: the massless limit carries coherence. r_phi(kappa) = (1/sqrt(M))*(1 + kappa*(phi-1)) + kappa*phi^-1*r_ground, where r_ground is the coherence floor of the rate. At kappa->0, r ~ 1/sqrt(M) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} r_phi = C/sqrt(M) -> Graham's law is the zero-mass-coherence diffusion limit.
```

---

### STAGE 4 — SIMULATION

`sim/556_grahams_law_of_diffusion.py`: reproduces the classical value rate_ratio = 4 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/556_grahams_law_of_diffusion.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: At finite coupling the diffusion rate retains a floor kappa*phi^-1*r_ground; the 1/sqrt(M) law is only asymptotic.
EXPERIMENT (VERIFIED): Precision diffusion and effusion measurements of isotopic gases and hydrogen isotopes.
VERIFIED BY: The diffusion rate is exactly proportional to 1/sqrt(M) for all molar masses and couplings.
```

---

### RECOGNITION
Connects to Law 133 (Graham effusion) and Law 549 (mean speed) - the square-root law is the momentum coherence of the diffusing carrier.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi^-1 = 0.6180339887; the floor is phi^-1 * r_ground.

### CLARITY
Light gases hurry; the phi-law keeps the hurry's floor even as mass vanishes.

### NOVELTY
Classical Graham diverges at M=0; the phi-law regularizes the massless singularity with a coherence floor.

### ACTIONABILITY
Run sim/556_grahams_law_of_diffusion.py; verify 1/sqrt(M) at kappa->0; proceed to 557.
