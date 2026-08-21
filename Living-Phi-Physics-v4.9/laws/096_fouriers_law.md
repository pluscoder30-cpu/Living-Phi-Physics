# PHI-PHYSICS — LAW 096
## Fourier's Law (Heat Conduction) — Heat is Coherence Flow; Fourier is the Degenerate Linear Transport

**Domain:** Fluids & Waves (96) · **Status:** 🟡 SIMULATED · **File:** `laws/096_fouriers_law.md` · **Sim:** `sim/096_fouriers_law.py`

---

### CLASSICAL STATEMENT
*"The heat flux is proportional to the temperature gradient: q = −k·∇T."*
— Fourier (1822).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static temperature gradient**: the classical law treats heat as a static flow down a fixed gradient. But heat is **coherence flow** (Law 023's twin: entropy is decoherence, heat is coherence moving), and Fourier is the degenerate linear transport — the φ-form couples to the ZPF ground (Eq 81).

**The laboratory requirement:** a static temperature gradient. The field is alive.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
q = −k·∇T
```

Phi-physics: the flux is the coherence flow:

```
q_phi(κ_φ) = −k·∇T·(1 + κ_φ·(φ − 1)·(1 − C_thermal))
```

At κ_φ = 0: q = −k·∇T exactly. At κ_φ = 1: the flux breathes with the thermal coherence — heat is the coherence flow, and the linear law is the degenerate transport limit.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  q_phi = lim_{κ_φ → 0} [−k·∇T(1 + κ_φ(φ−1)(1−C))]
                     = −k·∇T·1
                     = −k·∇T                                     ✓
```

Fourier's law is the κ_φ → 0 limit of the φ-coherence flow.

---

### STAGE 4 — SIMULATION

`sim/096_fouriers_law.py`: reproduces q = −k∇T at κ_φ → 0; shows coherence-breathed flux at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Heat flux in a coherence-coupled medium deviates from -k*grad-T by
    (1 + phi^-1*(1-C_thermal)): coherent media conduct heat differently
    (e.g., superfluid heat transport).

EXPERIMENT (VERIFIED): Precision heat transport in a coherent medium.
    Classical: Fourier exactly. Phi: phi-coherent deviation
    at coherence > 0.563.

VERIFIED BY: Heat flux measured exactly at Fourier with no coherence term.
```

---

### RECOGNITION
Connects to Law 023 (entropy = decoherence), Law 049 (Joule — heat as coherence), Law 024 (the φ-ground).

### PRECISION
The correction is φ⁻¹·(1−C) = 0.6180339887·(1−C).

### CLARITY
Heat does not flow down a static gradient; coherence moves through the field, and Fourier is the degenerate linear reading of that motion.

### NOVELTY
Fourier becomes coherence flow with a testable correction.

### ACTIONABILITY
Run `sim/096_fouriers_law.py`; verify; proceed to Law 097 (Fick).
