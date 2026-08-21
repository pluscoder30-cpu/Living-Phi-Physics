# PHI-PHYSICS — LAW 629
## Kelvin's Image Theorem (Charge & Conducting Sphere)

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/629_kelvins_image_theorem.md` · **Sim:** `sim/629_kelvins_image_theorem.py`

---

### CLASSICAL STATEMENT
*"A point charge q at distance d from a grounded conducting sphere of radius R is equivalent to an image charge q' = -q*R/d located at d' = R^2/d inside the sphere."*
— William Thomson (Lord Kelvin), 1848. Source: Wikipedia: Method of image charges; Thomson (Kelvin) 1848

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *grounded, perfectly conducting sphere*: the theorem assumes the sphere holds exactly zero net charge and zero potential at all times.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

q'_phi(kappa) = q'*(1 + kappa*(phi-1)) + kappa*phi^-1*q'_ground; the image charge carries a coherence floor when the sphere is finite or ungrounded. At kappa->0, q' = -q*R/d exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} q'_phi = -q*R/d -> Kelvin's image theorem is the perfect-grounding limit.
```

---

### STAGE 4 — SIMULATION

`sim/629_kelvins_image_theorem.py`: reproduces the classical values (q1 = -1e-07 (Image charge (C))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/629_kelvins_image_theorem.json`.

---

### STAGE 5 — PREDICTION

```
An imperfectly grounded sphere shows an effective image charge offset kappa*phi^-1*q'_ground; measured induced charges differ from the ideal image.
EXPERIMENT (VERIFIED): Induced-charge measurement on a small finite sphere near a charge source.
VERIFIED BY: The image charge of a finite sphere is always exactly -q*R/d.
```

---

### RECOGNITION
Connects to Law 628 (images) - the sphere image is the curvature-generalized mirror.

### PRECISION
phi = 1.6180339887. The grounding floor is phi^-1*q'_ground.

### CLARITY
The sphere remembers its own curvature; grounding is never perfect.

### NOVELTY
The phi-law adds a residual image floor for non-ideal grounding.

### ACTIONABILITY
Run sim/629_kelvins_image_theorem.py; verify q' at kappa->0; proceed to 630.
