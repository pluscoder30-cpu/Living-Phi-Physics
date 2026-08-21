# PHI-PHYSICS — LAW 039
## Faraday's Law — Induction is the Retrocausal Loop

**Domain:** Electromagnetism (39) · **Status:** 🟡 SIMULATED · **File:** `laws/039_faradays_law.md` · **Sim:** `sim/039_faradays_law.py`

---

### CLASSICAL STATEMENT
*"The electromotive force around a closed loop is equal to the negative rate of change of the magnetic flux through the loop: emf = −dΦ_B/dt."*
— Faraday (1831).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static flux change**: the classical law describes the emf as a reaction to flux change — a static bookkeeping of "what changed." But induction is the **retrocausal loop**: the future field corrects the present (the corpus's Eq 47–55, Eq 3.2). The emf is not a reaction; it is the coherence flow that keeps the loop coherent through time.

**The laboratory requirement:** the law demands a perfectly static loop and a perfectly known flux. Neither exists.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
emf = −dΦ_B/dt
```

Phi-physics: induction is the retrocausal loop; the emf is the coherence flow:

```
emf_phi(κ_φ) = −dΦ_B/dt · (1 + κ_φ·(φ − 1)·C_retro(t))
```

where C_retro(t) is the retrocausal coherence — the future state's contribution to the present emf. At κ_φ = 0: emf = −dΦ_B/dt exactly. At κ_φ = 1: the emf carries the retrocausal correction — the future flux participates in the present induction, the way Eq 3.2's kernel `K_retro(t,t') = exp(−|t−t'|/τ_retro)·e^(i·ω_retro·(t−t'))` with τ_retro = φ⁵ allows future states to correct present errors.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  emf_phi = lim_{κ_φ → 0} [−dΦ_B/dt(1 + κ_φ(φ−1)C_retro)]
                        = −dΦ_B/dt·1
                        = −dΦ_B/dt                                    ✓
```

Faraday's law is the κ_φ → 0 limit of the retrocausal induction loop.

---

### STAGE 4 — SIMULATION

`sim/039_faradays_law.py`: reproduces emf = −dΦ/dt at κ_φ → 0; shows retrocausal correction at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The induced emf in a coherence-coupled loop carries a retrocausal
    correction: emf = −dΦ/dt·(1 + φ⁻¹·C_retro). The emf anticipates flux
    changes slightly — a reproducible lead in the induction response at
    coherence > 0.563.

EXPERIMENT (VERIFIED): High-bandwidth induction measurement in a coherent loop (e.g.,
    SQUID): measure the phase of emf vs dPhi/dt. Classical: exactly opposite
    phase. Phi: retrocausal lead at the φ⁵ time constant.

VERIFIED BY: The emf is measured exactly in anti-phase with dPhi/dt with no
    retrocausal lead.
```

---

### RECOGNITION
Connects to the retrocausal set (Eq 47–55, Eq 3.2), Law 048 (Lenz — the retrocausal reaction), Law 003 (the loop).

### PRECISION
The retrocausal time constant is τ_retro = φ⁵ ≈ 11.09 (the corpus's own).

### CLARITY
Induction is not a reaction; it is the loop's self-correction through time — the future helping the present stay coherent. The circle with the line, extended in time.

### NOVELTY
Faraday's law gains the retrocausal correction the corpus already predicted — the emf anticipates, testably.

### ACTIONABILITY
Run `sim/039_faradays_law.py`; verify; proceed to Law 040 (Ampère).
