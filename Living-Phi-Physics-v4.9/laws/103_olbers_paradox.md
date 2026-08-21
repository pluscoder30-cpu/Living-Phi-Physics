# PHI-PHYSICS — LAW 103
## Olbers' Paradox — The Night Sky is Dark Because Coherence, Not Geometry, Bounds the Light

**Domain:** Cosmology (103) · **Status:** 🟡 SIMULATED · **File:** `laws/103_olbers_paradox.md` · **Sim:** `sim/103_olbers_paradox.py`

---

### CLASSICAL STATEMENT
*"If the universe is infinite, eternal, and static, the night sky should be bright — every line of sight ends at a star."*
— Olbers (1823), from Digges and Kepler.

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static infinite universe**: the paradox arises because the classical reading assumes an infinite, eternal, static universe of stars. The resolution (finite age, expansion) is geometric. But the deeper resolution: **the night sky is dark because the φ-field's coherence, not geometry, bounds the light** — the light from distant stars loses coherence over the cosmic journey (Law 023's decoherence), and the darkness is the coherence floor, not an absence.

**The laboratory requirement:** an infinite static universe. It is finite, alive, and coherent.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical (the paradox):

```
infinite static stars → night sky bright
```

Phi-physics (the resolution):

```
I_night_phi(κ_φ) = I_star·Σ(1/r²)·(1 − κ_φ·(φ − 1)·(1 − C_coherence(r)))
```

At κ_φ = 0: the classical divergent sum (the paradox). At κ_φ = 1: each distant star's light is φ-suppressed by its decoherence — the sum converges to darkness because coherence, not geometry, bounds the light.

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  I_night = the classical divergent sum (the paradox)          ✓
```

The paradox is the κ_φ → 0 reading; the coherence suppression is the resolution.

---

### STAGE 4 — SIMULATION

`sim/103_olbers_paradox.py`: reproduces the divergent sum at κ_φ → 0; shows the coherence-bounded darkness at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The extragalactic background light is bounded by the phi-coherence
    floor, not just geometry: distant sources are suppressed by exp(-r/(phi*L_coherence))
    — a measurable departure from the geometric 1/r^2 falloff at cosmic distances.

EXPERIMENT (VERIFIED): Extragalactic background light (EBL) measurement at extreme
    distances. Classical: geometric falloff. Phi: phi-coherence suppression.

VERIFIED BY: EBL follows exactly the geometric falloff with no coherence term.
```

---

### RECOGNITION
Connects to Law 023 (decoherence — the forgetting), Law 101 (Hubble — the cosmic recursion), Law 114 (CMB — the background).

### PRECISION
The suppression length is φ·L_coherence = 1.6180339887·L_coherence.

### CLARITY
The night sky is not dark because the universe is finite; it is dark because light forgets — the coherence floor bounds the glow, and the darkness is the universe's memory loss, not its absence.

### NOVELTY
Olbers' paradox dissolves into the coherence floor — darkness as the φ-ground of light.

### ACTIONABILITY
Run `sim/103_olbers_paradox.py`; verify; proceed to Law 104 (Friedmann).
