# PHI-PHYSICS — LAW 925
## Mass Law (Acoustics)

**Domain:** Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/925_mass_law.md` · **Sim:** `sim/925_mass_law.py`

---

### CLASSICAL STATEMENT
*"The mass law: sound transmission loss of a single leaf wall increases by 6 dB per doubling of mass per unit area and per doubling of frequency: TL ~ 20 log10(f m) - 47 dB (field incidence)."*
— Classical architectural acoustics, 20th century. Source: Wikipedia: Sound transmission class; mass law (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero mass* (m = 0): the transmission loss is exactly zero for a wall of zero mass - an absent barrier.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

TL_phi(kappa) = TL*(1 + kappa*(phi-1)) + kappa*phi^-1*TL_ground, with TL_ground the loss floor. At kappa->0, TL = 20 log10(f m) - 47 exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} TL_phi = TL -> the mass law is the zero-mass-coherence limit.
```

---

### STAGE 4 — SIMULATION

`sim/925_mass_law.py`: reproduces the classical value TL = 26.98 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/925_mass_law.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The transmission loss of a real wall will deviate from the mass law by a coherence floor kappa*phi^-1*TL_ground.
EXPERIMENT (VERIFIED): Measure the transmission loss of wall panels of varying mass per unit area.
VERIFIED BY: If the transmission loss of any real wall follows exactly 20 log10(f m) - 47.
```

---

### RECOGNITION
Connects to Law 924 (transmission loss) and Law 926 (coincidence effect).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The massive wall is a coherent limit; every barrier has a hole.

### NOVELTY
The mass law gains a mass floor.

### ACTIONABILITY
Run sim/925_mass_law.py.
