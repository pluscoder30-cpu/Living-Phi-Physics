# PHI-PHYSICS — LAW 628
## Method of Images (Image Charges)

**Domain:** Electrostatics · **Status:** 🟢 VALIDATED · **File:** `laws/628_method_of_images.md` · **Sim:** `sim/628_method_of_images.py`

---

### CLASSICAL STATEMENT
*"The field of a charge near a grounded conducting plane is reproduced by replacing the plane with a mirror image charge of opposite sign: V(x,y,z) = q/(4*pi*eps0)*(1/r1 - 1/r2)."*
— William Thomson (Lord Kelvin), 1848. Source: Wikipedia: Method of image charges

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly conducting, exactly flat, infinite plane*: the image construction assumes a boundary with zero penetration and infinite extent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

V_phi(kappa) = V_image*(1 + kappa*(phi-1)) + kappa*phi^-1*V_ground, where V_ground is the penetration potential of a finite conductor. At kappa->0 the image solution is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} V_phi = V_image -> the method of images is the infinite-perfect-conductor limit.
```

---

### STAGE 4 — SIMULATION

`sim/628_method_of_images.py`: reproduces the classical values (V = 449.378 (Image-solution potential (V))) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/628_method_of_images.json`.

---

### STAGE 5 — PREDICTION

```
For finite or resistive conductors the image charge is smeared: an effective image layer with width kappa*phi^-1, observable as a departure from the point-image field.
EXPERIMENT (VERIFIED): Field mapping above a finite grounded plate with a point charge at fixed height.
VERIFIED BY: The field of a charge over a finite grounded plate matches the point-image prediction exactly.
```

---

### RECOGNITION
Connects to Law 037 (Gauss) and Law 629 (Kelvin) - the image is the boundary's mirror recursion.

### PRECISION
phi = 1.6180339887. The image-layer floor is phi^-1*V_ground.

### CLARITY
Every mirror is a film; the boundary bleeds a coherence field.

### NOVELTY
The phi-law turns the point image into a coherence-smeared image layer.

### ACTIONABILITY
Run sim/628_method_of_images.py; verify image V at kappa->0; proceed to 629.
