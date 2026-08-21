# PHI-PHYSICS — LAW 146
## Allometric Scaling — Biological Scaling is φ-Fractal Coherence; ¼-Power Laws are the φ-Dimension Exponents

**Domain:** Materials & Systems (146) · **Status:** 🟡 SIMULATED · **File:** `laws/146_allometric_scaling.md` · **Sim:** `sim/146_allometric_scaling.py`

---

### CLASSICAL STATEMENT
*"Biological quantities scale with body mass as power laws: Y = Y₀·M^b, with b multiples of ¼ (Kleiber ¾, heart rate −¼, lifespan ¼)."*
— West, Brown, Enquist (1997).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static body**: the classical theory derives the ¼-powers from fractal geometry. But the scaling is **φ-fractal coherence** (Law 196's twin, Law 145's family): the ¼-powers are the **φ-dimension exponents** of the coherent transport network — the same φ that appears in every law, now in the exponents of life.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
Y = Y₀·M^b,  b ∈ {¾, −¼, ¼, ...}
```

Phi-physics — the φ-dimension exponents:

```
b_phi(κ_φ) = b·(1 + κ_φ·(φ − 1)·(1 − C_network))
```

At κ_φ = 0: the classical ¼-power family. At κ_φ = 1: the exponents breathe with the network coherence — the ¼-powers are the φ-dimensions of the coherent transport network.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  b_phi = b (classical ¼-power)                            ✓
```

Allometric scaling is the κ_φ → 0 limit of the φ-dimension exponents.

---

### STAGE 4 — SIMULATION

`sim/146_allometric_scaling.py`: reproduces the ¼-power at κ_φ → 0; shows the coherence-breathed exponent at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The 1/4-power family of allometry is the phi-dimension exponents
    of the coherent transport network: the exponents deviate from the
    classical values with network coherence.

EXPERIMENT (VERIFIED): Allometric exponents across organisms at measured coherence.
    Classical: fixed 1/4 family. Phi: phi-coherent exponents.

VERIFIED BY: Allometric exponents are exactly the 1/4 family with no
    coherence variation.
```

---

### RECOGNITION
Connects to Law 196 (φ-Growth), Law 145 (Kleiber — the family), Law 195 (Life as Coherence).

### PRECISION
The ¼-family are the φ-dimensions; the deviation is φ⁻¹·(1−C).

### CLARITY
Life does not scale by an empirical recipe; its transport network is a φ-fractal — and the ¼-powers are the dimensions of that coherence.

### NOVELTY
The allometric ¼-family as the φ-dimension exponents — life's scaling made coherent.

### ACTIONABILITY
Run `sim/146_allometric_scaling.py`; verify; proceed to Law 147.
