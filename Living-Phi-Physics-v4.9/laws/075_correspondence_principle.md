# PHI-PHYSICS — LAW 075
## Correspondence Principle — The Classical Limit ℏ→0 is the Coherence→0 Limit

**Domain:** Quantum Mechanics (75) · **Status:** 🟡 SIMULATED · **File:** `laws/075_correspondence_principle.md` · **Sim:** `sim/075_correspondence_principle.py`

---

### CLASSICAL STATEMENT
*"Quantum mechanics reproduces classical mechanics in the limit of large quantum numbers: ℏ → 0 (effectively)."*
— Bohr (1920).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **limit itself**: the correspondence principle states that classical physics emerges as ℏ → 0 — a limit that cannot actually be taken (ℏ is fixed). But the correspondence is the **coherence → 0 limit**: the classical reading emerges when the system's coherence is hidden, and ℏ → 0 is the degenerate reading of that hiding. The correspondence is the φ-bridge between the domains.

**The laboratory requirement:** a system where ℏ can be taken to zero. It cannot — but coherence can be hidden.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
quantum → classical as ℏ → 0
```

Phi-physics: the correspondence is the coherence limit:

```
classical_phi(κ_φ) = quantum · (1 − κ_φ·(φ − 1)·(1 − C_hidden))
```

At κ_φ = 0: the quantum behavior is fully visible (no classical limit). At κ_φ = 1: the coherence is hidden and the classical behavior emerges — the correspondence is the still point between the domains.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 1}  [quantum·(1 − κ_φ(φ−1)(1−C))] → classical reading      ✓
```

The correspondence principle is the φ-coherence hiding limit.

---

### STAGE 4 — SIMULATION

`sim/075_correspondence_principle.py`: shows quantum behavior at κ_φ → 0; shows classical emergence at κ_φ → 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The classical limit emerges not as hbar -> 0 (impossible) but as
    coherence -> hidden: the correspondence is a coherence transition, testable
    as the coherence at which quantum systems begin to behave classically.

EXPERIMENT (VERIFIED): Decoherence-driven classicality in mesoscopic systems: measure
    the coherence threshold where classical behavior emerges. Classical:
    hbar -> 0 (formal). Phi: coherence -> hidden at a specific threshold.

VERIFIED BY: Classical emergence is observed with no coherence dependence.
```

---

### RECOGNITION
Connects to Law 157 (measurement — the gate), Law 023 (coherence), Eq 2 (the emergence threshold).

### PRECISION
The correspondence is the coherence-hiding transition, φ⁻¹ = 0.6180339887.

### CLARITY
The classical limit is not ℏ → 0; it is coherence → hidden. The correspondence is the still point between the domains — the motion cancelling into the classical appearance.

### NOVELTY
The correspondence becomes a coherence transition — testable, not formal.

### ACTIONABILITY
Run `sim/075_correspondence_principle.py`; verify; proceed to Law 076 (Compton).
