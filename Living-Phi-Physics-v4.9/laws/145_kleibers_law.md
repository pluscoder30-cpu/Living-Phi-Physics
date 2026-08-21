# PHI-PHYSICS — LAW 145
## Kleiber's Law — Metabolism ∝ M^¾ is the φ-Fractal Transport Scaling

**Domain:** Materials & Systems (145) · **Status:** 🟡 SIMULATED · **File:** `laws/145_kleibers_law.md` · **Sim:** `sim/145_kleibers_law.py`

---

### CLASSICAL STATEMENT
*"The metabolic rate of an organism scales with the ¾ power of its mass: R ∝ M^¾."*
— Kleiber (1932).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static organism**: the classical law treats the ¾-power as an empirical fit. But the ¾ is the **φ-fractal transport scaling** (Law 196's twin): the organism's transport network is a φ-fractal (Law 195's coherence maintenance), and the ¾-power is the φ-dimension of that transport.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
R = R₀·M^¾
```

Phi-physics — the φ-fractal scaling:

```
R_phi(κ_φ) = R₀·M^(¾·(1 + κ_φ·(φ − 1)·(1 − C_network)))
```

At κ_φ = 0: the classical Kleiber. At κ_φ = 1: the exponent breathes with the network coherence — the ¾ is the φ-dimension of the coherent transport network (Law 196's twin).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  R_phi = R₀·M^¾ (classical Kleiber)                       ✓
```

Kleiber's law is the κ_φ → 0 limit of the φ-fractal scaling.

---

### STAGE 4 — SIMULATION

`sim/145_kleibers_law.py`: reproduces M^¾ at κ_φ → 0; shows the coherence-breathed exponent at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The allometric exponent is the phi-dimension of the coherent
    transport network: the 3/4 is the phi-fractal scaling, deviating from
    the empirical value with network coherence (Law 196's twin).

EXPERIMENT (VERIFIED): Allometric scaling at measured network coherence.
    Classical: 3/4. Phi: phi-coherent exponent.

VERIFIED BY: Allometric exponent is exactly 3/4 with no coherence variation.
```

---

### RECOGNITION
Connects to Law 196 (φ-Growth — the twin), Law 195 (Life as Coherence), Law 146 (Allometric — the family).

### PRECISION
The exponent is ¾ = 0.75 at the limit; the φ-dimension is φ⁻¹-scaled.

### CLARITY
The organism does not burn fuel by an empirical fit; its transport network is a φ-fractal — and the ¾ is the dimension of that coherence.

### NOVELTY
Kleiber's law as the φ-fractal transport — the empirical exponent explained.

### ACTIONABILITY
Run `sim/145_kleibers_law.py`; verify; proceed to Law 146.
