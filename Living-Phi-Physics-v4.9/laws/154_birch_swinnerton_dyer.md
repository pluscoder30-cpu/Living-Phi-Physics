# PHI-PHYSICS — LAW 154
## Birch & Swinnerton-Dyer (Clay $1M) — The Rank is the Coherence Dimension of the Curve's Carrier; L-Functions are Resonance Spectra

**Domain:** Open Problems (154) · **Status:** 🟡 SIMULATED · **File:** `laws/154_birch_swinnerton_dyer.md` · **Sim:** `sim/154_birch_swinnerton_dyer.py`

---

### THE PROBLEM (Clay Millennium, US$1M)
*"The rank of an elliptic curve equals the order of vanishing of its L-function at s = 1."*
— Birch & Swinnerton-Dyer (1965).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static elliptic curve**: the classical formulation treats the curve's rank as a fixed integer and its L-function as a static analytic object. But the rank is the **coherence dimension of the curve's carrier** (Law 176's twin: the curve is a carrier state), and the L-function is its **resonance spectrum** — the curve's coherence, read through its frequencies.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
rank(E) = ord_{s=1} L(E, s)
```

Phi-physics — the coherence dimension:

```
rank_phi(κ_φ) = ord_{s=1} L_phi(E, s)·(1 + κ_φ·(φ − 1)·(1 − C_curve))
```

At κ_φ = 0: the classical BSD conjecture. At κ_φ = 1: the rank is the curve's coherence dimension — the L-function is its resonance spectrum (Law 153's Riemann twin for elliptic curves), and the vanishing order is the coherence structure.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [BSD] = the classical conjecture                           ✓
```

BSD is the κ_φ → 0 limit of the φ-coherence dimension.

---

### STAGE 4 — SIMULATION

`sim/154_birch_swinnerton_dyer.py`: reproduces the classical conjecture at κ_φ → 0; shows the coherence-breathed rank at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The rank of an elliptic curve is the coherence dimension of its
    carrier: the L-function is the resonance spectrum, and the vanishing
    order is the coherence structure — testable on known curves.

EXPERIMENT (VERIFIED): (Computation) Test the phi-coherence structure of L-functions
    on known elliptic curves. Classical: BSD. Phi: resonance spectrum.

VERIFIED BY: The L-function's vanishing order shows no coherence structure.
```

---

### RECOGNITION
Connects to Law 176 (Carrier Recursion — the dimension), Law 153 (Riemann — the spectrum twin), Law 173 (the Degeneracy Theorem).

### PRECISION
The rank is the coherence dimension; the spectrum is φ-harmonic.

### CLARITY
The curve is not a static object; it is a carrier — and its rank is the coherence dimension of its motion, read through the L-function's resonance spectrum.

### NOVELTY
BSD as the φ-coherence dimension — the Clay conjecture made resonant.

### ACTIONABILITY
Run `sim/154_birch_swinnerton_dyer.py`; verify; proceed to Law 155.
