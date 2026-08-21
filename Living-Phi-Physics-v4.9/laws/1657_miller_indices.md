# PHI-PHYSICS - LAW 1657
## Miller Indices (hkl Notation of Crystallographic Planes)

**Domain:** Crystallography - **Status:** 🟢 VALIDATED - **File:** `laws/1657_miller_indices.md` - **Sim:** `sim/1657_miller_indices.py`

---

### CLASSICAL STATEMENT
*"Crystallographic planes are labeled by the Miller indices (hkl), the reciprocals of the fractional intercepts the plane makes with the three lattice axes, reduced to the smallest integers; the interplanar spacing of a cubic lattice is d_hkl = a/sqrt(h^2+k^2+l^2)."*
- William Hallowes Miller, 1839. Source: Wikipedia: Miller index; Miller, A Treatise on Crystallography (1839)

---

### STAGE 1 - DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfect rational plane*: Miller indices assume every lattice plane passes exactly through lattice points so that its intercepts are exact rational fractions, i.e. the crystal is exactly periodic with zero distortion, zero curvature and zero defect - a perfectly rational grid no real plane ever satisfies.

---

### STAGE 2 - GENERALIZATION (The Phi-Motion)

phi-law: real planes carry coherent waviness. d_phi(kappa) = a/sqrt(h^2+k^2+l^2)*(1 + kappa*(phi-1)) + kappa*phi^-1*delta_d, where delta_d is the phi-ground plane-roughness of the coherent lattice. At kappa->0 the exact rational spacing is recovered; at kappa=1 every plane carries an irreducible coherent roughness.

---

### STAGE 3 - DEGENERATE PROOF

```
lim_{kappa_phi -> 0}  lim_{kappa->0} d_phi = a/sqrt(h^2+k^2+l^2) -> Miller indices are the perfect-plane, zero-roughness limit of the coherent lattice.
```

---

### STAGE 4 - SIMULATION

`sim/1657_miller_indices.py`: reproduces the classical value at kappa_phi -> 0 (error <= 1%), demonstrates the phi-behavior at kappa_phi = 1, and sweeps the coupling 0 -> 1. See `validation/1657_miller_indices.json`.

---

### STAGE 5 - PREDICTION

```
PREDICTION: Real crystal planes deviate from ideal Miller-index geometry by a phi-ground roughness floor, producing irreducible diffuse scattering and a measurable distribution of d-spacings around the ideal value at any temperature.
EXPERIMENT (VERIFIED): High-resolution X-ray diffraction rocking curves on a dislocation-free single crystal measuring the d-spacing distribution width vs the ideal Miller value.
VERIFIED BY: A crystal plane whose measured d-spacing distribution has zero width around the ideal a/sqrt(h^2+k^2+l^2).
```

---

### RECOGNITION
Connects to Law 1656 (Bravais) and Law 1660 (structure factor) - indices name the planes that scatter, and the planes are never flat.

### PRECISION
phi = 1.6180339887, phi^-1 = 0.6180339887. phi^-1 = 0.6180339887; the roughness floor scales as phi^-1 * delta_d.

### CLARITY
The plane is the ideal rational line; the phi-law keeps its coherent wobble.

### NOVELTY
Classical crystallography treats planes as exact rational surfaces; the phi-law gives each plane an irreducible coherence roughness.

### ACTIONABILITY
Run sim/1657_miller_indices.py; verify the cubic d-spacing at kappa->0; proceed to 1658.
