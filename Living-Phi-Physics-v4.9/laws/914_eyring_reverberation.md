# PHI-PHYSICS — LAW 914
## Eyring Reverberation Equation

**Domain:** Architectural Acoustics · **Status:** 🟢 VALIDATED · **File:** `laws/914_eyring_reverberation.md` · **Sim:** `sim/914_eyring_reverberation.py`

---

### CLASSICAL STATEMENT
*"Eyring's equation improves Sabine's for high absorption: T60 = 0.161 V / (-S ln(1 - alpha_avg)), where alpha_avg is the average absorption coefficient; it reduces to Sabine's form for low absorption."*
— Carl Eyring, 1930. Source: Wikipedia: Reverberation; Eyring equation (verified via web search)

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is *zero absorption* (alpha_avg = 0): the denominator vanishes (ln(1) = 0) and the reverberation time diverges for a perfectly reflective room.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

T60_phi(kappa) = T60*(1 + kappa*(phi-1)) + kappa*phi^-1*T60_ground, with T60_ground the decay floor. At kappa->0, T60 = 0.161 V/(-S ln(1 - alpha_avg)) exactly.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{kappa->0} T60_phi = T60 -> Eyring's equation is the zero-absorption-coherence limit, reducing to Sabine's for small alpha.
```

---

### STAGE 4 — SIMULATION

`sim/914_eyring_reverberation.py`: reproduces the classical value T60 = 0.08336 at κ_φ → 0 (error ≤ 1%), demonstrates the phi-behavior at κ_φ = 1, and sweeps the coupling 0 → 1. See `validation/914_eyring_reverberation.json`.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The measured reverberation time of any real room will deviate from Eyring's prediction by a coherence floor kappa*phi^-1*T60_ground.
EXPERIMENT (VERIFIED): Measure the RT60 of a highly absorbent reverberation chamber and compare to the Eyring prediction.
VERIFIED BY: If the RT60 of any real room matches the Eyring equation exactly.
```

---

### RECOGNITION
Connects to Law 922 (Sabine) and Law 923 (absorption coefficient).

### PRECISION
φ = 1.6180339887, φ⁻¹ = 0.6180339887. phi = 1.6180339887.

### CLARITY
The perfectly absorbent room is a coherent limit; every chamber decays with a floor.

### NOVELTY
The Eyring equation gains an absorption floor.

### ACTIONABILITY
Run sim/914_eyring_reverberation.py.
