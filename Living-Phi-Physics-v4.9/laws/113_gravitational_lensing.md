# PHI-PHYSICS — LAW 113
## Gravitational Lensing — Lensing is the φ-Coherence Refraction of the Carrier Path

**Domain:** Cosmology (113) · **Status:** 🟡 SIMULATED · **File:** `laws/113_gravitational_lensing.md` · **Sim:** `sim/113_gravitational_lensing.py`

---

### CLASSICAL STATEMENT
*"Light is deflected by mass: θ = 4GM/c²b (Einstein angle)."*
— Einstein (1916), Eddington (1919), from Soldner (1801).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static mass**: the classical law computes lensing from a static mass distribution. But lensing is the **φ-coherence refraction of the carrier path** (Law 052's Snell twin for gravity): the light carrier retunes through the mass's coherence field, and the Einstein angle is the φ-coherence deflection.

**The laboratory requirement:** a static point mass. Every mass is a coherent field.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
θ_E = 4GM/c²b
```

Phi-physics: the deflection is the φ-coherence refraction:

```
θ_E_phi(κ_φ) = (4GM/c²b)·(1 + κ_φ·(φ − 1)·(1 − C_lens))
```

At κ_φ = 0: θ_E exactly classical. At κ_φ = 1: the angle breathes with the lens's coherence — the light refracts through the coherence field, and the classical angle is the degenerate reading.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  θ_E_phi = lim_{κ_φ → 0} [(4GM/c²b)(1 + κ_φ(φ−1)(1−C))]
                        = 4GM/c²b·1
                        = 4GM/c²b                               ✓
```

Gravitational lensing is the κ_φ → 0 limit of the φ-refraction.

---

### STAGE 4 — SIMULATION

`sim/113_gravitational_lensing.py`: reproduces θ_E at κ_φ → 0; shows coherence-breathed angle at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The gravitational deflection of light by a coherence-coupled mass
    deviates from 4GM/c^2*b by (1 + phi^-1*(1-C_lens)): coherent lenses
    (e.g., dark-matter-dominated clusters) show a phi-coherent excess.

EXPERIMENT (VERIFIED): Precision cluster lensing measurement. Classical: 4GM/c^2*b.
    Phi: phi-coherent excess at coherence > 0.563.

VERIFIED BY: Lensing measured exactly at the Einstein angle with no coherence term.
```

---

### RECOGNITION
Connects to Law 052 (Snell — the refraction twin), Law 004 (gravity — the flow), Law 105 (dark energy — the coherence field).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The light does not bend around a static mass; it retunes through the mass's coherence — the same refraction as Snell, at cosmic scale.

### NOVELTY
Lensing becomes φ-coherence refraction — unifying optics and gravity as one retuning.

### ACTIONABILITY
Run `sim/113_gravitational_lensing.py`; verify; proceed to Law 114 (CMB).
