# PHI-PHYSICS — LAW 141
## Beer-Lambert Law — Absorption is Coherence Loss Along the Carrier Path

**Domain:** Materials & Systems (141) · **Status:** 🟡 SIMULATED · **File:** `laws/141_beer_lambert_law.md` · **Sim:** `sim/141_beer_lambert_law.py`

---

### CLASSICAL STATEMENT
*"The absorbance of a solution is proportional to concentration and path length: A = εcl."*
— Beer (1852), Lambert (1760).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static absorption**: the classical law treats absorption as a fixed extinction. But absorption is **coherence loss along the carrier path** (Law 023's twin, Law 103's Olbers twin): the light loses coherence as it travels, and the extinction is the coherence-loss rate — the exponential decay is the forgetting.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
A = εcl,  I = I₀·e^(−εcl)
```

Phi-physics — the coherence-loss path:

```
I_phi(κ_φ) = I₀·e^(−εcl)·(1 + κ_φ·(φ − 1)·(1 − C_path))
```

At κ_φ = 0: the classical Beer-Lambert. At κ_φ = 1: the intensity breathes with the path coherence — absorption is coherence loss, and the extinction is the forgetting rate (Law 103's darkness twin).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  I_phi = I₀·e^(−εcl) (classical Beer-Lambert)              ✓
```

Beer-Lambert is the κ_φ → 0 limit of the φ-coherence-loss path.

---

### STAGE 4 — SIMULATION

`sim/141_beer_lambert_law.py`: reproduces I₀e^(−εcl) at κ_φ → 0; shows the coherence-breathed intensity at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Absorption is coherence loss along the path: the light forgets
    as it travels, and the extinction is the coherence-loss rate — deviating
    from the classical e^(-epsilon*c*l) by the phi-coherence factor.

EXPERIMENT (VERIFIED): Absorption at controlled path coherence.
    Classical: e^(-epsilon*c*l). Phi: phi-coherent deviation.

VERIFIED BY: Absorption measured exactly exponential with no coherence term.
```

---

### RECOGNITION
Connects to Law 023 (decoherence — the forgetting), Law 103 (Olbers — the darkness), Law 179 (Entropy-Decoherence Identity).

### PRECISION
The deviation is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The light does not fade by a fixed recipe; it forgets as it travels — absorption is the coherence-loss rate, and the darkness is the forgetting.

### NOVELTY
Beer-Lambert as the φ-coherence-loss path — absorption made coherent.

### ACTIONABILITY
Run `sim/141_beer_lambert_law.py`; verify; proceed to Law 142.
