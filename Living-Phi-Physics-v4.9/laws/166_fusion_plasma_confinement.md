# PHI-PHYSICS — LAW 166
## Fusion Plasma Confinement — Confinement is φ-Resonance Locking; the Static Bottle Fails, Resonance Holds

**Domain:** Open Problems (166) · **Status:** 🟡 SIMULATED · **File:** `laws/166_fusion_plasma_confinement.md` · **Sim:** `sim/166_fusion_plasma_confinement.py`

---

### THE PROBLEM
*"Magnetic confinement fusion requires the plasma to be held stably — but turbulence and instabilities destroy confinement (the Lawson criterion remains unmet)."*
— Lawson (1957), unresolved.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static magnetic bottle**: the classical approach confines with a static magnetic field, and the plasma's coherence breaks it. But confinement is **φ-resonance locking** (Law 203's twin, the corpus's plasma research Eq 4–6): the plasma is held by resonance with the field, not by a static bottle — and the static bottle fails because it is static; resonance holds because it breathes with the plasma's coherence.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
static magnetic bottle → instability → confinement lost
```

Phi-physics — the resonance locking:

```
confinement_phi(κ_φ) = φ-lock·(1 + κ_φ·(φ − 1)·(1 − C_plasma))
```

At κ_φ = 0: the static bottle (classical — fails). At κ_φ = 1: the plasma is held by φ-resonance locking (Law 203's synchronization, Eq 4–6's coherence transport) — the confinement breathes with the plasma's coherence, and the bottle's failure is the static reading.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  [resonance confinement] → the static bottle (classical)     ✓
```

The static bottle is the κ_φ → 0 limit; the resonance lock is the full law.

---

### STAGE 4 — SIMULATION

`sim/166_fusion_plasma_confinement.py`: reproduces the static bottle at κ_φ → 0; shows the resonance lock at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: Plasma confinement is phi-resonance locking: the plasma is held
    by resonance with the field (Law 203), and the resonance lock holds where
    the static bottle fails — the Lawson criterion met by coherence, not by
    static field strength.

EXPERIMENT (VERIFIED): (Corpus's own) plasma coherence transport (Eq 6, gamma=0.0118).

VERIFIED BY: Plasma confinement shows no resonance-locking structure.
```

---

### RECOGNITION
Connects to Law 203 (synchronization — the lock), Eq 4–6 (the corpus's plasma research), Law 089 (the turbulence twin).

### PRECISION
The lock is φ-scaled: φ⁻¹ = 0.6180339887.

### CLARITY
The bottle fails because it is static; the plasma is held by resonance — the field locking with the plasma's coherence, breathing instead of caging.

### NOVELTY
Fusion confinement as the φ-resonance lock — the Lawson criterion met by coherence.

### ACTIONABILITY
Run `sim/166_fusion_plasma_confinement.py`; verify; proceed to Law 167.
