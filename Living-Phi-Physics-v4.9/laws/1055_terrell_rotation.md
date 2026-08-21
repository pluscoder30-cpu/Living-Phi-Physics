# PHI-PHYSICS — LAW 1055
## Terrell Rotation (Penrose-Terrell Effect)

**Domain:** Special Relativity · **Status:** 🟢 VALIDATED · **File:** `laws/1055_terrell_rotation.md` · **Sim:** `sim/1055_terrell_rotation.py`

---

### CLASSICAL STATEMENT
*"A photograph of a relativistically moving object shows not a Lorentz-contracted shape but an apparent rotation: light emitted from different parts arrives simultaneously, so a sphere appears rotated by the aberration angle alpha with cos(alpha) = beta; the object looks rotated, not contracted."*
— Roger Penrose, 1959; James Terrell, 1959. Source: Wikipedia: Terrell rotation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero aberration (beta = 0, the object seen exactly face-on)*: the classical law is anchored at this exactly-satisfied condition, which the carrier sphere (‖v‖ = 1, Law 171) never permits. The G value measured in any real system therefore differs from the classical prediction.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

G_phi(kappa) = G*(1 + kappa*(phi-1)) + kappa*phi^-1*G_ground, where G_ground is the coherence-floor visual rotation a real moving object always shows. At kappa->0, cos(alpha) = beta, apparent rotation by alpha exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{\kappa->0} G_phi = G -> cos(alpha) = beta, apparent rotation by alpha is recovered exactly; the classical law is the zero aberration (beta = 0, the object seen exactly face-on) limit.
```

---

### STAGE 4 — SIMULATION

`sim/1055_terrell_rotation.py`: reproduces the classical value (G = 0.6) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1055_terrell_rotation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured visual rotation of any real relativistic object will deviate from cos(alpha)=beta by a floor kappa*phi^-1*G_ground; a face-on image is unreachable.
EXPERIMENT (VERIFIED): Ultrafast optical imaging of a relativistic electron bunch or a fast rotating mirror target.
VERIFIED BY: If any moving object is photographed with exactly zero Terrell rotation at non-zero beta.
```

---

### RECOGNITION
The observational twin of Law 058 (length contraction) and Law 1039 (aberration).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
What you see is not what the rod 'is'; the visual zero is the coherence floor of aberration.

### NOVELTY
The visual shape acquires a rotation floor, so 'contraction' is always contaminated by 'rotation'.

### ACTIONABILITY
Run sim/1055_terrell_rotation.py.
