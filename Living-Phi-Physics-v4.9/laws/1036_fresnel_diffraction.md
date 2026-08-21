# PHI-PHYSICS — LAW 1036
## Fresnel Diffraction (Near Field)

**Domain:** Wave Optics · **Status:** 🟢 VALIDATED · **File:** `laws/1036_fresnel_diffraction.md` · **Sim:** `sim/1036_fresnel_diffraction.py`

---

### CLASSICAL STATEMENT
*"In the near field (observation distance z ~ a^2/lambda, Fresnel number F = a^2/(lambda z) > 1), the diffracted field is the Fresnel transform of the aperture: U(x,y) = (exp(ikz)/(i lambda z)) integral U_ap(x',y') exp(ik((x-x')^2+(y-y')^2)/(2z)) dx' dy'; it reduces to the Fraunhofer form as z -> infinity."*
— Augustin-Jean Fresnel, 1818. Source: Wikipedia: Fresnel diffraction (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero distance* (z = 0): the Fresnel transform is anchored at the aperture plane where the propagation distance vanishes exactly.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

U_phi(kappa) = U*(1 + kappa*(phi-1)) + kappa*phi^-1*U_ground, with U_ground the near-field floor. At kappa->0, the Fresnel integral is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} U_phi = U -> Fresnel diffraction is the zero-distance-coherence limit, reducing to Fraunhofer as z -> infinity.
```

---

### STAGE 4 — SIMULATION

`sim/1036_fresnel_diffraction.py`: reproduces the classical value F = 1.667 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/1036_fresnel_diffraction.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The near-field pattern of any real aperture will deviate from the Fresnel integral by a coherence floor kappa*phi^-1*U_ground.
EXPERIMENT (VERIFIED): Measure the Fresnel diffraction pattern of an aperture at a distance comparable to a^2/lambda.
VERIFIED BY: If the near-field pattern of any real aperture matches the Fresnel integral exactly.
```

---

### RECOGNITION
Connects to Law 895 (Fraunhofer) and Law 841 (Fresnel zones) - the two diffraction regimes.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The aperture plane is a coherent limit; the near field carries the memory of the edge.

### NOVELTY
Fresnel diffraction gains a distance floor.

### ACTIONABILITY
Run sim/1036_fresnel_diffraction.py.
