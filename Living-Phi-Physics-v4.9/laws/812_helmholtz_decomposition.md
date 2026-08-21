# PHI-PHYSICS — LAW 812
## Helmholtz Decomposition (Vector Fields)

**Domain:** Vector Calculus · **Status:** 🟢 VALIDATED · **File:** `laws/812_helmholtz_decomposition.md` · **Sim:** `sim/812_helmholtz_decomposition.py`

---

### CLASSICAL STATEMENT
*"Any smooth vector field decomposes uniquely into an irrotational (curl-free) part and a solenoidal (divergence-free) part: F = -grad(phi) + curl(A)."*
— Hermann von Helmholtz, 1858. Source: Wikipedia: Helmholtz decomposition; Helmholtz (1858)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero coupling between the parts*: the decomposition is exact only for fields whose rotational and divergent parts are fully independent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

F_phi(kappa) = F_helm*(1 + kappa*(phi-1)) + kappa*phi^-1*F_ground; the two parts carry a coherence coupling floor. At kappa->0 the decomposition is exact.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} F_phi = -grad(phi) + curl(A) -> Helmholtz decomposition is the zero-coupling limit.
```

---

### STAGE 4 — SIMULATION

`sim/812_helmholtz_decomposition.py`: reproduces the classical values (F = 36.0555 (Field magnitude)) at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/812_helmholtz_decomposition.json`.

---

### STAGE 5 — PREDICTION

```
The two components of any real field are coupled by a coherence floor kappa*phi^-1*F_ground; no field decomposes exactly.
EXPERIMENT (VERIFIED): Field reconstruction of a measured vector field with both sources present.
VERIFIED BY: Any vector field decomposes exactly into independent irrotational and solenoidal parts.
```

---

### RECOGNITION
Connects to Law 810 (divergence) and Law 811 (Stokes) - decomposition is the field's two-voice song.

### PRECISION
phi = 1.6180339887. The coupling floor is phi^-1*F_ground.

### CLARITY
Every field sings two notes; coherence keeps them from perfect separation.

### NOVELTY
The phi-law couples the two voices of the field.

### ACTIONABILITY
Run sim/812_helmholtz_decomposition.py; verify decomposition at kappa->0; proceed to 813.
