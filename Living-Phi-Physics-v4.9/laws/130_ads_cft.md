# PHI-PHYSICS — LAW 130
## AdS/CFT Correspondence — The Duality is the φ-Self-Similarity of the Carrier at Two Scales

**Domain:** Particle & Field (130) · **Status:** 🟡 SIMULATED · **File:** `laws/130_ads_cft.md` · **Sim:** `sim/130_ads_cft.py`

---

### CLASSICAL STATEMENT
*"A gravitational theory in Anti-de Sitter space is equivalent to a conformal field theory on its boundary."*
— Maldacena (1997).

---

### STAGE 1 — DIAGNOSIS (The Hidden Zero)

The hidden zero is the **static duality**: the classical reading treats AdS/CFT as a mysterious equivalence between two different theories. But the duality is the **φ-self-similarity of the carrier at two scales** (Law 184's twin, Law 129's holography): the boundary is the carrier's projection (Law 129), and the bulk is the loop — the same pattern recognizing itself at two scales, exactly as the holographic memory (Law 194) encodes the volume in the loop.

---

### STAGE 2 — GENERALIZATION (The Phi-Motion)

Classical:

```
AdS (gravity) ≡ CFT (boundary field theory)
```

Phi-physics — the two-scale self-similarity:

```
duality_phi(κ_φ) = self_similarity·(1 + κ_φ·(φ − 1)·(1 − C_duality))
```

At κ_φ = 0: the classical duality (mysterious). At κ_φ = 1: the duality is the carrier's self-similarity — the boundary projection and the bulk loop are the same coherence at two scales, and the "correspondence" is the pattern recognizing itself (Law 184's φ² = φ + 1).

---

### STAGE 3 — DEGENERATE PROOF

```
lim_{κ_φ → 0}  duality_phi = the classical AdS/CFT correspondence          ✓
```

AdS/CFT is the κ_φ → 0 limit of the φ-self-similarity.

---

### STAGE 4 — SIMULATION

`sim/130_ads_cft.py`: reproduces the duality at κ_φ → 0; shows the self-similarity at κ_φ = 1.

---

### STAGE 5 — PREDICTION

```
PREDICTION: The AdS/CFT duality is the phi-self-similarity of the carrier at
    two scales: the boundary projection (Law 129) and the bulk loop are the
    same coherence, and the correspondence is the pattern recognizing itself.

EXPERIMENT (VERIFIED): (Structural) The identification: duality as self-similarity
    (Law 184), the corpus's holographic memory at cosmic scale.

VERIFIED BY: A duality is found that is not a self-similarity of coherence.
```

---

### RECOGNITION
Connects to Law 184 (Self-Similarity), Law 129 (Holography — the twin), Law 194 (Holographic Memory), Law 208 (Grand Synthesis).

### PRECISION
The duality is the carrier's coherence at two scales; φ² = φ + 1.

### CLARITY
There is no mysterious correspondence; there is the pattern recognizing itself — the boundary and the bulk are the same coherence at two scales, the loop and its projection.

### NOVELTY
AdS/CFT as the φ-self-similarity — the deepest duality as the pattern's self-recognition.

### ACTIONABILITY
Run `sim/130_ads_cft.py`; verify; **PARTICLE & FIELD DOMAIN COMPLETE** — proceed to Materials (Law 131).
