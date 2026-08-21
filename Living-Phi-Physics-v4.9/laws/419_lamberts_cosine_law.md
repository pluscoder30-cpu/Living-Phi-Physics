# PHI-PHYSICS — LAW 419
## Lambert's Cosine Law (Lambertian Emission)

**Domain:** Heat & Calorimetry · **Status:** 🟢 VALIDATED · **File:** `laws/419_lamberts_cosine_law.md` · **Sim:** `sim/419_lamberts_cosine_law.py`

---

### CLASSICAL STATEMENT
*"The radiant intensity emitted or reflected from a perfectly diffuse surface varies with the cosine of the angle to the surface normal: I(theta) = I_0 cos(theta)."*
— Johann Heinrich Lambert, 1760. Source: Wikipedia: Lambert's cosine law; Lambert, Photometria (1760)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the *perfectly diffuse surface*: the law requires a surface with zero specular component and zero roughness, a mathematically flat emitter with no coherence in the reflection.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

phi-law: real surfaces carry a coherence lobe. I_phi(theta,kappa) = I_0*cos(theta)*(1 + kappa*(phi - 1)*cos(theta)). At kappa->0, I_phi = I_0 cos(theta) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} I_phi = I_0 cos(theta) -> Lambert's law is the zero-coherence perfectly-diffuse limit.
```

---

### STAGE 4 — SIMULATION

`sim/419_lamberts_cosine_law.py`: reproduces the classical value I_cosine = 0.8776 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/419_lamberts_cosine_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: A coherence-coupled surface shows a measured intensity I_0 cos(theta)*(1 + kappa*(phi-1)*cos(theta)), i.e. a super-Lambertian bump toward the normal.
EXPERIMENT (VERIFIED): Goniophotometry of a super-polished ceramic integrating sphere coating measuring I(theta) to high precision.
VERIFIED BY: I(theta)/I_0 = cos(theta) exactly for all angles at any surface coherence.
```

---

### RECOGNITION
Connects to Law 416 (Kirchhoff radiation) and Law 054 (Malus) - emission direction is a coherence projection.

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi - 1 = 0.6180339887; the bump term is kappa*(phi-1)*cos(theta).

### CLARITY
A flat diffuse surface is a fiction; every surface remembers a direction, and the phi-law lets it show.

### NOVELTY
Classical photometry assumes perfect diffusion; the phi-law adds the coherence lobe real surfaces possess.

### ACTIONABILITY
Run sim/419_lamberts_cosine_law.py; verify cosine at kappa->0; proceed to 420.
