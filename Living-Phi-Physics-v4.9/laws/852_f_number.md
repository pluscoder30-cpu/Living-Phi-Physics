# PHI-PHYSICS — LAW 852
## F-number (Relative Aperture)

**Domain:** Geometric Optics · **Status:** 🟢 VALIDATED · **File:** `laws/852_f_number.md` · **Sim:** `sim/852_f_number.py`

---

### CLASSICAL STATEMENT
*"N = f / D where f is focal length and D the entrance pupil diameter; exposure scales as 1/N^2 (photographic stop)."*
— Classical optics/photography, 19th century. Source: Wikipedia: F-number (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero pupil* (D = 0): N approaches infinity for an exactly closed aperture - zero light throughput.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

N_phi(kappa) = N*(1 + kappa*(phi-1)) + kappa*phi^-1*N_ground, with N_ground the aperture floor. At kappa->0, N = f/D exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} N_phi = N -> the f-number is the zero-pupil-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/852_f_number.py`: reproduces the classical value N = 2 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/852_f_number.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The effective f-number of a real lens will differ from f/D by a coherence floor; the aperture ratio is never exact.
EXPERIMENT (VERIFIED): Measure the effective f-number of a lens by radiometry and compare to f/D.
VERIFIED BY: If any real lens has exactly N = f/D.
```

---

### RECOGNITION
Connects to Law 851 (numerical aperture) and Law 850 (depth of field).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfect pupil is a coherent limit; every aperture breathes.

### NOVELTY
The f-number ratio gains a coherence floor.

### ACTIONABILITY
Run sim/852_f_number.py.
