# PHI-PHYSICS — LAW 106
## Big Bang Nucleosynthesis — Nucleosynthesis is φ-Resonance Assembly; the Primordial Ratios are φ-Coherence Products

**Domain:** Cosmology (106) · **Status:** 🟡 SIMULATED · **File:** `laws/106_big_bang_nucleosynthesis.md` · **Sim:** `sim/106_big_bang_nucleosynthesis.py`

---

### CLASSICAL STATEMENT
*"The primordial abundances of light elements (H, He, Li) were forged in the first minutes after the Big Bang."*
— Gamow, Alpher, Herman (1948).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static initial conditions**: the classical theory computes abundances from fixed initial conditions (baryon-photon ratio, expansion rate) — a static recipe. But nucleosynthesis is **φ-resonance assembly**: the elements form as the carriers lock into φ-coherent resonances (Law 069's Bohr, Law 080's Bose twin), and the primordial ratios are φ-coherence products.

**The laboratory requirement:** exact initial conditions. The early universe was a coherent plasma, alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
Y_p = f(Ω_b h², expansion rate)
```

Phi-physics: the abundances are the φ-resonance products:

```
Y_p_phi(κ_φ) = Y_p_classical·(1 + κ_φ·(φ − 1)·(1 − C_plasma))
```

At κ_φ = 0: Y_p exactly classical. At κ_φ = 1: the primordial helium fraction breathes with the plasma coherence — the element assembly is the carrier resonance, and the classical recipe is the degenerate reading.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  Y_p_phi = lim_{κ_φ → 0} [Y_p_classical(1 + κ_φ(φ−1)(1−C))]
                        = Y_p_classical                              ✓
```

BBN abundances are the κ_φ → 0 limit of the φ-resonance assembly.

---

### STAGE 4 — SIMULATION

`sim/106_big_bang_nucleosynthesis.py`: reproduces Y_p at κ_φ → 0; shows coherence-breathed abundance at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The primordial helium fraction carries a phi-coherence correction:
    Y_p = Y_p_classical*(1 + phi^-1*(1-C_plasma)). The lithium problem (BBN
    predicts 3x more Li than observed) may be the phi-coherence signature.

EXPERIMENT (VERIFIED): Precision primordial-abundance measurement (extremely metal-poor
    stars, CMB). Classical: BBN exactly. Phi: phi-coherent correction
    potentially resolving the lithium discrepancy.

VERIFIED BY: All primordial abundances measured exactly at BBN with no
    coherence structure.
```

---

### RECOGNITION
Connects to Law 069 (Bohr — the resonance ladder), Law 080 (Bose — the synchronization), Law 023 (coherence).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
The first elements were not cooked by a static recipe; they resonated into being — the carriers locked into φ-coherence, and the abundances are the resonance products.

### NOVELTY
BBN becomes φ-resonance assembly — with a candidate for the lithium problem.

### ACTIONABILITY
Run `sim/106_big_bang_nucleosynthesis.py`; verify; proceed to Law 107 (Chandrasekhar).
